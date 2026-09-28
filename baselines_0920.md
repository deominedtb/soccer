# baselines_0920

Five competitions on this slate — Premier League, LaLiga, Serie A,
Bundesliga, Ligue 1 — the same five as slates 0918 and 0919. Every line
below was recomputed from ESPN's public match record, not searched: 1,751
completed 2025–26 league matches and 230 completed 2026–27 ones, each read
from its own match summary (boxscore for fouls, cards, corners and shots;
key events for goal minute and scoring side; gameInfo for venue and
referee), with Understat as the independent xG source. **Zero baseline
searches were spent.**

**Hosts.** `site.api.espn.com` again returned HTTP 403 (Akamai access
denied) from this machine, as on 0919. The identical data is served by
`site.web.api.espn.com`, which is what every figure below and on every
card of this slate was taken from. Event lists came from
`sports.core.api.espn.com`. Understat's league pages are client-side; the
endpoint the page itself calls is `understat.com/getLeagueData/{league}/{season}`,
which requires the XMLHttpRequest and Referer headers.

**Method validation.** Three checks the pipeline had to pass before any
figure here was used.
1. The goal-timing parser was reconciled against the official final score
   on **every** match, not a sample: 1,751 of 1,751 for 2025–26 and 230 of
   230 for 2026–27. The first-half figures rest on that. The reconciliation
   also settled a convention: ESPN attributes an own goal to the team that
   *benefits* from it, not to the scorer's team. Flipping it, as an earlier
   run did, breaks 125 matches; not flipping it breaks none.
2. The 2025–26 lines reproduce baselines_0919.md and baselines_0918.md,
   which were built by independent counts off FotMob, Wikipedia and
   Understat rather than off this pipeline, to within rounding on every
   row of all five divisions.
3. The 2025–26 Understat xG figures reproduce baselines_0919.md exactly:
   EPL 1.53, LaLiga 1.50, Serie A 1.40, Bundesliga 1.70, Ligue 1 1.51.

**Known gap.** ESPN's Ligue 1 2025–26 event list holds 305 matches, not
306 — Toulouse and Nantes are each recorded with 33 matches played in the
standings against 34 for the rest of the division. One fixture is missing
from the public record. The Ligue 1 2025–26 lines below are therefore
computed over 305 matches and differ from a 306-match count in the second
decimal. Stated, not repaired.

Counting conventions match the earlier files: **cards per game is yellows
plus reds per match, both teams**; corners and fouls are **per team** per
match; clean sheet / failed to score is per team-appearance; first-half
goals is per match, both sides. On a fixture card the per-team card and
foul figures are labelled as such, because a team line of 2.18 and a
league line of 3.77 are the same units seen from different sides.

---

## Premier League

### 2025–26 (380 matches)
- goals per game 2.75; over 2.5 55.0%; BTTS 56.1%; home win 42.6%; draw 22.6%
- clean sheet / failed to score 25.5% per team-appearance
- first-half goals 1.19 per match
- cards per game 3.86; fouls 10.82 per team; corners 5.00 per team; shots 12.4 per team
- xG 1.53 per team per match — Understat, 760 team-matches

### 2026–27 so far (46 matches, matchweeks 1–4 plus six of 5)
- goals per game 2.83; over 2.5 54.3%; BTTS 50.0%; home win 37.0%; draw 26.1%
- clean sheet / failed to score 29.3% per team-appearance
- first-half goals 1.26 per match
- cards per game 3.91; fouls 11.40 per team; corners 4.68 per team
- xG 1.63 per team per match — Understat, 92 team-matches

## LaLiga

### 2025–26 (380 matches)
- goals per game 2.69; over 2.5 50.0%; BTTS 56.6%; home win 48.9%; draw 22.4%
- clean sheet / failed to score 23.7% per team-appearance
- first-half goals 1.15 per match
- cards per game 4.52; fouls 12.58 per team; corners 4.86 per team; shots 12.1 per team
- xG 1.50 per team per match — Understat, 760 team-matches

