#!/usr/bin/env python3
"""
rates.py — Phase 1.6 of CONTEXT ENGINE v4.3. Mechanical: no searches, no judgement.

    python rates.py 1010             # reads fixtures_1010.md, writes rates_1010.md
    python rates.py 1010 --refs      # also builds each division's referee record

Computes every RESEARCH SPEC rate a card's facts strip needs, for both sides of
each league fixture and for the division itself, so Phase 2 spends its searches
on people (transfers, manager, injuries, the referee appointment) and not on
numbers. Built for the lower divisions, where nobody tabulates these rates, but
it runs on any league in settle.py's LEAGUES.

Sources, one job each:
- ESPN public scoreboard: goals, half-time goals, cards, fouls and corners for
  every match. The same records and the same windows settle.py audits against,
  so the strip and the scorecard always read one record.
- FotMob public stats files: team xG for and against (ESPN has none).
- ESPN match summaries (--refs): the referee of every settled match, joined to
  that match's cards and fouls.

Windows follow the strip's rule: this season from five matches, otherwise last
season (in the division the side actually played in), and the label says which.
No price is requested, read or written, and nothing here is a forecast.
"""

import argparse
import gzip
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from zoneinfo import ZoneInfo

import settle as S

ROME, UTC = ZoneInfo("Europe/Rome"), ZoneInfo("UTC")
FOTMOB_CACHE = os.path.join(S.DATA, "fotmob")
UA = {"User-Agent": "Mozilla/5.0 (context-engine rates)", "Accept-Encoding": "gzip"}

# ESPN slug -> FotMob league id (checked against FotMob's league names, 2026-10-09)
FOTMOB = {
    "eng.1": 47, "eng.2": 48, "eng.3": 108, "eng.4": 109, "eng.5": 117,
    "esp.1": 87, "esp.2": 140, "ita.1": 55, "ita.2": 86, "ger.1": 54, "ger.2": 146,
    "fra.1": 53, "fra.2": 110, "ned.1": 57, "ned.2": 111, "por.1": 61, "bel.1": 40,
    "aut.1": 38, "sui.1": 69, "sco.1": 64, "sco.2": 123, "den.1": 46, "gre.1": 135,
    "swe.1": 67, "usa.1": 130, "usa.usl.1": 8972, "usa.usl.l1": 9296,
}


# ───────────────────────── fixtures ─────────────────────────

def read_fixtures(n):
    path = f"fixtures_{n}.md"
    if not os.path.exists(path):
        sys.exit(f"{path} not found — run Phase 1 first")
    text = open(path, encoding="utf-8").read()
    m = re.search(r"(20\d\d)-(\d\d)-(\d\d)", text[:400])
    day = date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
    rows, header = [], None
    for line in text.splitlines():
        if line.startswith("#") or " | " not in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        rows.append(dict(zip(header, cells)))
    for i, r in enumerate(rows, 1):
        r["fid"] = f"f{i}"
    return day, rows


def kickoff_utc(r, day):
    """Kickoff as ESPN's UTC string, for the 'before kickoff' cut. Falls back to midnight."""
    k = r.get("kickoff", "")
    try:
        if re.match(r"\d{4}-\d\d-\d\d \d\d:\d\d", k):
            local = datetime.strptime(k[:16], "%Y-%m-%d %H:%M")
        else:
            hh, mm = re.match(r"(\d\d?):(\d\d)", k).groups()
            local = datetime(day.year, day.month, day.day, int(hh), int(mm))
        return local.replace(tzinfo=ROME).astimezone(UTC).strftime("%Y-%m-%dT%H:%MZ")
    except (AttributeError, ValueError):
        return day.strftime("%Y-%m-%dT00:00Z")


def espn_event(r, slug, day):
    """The fixture's ESPN event (parsed), from the source column or by name."""
    src = re.match(r"espn:([^/]+)/(\d+)", r.get("source", ""))
    ymd = day.strftime("%Y%m%d")
    if src:
        try:
            for ev in S.cached(slug, ymd).get("events", []):
                if ev.get("id") == src.group(2):
                    return S.parse_event(ev, slug)
        except RuntimeError:
            pass
    m, score, swapped = S.find_match({"home": r["home"], "away": r["away"]}, slug, day)
    return None if (not m or swapped) else m


# ───────────────────────── rates ─────────────────────────

