#!/usr/bin/env python3
"""
settle.py — Phase 4 of CONTEXT ENGINE v4. Runs after the matches, never before.

    python settle.py 0920            # settle one slate
    python settle.py --all           # every v4 slate whose matches are finished
    python settle.py --scorecard     # rebuild scorecard.md from what is settled
    python settle.py --check         # print pipeline baselines to compare with baselines_N.md
    python settle.py --all --refresh # re-pull the current calendar year from ESPN

For each carded fixture on slate N it finds the match on ESPN's public
scoreboard, records the 90-minute result, and writes results_N.md plus
settle_data/results_N.json. Then it rebuilds scorecard.md across every
settled slate:

1. Verdict audit. For each league fixture it works out, AFTER the match,
   which way the pre-kickoff base rates leaned in each family (both sides'
   rates against their own league line, from ESPN match records dated
   before kickoff), then checks whether the match landed on that side.
   Hit rates are grouped by the card's verdict and set beside the league
   prior, so the question it answers is: does "Well-suited" pick out
   families where the evidence came in more often than the league rate alone?

2. Your picks. If picks_N.md exists, each line is graded (win / loss / push,
   half results on quarter lines) and grouped by the verdict the card gave
   that family. A price you wrote there is used for profit. This is the only
   place a price is read, and nothing here flows back into a card or board.

Nothing in this script is used before kickoff.
"""

import argparse
import glob
import http.client
import json
import math
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from difflib import SequenceMatcher

from verdicts import FAMILY_KEYS, LEVEL, SHORT, family_key, read_slate

HOSTS = ["site.api.espn.com", "site.web.api.espn.com"]
SB = "https://{host}/apis/site/v2/sports/soccer/{slug}/scoreboard?dates={dates}&limit=1000"
UA = {"User-Agent": "Mozilla/5.0 (context-engine settle)"}
DATA = "settle_data"
CACHE = os.path.join(DATA, "espn")
FRESH_SECONDS = 3 * 3600

# Card competition name -> ESPN slug. Longest key wins on substring match.
COMPETITIONS = {
    "premier league": "eng.1", "championship": "eng.2", "efl cup": "eng.league_cup",
    "carabao cup": "eng.league_cup", "fa cup": "eng.fa",
    "laliga": "esp.1", "laliga ea sports": "esp.1", "laliga 2": "esp.2",
    "laliga hypermotion": "esp.2", "copa del rey": "esp.copa_del_rey",
    "serie a": "ita.1", "serie b": "ita.2", "coppa italia": "ita.coppa_italia",
    "bundesliga": "ger.1", "2. bundesliga": "ger.2", "dfb-pokal": "ger.dfb_pokal",
    "ligue 1": "fra.1", "ligue 2": "fra.2", "coupe de france": "fra.coupe_de_france",
    "uefa champions league": "uefa.champions", "uefa europa league": "uefa.europa",
    "uefa conference league": "uefa.europa.conf",
    "nations league": "uefa.nations",
}
LEAGUES = {"eng.1", "esp.1", "ita.1", "ger.1", "fra.1", "eng.2", "esp.2", "ita.2", "ger.2", "fra.2",
           "uefa.nations"}
SECOND_TIER = {"eng.1": "eng.2", "esp.1": "esp.2", "ita.1": "ita.2", "ger.1": "ger.2", "fra.1": "fra.2"}
MIN_THIS = 5      # the strip's rule: this season's figure from five matches
MIN_LAST = 10
MIN_PRIOR = 30
MIN_LAST_NATIONS = 4  # a full Nations League edition is 4 matches in a 3-team group, 6 in a 4-team one

ALIASES = {
    "man city": "manchester city", "man united": "manchester united",
    "man utd": "manchester united", "spurs": "tottenham hotspur",
    "psg": "paris saint germain", "inter": "internazionale",
    "bayern munchen": "bayern munich", "olympique lyonnais": "lyon",
    "stade brestois": "brest", "stade rennais": "rennes", "estac troyes": "troyes",
    "wolves": "wolverhampton wanderers", "athletic club": "athletic bilbao",
}
STOP = {"fc", "cf", "afc", "sc", "ac", "as", "ssc", "rc", "rcd", "ogc", "losc", "cd",
        "ca", "sv", "tsg", "vfb", "vfl", "club", "de", "sad", "ud", "sd", "us", "ss",
        "aj", "sco", "1", "07", "04", "05", "1846", "1899", "calcio", "afc"}


# ───────────────────────── ESPN ─────────────────────────

def fetch(slug, dates):
    last = None
    for attempt in range(3):
        for host in HOSTS:
            url = SB.format(host=host, slug=slug, dates=dates)
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                    return json.loads(r.read())
            except (urllib.error.URLError, TimeoutError, ValueError, http.client.HTTPException) as e:
                last = e
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"ESPN {slug} {dates}: {last}")


def slim(ev):
    """Keep only what parse_event reads; a season file drops from ~5 MB to a few hundred KB."""
    comp = (ev.get("competitions") or [{}])[0]
    return {
        "id": ev.get("id"), "date": ev.get("date"),
        "season": {"year": (ev.get("season") or {}).get("year")},
        "competitions": [{
            "status": {"type": {k: ((comp.get("status") or {}).get("type") or {}).get(k)
                                for k in ("name", "state", "completed")}},
            "competitors": [{
                "homeAway": c.get("homeAway"), "score": c.get("score"),
                "team": {k: (c.get("team") or {}).get(k)
                         for k in ("id", "displayName", "shortDisplayName", "name", "location")},
                "statistics": [s for s in c.get("statistics", [])
                               if s.get("name") in ("wonCorners", "foulsCommitted")],
            } for c in comp.get("competitors", [])],
            "details": [{
                "clock": {"displayValue": (d.get("clock") or {}).get("displayValue")},
                "team": {"id": (d.get("team") or {}).get("id")},
                "athletesInvolved": [{"id": a.get("id")} for a in (d.get("athletesInvolved") or [])[:1]],
                **{k: d.get(k) for k in ("scoringPlay", "yellowCard", "redCard", "ownGoal", "shootout")},
            } for d in comp.get("details", [])],
        }],
    }


