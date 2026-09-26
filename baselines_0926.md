# baselines_0926

UEFA Nations League 2026–27, matchday 1 (Groups A3, B1, C1, C3 and C4 open
today). Three divisions on this slate (League A, League B, League C); each
division's line is written the first time a fixture from it is carded, and
read from this file afterwards. 2026–27 has no completed match in any of
today's groups, so every line is a completed earlier edition of the same
division.

Method, as on 0919, 0920, 0924 and 0925: recomputed from ESPN's public match
record, not searched. Event lists from
`site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=YYYYMM`
(monthly queries), each match then read from its own summary — boxscore for
fouls, yellow and red cards, corners and shots; key events for goal minute,
scoring side and penalty kicks; group membership from
`…/uefa.nations/standings?season={2020,2022,2024,2026}`. **Zero baseline
searches spent.**

Counting conventions match the earlier files: cards per game is yellows plus
reds per match, both teams (ESPN boxscore); fouls, corners and shots are per
team per match; clean sheet / failed to score is per team-appearance;
first-half goals is per match, both sides. Penalties are penalty kicks taken
(scored, saved or missed) in ESPN's key events. No xG exists for this
competition in ESPN's record: **no divisional xG line, none estimated.**

---

## UEFA Nations League B — first carded on f1 (Slovenia – Scotland)

Recomputed for this slate from the same 90 summaries as the League B entries
in baselines_0924.md and baselines_0925.md; every figure below matches them.
The raw rerun gives 2024–25 goals 2.65, first-half goals 1.10 and 12 penalty
kicks because Wales 1–0 Montenegro (698976) has no key events in ESPN's
record; its 36th-minute Wilson penalty is added from ESPN's commentary, as on
0924 and 0925, and the goal-timing parser then reconciles against the
official score on 90 of 90.

### 2024–25 League B (48 matches — the primary line on every League B card)
Group stage only, four groups of four, six matches per side: B1 Czechia,
Ukraine, Georgia, Albania; B2 England, Greece, Finland, Republic of Ireland;
B3 Norway, Austria, Slovenia, Kazakhstan; B4 Türkiye, Wales, Iceland,
Montenegro. The March 2025 A/B and B/C play-offs are not in the line
(two-legged promotion/relegation ties, not group play).
Five of the sixteen are in 2026–27 League B (Austria, Republic of Ireland,
Slovenia, Ukraine, Georgia). Today's Group B1 has one of them: Slovenia (third
in B3, kept their place by beating Slovakia in the B/C play-off). Scotland and
Switzerland come down from League A (Scotland third in A1 and beaten by Greece
in the A/B play-off, Switzerland fourth in A4); North Macedonia come up from
League C (C4 winners).
- goals per game 2.67; over 2.5 50.0%; BTTS 43.8%; home win 45.8%; draw 18.8%; away win 35.4%
- clean sheet / failed to score 32.3% per team-appearance; under 1.5 goals 22.9% of matches; four 0–0s
- first-half goals 1.12 per match
- cards per game 4.42 (2.21 per team; 209 yellows, 3 reds); fouls 11.48 per team (22.96 per match); 5.20 fouls per card; corners 4.52 per team
- shots 12.68 per team; shots on target 4.19 per team
- penalty kicks 0.27 per match (13 in 48)

### 2022–23 League B (42 matches — cross-check, not the card line)
B1 Ukraine, Republic of Ireland, Armenia, Scotland; B2 Israel, Iceland,
Albania (Russia excluded, so B2 played six matches, not twelve); B3
Bosnia-Herzegovina, Finland, Romania, Montenegro; B4 Norway, Sweden,
Slovenia, Serbia. Group stage only.
- goals per game 2.67; over 2.5 47.6%; BTTS 52.4%; home win 45.2%; draw 28.6%; away win 26.2%
- clean sheet / failed to score 26.2% per team-appearance; under 1.5 goals 21.4%; two 0–0s
- first-half goals 1.07 per match
- cards per game 4.57 (2.29 per team; 184 yellows, 8 reds); fouls 11.17 per team; 4.89 fouls per card; corners 4.77 per team
- shots 11.61 per team; shots on target 3.99 per team
- penalty kicks 0.21 per match (9 in 42)

