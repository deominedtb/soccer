# baselines_0919

Five competitions on this slate — Premier League, LaLiga, Serie A,
Bundesliga, Ligue 1 — the same five as slate 0918. The 2025–26 lines are
carried verbatim from baselines_0918.md: those seasons are complete, the
figures cannot have changed, and no baseline search was spent
re-establishing them. The 2026–27 lines below were recomputed, not
searched, from every completed league match of this season in ESPN's
public match record (results for the goal-based rates, per-match
boxscores for corners, fouls and cards, key events for first-half goals),
with Understat as the independent xG source.

**Host change.** `site.api.espn.com` returned HTTP 403 (Akamai access
denied) from this machine all day on 2026-09-19. The identical data is
served by `site.web.api.espn.com`, which is what every figure below and
on every card of this slate was taken from. Understat's league pages are
client-side; the endpoint the page itself calls is
`understat.com/getLeagueData/{league}/{season}`, which requires the
XMLHttpRequest and Referer headers and returns gzip.

**Method validation.** Before any figure here was used, the pipeline was
checked against two independent things it had to reproduce.
1. The goal-timing parser was reconciled against final scores on 203
   matches across all five divisions and both seasons: goals extracted
   from key events matched the official score in 203 of 203, own goals
   included. First-half figures below rest on that.
2. The recomputed 2026–27 lines reproduce baselines_0918.md, which was
   built yesterday by an independent count, on every row within the one
   extra matchday each division has since played. The 2025–26 Understat
   xG figures reproduce that file exactly (EPL 1.53, LaLiga 1.50, Serie A
   1.40, Bundesliga 1.70, Ligue 1 1.51).

Counting conventions match the earlier files: cards per game is yellows
plus reds per match; corners and fouls are per team per match; clean
sheet / failed to score is per team-appearance; first-half goals is per
match, both sides.

---

## Premier League

### 2025–26 (380 matches) — carried from baselines_0918.md
- goals per game 2.75; over 2.5 55.0%; BTTS 56.1%; home win 42.6% — Understat league data, counted
- cards per game 3.86 (1,424 Y + 44 R / 380); corners 4.98 per team; fouls 10.8 per team per match — FotMob 47/27110
- xG 1.53 per team per match — Understat, 760 team-matches

### 2026–27 so far (41 matches, matchweeks 1–4 plus one of 5)
- goals per game 2.85; over 2.5 53.7%; BTTS 51.2%; home win 34.1%; draw 34.1%
- clean sheet / failed to score 29.3% per team-appearance
- first-half goals 1.27 per match
- cards per game 3.93; fouls 11.57 per team; corners 4.65 per team
- xG 1.46 per team per match (ESPN season objects); 1.64 (Understat, 82 team-matches)
- 41 matches, not 40: the 18 September Brentford–Chelsea fixture from
  slate 0918 is now in the completed record.

## LaLiga

### 2025–26 (380 matches) — carried from baselines_0918.md
- goals per game 2.69; over 2.5 50.0%; BTTS 56.6%; home win 48.9% — FotMob fixtures list, counted
- cards per game 4.52 (1,612 Y + 107 R / 380); corners 4.83 per team; fouls 12.6 per team per match
- xG 1.50 per team per match — Understat, 760 team-matches

### 2026–27 so far (60 matches, jornadas 1–6 plus part of 7)
- goals per game 3.07; over 2.5 56.7%; BTTS 56.7%; home win 45.0%; draw 23.3%
- clean sheet / failed to score 25.0% per team-appearance
- first-half goals 1.43 per match
- cards per game 4.48; fouls 12.36 per team; corners 4.94 per team
- xG 1.46 per team per match (ESPN); 1.64 (Understat, 120 team-matches)
- 60 matches now, against 59 yesterday: Espanyol–Elche is in the record.
  Jornada 7 is spread across the week, and Athletic Club have played 5
  league matches where most of the division has played 6 — one of their
  earlier fixtures is outstanding, not missing from the count.

## Serie A

### 2025–26 (380 matches) — carried from baselines_0918.md
- goals per game 2.43; over 2.5 45.8%; BTTS 45.3%; home win 38.9% — Wikipedia results grid, counted
- cards per game 3.77 (1,366 Y + 68 R / 380); corners 4.41 per team; fouls 12.7 per team per match
- xG 1.40 per team per match — Understat, 760 team-matches

### 2026–27 so far (41 matches, giornate 1–4 plus one of 5)
- goals per game 3.02; over 2.5 58.5%; BTTS 61.0%; home win 43.9%; draw 14.6%
- clean sheet / failed to score 19.5% per team-appearance
- first-half goals 1.20 per match
- cards per game 3.12; fouls 11.21 per team; corners 4.77 per team
- xG 1.45 per team per match (ESPN); 1.72 (Understat, 82 team-matches)
- The 14.6% draw rate is the lowest of the five divisions and the
  mirror image of Ligue 1's 35.1%. Both are 41 and 37 matches deep and
  neither is a season.