def cached(slug, dates, refresh=False):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{slug}_{dates}.json")
    this_year = str(date.today().year)
    stale = dates.startswith(this_year) and (
        refresh or not os.path.exists(path) or time.time() - os.path.getmtime(path) > FRESH_SECONDS)
    if os.path.exists(path) and not stale:
        return json.load(open(path, encoding="utf-8"))
    doc = {"events": [slim(ev) for ev in fetch(slug, dates).get("events", [])]}
    json.dump(doc, open(path, "w", encoding="utf-8"))
    return doc


SUMMARY = "https://{host}/apis/site/v2/sports/soccer/{slug}/summary?event={eid}"


def fetch_summary(slug, eid):
    last = None
    for attempt in range(3):
        for host in HOSTS:
            url = SUMMARY.format(host=host, slug=slug, eid=eid)
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                    return json.loads(r.read())
            except (urllib.error.URLError, TimeoutError, ValueError, http.client.HTTPException) as e:
                last = e
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"ESPN summary {slug} {eid}: {last}")


def officials_for(slug, eid):
    """Cached list of {'name', 'role'} for one settled match, from the summary endpoint
    (the scoreboard pull settle.py otherwise uses never carries officials)."""
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{slug}_officials_{eid}.json")
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    try:
        raw = fetch_summary(slug, eid)
        officials = [{"name": o.get("fullName"), "role": (o.get("position") or {}).get("name")}
                     for o in (raw.get("gameInfo") or {}).get("officials") or []]
    except RuntimeError:
        officials = []
    json.dump(officials, open(path, "w", encoding="utf-8"))
    return officials


def referee_for(slug, eid):
    officials = officials_for(slug, eid)
    for o in officials:
        if (o.get("role") or "").lower() == "referee":
            return o.get("name")
    return officials[0]["name"] if officials else None


def minute(display):
    m = re.match(r"\s*(\d+)", display or "")
    return int(m.group(1)) if m else None


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def parse_event(ev, slug):
    comp = (ev.get("competitions") or [{}])[0]
    st = (comp.get("status") or {}).get("type") or {}
    sides = {}
    for c in comp.get("competitors", []):
        stats = {s.get("name"): s.get("displayValue") for s in c.get("statistics", [])}
        t = c.get("team") or {}
        sides[c.get("homeAway")] = {
            "id": t.get("id"),
            "names": [t.get(k) for k in ("displayName", "shortDisplayName", "name", "location") if t.get(k)],
            "score": num(c.get("score")),
            "corners": num(stats.get("wonCorners")),
            "fouls": num(stats.get("foulsCommitted")),
        }
    if "home" not in sides or "away" not in sides:
        return None
    ids = {sides["home"]["id"]: "h", sides["away"]["id"]: "a"}
    g_all = {"h": 0, "a": 0}
    g90 = {"h": 0, "a": 0}
    g1h = {"h": 0, "a": 0}
    cards = {"h": 0, "a": 0}
    booked = set()
    for d in comp.get("details", []):
        if d.get("shootout"):
            continue
        side = ids.get((d.get("team") or {}).get("id"))
        mi = minute((d.get("clock") or {}).get("displayValue"))
        if d.get("scoringPlay") and side:
            g_all[side] += 1
            if mi is not None and mi <= 90:
                g90[side] += 1
            if mi is not None and mi <= 45:
                g1h[side] += 1
        # The baselines' count (ESPN boxscore): players only, yellows plus straight
        # reds; a second-yellow red is not added on top of the two yellows.
        player = ((d.get("athletesInvolved") or [{}])[0] or {}).get("id")
        if not side or not player:
            continue
        if d.get("yellowCard"):
            cards[side] += 1
            booked.add(player)
        elif d.get("redCard") and player not in booked:
            cards[side] += 1
    hs, as_ = sides["home"]["score"], sides["away"]["score"]
    status = st.get("name", "")
    extra = status in ("STATUS_FINAL_AET", "STATUS_FINAL_PEN") or "AET" in status or "PEN" in status
    reconciled = hs is not None and g_all == {"h": int(hs), "a": int(as_)}
    if extra:
        h90, a90 = g90["h"], g90["a"]
    else:
        h90, a90 = (int(hs), int(as_)) if hs is not None else (None, None)
    return {
        "id": ev.get("id"), "slug": slug, "utc": ev.get("date", ""),
        "season": (ev.get("season") or {}).get("year"),
        "done": bool(st.get("completed")) and st.get("state") == "post",
        "status": status, "extra_time": extra, "reconciled": reconciled,
        "home_id": sides["home"]["id"], "away_id": sides["away"]["id"],
        "home": sides["home"]["names"][0] if sides["home"]["names"] else "",
        "away": sides["away"]["names"][0] if sides["away"]["names"] else "",
        "home_names": sides["home"]["names"], "away_names": sides["away"]["names"],
        "hg": h90, "ag": a90, "h1h": g1h["h"], "h1a": g1h["a"],
        "ch": cards["h"], "ca": cards["a"],
        "kh": sides["home"]["corners"], "ka": sides["away"]["corners"],
        "fh": sides["home"]["fouls"], "fa": sides["away"]["fouls"],
    }


_season_memo = {}


def season_matches(slug, season, refresh=False):
    """Completed matches of one league season (Aug–May spans two calendar pulls)."""
    key = (slug, season)
    if key in _season_memo:
        return _season_memo[key]
    out, seen = [], set()
    for yr in (season, season + 1):
        if yr > date.today().year:
            continue
        for ev in cached(slug, str(yr), refresh).get("events", []):
            m = parse_event(ev, slug)
            if m and m["done"] and m["season"] == season and m["id"] not in seen \
                    and m["hg"] is not None:
                seen.add(m["id"])
                out.append(m)
    out.sort(key=lambda m: m["utc"])
    _season_memo[key] = out
    return out


# ───────────────────────── matching ─────────────────────────