### Both editions pooled (90 matches)
- goals per game 2.67; over 2.5 48.9%; BTTS 47.8%; home win 45.6%; draw 23.3%
- first-half goals 1.10; cards per game 4.49; fouls 11.33 per team; 5.05 fouls per card; corners 4.64 per team; penalty kicks 0.24 per match

**League B is steady on volume, not on outcome.** Goals per match (2.67 in
both), first-half goals (1.12 against 1.07), cards (4.42 against 4.57), fouls
(11.48 against 11.17 per team) and corners (4.52 against 4.77) barely moved
between editions. The split of outcomes did: BTTS 43.8% against 52.4%, draws
18.8% against 28.6%, away wins 35.4% against 26.2%, reds 3 against 8. The
2024–25 line is printed because it is the most recent edition.

### Sides relegated from League A into League B (context line, not a baseline)
The eight sides relegated from League A for 2022–23 (Ukraine, Iceland,
Bosnia-Herzegovina, Sweden) and 2024–25 (Czechia, England, Austria, Wales), from
the same League B match rows: 46 matches, 1.72 points per match (W21 D16 L9),
1.72 scored and 1.07 conceded; over 2.5 50.0%, BTTS 56.5%, failed to score
13.0%. Away: 23 matches, 1.43 points per match (W8 D9 L6), 1.52 scored and
1.35 conceded, over 2.5 52.2%, BTTS 60.9%, failed to score 13.0%, corners 4.22
won and 4.65 conceded per match, cards 2.35 per match against their opponents'
1.74. Home: 23 matches, 2.00 points per match (W13 D7 L3). Matchday one: W3 D4
L1, seven of the eight away (W3 D3 L1 away; two of those seven were in
Ljubljana: Slovenia 0–2 Sweden in June 2022, Slovenia 1–1 Austria in September
2024). Group finishes: first four times (Bosnia-Herzegovina, Czechia, England,
Wales), second three times, fourth once (Sweden). All eight went down as
fourth-placed League A sides; Scotland come down through the March 2025 A/B
play-off, a route no side in this line took.

## Sources for every line above
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 90 League B matches; commentary of event 698976 for the Wilson penalty.
- ESPN standings `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}` for group membership, finishing positions and movement between divisions.

---

## UEFA Nations League C — first carded on f2 (San Marino – Finland)

Recomputed for this slate from the same 96 League C group summaries (48 per
edition) as the League C entry in baselines_0925.md, with the same counting
conventions as the League B entry above; every figure below matches that
entry. **Zero baseline searches spent.** Goal counts from key events
reconcile against the official score on 95 of 96. The exception is again
Romania – Kosovo, 15 November 2024 (698999): abandoned after the 90'+9'
whistle at 0–0 and awarded 3–0; it is counted as played, 0–0, with its box
score (10 cards, 26 fouls, 12 corners), and the line without it is given so
the effect is visible. No match went to extra time; every match has a
two-team box score. No xG exists for this competition in ESPN's record: **no
divisional xG line, none estimated.**

### 2024–25 League C (48 matches — the primary line on every League C card)
Group stage only, four groups of four, six matches per side: C1 Sweden,
Slovakia, Estonia, Azerbaijan; C2 Romania, Kosovo, Cyprus, Lithuania; C3
Northern Ireland, Bulgaria, Belarus, Luxembourg; C4 North Macedonia, Armenia,
Faroe Islands, Latvia. The play-offs (B/C March 2025, C/D March 2026) are not
in the line.
Nine of the sixteen are in 2026–27 League C (Armenia, Belarus, Bulgaria,
Cyprus, Estonia, Faroe Islands, Latvia, Luxembourg, Slovakia). Today's Group
C1 has one of them: Belarus (third in C3). Finland (fourth in B2) and Albania
(fourth in B1) come down from League B; San Marino (first in D1) come up from
League D.
- goals per game 2.40; over 2.5 47.9%; BTTS 37.5%; home win 41.7%; draw 25.0%; away win 33.3%
- clean sheet / failed to score 36.5% per team-appearance; under 1.5 goals 33.3% of matches; five 0–0s (the abandoned match one of them)
- first-half goals 1.15 per match
- cards per game 4.85 (2.43 per team; 225 yellows, 8 reds); fouls 12.91 per team (25.81 per match); 5.32 fouls per card; corners 4.58 per team
- shots 12.05 per team; shots on target 4.32 per team
- penalty kicks 0.38 per match (18 in 48)
- without Romania – Kosovo (47): goals 2.45; over 2.5 48.9%; BTTS 38.3%; home win 42.6%; first-half goals 1.17; cards 4.74; 5.44 fouls per card