### 2026–27 so far (64 matches, jornadas 1–6 plus four of 7)
- goals per game 3.05; over 2.5 56.2%; BTTS 56.2%; home win 43.8%; draw 21.9%
- clean sheet / failed to score 25.8% per team-appearance
- first-half goals 1.42 per match
- cards per game 4.44; fouls 12.41 per team; corners 4.82 per team
- xG 1.62 per team per match — Understat, 128 team-matches

## Serie A

### 2025–26 (380 matches)
- goals per game 2.43; over 2.5 45.8%; BTTS 45.3%; home win 38.9%; draw 26.8%
- clean sheet / failed to score 32.1% per team-appearance
- first-half goals 1.04 per match
- cards per game 3.77; fouls 12.67 per team; corners 4.43 per team; shots 12.6 per team
- xG 1.40 per team per match — Understat, 760 team-matches

### 2026–27 so far (45 matches, giornate 1–4 plus five of 5)
- goals per game 2.96; over 2.5 55.6%; BTTS 60.0%; home win 40.0%; draw 17.8%
- clean sheet / failed to score 20.0% per team-appearance
- first-half goals 1.16 per match
- cards per game 3.22; fouls 11.21 per team; corners 4.78 per team
- xG 1.71 per team per match — Understat, 90 team-matches

The division's most striking early gap is disciplinary, not attacking:
3.22 cards per game against 3.77 last season, on 11.21 fouls per team
against 12.67. Serie A 2026–27 is so far both cleaner and more open than
the Serie A that finished in May.

## Bundesliga

### 2025–26 (306 matches)
- goals per game 3.24; over 2.5 63.7%; BTTS 61.8%; home win 43.8%; draw 21.9%
- clean sheet / failed to score 21.1% per team-appearance
- first-half goals 1.44 per match
- cards per game 3.82; fouls 10.43 per team; corners 4.89 per team; shots 13.1 per team
- xG 1.70 per team per match — Understat, 612 team-matches

### 2026–27 so far (33 matches, matchdays 1–3 plus three of 4)
- goals per game 3.97; over 2.5 81.8%; BTTS 60.6%; home win 51.5%; draw 15.2%
- clean sheet / failed to score 22.7% per team-appearance
- first-half goals 1.45 per match
- cards per game 3.67; fouls 11.32 per team; corners 5.42 per team
- xG 2.01 per team per match — Understat, 66 team-matches

3.97 goals per game and 81.8% over 2.5 are the most extreme divisional
figures on this slate, and they rest on 33 matches. The same division's
completed 2025–26 season reads 3.24 and 63.7%. The gap between the two
baselines is wider than the gap between most clubs, and the Understat xG
line agrees with the goals rather than contradicting it (2.01 against
1.70), which is the one thing that makes the run harder to dismiss as
finishing variance.

## Ligue 1

### 2025–26 (305 of 306 matches — see Known gap)
- goals per game 2.83; over 2.5 52.8%; BTTS 50.8%; home win 46.2%; draw 23.0%
- clean sheet / failed to score 28.4% per team-appearance
- first-half goals 1.22 per match
- cards per game 3.91; fouls 12.08 per team; corners 4.82 per team; shots 12.3 per team
- xG 1.51 per team per match — Understat, 612 team-matches

### 2026–27 so far (42 matches, journées 1–4 plus six of 5)
- goals per game 2.83; over 2.5 57.1%; BTTS 57.1%; home win 38.1%; draw 33.3%
- clean sheet / failed to score 26.2% per team-appearance
- first-half goals 1.19 per match
- cards per game 3.21; fouls 12.10 per team; corners 4.79 per team
- xG 1.65 per team per match — Understat, 84 team-matches