def norm(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"['’`]", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    s = ALIASES.get(s, s)
    toks = [t for t in s.split() if t not in STOP]
    return " ".join(toks) or s


def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    ta, tb = set(a.split()), set(b.split())
    jac = len(ta & tb) / len(ta | tb)
    contain = 0.9 if (a in b or b in a) else 0.0
    return max(jac, contain, SequenceMatcher(None, a, b).ratio())


def side_sim(name, names):
    return max((sim(name, n) for n in names), default=0.0)


def find_match(card, slug, day, refresh=False):
    """Best ESPN event for this card on day ±1. Returns (match, score, swapped)."""
    best = (None, 0.0, False)
    for delta in (0, -1, 1):
        d = date.fromordinal(day.toordinal() + delta)
        try:
            events = cached(slug, d.strftime("%Y%m%d"), refresh).get("events", [])
        except RuntimeError:
            continue
        for ev in events:
            m = parse_event(ev, slug)
            if not m:
                continue
            straight = min(side_sim(card["home"], m["home_names"]), side_sim(card["away"], m["away_names"]))
            swapped = min(side_sim(card["home"], m["away_names"]), side_sim(card["away"], m["home_names"]))
            score, sw = (straight, False) if straight >= swapped else (swapped, True)
            score -= 0.01 * abs(delta)
            if score > best[1]:
                best = (m, score, sw)
        if best[1] >= 0.8:
            break
    return best if best[1] >= 0.55 else (None, best[1], False)


def slug_for(competition):
    c = competition.lower().strip()
    if c in COMPETITIONS:
        return COMPETITIONS[c]
    for k in sorted(COMPETITIONS, key=len, reverse=True):
        if k in c:
            return COMPETITIONS[k]
    return None


# ───────────────────────── base rates ─────────────────────────

def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def league_rates(ms):
    tot = [m["hg"] + m["ag"] for m in ms]
    corners = [m["kh"] + m["ka"] for m in ms if m["kh"] is not None and m["ka"] is not None]
    cards = [m["ch"] + m["ca"] for m in ms]
    h1 = [m["h1h"] + m["h1a"] for m in ms]
    team_goals = [m["hg"] for m in ms] + [m["ag"] for m in ms]
    n = len(ms)
    r = {
        "n": n,
        "gpg": mean(tot),
        "o25": mean([t >= 3 for t in tot]),
        "btts": mean([m["hg"] > 0 and m["ag"] > 0 for m in ms]),
        "h1": mean(h1),
        "cards_pm": mean(cards),
        "corners_pm": mean(corners),
        "fouls_pt": mean([m["fh"] for m in ms] + [m["fa"] for m in ms]),
        "home_win": mean([m["hg"] > m["ag"] for m in ms]),
        "away_win": mean([m["hg"] < m["ag"] for m in ms]),
        "draw": mean([m["hg"] == m["ag"] for m in ms]),
        "cs": mean([m["ag"] == 0 for m in ms] + [m["hg"] == 0 for m in ms]),
    }
    r["gpt"] = r["gpg"] / 2 if r["gpg"] is not None else None
    r["cards_pt"] = r["cards_pm"] / 2 if r["cards_pm"] is not None else None
    r["corners_pt"] = r["corners_pm"] / 2 if r["corners_pm"] is not None else None
    # league priors for above-the-line outcomes on count families
    r["p_h1_over"] = mean([x > r["h1"] for x in h1]) if h1 else None
    r["p_cards_over"] = mean([x > r["cards_pm"] for x in cards]) if cards else None
    r["p_corners_over"] = mean([x > r["corners_pm"] for x in corners]) if corners else None
    r["p_team_over"] = mean([x > r["gpt"] for x in team_goals]) if team_goals else None
    return r


def team_rates(ms, tid):
    rows = []
    for m in ms:
        h = m["home_id"] == tid
        rows.append({
            "gf": m["hg"] if h else m["ag"], "ga": m["ag"] if h else m["hg"],
            "h1": m["h1h"] + m["h1a"],
            "cards": m["ch"] if h else m["ca"],
            "cf": m["kh"] if h else m["ka"], "ca": m["ka"] if h else m["kh"],
        })
    tot = [r["gf"] + r["ga"] for r in rows]
    return {
        "n": len(rows),
        "o25": mean([t >= 3 for t in tot]),
        "btts": mean([r["gf"] > 0 and r["ga"] > 0 for r in rows]),
        "h1": mean([r["h1"] for r in rows]),
        "cards": mean([r["cards"] for r in rows]),
        "cf": mean([r["cf"] for r in rows]), "ca": mean([r["ca"] for r in rows]),
        "gf": mean([r["gf"] for r in rows]), "ga": mean([r["ga"] for r in rows]),
    }


def team_window(tid, slug, season, before):
    """The strip's rule: this season from 5 matches, else last season (own division)."""
    this_league = [m for m in season_matches(slug, season) if m["utc"] < before]
    this = [m for m in this_league if tid in (m["home_id"], m["away_id"])]
    if len(this) >= MIN_THIS:
        return this, this_league, f"{season % 100}/{(season + 1) % 100} {slug} ({len(this)})"
    for s in (slug, SECOND_TIER.get(slug)):
        if not s:
            continue
        lg = season_matches(s, season - 1)
        last = [m for m in lg if tid in (m["home_id"], m["away_id"])]
        if len(last) >= MIN_LAST:
            return last, lg, f"{(season - 1) % 100}/{season % 100} {s} ({len(last)})"
    if this:
        return this, this_league, f"{season % 100}/{(season + 1) % 100} {slug} ({len(this)}, thin)"
    return None, None, "no record"


def deviations(tid, slug, season, before):
    ms, lg, label = team_window(tid, slug, season, before)
    if not ms:
        return None, label
    t, L = team_rates(ms, tid), league_rates(lg)

    def dev(a, b):
        return None if a is None or b is None else a - b
    return {
        "o25": dev(t["o25"], L["o25"]), "btts": dev(t["btts"], L["btts"]),
        "h1": dev(t["h1"], L["h1"]), "cards": dev(t["cards"], L["cards_pt"]),
        "cf": dev(t["cf"], L["corners_pt"]), "ca": dev(t["ca"], L["corners_pt"]),
        "gf": dev(t["gf"], L["gpt"]), "ga": dev(t["ga"], L["gpt"]),
    }, label


def prior_rates(slug, season, before):
    ms = [m for m in season_matches(slug, season) if m["utc"] < before]
    if len(ms) >= MIN_PRIOR:
        return league_rates(ms), f"{season % 100}/{(season + 1) % 100} to date ({len(ms)})"
    ms = season_matches(slug, season - 1)
    return league_rates(ms), f"{(season - 1) % 100}/{season % 100} ({len(ms)})"


def add(*xs):
    return None if any(x is None for x in xs) else sum(xs)


# ─────────────────── UEFA Nations League (one slug, four divisions) ───────────────────
# uefa.nations covers Leagues A/B/C/D under a single ESPN slug, and its editions run two
# calendar years (season = the edition's start year, e.g. 2024 for 2024-25). Both facts
# break the club-league assumptions above: a raw season_matches() pool mixes four
# divisions with materially different rates, and "last season" is season-2, not season-1.
# These helpers filter to one division's own group-stage matches before doing anything else.

_division_memo = {}


def nations_divisions(season):
    """team_id -> 'A'/'B'/'C'/'D' for one uefa.nations edition, from its standings."""
    if season in _division_memo:
        return _division_memo[season]
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"uefa.nations_standings_{season}.json")
    if os.path.exists(path):
        raw = json.load(open(path, encoding="utf-8"))
    else:
        url = f"https://site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={season}"
        raw, last = None, None
        # this endpoint 403s on settle.py's usual UA string; a generic one works
        browser_ua = {"User-Agent": "Mozilla/5.0"}
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=browser_ua), timeout=60) as r:
                    raw = json.loads(r.read())
                break
            except (urllib.error.URLError, TimeoutError, ValueError, http.client.HTTPException) as e:
                last = e
                time.sleep(2 * (attempt + 1))
        if raw is None:
            raise RuntimeError(f"ESPN uefa.nations standings {season}: {last}")
        json.dump(raw, open(path, "w", encoding="utf-8"))
    out = {}
    for ch in raw.get("children", []):
        mm = re.search(r"\b([ABCD])\d*\b", (ch.get("name") or "").upper())
        if not mm:
            continue
        for e in (ch.get("standings") or {}).get("entries", []):
            tid = (e.get("team") or {}).get("id")
            if tid:
                out[tid] = mm.group(1)
    _division_memo[season] = out
    return out