def full_rates(ms, tid):
    rows = []
    for m in ms:
        h = m["home_id"] == tid
        rows.append({
            "gf": m["hg"] if h else m["ag"], "ga": m["ag"] if h else m["hg"],
            "h1": m["h1h"] + m["h1a"],
            "cards": m["ch"] if h else m["ca"], "fouls": m["fh"] if h else m["fa"],
            "cf": m["kh"] if h else m["ka"], "ca": m["ka"] if h else m["kh"],
        })
    mean = S.mean
    tot = [r["gf"] + r["ga"] for r in rows]
    return {
        "n": len(rows),
        "gf": mean([r["gf"] for r in rows]), "ga": mean([r["ga"] for r in rows]),
        "o25": mean([t >= 3 for t in tot]),
        "btts": mean([r["gf"] > 0 and r["ga"] > 0 for r in rows]),
        "cs": mean([r["ga"] == 0 for r in rows]), "fts": mean([r["gf"] == 0 for r in rows]),
        "h1": mean([r["h1"] for r in rows]),
        "cards": mean([r["cards"] for r in rows]), "fouls": mean([r["fouls"] for r in rows]),
        "cf": mean([r["cf"] for r in rows]), "ca": mean([r["ca"] for r in rows]),
        "kn": sum(r["cf"] is not None for r in rows),
    }


def f2(x):
    return "not published" if x is None else f"{x:.2f}"


def pc(x):
    return "–" if x is None else f"{100 * x:.0f}%"


def season_label(season, slug):
    return str(season) if slug in S.CALENDAR else f"{season % 100}/{(season + 1) % 100}"


# ───────────────────────── FotMob xG ─────────────────────────

def get_json(url, path, max_age):
    os.makedirs(FOTMOB_CACHE, exist_ok=True)
    if os.path.exists(path) and (max_age is None or time.time() - os.path.getmtime(path) < max_age):
        return json.load(open(path, encoding="utf-8"))
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    doc = json.loads(raw)
    json.dump(doc, open(path, "w", encoding="utf-8"))
    return doc


_xg_memo = {}


def fotmob_xg(slug, back):
    """{team name: (xg_pg, xga_pg, matches)} for a division, current season (back=0) or
    the one before (back=1). Empty dict when FotMob publishes no xG for it."""
    key = (slug, back)
    if key in _xg_memo:
        return _xg_memo[key]
    out = {}
    lid = FOTMOB.get(slug)
    if lid:
        try:
            lg = get_json(f"https://www.fotmob.com/api/data/leagues?id={lid}",
                          os.path.join(FOTMOB_CACHE, f"league_{lid}.json"), 6 * 3600)
            links = (lg.get("stats") or {}).get("seasonStatLinks") or []
            tid = links[back]["TournamentId"] if len(links) > back else None
            if tid:
                age = 6 * 3600 if back == 0 else None
                tabs = {}
                for stat in ("expected_goals_team", "expected_goals_conceded_team"):
                    doc = get_json(f"https://data.fotmob.com/stats/{lid}/season/{tid}/{stat}.json",
                                   os.path.join(FOTMOB_CACHE, f"{lid}_{tid}_{stat}.json"), age)
                    tabs[stat] = {e["ParticipantName"]: e for e in doc["TopLists"][0]["StatList"]}
                for name, e in tabs["expected_goals_team"].items():
                    c = tabs["expected_goals_conceded_team"].get(name)
                    n = e.get("MatchesPlayed") or 0
                    if n and c:
                        out[name] = (e["StatValue"] / n, c["StatValue"] / n, n)
        except (urllib.error.URLError, KeyError, IndexError, ValueError, TimeoutError):
            out = {}
    _xg_memo[key] = out
    return out


def xg_for(names, slug, back):
    tab = fotmob_xg(slug, back)
    best, score = None, 0.0
    for name in tab:
        s = S.side_sim(name, names)
        if s > score:
            best, score = name, s
    return tab[best] if best and score >= 0.6 else None


# ───────────────────────── referees ─────────────────────────

