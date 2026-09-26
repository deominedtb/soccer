# baselines_0925

UEFA Nations League 2026–27, matchday 1 (Groups A1, B2, B4 and C2 open
today). Three divisions on this slate (League A, League B, League C); each
division's line is written the first time a fixture from it is carded, and
read from this file afterwards. 2026–27 has no completed match in any of
today's groups, so every line is a completed earlier edition of the same
division.

Method, as on 0919, 0920 and 0924: recomputed from ESPN's public match
record, not searched. Event lists from
`site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=YYYYMM`
(monthly queries), each match then read from its own summary — boxscore for
fouls, yellow and red cards, corners and shots; key events for goal minute,
scoring side and penalty kicks; group membership from
`…/uefa.nations/standings?season={2022,2024,2026}`. **Zero baseline searches
spent.**

Counting conventions match the earlier files: cards per game is yellows plus
reds per match, both teams (ESPN boxscore); fouls, corners and shots are per
team per match; clean sheet / failed to score is per team-appearance;
first-half goals is per match, both sides. Penalties are penalty kicks taken
(scored, saved or missed) in ESPN's key events. No xG exists for this
competition in ESPN's record: **no divisional xG line, none estimated.**

---

## UEFA Nations League B — first carded on f1 (Georgia – Northern Ireland)

Recomputed for this slate from the same 90 summaries as the League B entry in
baselines_0924.md; every figure below matches that entry. The raw rerun gives
2024–25 goals 2.65, first-half goals 1.10 and 12 penalty kicks because
Wales 1–0 Montenegro (698976) has no key events in ESPN's record; its
36th-minute Wilson penalty is added from ESPN's commentary, as on 0924, and
the goal-timing parser then reconciles against the official score on 90 of 90.

### 2024–25 League B (48 matches — the primary line on every League B card)
Group stage only, four groups of four, six matches per side: B1 Czechia,
Ukraine, Georgia, Albania; B2 England, Greece, Finland, Republic of Ireland;
B3 Norway, Austria, Slovenia, Kazakhstan; B4 Türkiye, Wales, Iceland,
Montenegro. The March 2025 A/B and B/C play-offs are not in the line
(two-legged promotion/relegation ties, not group play).
Five of the sixteen are in 2026–27 League B (Austria, Republic of Ireland,
Slovenia, Ukraine, Georgia). Today's Group B2 has two of them (Georgia and
Ukraine, both B1 in 2024–25); Northern Ireland come up from League C and
Hungary down from League A. Group B4 (Poland, Bosnia-Herzegovina, Sweden,
Romania) has none: Poland and Bosnia-Herzegovina come down from League A,
Sweden and Romania up from League C.
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

### Sides promoted from League C into League B (context line, not a baseline)
The eight sides promoted from League C for 2022–23 (Slovenia, Armenia,
Montenegro, Albania) and 2024–25 (Türkiye, Georgia, Kazakhstan, Greece), from
the same League B match rows: 46 matches, 1.13 points per match (W14 D10
L22), 1.02 scored and 1.52 conceded; over 2.5 45.7%, BTTS 39.1%, failed to
score 41.3%. Away: 23 matches, 0.96 points per match (W6 D4 L13), 0.96 scored
and 1.74 conceded, over 2.5 52.2%, BTTS 39.1%, failed to score 43.5%, corners
3.61 won and 6.00 conceded per match. Matchday one: W4 D3 L1 (two of the
eight were away: Albania 1–1 in Iceland, Türkiye 0–0 in Wales). Group
finishes: none first; second twice (Greece, Türkiye), third four times,
fourth twice.

## Sources for every line above
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 90 League B matches.
- ESPN standings `site.web.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}` for group membership and promoted sides.

---

## UEFA Nations League C — first carded on f2 (Armenia – Latvia)

New to the archive. Recomputed from the same ESPN pipeline and the same
counting conventions as the League B entry above: 96 League C group matches
(48 per edition), each read from its own summary. **Zero baseline searches
spent.** Goal counts from key events reconcile against the official score on
95 of 96. The exception is Romania – Kosovo, 15 November 2024 (698999):
ESPN's commentary records "Match abandoned", Romania 0, Kosovo 0, after the
90'+9' whistle, and the official score is the awarded 3–0. It is counted
here as played, 0–0, with its box score (10 cards, 26 fouls, 12 corners);
the line without it is given below so the effect is visible. No match went
to extra time; every match has a two-team box score. No xG exists for this
competition in ESPN's record: **no divisional xG line, none estimated.**

### 2024–25 League C (48 matches — the primary line on every League C card)
Group stage only, four groups of four, six matches per side: C1 Sweden,
Slovakia, Estonia, Azerbaijan; C2 Romania, Kosovo, Cyprus, Lithuania; C3
Northern Ireland, Bulgaria, Belarus, Luxembourg; C4 North Macedonia, Armenia,
Faroe Islands, Latvia. The play-offs (B/C March 2025, C/D March 2026) are not
in the line.
Nine of the sixteen are in 2026–27 League C (Armenia, Belarus, Bulgaria,
Cyprus, Estonia, Faroe Islands, Latvia, Luxembourg, Slovakia). Gone up: Sweden,
Romania, Northern Ireland, North Macedonia, Kosovo. Gone down: Azerbaijan,
Lithuania. Come down from League B: Albania, Finland, Iceland, Kazakhstan,
Montenegro. Come up from League D: Moldova, San Marino. Today's Group C2
(Armenia, Latvia, Cyprus, Montenegro) has three 2024–25 League C sides;
Armenia and Latvia were both in C4.
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

