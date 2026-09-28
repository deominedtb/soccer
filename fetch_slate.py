#!/usr/bin/env python3
"""
fetch_slate.py — Phase 1A of CONTEXT ENGINE v4.

Pulls the day's fixture list straight from ESPN's public scoreboard
endpoint. No key, no scraping, no search budget spent. Prices are not
requested and not parsed: this script cannot produce a price.

    python3 fetch_slate.py                      # today, leagues.txt
    python3 fetch_slate.py 2026-09-19           # a given date
    python3 fetch_slate.py 2026-09-19 --n 12    # writes fixtures_12.md
    python3 fetch_slate.py --leagues ita.1,esp.1

Writes fixtures_N.md and progress_N.md in the current directory and
prints the table to stdout. Kickoffs are converted to Europe/Rome.

leagues.txt is one slug per line, "#" comments allowed. Verify slugs
once against
    https://sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000
and do not trust a slug you have not seen in that list.
"""

import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, date as _date
from zoneinfo import ZoneInfo

BASE = "https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/scoreboard?dates={ymd}&limit=200"
ROME = ZoneInfo("Europe/Rome")
UA = {"User-Agent": "Mozilla/5.0 (context-engine)"}

DEFAULT_LEAGUES = [
    "ita.1", "esp.1", "eng.1", "ger.1", "fra.1",
    "ned.1", "por.1", "bel.1", "aut.1", "sui.1",
    "uefa.champions", "uefa.europa", "uefa.europa_conf",
]


def read_leagues(explicit):
    if explicit:
        return [s.strip() for s in explicit.split(",") if s.strip()]
    try:
        with open("leagues.txt", encoding="utf-8") as fh:
            out = []
            for line in fh:
                line = line.split("#", 1)[0].strip()
                if line:
                    out.append(line)
            if out:
                return out
    except FileNotFoundError:
        pass
    return DEFAULT_LEAGUES


def fetch(slug, ymd):
    url = BASE.format(slug=slug, ymd=ymd)
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:                      # noqa: BLE001
        return None, type(e).__name__


def parse(doc, slug):
    rows = []
    league_name = slug
    leagues = doc.get("leagues") or []
    if leagues:
        league_name = leagues[0].get("name") or slug
    for ev in doc.get("events", []):
        comp = (ev.get("competitions") or [{}])[0]
        state = ((comp.get("status") or {}).get("type") or {}).get("state", "")
        if state not in ("pre", ""):            # only unplayed fixtures
            continue
        try:
            ko = datetime.strptime(ev["date"], "%Y-%m-%dT%H:%MZ")
            ko = ko.replace(tzinfo=ZoneInfo("UTC")).astimezone(ROME)
            kickoff = ko.strftime("%Y-%m-%d %H:%M")
        except Exception:                        # noqa: BLE001
            kickoff = ""
        home = away = ""
        for c in comp.get("competitors", []):
            name = (c.get("team") or {}).get("displayName", "")
            if c.get("homeAway") == "home":
                home = name
            else:
                away = name
        venue = (comp.get("venue") or {}).get("fullName", "")
        rows.append({
            "league": league_name,
            "slug": slug,
            "kickoff": kickoff,
            "venue": venue,
            "home": home,
            "away": away,
            "id": ev.get("id", ""),
        })
    return rows


def main(argv):
    ymd_arg, n, leagues_arg = None, None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--n":
            i += 1
            n = argv[i]
        elif a == "--leagues":
            i += 1
            leagues_arg = argv[i]
        else:
            ymd_arg = a
        i += 1

    d = datetime.strptime(ymd_arg, "%Y-%m-%d").date() if ymd_arg else _date.today()
    ymd = d.strftime("%Y%m%d")
    n = n or d.strftime("%m%d")

    rows, failed = [], []
    for slug in read_leagues(leagues_arg):
        doc, err = fetch(slug, ymd)
        if err:
            failed.append(f"{slug} ({err})")
            continue
        rows.extend(parse(doc, slug))

    rows.sort(key=lambda r: (r["kickoff"], r["league"]))

    fx = [f"# fixtures_{n} — {d.isoformat()} — pulled {datetime.now(ROME):%Y-%m-%d %H:%M} Europe/Rome",
          "# source: ESPN public scoreboard. No prices requested or parsed.",
          "",
          "league | kickoff | venue | home | away | matchday | source"]
    pr = []
    for idx, r in enumerate(rows, 1):
        venue = r["venue"] or "-"
        fx.append(f"{r['league']} | {r['kickoff']} | {venue} | {r['home']} | "
                  f"{r['away']} |  | espn:{r['slug']}/{r['id']}")
        pr.append(f"f{idx} | {r['kickoff'][-5:]} | {r['home']} – {r['away']} | TODO")

    if failed:
        fx.append("")
        fx.append("# not reached: " + ", ".join(failed))

    with open(f"fixtures_{n}.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(fx) + "\n")
    with open(f"progress_{n}.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(pr) + "\n")

    print("\n".join(fx))
    print(f"\n{len(rows)} fixtures -> fixtures_{n}.md, progress_{n}.md")
    if failed:
        print("not reached: " + ", ".join(failed))


if __name__ == "__main__":
    main(sys.argv[1:])
