# baselines_0918

Five competitions on this slate, one fixture each. The 2025–26 lines are
carried verbatim from baselines_0917.md / baselines_0916.md — those seasons
are complete, the figures cannot have changed, and no baseline search was
spent re-establishing them. The 2026–27 lines below are new and were
computed, not searched: every completed league match of this season was
read from ESPN's public match record (results for the goal-based rates,
per-match boxscores for corners, fouls and cards, key-event periods for
first-half goals) and every club's season statistics object for the
aggregate card, foul, corner and xG totals. Understat's league data is
used as the independent xG cross-check and for PPDA and deep completions.

Counting conventions match the earlier files: cards per game is yellows
plus reds per match; corners and fouls are per team per match; clean
sheet / failed to score is per team-appearance; first-half goals is per
match, both sides.

---

## Bundesliga

### 2025–26 (306 matches) — carried from baselines_0917.md
- goals per game 3.24; over 2.5 63.7%; BTTS 61.8%; home win 43.8% — Understat league data, counted
- cards per game 3.82 (1,116 Y + 52 R / 306); corners 4.88 per team; fouls 10.4 per team per match — FotMob 54/26891
- xG 1.70 per team per match — Understat getLeagueData/Bundesliga/2025, counted over 612 team-matches (new this slate)

### 2026–27 so far (27 matches, matchdays 1–3)
- goals per game 3.85; over 2.5 81.5%; BTTS 59.3%; home win 51.9%; draw 18.5%
- clean sheet / failed to score 24.1% per team-appearance
- first-half goals 1.37 per match
- cards per game 3.22 (84 Y + 3 R / 27); fouls 11.24 per team; corners 5.72 per team
- xG 1.71 per team per match (ESPN season objects); 1.97 (Understat, 54 team-matches)
- The 3.85 and 81.5% figures reproduce the line already in baselines_0917.md
  from an independent FotMob count, which is why this file trusts the method.

## Serie A

### 2025–26 (380 matches) — carried from baselines_0917.md
- goals per game 2.43; over 2.5 45.8%; BTTS 45.3%; home win 38.9% — Wikipedia results grid, counted
- cards per game 3.77 (1,366 Y + 68 R / 380); corners 4.41 per team; fouls 12.7 per team per match — FotMob 55/27044
- xG 1.40 per team per match — Understat getLeagueData/Serie_A/2025, 760 team-matches (new this slate)

### 2026–27 so far (40 matches, giornate 1–4)
- goals per game 3.02; over 2.5 57.5%; BTTS 60.0%; home win 42.5%; draw 15.0%
- clean sheet / failed to score 20.0% per team-appearance
- first-half goals 1.23 per match
- cards per game 3.08 (121 Y + 2 R / 40); fouls 11.25 per team; corners 4.74 per team
- xG 1.45 per team per match (ESPN); 1.71 (Understat, 80 team-matches)

## Ligue 1

### 2025–26 (306 matches) — carried from baselines_0917.md
- goals per game 2.82; over 2.5 52.6%; BTTS 50.7%; home win 46.1% — Understat league data, counted
- cards per game 3.90 (1,119 Y + 75 R / 306); corners 4.79 per team; fouls 12.1 per team per match — FotMob 53/27212
- xG 1.51 per team per match — Understat getLeagueData/Ligue_1/2025, 612 team-matches (new this slate)

### 2026–27 so far (36 matches, journées 1–4)
- goals per game 2.75; over 2.5 52.8%; BTTS 55.6%; home win 27.8%; draw 36.1%
- clean sheet / failed to score 27.8% per team-appearance
- first-half goals 1.22 per match
- cards per game 2.97 (102 Y + 5 R / 36); fouls 11.74 per team; corners 4.83 per team
- xG 1.55 per team per match (ESPN); 1.66 (Understat, 72 team-matches)
- The home-win collapse (27.8% against 46.1% last season, with 36.1% draws)
  is the single most extreme divisional number on this slate and is reported
  as an observed rate over 36 matches, not as a trend.

## Premier League

### 2025–26 (380 matches) — carried from baselines_0917.md
- goals per game 2.75; over 2.5 55.0%; BTTS 56.1%; home win 42.6% — Understat league data, counted
- cards per game 3.86 (1,424 Y + 44 R / 380); corners 4.98 per team; fouls 10.8 per team per match — FotMob 47/27110
- xG 1.53 per team per match — Understat getLeagueData/EPL/2025, 760 team-matches (new this slate)

### 2026–27 so far (40 matches, matchweeks 1–4)
- goals per game 2.85; over 2.5 52.5%; BTTS 52.5%; home win 32.5%; draw 35.0%
- clean sheet / failed to score 28.8% per team-appearance
- first-half goals 1.30 per match
- cards per game 3.98 (154 Y + 5 R / 40); fouls 11.65 per team; corners 4.56 per team
- xG 1.46 per team per match (ESPN); 1.64 (Understat, 80 team-matches)

## LaLiga

### 2025–26 (380 matches) — carried from baselines_0917.md
- goals per game 2.69; over 2.5 50.0%; BTTS 56.6%; home win 48.9% — FotMob fixtures list, counted
- cards per game 4.52 (1,612 Y + 107 R / 380); corners 4.83 per team; fouls 12.6 per team per match; xG 1.35 per team — FotMob 87/27233
- xG 1.50 per team per match — Understat getLeagueData/La_liga/2025, 760 team-matches (new this slate; the FotMob 1.35 above is left in place as the figure the earlier files used)

### 2026–27 so far (59 matches, jornadas 1–6 plus part of 7)
- goals per game 3.05; over 2.5 55.9%; BTTS 55.9%; home win 45.8%; draw 23.7%
- clean sheet / failed to score 25.4% per team-appearance
- first-half goals 1.42 per match
- cards per game 4.46 (248 Y + 15 R / 59); fouls 12.37 per team; corners 4.97 per team
- xG 1.46 per team per match (ESPN); 1.65 (Understat, 118 team-matches)
- 59 matches, not 60: one jornada 1–6 fixture is missing from the completed
  record. It is counted as unplayed rather than imputed.

---

## Cross-slate note
Every one of the five divisions is scoring above its own 2025–26 rate at
this point of 2026–27 — Bundesliga +0.61 goals per game, Serie A +0.59,
Premier League +0.10, LaLiga +0.36, Ligue 1 −0.07 the only exception. The
samples are 27 to 59 matches and none of them is a season. Where a card
below leans on a 2026–27 divisional figure it says which of the two
baselines it is using, because the gap between them is wider than the gap
between most clubs on this slate.

## Sources for the 2026–27 lines
- ESPN public match record, per competition: `site.api.espn.com/apis/site/v2/sports/soccer/{ger.1,ita.1,fra.1,eng.1,esp.1}/teams/{id}/schedule?season=2026` for the completed match list, `/summary?event={id}` for each match's boxscore and key events.
- ESPN season statistics objects: `sports.core.api.espn.com/v2/sports/soccer/leagues/{slug}/seasons/2026/types/1/teams/{id}/statistics/0` for every club in each division.
- Understat `getLeagueData/{Bundesliga,Serie_A,Ligue_1,EPL,La_liga}/{2025,2026}` for xG, npxG, PPDA and deep completions.