Ligue 1 is the only one of the five scoring at exactly its own 2025–26
rate (2.83 against 2.83) while its over-2.5 share rises — more matches
clearing the line, the same goals in total, spread more evenly. The
home-win depression flagged on slates 0918 and 0919 persists at 38.1%
against 46.2%, with a 33.3% draw rate. Reported as an observed rate over
42 matches, not as a trend.

---

## Second-tier baselines (2025–26)

Four clubs carded on this slate played 2025–26 in the division below, so
their last-season rates are second-tier rates and cannot be read against
the top-flight lines above. These divisional lines are computed by the
same pipeline from the same match records, so a promoted club's rate and
the line it is read against are counted identically.

**Understat does not cover any second tier, so no 2025–26 xG exists for a
promoted club on this slate, and none is estimated.**

### LaLiga 2 (468 matches) — Málaga (f2), Deportivo (f15)
- goals per game 2.63; over 2.5 50.2%; BTTS 56.0%; home win 44.4%; draw 25.2%
- clean sheet / failed to score 26.2%; first-half goals 1.17 per match
- cards per game 5.31; fouls 13.38 per team; corners 4.74 per team

### Serie B (390 matches) — Frosinone (f7)
- goals per game 2.54; over 2.5 48.2%; BTTS 53.3%; home win 44.9%; draw 31.3%
- clean sheet / failed to score 27.3%; first-half goals 1.13 per match
- cards per game 4.52; fouls 14.98 per team; corners 4.77 per team

### 2. Bundesliga (306 matches) — Schalke 04 and Elversberg (f13)
- goals per game 2.93; over 2.5 57.8%; BTTS 59.5%; home win 46.1%; draw 24.2%
- clean sheet / failed to score 22.9%; first-half goals 1.30 per match
- cards per game 4.65; fouls 12.30 per team; corners 5.02 per team

The disciplinary step between divisions is the one that matters most for
reading a promoted club's card rate: LaLiga 2 books 5.31 per match against
LaLiga's 4.52, Serie B 4.52 against Serie A's 3.77, 2. Bundesliga 4.65
against the Bundesliga's 3.82. A promoted side's last-season cards figure
is drawn from a harsher division in all three cases, and on this slate
every promoted club's card rate is therefore quoted against its own
second-tier line, never against the top-flight one.

---

## Cross-slate note
Four of the five divisions are scoring above their own 2025–26 rate at
this point of 2026–27 — Bundesliga +0.73 goals per game, Serie A +0.53,
LaLiga +0.36, Premier League +0.08 — and Ligue 1 is level at +0.00. The
samples are 33 to 64 matches and none of them is a season. Where a card
leans on a 2026–27 divisional figure it says which of the two baselines it
is using. Three of the five are also booking *less* than last season
(Serie A −0.55, Ligue 1 −0.70, Bundesliga −0.15) on *more* fouls in four
divisions, which is a referee-interpretation pattern, not a team one, and
it is why the referee row on every card of this slate is read against the
2026–27 divisional card line rather than the completed season.

## Sources for every line above
- ESPN event lists: `sports.core.api.espn.com/v2/sports/soccer/leagues/{eng.1,esp.1,ita.1,ger.1,fra.1,esp.2,ita.2,ger.2}/events?dates=…&limit=500` (paged).
- ESPN match summaries: `site.web.api.espn.com/apis/site/v2/sports/soccer/{slug}/summary?event={id}` — boxscore statistics (fouls, yellow and red cards, corners, shots, shots on target, possession), keyEvents (goal minute and scoring side), gameInfo (venue, officials). 2,915 matches read in total.
- ESPN standings: `site.web.api.espn.com/apis/v2/sports/soccer/{slug}/standings?season={2026,2025,2024,2023}` for position, points, goals and matches played, and for which clubs are promoted and how long they were away.
- Understat `getLeagueData/{EPL,La_liga,Serie_A,Bundesliga,Ligue_1}/{2025,2026}` for per-match xG, npxG, xGA, PPDA and deep completions.