def referee_table(slug, season):
    """Every referee's record in this division, this season and last, from ESPN summaries."""
    ms = S.season_matches(slug, season) + S.season_matches(slug, season - 1)
    with ThreadPoolExecutor(6) as ex:
        refs = list(ex.map(lambda m: S.referee_for(slug, m["id"]), ms))
    by = {}
    for m, ref in zip(ms, refs):
        if not ref:
            continue
        cur = m["season"] == season
        d = by.setdefault(ref, {"n": 0, "n_this": 0, "cards": [], "fouls": []})
        d["n"] += 1
        d["n_this"] += cur
        d["cards"].append(m["ch"] + m["ca"])
        if m["fh"] is not None and m["fa"] is not None:
            d["fouls"].append(m["fh"] + m["fa"])
    covered = sum(1 for r in refs if r)
    return by, covered, len(ms)


def appointed(slug, eid):
    """The referee if ESPN already lists one for the unplayed match (not cached: it changes)."""
    try:
        raw = S.fetch_summary(slug, eid)
    except RuntimeError:
        return None
    for o in (raw.get("gameInfo") or {}).get("officials") or []:
        if ((o.get("position") or {}).get("name") or "").lower() == "referee":
            return o.get("fullName")
    return None


# ───────────────────────── output ─────────────────────────

def baseline_block(slug, name, season, before):
    L, label = S.prior_rates(slug, season, before)
    if not L or not L["n"]:
        return [f"## {name} ({slug}) — no ESPN record", ""], None
    return [
        f"## {name} ({slug}) — division line, {label} matches",
        "",
        f"goals pg {f2(L['gpg'])} · over 2.5 {pc(L['o25'])} · BTTS {pc(L['btts'])} · "
        f"clean sheet / failed to score {pc(L['cs'])} (per team) · 1H goals pg {f2(L['h1'])} · "
        f"cards pg {f2(L['cards_pm'])} ({f2(L['cards_pt'])} per team) · "
        f"fouls per team {f2(L['fouls_pt'])} · corners pg {f2(L['corners_pm'])} "
        f"({f2(L['corners_pt'])} per team) · home win {pc(L['home_win'])} · "
        f"draw {pc(L['draw'])} · away win {pc(L['away_win'])}",
        "",
    ], L