### 2022–23 League C (48 matches — cross-check, not the card line)
C1 Türkiye, Luxembourg, Faroe Islands, Lithuania; C2 Greece, Kosovo, Northern
Ireland, Cyprus; C3 Kazakhstan, Azerbaijan, Slovakia, Belarus; C4 Georgia,
Bulgaria, North Macedonia, Gibraltar. Group stage only.
- goals per game 2.65; over 2.5 45.8%; BTTS 41.7%; home win 43.8%; draw 22.9%; away win 33.3%
- clean sheet / failed to score 32.3% per team-appearance; under 1.5 goals 25.0%; three 0–0s
- first-half goals 1.10 per match
- cards per game 4.21 (2.10 per team; 193 yellows, 9 reds); fouls 11.16 per team; 5.30 fouls per card; corners 4.36 per team
- shots 11.62 per team; shots on target 3.98 per team
- penalty kicks 0.29 per match (14 in 48)

### Both editions pooled (96 matches)
- goals per game 2.52; over 2.5 46.9%; BTTS 39.6%; home win 42.7%; draw 24.0%
- first-half goals 1.12; cards per game 4.53; fouls 12.03 per team; 5.31 fouls per card; corners 4.47 per team; penalty kicks 0.33 per match

**League C is steady on outcome and first halves, not on volume.** Home wins
(41.7% against 43.8%), away wins (33.3% in both), over 2.5 (47.9% against
45.8%) and first-half goals (1.15 against 1.10) barely moved between
editions. Goals per match (2.40 against 2.65), BTTS (37.5% against 41.7%),
cards (4.85 against 4.21) and fouls (12.91 against 11.16 per team) did. The
2024–25 line is printed because it is the most recent edition.