def nations_league_matches(season, letter, before=None):
    """Completed group-stage matches of one division in one edition (cross-division
    promotion/relegation play-offs are excluded automatically: the two sides differ
    in division there, so neither passes the same-letter filter)."""
    divs = nations_divisions(season)
    ms = season_matches("uefa.nations", season)
    if before is not None:
        ms = [m for m in ms if m["utc"] < before]
    return [m for m in ms if divs.get(m["home_id"]) == letter and divs.get(m["away_id"]) == letter]


def nations_team_window(tid, season, before):
    letter = nations_divisions(season).get(tid)
    if not letter:
        return None, None, "no record"
    this_league = nations_league_matches(season, letter, before)
    this = [m for m in this_league if tid in (m["home_id"], m["away_id"])]
    if len(this) >= MIN_THIS:
        return this, this_league, f"{season}-{season + 1} League {letter} ({len(this)})"
    prev = season - 2
    letter_prev = nations_divisions(prev).get(tid)
    if letter_prev:
        lg = nations_league_matches(prev, letter_prev)
        last = [m for m in lg if tid in (m["home_id"], m["away_id"])]
        if len(last) >= MIN_LAST_NATIONS:
            return last, lg, f"{prev}-{prev + 1} League {letter_prev} ({len(last)})"
    if this:
        return this, this_league, f"{season}-{season + 1} League {letter} ({len(this)}, thin)"
    return None, None, "no record"


def nations_deviations(tid, season, before):
    ms, lg, label = nations_team_window(tid, season, before)
    if not ms:
        return None, label
    t, L = team_rates(ms, tid), league_rates(lg)

    def dev(a, b):
        return None if a is None or b is None else a - b
    return {
        "o25": dev(t["o25"], L["o25"]), "btts": dev(t["btts"], L["btts"]),
        "h1": dev(t["h1"], L["h1"]), "cards": dev(t["cards"], L["cards_pt"]),
        "cf": dev(t["cf"], L["corners_pt"]), "ca": dev(t["ca"], L["corners_pt"]),
        "gf": dev(t["gf"], L["gpt"]), "ga": dev(t["ga"], L["gpt"]),
    }, label


def nations_prior_rates(season, letter, before):
    ms = nations_league_matches(season, letter, before)
    if len(ms) >= MIN_PRIOR:
        return league_rates(ms), f"League {letter} {season}-{season + 1} to date ({len(ms)})"
    prev = season - 2
    ms = nations_league_matches(prev, letter)
    return league_rates(ms), f"League {letter} {prev}-{prev + 1} ({len(ms)})"