def side_lines(tag, names, tid, slug, season, before, venue):
    ms, _, label = S.team_window(tid, slug, season, before)
    if not ms:
        return [f"- **{tag}** — no ESPN record in this division or its neighbours"], None
    t = full_rates(ms, tid)
    window_slug = label.split()[1] if len(label.split()) > 1 else slug
    split = [m for m in ms if (m["home_id"] if venue == "home" else m["away_id"]) == tid]
    v = full_rates(split, tid) if split else None
    this_season = label.startswith(f"{season % 100}/{(season + 1) % 100} {slug} ")
    xg = xg_for(names, window_slug, 0 if this_season else 1)
    xg_now = xg_for(names, slug, 0) if not this_season else None
    out = [f"- **{tag}** — window {label}"]
    out.append(f"  - goals for / against pg {f2(t['gf'])} / {f2(t['ga'])} · over 2.5 {pc(t['o25'])} · "
               f"BTTS {pc(t['btts'])} · clean sheet {pc(t['cs'])} · failed to score {pc(t['fts'])} · "
               f"1H goals pg (match) {f2(t['h1'])}")
    out.append(f"  - cards pg {f2(t['cards'])} · fouls pg {f2(t['fouls'])} · "
               f"corners for / against pg {f2(t['cf'])} / {f2(t['ca'])}"
               + (f" (fouls and corners recorded in {t['kn']} of {t['n']})" if 0 < t["kn"] < t["n"] else ""))
    out.append(f"  - xG for / against pg (FotMob) "
               + (f"{f2(xg[0])} / {f2(xg[1])} ({xg[2]})" if xg else "not published"))
    if xg_now:
        out.append(f"  - this season so far, xG for / against pg {f2(xg_now[0])} / {f2(xg_now[1])} "
                   f"({xg_now[2]})")
    if v:
        out.append(f"  - {venue} only ({v['n']}): goals {f2(v['gf'])} / {f2(v['ga'])} · "
                   f"over 2.5 {pc(v['o25'])} · BTTS {pc(v['btts'])} · 1H {f2(v['h1'])} · "
                   f"cards {f2(v['cards'])} · corners {f2(v['cf'])} / {f2(v['ca'])}")
    if window_slug != slug:
        out.append(f"  - window is from {window_slug}, a different division: read it against "
                   f"that division's line, not this one")
    return out, t


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("slate")
    ap.add_argument("--refs", action="store_true", help="build each division's referee record")
    a = ap.parse_args()

    day, rows = read_fixtures(a.slate)
    if not day:
        sys.exit("no slate date in the fixtures file header")
    out = [f"# rates_{a.slate} — {day.isoformat()} — built {datetime.now(ROME):%Y-%m-%d %H:%M} Europe/Rome",
           "# Mechanical (rates.py). ESPN match records for counts, FotMob for xG. "
           "Pre-kickoff records only. No prices, no forecasts.", ""]
    skipped, divisions = [], {}
    for r in rows:
        slug = None
        src = re.match(r"espn:([^/]+)/", r.get("source", ""))
        if src:
            slug = src.group(1)
        slug = slug or S.slug_for(r.get("league", ""))
        league = slug and slug != "uefa.nations" and (
            slug in S.LEAGUES or re.fullmatch(r"[a-z]{3}\.\d", slug))
        if not league:
            skipped.append(f"{r['fid']} {r['home']} – {r['away']} ({r.get('league')}): "
                           f"{'not mapped' if not slug else 'cup or international, not computed here'}")
            continue
        divisions.setdefault(slug, (r.get("league") or slug, []))[1].append(r)

    for slug, (name, fx) in divisions.items():
        season = S.season_for(slug, day)
        first_before = min(kickoff_utc(r, day) for r in fx)
        block, L = baseline_block(slug, name, season, first_before)
        out += block
        refs = None
        if a.refs:
            refs, covered, total = referee_table(slug, season)
            lg_cards = S.mean([c for d in refs.values() for c in d["cards"]])
        for r in fx:
            before = kickoff_utc(r, day)
            ev = espn_event(r, slug, day)
            out.append(f"### {r['fid']} · {r['home']} – {r['away']} · {r.get('kickoff', '')}")
            out.append("")
            if not ev:
                out += ["- not found on ESPN for this date; rates not computed", ""]
                continue
            for tag, names, tid, venue in ((r["home"], ev["home_names"], ev["home_id"], "home"),
                                           (r["away"], ev["away_names"], ev["away_id"], "away")):
                lines, _ = side_lines(tag, names, tid, slug, season, before, venue)
                out += lines
            if a.refs:
                ref = appointed(slug, ev["id"])
                if ref and ref in refs:
                    d = refs[ref]
                    fpc = (S.mean(d["fouls"]) / S.mean(d["cards"])) if d["fouls"] and S.mean(d["cards"]) else None
                    out.append(f"- **Referee (ESPN)** {ref} — {d['n']} matches ({d['n_this']} this season) · "
                               f"cards pg {f2(S.mean(d['cards']))} vs division {f2(lg_cards)} · "
                               f"fouls pg {f2(S.mean(d['fouls']))} · fouls per card {f2(fpc)}")
                elif ref:
                    out.append(f"- **Referee (ESPN)** {ref} — no match of theirs in this division's record")
                else:
                    out.append("- **Referee** not listed on ESPN yet; look up the appointment and read "
                               "the table below")
            out.append("")
        if a.refs and refs:
            out += [f"#### Referees — {name}, {season_label(season - 1, slug)} and "
                    f"{season_label(season, slug)} ({covered} of {total} matches carry a referee)", "",
                    "referee | matches (this season) | cards pg | fouls pg | fouls per card",
                    "--- | --- | --- | --- | ---"]
            for ref, d in sorted(refs.items(), key=lambda kv: -kv[1]["n"]):
                if d["n"] < 3:
                    continue
                c, f = S.mean(d["cards"]), S.mean(d["fouls"])
                out.append(f"{ref} | {d['n']} ({d['n_this']}) | {f2(c)} | {f2(f)} | "
                           f"{f2(f / c) if c and f else '–'}")
            out.append(f"division | | {f2(lg_cards)} | | ")
            out.append("")

    if skipped:
        out += ["## Not computed", ""] + [f"- {s}" for s in skipped] + [""]
    path = f"rates_{a.slate}.md"
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    n_done = sum(len(fx) for _, fx in divisions.values())
    print(f"rates_{a.slate}.md: {n_done} fixtures in {len(divisions)} divisions, {len(skipped)} not computed")


if __name__ == "__main__":
    main()