**League C is steady on outcome and first halves, not on volume.** Home
wins (41.7% against 43.8%), away wins (33.3% in both), over 2.5 (47.9%
against 45.8%) and first-half goals (1.15 against 1.10) barely moved between
editions. Goals per match (2.40 against 2.65), BTTS (37.5% against 41.7%),
cards (4.85 against 4.21) and fouls (12.91 against 11.16 per team) did. The
2024–25 line is printed because it is the most recent edition.

## Sources for the League C lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 96 League C matches; commentary of event 698999 for the abandonment.
- ESPN standings `site.web.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2022,2024,2026}` for group membership and movement between divisions.

---

## UEFA Nations League A — first carded on f3 (Italy – Belgium)

Recomputed for this slate from the same 96 summaries as the League A entry in
baselines_0924.md, with the same counting conventions as the League B and C
entries above. **Zero baseline searches spent.** Key events de-duplicated on
type, period, minute, team and participants (Scotland 2–3 Poland carries every
event twice in ESPN's record); the goal-timing parser then reconciles against
the official score on 96 of 96. No match went to extra time; every match has a
two-team box score. Every figure below matches the 0924 entry (2024–25 cards
per game 4.125, printed 4.13 there and here). No xG exists for this
competition in ESPN's record: **no divisional xG line, none estimated.**

### 2024–25 League A (48 matches — the primary line on every League A card)
Group stage only, four groups of four, six matches per side: A1 Portugal,
Croatia, Scotland, Poland; A2 France, Italy, Belgium, Israel; A3 Germany,
Netherlands, Hungary, Bosnia-Herzegovina; A4 Spain, Denmark, Serbia,
Switzerland. The March 2025 quarter-finals and A/B play-offs and the June 2025
Finals are not in the line.
Ten of the sixteen are in 2026–27 League A; Poland, Scotland, Israel,
Bosnia-Herzegovina, Hungary and Switzerland are not, and Türkiye, Greece,
England, Czechia, Norway and Wales are in. Today's Group A1 (Italy, Belgium,
France, Türkiye) has three of the 2024–25 line's sides, all from Group A2;
Türkiye come up from League B.
- goals per game 2.94; over 2.5 56.3%; BTTS 58.3%; home win 43.8%; draw 29.2%; away win 27.1%
- clean sheet / failed to score 26.0% per team-appearance; under 1.5 goals 22.9% of matches; five 0–0s
- first-half goals 1.33 per match
- cards per game 4.13 (2.06 per team; 188 yellows, 10 reds); fouls 11.39 per team (22.77 per match); 5.52 fouls per card; corners 4.75 per team
- shots 12.93 per team; shots on target 4.48 per team
- penalty kicks 0.42 per match (20 in 48)

### 2022–23 League A (48 matches — cross-check, not the card line)
A1 Croatia, Denmark, France, Austria; A2 Spain, Portugal, Switzerland,
Czechia; A3 Italy, Hungary, Germany, England; A4 Netherlands, Belgium,
Poland, Wales. Group stage only.
- goals per game 2.63; over 2.5 45.8%; BTTS 52.1%; home win 39.6%; draw 22.9%; away win 37.5%
- clean sheet / failed to score 25.0% per team-appearance; under 1.5 goals 25.0%; one 0–0
- first-half goals 1.02 per match
- cards per game 3.33 (1.67 per team; 159 yellows, 1 red); fouls 11.01 per team (22.02 per match); 6.61 fouls per card; corners 4.68 per team
- shots 11.38 per team; shots on target 4.18 per team
- penalty kicks 0.23 per match (11 in 48)

### Both editions pooled (96 matches)
- goals per game 2.78; over 2.5 51.0%; BTTS 55.2%; home win 41.7%; draw 26.0%
- first-half goals 1.18; cards per game 3.73; fouls 11.20 per team; 6.01 fouls per card; corners 4.71 per team; penalty kicks 0.32 per match

**League A moved between editions on goals and cards, not on fouls or
corners.** Fouls (11.39 against 11.01 per team) and corners (4.75 against
4.68) barely moved. Goals rose by 0.31 per match, over 2.5 by 10.4 points,
first-half goals by 0.31, and cards by 0.79 per match on almost the same foul
count (5.52 fouls per card against 6.61), with ten reds against one. Penalty
kicks nearly doubled. Against the League B line above, League A 2024–25 scored
more (2.94 against 2.67), booked less (4.13 against 4.42) and awarded more
penalty kicks (0.42 against 0.27). The 2024–25 line is printed because it is
the most recent edition and shares ten of its sixteen sides with 2026–27.

## Sources for the League A lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 96 League A matches.
- ESPN standings `site.web.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2022,2024,2026}` for group membership and movement between divisions.