def lean_tests(card, m, slug, season):
    """One test per family (two for team goals). Lean is worked out after the match."""
    before = m["utc"]
    if slug == "uefa.nations":
        dh, lh = nations_deviations(m["home_id"], season, before)
        da, la = nations_deviations(m["away_id"], season, before)
        letter = nations_divisions(season).get(m["home_id"]) or nations_divisions(season).get(m["away_id"])
        P, plabel = nations_prior_rates(season, letter, before) if letter else (None, "division unknown")
    else:
        dh, lh = deviations(m["home_id"], slug, season, before)
        da, la = deviations(m["away_id"], slug, season, before)
        P, plabel = prior_rates(slug, season, before)
    info = {"home_window": lh, "away_window": la, "prior": plabel}
    if P is None:
        return [], info
    if not dh or not da:
        return [], info
    hg, ag = m["hg"], m["ag"]
    goals, h1 = hg + ag, m["h1h"] + m["h1a"]
    cards = m["ch"] + m["ca"]
    corners = add(m["kh"], m["ka"])
    tests = []

    def over_under(fam, d, actual, line, p_over, label=None):
        if d is None or d == 0 or actual is None or line is None or p_over is None:
            return
        lean = "over" if d > 0 else "under"
        if actual == line:
            hit = None
        else:
            hit = (actual > line) == (lean == "over")
        tests.append({"family": fam, "lean": lean if not label else f"{label} {lean}",
                      "d": round(d, 3), "hit": hit,
                      "prior": p_over if lean == "over" else 1 - p_over,
                      "line": round(line, 2), "actual": actual})

    over_under("totals", add(dh["o25"], da["o25"]), goals, 2.5, P["o25"])
    d = add(dh["btts"], da["btts"])
    if d:
        lean = "yes" if d > 0 else "no"
        both = hg > 0 and ag > 0
        tests.append({"family": "btts", "lean": lean, "d": round(d, 3),
                      "hit": both == (lean == "yes"),
                      "prior": P["btts"] if lean == "yes" else 1 - P["btts"],
                      "line": None, "actual": "yes" if both else "no"})
    over_under("team", add(dh["gf"], da["ga"]), hg, P["gpt"], P["p_team_over"], "home")
    over_under("team", add(da["gf"], dh["ga"]), ag, P["gpt"], P["p_team_over"], "away")
    over_under("halves", add(dh["h1"], da["h1"]), h1, P["h1"], P["p_h1_over"], "1H goals")
    over_under("disc", add(dh["cards"], da["cards"]), cards, P["cards_pm"], P["p_cards_over"], "cards")
    over_under("corners", add(dh["cf"], da["ca"], da["cf"], dh["ca"]), corners,
               P["corners_pm"], P["p_corners_over"], "corners")
    gd = add(dh["gf"], -dh["ga"], -da["gf"], da["ga"])
    if gd:
        side = "home" if gd > 0 else "away"
        won = (hg > ag) if side == "home" else (ag > hg)
        p_side = P["home_win"] if side == "home" else P["away_win"]
        tests.append({"family": "1x2", "lean": side, "d": round(gd, 3), "hit": won,
                      "prior": p_side, "line": None, "actual": f"{hg}-{ag}"})
        decided = P["home_win"] + P["away_win"]
        tests.append({"family": "ah", "lean": f"{side} DNB", "d": round(gd, 3),
                      "hit": None if hg == ag else won,
                      "prior": p_side / decided if decided else None,
                      "line": 0, "actual": f"{hg}-{ag}"})
    for t in tests:
        row = card["rows"].get(t["family"], {})
        t["level"] = row.get("level")
        t["verdict"] = row.get("short")
    return tests, info


# ───────────────────────── picks ─────────────────────────

PICK_FAMILY = {
    "1x2": "1x2", "result": "1x2", "moneyline": "1x2", "double chance": "1x2",
    "ah": "ah", "asian handicap": "ah", "handicap": "ah", "dnb": "ah",
    "totals": "totals", "goals": "totals", "o/u": "totals", "total goals": "totals",
    "btts": "btts", "team goals": "team", "halves": "halves", "1h": "halves",
    "first half": "halves", "discipline": "disc", "cards": "disc", "fouls": "disc",
    "corners": "corners",
}


def read_picks(slate):
    path = f"picks_{slate}.md"
    if not os.path.exists(path):
        return []
    out = []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.split("#", 1)[0].strip()
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 3 or not re.fullmatch(r"f\d+", cells[0], re.I):
            continue
        fam = PICK_FAMILY.get(cells[1].lower()) or family_key(cells[1])
        price = num(cells[3]) if len(cells) > 3 and cells[3] else None
        stake = num(cells[4]) if len(cells) > 4 and cells[4] else 1.0
        out.append({"line": n, "fid": cells[0].lower(), "family": fam, "family_raw": cells[1],
                    "selection": cells[2], "price": price, "stake": stake or 1.0})
    return out


def _side(tok, card, m):
    tok = tok.strip().lower()
    if tok in ("home", "1", "h"):
        return "h"
    if tok in ("away", "2", "a"):
        return "a"
    hs = max(sim(tok, card["home"]), side_sim(tok, m["home_names"]))
    as_ = max(sim(tok, card["away"]), side_sim(tok, m["away_names"]))
    if max(hs, as_) < 0.5:
        return None
    return "h" if hs >= as_ else "a"


def _ou(value, line, direction):
    """Asian-style over/under on any line; returns a list of half-stake outcomes."""
    parts = [line] if (line * 4) % 2 == 0 else [line - 0.25, line + 0.25]
    res = []
    for ln in parts:
        if value == ln:
            res.append("P")
        else:
            res.append("W" if (value > ln) == (direction == "over") else "L")
    return res


def _ah(margin, line):
    parts = [line] if (line * 4) % 2 == 0 else [line - 0.25, line + 0.25]
    return ["P" if margin + ln == 0 else ("W" if margin + ln > 0 else "L") for ln in parts]


def _combine(parts):
    if len(parts) == 1:
        return {"W": "win", "L": "loss", "P": "push"}[parts[0]]
    s = set(parts)
    if s == {"W"}:
        return "win"
    if s == {"L"}:
        return "loss"
    if s == {"W", "P"}:
        return "half-win"
    if s == {"L", "P"}:
        return "half-loss"
    return "push"