## Bundesliga

### 2025–26 (306 matches) — carried from baselines_0918.md
- goals per game 3.24; over 2.5 63.7%; BTTS 61.8%; home win 43.8% — Understat league data, counted
- cards per game 3.82 (1,116 Y + 52 R / 306); corners 4.88 per team; fouls 10.4 per team per match
- xG 1.70 per team per match — Understat, 612 team-matches

### 2026–27 so far (28 matches, matchdays 1–3 plus one of 4)
- goals per game 3.96; over 2.5 82.1%; BTTS 57.1%; home win 53.6%; draw 17.9%
- clean sheet / failed to score 25.0% per team-appearance
- first-half goals 1.43 per match
- cards per game 3.25; fouls 11.21 per team; corners 5.71 per team
- xG 1.71 per team per match (ESPN); 1.98 (Understat, 56 team-matches)
- 3.96 goals per game and 82.1% over 2.5 are the most extreme divisional
  figures anywhere on this slate, and they rest on 28 matches. The same
  division's completed 2025–26 season reads 3.24 and 63.7%. The gap
  between the two baselines is larger than the gap between most clubs.

## Ligue 1

### 2025–26 (306 matches) — carried from baselines_0918.md
- goals per game 2.82; over 2.5 52.6%; BTTS 50.7%; home win 46.1% — Understat league data, counted
- cards per game 3.90 (1,119 Y + 75 R / 306); corners 4.79 per team; fouls 12.1 per team per match
- xG 1.51 per team per match — Understat, 612 team-matches

### 2026–27 so far (37 matches, journées 1–4 plus one of 5)
- goals per game 2.76; over 2.5 54.1%; BTTS 56.8%; home win 29.7%; draw 35.1%
- clean sheet / failed to score 27.0% per team-appearance
- first-half goals 1.22 per match
- cards per game 2.95; fouls 11.74 per team; corners 4.84 per team
- xG 1.55 per team per match (ESPN); 1.65 (Understat, 74 team-matches)
- The home-win collapse flagged on slate 0918 has not corrected: 29.7%
  against 46.1% last season, with 35.1% draws. Reported as an observed
  rate over 37 matches, not as a trend. It is also the only division of
  the five scoring below its own 2025–26 goals per game.

---

## Second-tier baselines

Seven clubs carded on this slate played 2025–26 in a division below the
one they are in now, so their last-season rates are second-tier rates and
cannot be read against the top-flight baselines above. Where a card uses
one, the divisional line it is read against is computed by the same
pipeline and stated on that card. Understat does not cover any of these
divisions, so **no 2025–26 xG exists for a promoted club on this slate**
and none is estimated.

- Championship (eng.2) — Hull City, Coventry City, Ipswich Town
- LaLiga 2 (esp.2) — Racing Santander
- Serie B (ita.2) — Venezia
- Ligue 2 (fra.2) — Le Mans, Troyes

## Cross-slate note
Four of the five divisions are scoring above their own 2025–26 rate at
this point of 2026–27 — Bundesliga +0.72 goals per game, Serie A +0.59,
LaLiga +0.38, Premier League +0.10 — and Ligue 1 is the exception at
−0.06. The samples are 28 to 60 matches and none of them is a season.
Where a card leans on a 2026–27 divisional figure it says which of the
two baselines it is using.

## Sources for the 2026–27 lines
- ESPN public match record, per competition: `site.web.api.espn.com/apis/site/v2/sports/soccer/{eng.1,esp.1,ita.1,ger.1,fra.1}/teams/{id}/schedule?season={2026,2025}` for the completed match list, and `/summary?event={id}` for each match's boxscore (fouls, yellow and red cards, corners, shots, shots on target, possession), key events (goal minute and scoring team, for first-half goals) and gameInfo.officials (the match referee).
- ESPN season statistics objects: `sports.core.api.espn.com/v2/sports/soccer/leagues/{slug}/seasons/2026/types/1/teams/{id}/statistics/0` for expected goals and expected goals conceded per match. ESPN publishes no xG for 2025–26; that gap is filled from Understat, not estimated.
- ESPN standings: `site.web.api.espn.com/apis/v2/sports/soccer/{slug}/standings?season={2026,2025,2024,2023}` for position, points, goals and matches played, and for which clubs are promoted and how long they were away.
- Understat `getLeagueData/{EPL,La_liga,Serie_A,Bundesliga,Ligue_1}/{2025,2026}` for per-match xG, npxG, xGA, PPDA and deep completions.