**Format, 2026–27 only (Wikipedia's 2026–27 Nations League page, format
section; Sports Mole's preview says the same):** League C group winners are
promoted, runners-up play the last-placed League B sides, and no side is
relegated from League C, because League D is abolished from 2028–29. This is
the first League C edition in the archive with no relegation.

### Sides promoted from League D into League C (context line, not a baseline)
The four sides promoted from League D for 2022–23 (Faroe Islands, Gibraltar)
and 2024–25 (Estonia, Latvia), all as League D group winners, from the same
League C match rows: 24 matches, 0.71 points per match (W4 D5 L15), 0.71
scored and 2.00 conceded; over 2.5 58.3%, BTTS 45.8%, failed to score 50.0%,
clean sheet 8.3%; first-half goals 0.29 scored and 1.04 conceded; corners
2.63 won and 6.08 conceded; cards 1.96 per match against their opponents'
1.71. Home: 12 matches, 1.08 points per match (W4 D1 L7), 0.92 scored and
1.50 conceded, over 2.5 58.3%, BTTS 50.0%, failed to score 41.7%, corners 2.92
won and 5.58 conceded, cards 2.08 against 2.00. Away: 12 matches, 0.33 points
per match (W0 D4 L8). Matchday one: L4, 1 scored and 13 conceded (0–4 in
Georgia, 0–4 in Türkiye, 0–1 at home to Slovakia, 1–4 in Armenia). Group
finishes: third twice (Faroe Islands, Estonia), fourth twice (Gibraltar,
Latvia).

### Sides relegated from League B into League C (context line, not a baseline)
The seven sides relegated from League B for 2022–23 (Türkiye, Northern
Ireland, Slovakia, Bulgaria) and 2024–25 (Sweden, Romania, Armenia) — seven,
not eight, because 2022–23 League B Group B2 ran with three teams after
Russia's exclusion — from the same League C match rows: 42 matches, 1.74
points per match (W21 D10 L11), 1.95 scored and 1.07 conceded; over 2.5
61.9%, BTTS 52.4%, failed to score 19.0%, clean sheet 35.7%; corners 6.29 won
and 2.83 conceded; cards 1.98 per match against their opponents' 2.52. Away:
21 matches, 1.81 points per match (W11 D5 L5), 1.76 scored and 0.95
conceded, over 2.5 61.9%, BTTS 47.6%, failed to score 14.3%, corners 5.86 won
and 3.14 conceded, cards 2.33 against 2.43. Matchday one: W5 D1 L1. Group
finishes: first three times (Türkiye, Sweden, Romania), second twice
(Bulgaria, Armenia), third twice (Northern Ireland, Slovakia).

### Meetings between the two groups (context line, not a baseline)
Eight League C matches between a side promoted from League D and a side
relegated from League B: the relegated side went W6 D1 L1, 3.63 goals per
match. The four played at the promoted side's ground: Gibraltar 1–1 Bulgaria
(June 2022), Faroe Islands 2–1 Türkiye (September 2022), Estonia 0–3 Sweden
(October 2024), Latvia 1–2 Armenia (November 2024) — home side W1 D1 L2, 2.75
goals per match, over 2.5 and BTTS in three of four, corners 2.25 won and
7.25 conceded per match (the visitor won more in all four), cards 2.50 for the
home side against 2.00.

### League D 2024–25 (12 matches — context for San Marino's 2024–25 line, not a baseline)
D1 San Marino, Gibraltar, Liechtenstein; D2 Moldova, Malta, Andorra; two
groups of three, four matches per side. Same counting conventions.
- goals per game 1.58; over 2.5 16.7%; BTTS 25.0%; home win 41.7%; draw 33.3%; away win 25.0%
- clean sheet / failed to score 45.8% per team-appearance; under 1.5 goals 58.3%; two 0–0s
- first-half goals 0.58 per match
- cards per game 7.42 (86 yellows, 3 reds); fouls 16.58 per team; 4.47 fouls per card; corners 3.08 per team
- shots 9.38 per team; shots on target 2.88 per team
- penalty kicks 0.75 per match (9 in 12)

Against League C 2024–25, League D scored 0.82 fewer goals per match and
booked 2.57 more cards on 3.67 more fouls per team.

### Sides that stayed in League C hosting sides relegated from League B (context line, not a baseline — added on f3)
Recomputed from the same League C match rows, zero searches: every 2022–23 and
2024–25 League C match whose home side was in League C the previous edition and
whose visitor had just come down from League B. 17 matches (10 in 2022–23, 7
in 2024–25). Home side W4 D4 L9 (0.94 points per match), 0.94 scored and 1.76
conceded; the relegated visitor W9 D4 L4. 2.71 goals per match; over 2.5
58.8%; BTTS 41.2%; home side failed to score 52.9%, kept a clean sheet 17.6%;
first-half goals 1.24 per match (home 0.47, visitor 0.77); corners 3.35 won and
5.53 conceded by the home side, which won more corners in 4 of 17; cards 4.82
per match (2.41 each side). Faroe Islands 2–2 Armenia (October 2024) is one of
the 17; the four League C matches hosted by a side promoted from League D are
not (they are the "meetings" line above).

### Sides that stayed in League C hosting sides that also stayed (context line, not a baseline — added on f4)
Recomputed from the same League C match rows, zero searches: every 2022–23 and
2024–25 League C match in which both the home side and the visitor were in
League C the previous edition. 38 matches (16 in 2022–23, 22 in 2024–25). Home
side W19 D9 L10 (1.74 points per match), 1.32 scored and 0.76 conceded; 2.08
goals per match; over 2.5 31.6%; BTTS 26.3%; under 1.5 goals in 13 of 38, four
0–0s; home side failed to score 31.6%, kept a clean sheet 52.6%; first-half goals
0.84 per match (home 0.55, visitor 0.29), 15 of 38 goalless at half-time; cards
4.84 per match (home 2.39, visitor 2.45); fouls 13.30 per team; 5.49 fouls per
card; penalty kicks 0.21 per match (8 in 38); corners 4.89 won and 4.21
conceded by the home side, which won more corners in 15 of 38 (visitor 18, level
5). All twelve 2024–25 Group C3 matches (Bulgaria, Luxembourg, Belarus, Northern
Ireland) are among the 38, so both of tonight's sides sit inside this line:
twelve of the 38 are Bulgaria's or Luxembourg's (ten from 2024–25 Group C3, plus
Luxembourg's two 2022–23 matches with Lithuania), two of them against each
other.

## Sources for the League C lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 96 League C matches and 12 League D matches.
- ESPN standings `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}` for group membership, finishing positions and movement between divisions.
- Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League (format section) for the no-relegation rule; logged in sources_0926.md under f2.

### Sides relegated from League B hosting sides that stayed in League C (context line, not a baseline — added on f5)
Recomputed with zero searches, but **not from ESPN**: ESPN's API was blocked at
this run's egress proxy. Source: the public international-results record
compiled on GitHub (martj42/international_results, `results.csv` and
`goalscorers.csv`, raw files; the Kaggle "International football results"
dataset). It carries results, venues and goal minutes (with penalty and own-goal
flags) and no box score, so **no cards, fouls, corners or shots on this line.**
Reconciliation before use: from the same record, League C 2024–25 gives 48
matches, 2.40 goals, over 2.5 47.9%, BTTS 37.5%, home win 41.7%, first-half
goals 1.15 (Romania – Kosovo 0–0 as played); 2022–23 gives 48, 2.65, 45.8%,
41.7%, 43.8%, 1.10 — every figure matches the League C lines above. The
relegated-from-B line above (42: W21 D10 L11, 1.95 scored, 1.07 conceded, over
2.5 61.9%, BTTS 52.4%, clean sheet 35.7%, failed to score 19.0%; away W11 D5 L5,
1.76/0.95) and the f3 line (17: W4 D4 L9, 0.94/1.76, over 2.5 58.8%, BTTS
41.2%) also reproduce; the record gives the f3 line's visitor first-half goals
as 13 in 17 (0.76; the f3 line prints 0.77, total 1.24 in both). Goal counts
match the recorded score in all 96 matches (Romania – Kosovo recorded 0–0, as played). First half = goal minute 45 or
earlier (stoppage-time goals are recorded at 45).
Every 2022–23 and 2024–25 League C match whose home side had just come down from
League B and whose visitor was in League C the previous edition. 17 matches (10
in 2022–23, 7 in 2024–25). Home side W6 D5 L6 (1.35 points per match), 1.71
scored and 1.35 conceded (29–23); 3.06 goals per match; over 2.5 52.9%; BTTS
58.8%; under 1.5 goals in 4 of 17; home side kept a clean sheet 17.6%, failed to
score 29.4%; first-half goals 1.35 per match (home 0.65, visitor 0.71); at
half-time the home side led in 4, was level in 6 (three 0–0) and trailed in 7;
penalty goals 4 for the home side, 2 for the visitor. Margins ran from −3
(Bulgaria 2–5 Georgia, June 2022) to +6 (Sweden 6–0 Azerbaijan, November 2024);
the home side won by two or more in 4 of 17. The 17: Northern Ireland 0–1
Greece, 2–2 Cyprus, 2–1 Kosovo; Bulgaria 1–1 North Macedonia, 2–5 Georgia;
Slovakia 0–1 Kazakhstan, 1–2 Azerbaijan, 1–1 Belarus; Türkiye 2–0 Lithuania,
3–3 Luxembourg (2022–23); Romania 3–1 Lithuania, 0–0 Kosovo, 4–1 Cyprus;
Armenia 0–2 North Macedonia, 0–1 Faroe Islands; Sweden 2–1 Slovakia, 6–0
Azerbaijan (2024–25).

### Sides relegated from League B, at home in League C (context line, not a baseline — added on f5)
The home half of the relegated-from-B line above. From the same record: 21
matches, W10 D5 L6 (1.67 points per match), 2.14 scored and 1.19 conceded
(45–25); over 2.5 61.9%; BTTS 57.1%; clean sheet 23.8%, failed to score 23.8%;
first-half goals 1.57 per match (0.90 scored, 0.67 conceded). Corners and cards,
by subtraction of the away figures from the all-venue figures in the
relegated-from-B line above (the integer totals behind each printed two-decimal
rate are unique: corners won 264 and 123, conceded 119 and 66; cards 83 and 49,
opponents' 106 and 51): corners 6.71 won and 2.52 conceded per match (141 and
53 in 21); cards 1.62 per match against their opponents' 2.62 (34 and 55).

## Sources for the f5 lines
- GitHub raw files https://raw.githubusercontent.com/martj42/international_results/master/results.csv and …/goalscorers.csv, fetched 26 September 2026 (dataset last row 26 August 2026).