def grade(pick, card, m):
    sel = pick["selection"].lower().strip()
    fam = pick["family"]
    hg, ag = m["hg"], m["ag"]
    ou = re.search(r"\b(over|under|o|u)\s*([0-9]+(?:\.[0-9]+)?)", sel)
    direction = ({"o": "over", "u": "under"}.get(ou.group(1), ou.group(1)) if ou else None)
    line = float(ou.group(2)) if ou else None
    pre = sel[:ou.start()].strip() if ou else sel

    if fam == "1x2":
        dc = {"1x": ("h", "d"), "x2": ("d", "a"), "12": ("h", "a")}
        res = "d" if hg == ag else ("h" if hg > ag else "a")
        key = sel.replace(" ", "").replace("/", "")
        if key in dc:
            return "win" if res in dc[key] else "loss"
        if sel in ("draw", "x", "d"):
            return "win" if res == "d" else "loss"
        s = _side(sel, card, m)
        return None if not s else ("win" if res == s else "loss")
    if fam == "ah":
        lm = re.search(r"([+-]?\d+(?:\.\d+)?)\s*$", sel)
        ln = 0.0 if ("dnb" in sel or not lm) else float(lm.group(1))
        tok = re.sub(r"dnb|[+-]?\d+(?:\.\d+)?\s*$", "", sel).strip()
        s = _side(tok, card, m)
        if not s:
            return None
        margin = hg - ag if s == "h" else ag - hg
        return _combine(_ah(margin, ln))
    if fam == "btts":
        both = hg > 0 and ag > 0
        if sel.startswith("y"):
            return "win" if both else "loss"
        if sel.startswith("n"):
            return "loss" if both else "win"
        return None
    if fam == "totals" and ou:
        return _combine(_ou(hg + ag, line, direction))
    if fam == "team" and ou:
        s = _side(pre, card, m)
        return None if not s else _combine(_ou(hg if s == "h" else ag, line, direction))
    if fam == "halves":
        half = "2h" if re.search(r"\b2h|second", sel) else "1h"
        h = (m["h1h"], m["h1a"]) if half == "1h" else (hg - m["h1h"], ag - m["h1a"])
        if "both teams to score" in sel or "btts" in sel:
            yn = re.search(r"\b(yes|no)\s*$", sel)
            if not yn:
                return None
            both = h[0] > 0 and h[1] > 0
            return "win" if both == (yn.group(1) == "yes") else "loss"
        if ou:
            return _combine(_ou(h[0] + h[1], line, direction))
        tok = re.sub(r"\b[12]h\b|first half|second half|result", "", sel).strip()
        res = "d" if h[0] == h[1] else ("h" if h[0] > h[1] else "a")
        if tok in ("draw", "x", "d"):
            return "win" if res == "d" else "loss"
        s = _side(tok, card, m)
        return None if not s else ("win" if res == s else "loss")
    if fam == "disc" and not ou:
        mc = re.search(r"^(.*?)\s+most\s+(?:cards|bookings)\b", sel)
        if mc:
            s = _side(mc.group(1), card, m)
            if not s:
                return None
            mine, theirs = (m["ch"], m["ca"]) if s == "h" else (m["ca"], m["ch"])
            return "push" if mine == theirs else ("win" if mine > theirs else "loss")
    if fam in ("disc", "corners") and ou:
        fouls = "foul" in sel or pick["family_raw"].lower() == "fouls"
        if fam == "corners":
            vals = (m["kh"], m["ka"])
        elif fouls:
            vals = (m["fh"], m["fa"])
        else:
            vals = (m["ch"], m["ca"])
        tok = re.sub(r"cards?|corners?|fouls?|bookings?|total", "", pre).strip()
        s = _side(tok, card, m) if tok else None
        value = (vals[0] if s == "h" else vals[1]) if s else add(*vals)
        return None if value is None else _combine(_ou(value, line, direction))
    return None


def payout(result, price, stake):
    """Profit in units for a result at a decimal price."""
    if price is None:
        return None
    return {
        "win": stake * (price - 1), "loss": -stake, "push": 0.0,
        "half-win": stake * (price - 1) / 2, "half-loss": -stake / 2,
    }.get(result)


# ───────────────────────── settle a slate ─────────────────────────

def slate_date(slate):
    p = f"fixtures_{slate}.md"
    if os.path.exists(p):
        m = re.search(r"(20\d\d)-(\d\d)-(\d\d)", open(p, encoding="utf-8").read(400))
        if m and m.group(2) + m.group(3) == slate:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return date(date.today().year, int(slate[:2]), int(slate[2:]))


def settle(slate, refresh=False):
    day = slate_date(slate)
    season = day.year if day.month >= 7 else day.year - 1
    cards = read_slate(slate)
    fixtures, unsettled = [], []
    for card in cards:
        slug = slug_for(card["competition"])
        if not slug:
            unsettled.append((card, "competition not mapped to ESPN"))
            continue
        m, score, swapped = find_match(card, slug, day, refresh)
        if not m:
            unsettled.append((card, f"no ESPN match found (best name score {score:.2f})"))
            continue
        if not m["done"]:
            unsettled.append((card, f"not finished on ESPN ({m['status']})"))
            continue
        if swapped:
            unsettled.append((card, "ESPN has home and away the other way round; check the card"))
            continue
        m["referee"] = referee_for(slug, m["id"])
        tests, info = ([], {"note": "cup or European tie: results only, no lean audit"})
        if slug in LEAGUES:
            tests, info = lean_tests(card, m, slug, season)
        fixtures.append({"card": {k: card[k] for k in ("fid", "title", "home", "away",
                                                          "competition", "rows", "tier")},
                         "match": {k: m[k] for k in m if not k.endswith("_names")},
                         "match_score": round(score, 2), "tests": tests, "info": info})

    picks = []
    by_fid = {f["card"]["fid"]: f for f in fixtures}
    cards_by_fid = {c["fid"]: c for c in cards}
    for p in read_picks(slate):
        f = by_fid.get(p["fid"])
        card = cards_by_fid.get(p["fid"])
        if not f:
            p.update(result=None, note="fixture not settled or not carded")
        else:
            m = dict(f["match"])
            m["home_names"] = [m["home"], f["card"]["home"]]
            m["away_names"] = [m["away"], f["card"]["away"]]
            p["result"] = grade(p, card or f["card"], m) if p["family"] else None
            p["note"] = "" if p["result"] else "could not read this selection"
        row = (card or {}).get("rows", {}).get(p["family"], {}) if card else {}
        p["level"] = row.get("level") or ("none" if not card else None)
        p["verdict"] = row.get("short") or ("no card" if not card else "")
        p["profit"] = payout(p["result"], p["price"], p["stake"]) if p.get("result") else None
        picks.append(p)

    os.makedirs(DATA, exist_ok=True)
    doc = {"slate": slate, "date": day.isoformat(), "settled_at": datetime.now(timezone.utc).isoformat(timespec="minutes"),
           "fixtures": fixtures, "picks": picks,
           "unsettled": [{"fid": c["fid"], "title": c["title"], "why": why} for c, why in unsettled]}
    json.dump(doc, open(os.path.join(DATA, f"results_{slate}.json"), "w", encoding="utf-8"), indent=1)
    write_results_md(doc)
    return doc


def pct(x):
    return "–" if x is None else f"{100 * x:.0f}%"


def write_results_md(doc):
    s = doc["slate"]
    L = [f"# results_{s} — {doc['date']} — settled {doc['settled_at'][:16].replace('T', ' ')} UTC",
         "# source: ESPN public scoreboard (final). 90-minute figures; cards = yellows + reds,",
         "# both teams, the count baselines_N.md uses. Written after the matches; never read by Phase 1–3.",
         "",
         "fid | fixture | FT (90') | HT | goals | BTTS | 1H goals | cards | corners | fouls | referee | note",
         "--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---"]
    for f in doc["fixtures"]:
        m = f["match"]
        corners = add(m["kh"], m["ka"])
        fouls = add(m["fh"], m["fa"])
        note = []
        if m["extra_time"]:
            note.append("went to extra time; 90' score used")
        if not m["reconciled"]:
            note.append("goal timeline does not reconcile with the score")
        L.append(" | ".join([
            f["card"]["fid"], f["card"]["title"], f"{m['hg']}–{m['ag']}", f"{m['h1h']}–{m['h1a']}",
            str(m["hg"] + m["ag"]), "yes" if m["hg"] and m["ag"] else "no",
            str(m["h1h"] + m["h1a"]), str(m["ch"] + m["ca"]),
            "–" if corners is None else f"{corners:.0f}", "–" if fouls is None else f"{fouls:.0f}",
            m.get("referee") or "–",
            "; ".join(note)]))
    for u in doc["unsettled"]:
        L.append(f"{u['fid']} | {u['title']} | – | – | – | – | – | – | – | – | – | NOT SETTLED: {u['why']}")

    L += ["", "## Lean audit",
          "Which way each family's pre-kickoff base rates leaned — both sides' rates against their",
          "own league line, from ESPN records dated before kickoff — worked out after the match.",
          "It is the engine checking itself, not a pick. ✓ landed on the lean, ✗ did not, · push.",
          ""]
    for f in doc["fixtures"]:
        c = f["card"]
        if not f["tests"]:
            L.append(f"- **{c['fid']} {c['title']}** — {f['info'].get('note') or 'no lean: ' + f['info'].get('home_window', '') + ' / ' + f['info'].get('away_window', '')}")
            continue
        bits = []
        for t in f["tests"]:
            mark = "·" if t["hit"] is None else ("✓" if t["hit"] else "✗")
            bits.append(f"{SHORT[t['family']]} [{t['verdict']}] {t['lean']} {mark}")
        i = f["info"]
        L.append(f"- **{c['fid']} {c['title']}** — " + " · ".join(bits)
                 + f"  _(windows: {i['home_window']} / {i['away_window']}; prior {i['prior']})_")

    if doc["picks"]:
        L += ["", "## Your picks", "",
              "fid | family | selection | card verdict | result | price | profit",
              "--- | --- | --- | --- | --- | --- | ---"]
        for p in doc["picks"]:
            L.append(" | ".join([p["fid"], p["family_raw"], p["selection"], p["verdict"] or "–",
                                 p["result"] or f"ungraded ({p['note']})",
                                 "–" if p["price"] is None else f"{p['price']:.2f}",
                                 "–" if p["profit"] is None else f"{p['profit']:+.2f}"]))
    open(f"results_{s}.md", "w", encoding="utf-8").write("\n".join(L) + "\n")


# ───────────────────────── scorecard ─────────────────────────

def band(p, n):
    return 1.645 * math.sqrt(p * (1 - p) / n) if n and 0 < p < 1 else 0.0


def agg(tests):
    dec = [t for t in tests if t["hit"] is not None and t["prior"] is not None]
    n = len(dec)
    if not n:
        return None
    hit = sum(t["hit"] for t in dec) / n
    prior = sum(t["prior"] for t in dec) / n
    return {"n": n, "hit": hit, "prior": prior, "edge": hit - prior, "band": band(hit, n)}


def cell(a):
    if not a:
        return "–"
    return f"{pct(a['hit'])} vs {pct(a['prior'])} (n={a['n']})"


def write_scorecard():
    docs = []
    for p in sorted(glob.glob(os.path.join(DATA, "results_*.json"))):
        docs.append(json.load(open(p, encoding="utf-8")))
    tests = [dict(t, slate=d["slate"]) for d in docs for f in d["fixtures"] for t in f["tests"]]
    picks = [dict(p, slate=d["slate"]) for d in docs for p in d["picks"]]
    settled = sum(len(d["fixtures"]) for d in docs)
    audited = sum(1 for d in docs for f in d["fixtures"] if f["tests"])
    slates = [d["slate"] for d in docs]

    L = ["# Scorecard — context engine verdicts against results", "",
         f"Updated {date.today().isoformat()} · slates {', '.join(slates)} · "
         f"{settled} fixtures settled, {audited} league fixtures in the lean audit.", "",
         "## How to read it",
         "After each match, settle.py works out which way the pre-kickoff base rates leaned in each",
         "family (both sides' rates against their own league line, ESPN records before kickoff) and",
         "checks whether the match landed on that side. **Hit** is how often it did. **Prior** is how",
         "often the same side lands across the league — what you would get without reading the card.",
         "**Edge** is the difference. If the verdicts work, Well-suited should show the widest edge and",
         "Dangerous the narrowest. ± is a rough 90% band on the hit rate: an edge inside it is noise.",
         "",
         "The lean ignores the referee, injuries and lineups, which the cards do weigh — so this tests",
         "the base-rate half of each verdict, not the whole of it. Cup and European ties are settled",
         "but left out of the audit: their teams have no shared league line.", ""]

    def level_table(title, pool, note=None):
        out = [f"## {title}", ""] + ([note, ""] if note else []) + [
            "verdict | tests | hit | prior | edge | ±90%", "--- | --- | --- | --- | --- | ---"]
        for lv in ("good", "ok", "bad"):
            a = agg([t for t in pool if t["level"] == lv])
            if a:
                out.append(f"{LEVEL[lv]} | {a['n']} | {pct(a['hit'])} | {pct(a['prior'])} | "
                           f"{100 * a['edge']:+.0f} pts | ±{100 * a['band']:.0f}")
        a = agg([t for t in pool if t["verdict"] == "Split"])
        if a:
            out.append(f"_of which Split_ | {a['n']} | {pct(a['hit'])} | {pct(a['prior'])} | "
                       f"{100 * a['edge']:+.0f} pts | ±{100 * a['band']:.0f}")
        return out + [""]

    stat = [t for t in tests if t["family"] not in ("1x2", "ah")]
    L += level_table(
        "By verdict — the six goal and stat families", stat,
        "The cleanest read. 1X2 and AH are left out here because their prior only knows home "
        "or away, so any strength-based lean beats it; read those two down their own column below.")
    L += level_table("By verdict, all eight families", tests)

    L += ["## By family", "",
          "family | Well-suited | OK | Dangerous | all",
          "--- | --- | --- | --- | ---"]
    for fam in FAMILY_KEYS:
        ft = [t for t in tests if t["family"] == fam]
        L.append(" | ".join([SHORT[fam]] + [cell(agg([t for t in ft if t["level"] == lv]))
                                            for lv in ("good", "ok", "bad")] + [cell(agg(ft))]))
    L += ["", "Each cell: hit vs prior (tests). Team goals counts two tests per fixture, one per side.", ""]

    L += ["## Your picks", ""]
    graded = [p for p in picks if p.get("result")]
    if not picks:
        L += ["No picks logged yet. Write `picks_N.md` before kickoff, one line per pick:", "",
              "```",
              "# fixture | family | selection | price (optional) | stake (optional)",
              "f5 | BTTS | yes | 1.72",
              "f5 | Halves | 1H over 1.5 | 2.10",
              "f10 | 1X2 | draw | 3.40 | 2",
              "f4 | AH | Liverpool -0.25",
              "f12 | Corners | over 9.5",
              "f18 | Cards | under 4.5",
              "f3 | Team goals | Auxerre over 0.5",
              "```", "",
              "Families: 1X2 (home/draw/away, 1X/X2/12, or a team), AH (team + line, or `team dnb`),",
              "Totals, BTTS, Team goals, Halves (1H/2H goals or result), Cards / Fouls, Corners",
              "(total, or team + over/under). Quarter lines settle as half win / half loss."]
    else:
        L += ["verdict on the card | picks | W–L–P | hit | staked | profit | ROI",
              "--- | --- | --- | --- | --- | --- | ---"]
        for lv, name in (("good", "Well-suited"), ("ok", "OK"), ("bad", "Dangerous"), ("none", "no card")):
            g = [p for p in graded if p["level"] == lv]
            if not g:
                continue
            w = sum(p["result"] in ("win", "half-win") for p in g)
            lo = sum(p["result"] in ("loss", "half-loss") for p in g)
            pu = sum(p["result"] == "push" for p in g)
            priced = [p for p in g if p["profit"] is not None]
            staked = sum(p["stake"] for p in priced)
            prof = sum(p["profit"] for p in priced)
            L.append(" | ".join([name, str(len(g)), f"{w}–{lo}–{pu}",
                                 pct(w / (w + lo)) if w + lo else "–",
                                 f"{staked:.1f}" if priced else "–",
                                 f"{prof:+.2f}" if priced else "–",
                                 pct(prof / staked) if staked else "–"]))
        bad = [p for p in picks if not p.get("result")]
        if bad:
            L += ["", f"{len(bad)} pick(s) could not be graded — see the Your picks table in each results_N.md."]
    open("scorecard.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    return tests, picks


# ───────────────────────── main ─────────────────────────

def v4_slates():
    found = {re.search(r"fx_(\d{4})_f", p).group(1) for p in glob.glob("fx_[0-9][0-9][0-9][0-9]_f*.html")}
    return sorted(s for s in found if slate_date(s) < date.today())


def check(refresh=False):
    for slug in ("eng.1", "esp.1", "ita.1", "ger.1", "fra.1"):
        for season in (2025, 2026):
            ms = season_matches(slug, season, refresh)
            r = league_rates(ms)
            bad = sum(not m["reconciled"] for m in ms)
            print(f"{slug} {season}/{(season + 1) % 100}: {r['n']} matches · {r['gpg']:.2f} gpg · "
                  f"O2.5 {pct(r['o25'])} · BTTS {pct(r['btts'])} · 1H {r['h1']:.2f} · "
                  f"cards {r['cards_pm']:.2f} · corners/team {r['corners_pt']:.2f} · "
                  f"home win {pct(r['home_win'])} · timeline mismatches {bad}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("slates", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--scorecard", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    if a.check:
        check(a.refresh)
        return
    slates = v4_slates() if a.all else a.slates
    for s in slates:
        doc = settle(s, a.refresh)
        n_t = sum(len(f["tests"]) for f in doc["fixtures"])
        print(f"{s}: {len(doc['fixtures'])} settled, {len(doc['unsettled'])} not, "
              f"{n_t} lean tests, {len(doc['picks'])} picks -> results_{s}.md")
        for u in doc["unsettled"]:
            print(f"   {u['fid']} {u['title']}: {u['why']}")
    if slates or a.scorecard:
        write_scorecard()
        print("scorecard.md rebuilt")
    if not (slates or a.scorecard):
        ap.print_help()


if __name__ == "__main__":
    main()
