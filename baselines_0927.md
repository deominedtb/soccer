# baselines_0927

UEFA Nations League 2026–27, league phase. Four divisions on this slate
(League A Groups A2 and A4, League B Groups B3, League D Group D1); each
division's line is written the first time a fixture from it is carded, and
read from this file afterwards.

Method, as on 0919, 0920, 0924, 0925 and 0926: recomputed from ESPN's public
match record, not searched. Event lists from
`site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=YYYYMM`
(monthly queries), each match then read from its own summary — box score for
fouls, yellow and red cards, corners and shots; linescores for the 90-minute
and half-time score; key events for goal minute, scoring side and penalty
kicks; group membership from
`site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2018,2020,2022,2024,2026}`.
**Zero baseline searches spent.**

Counting conventions match the earlier files: cards per game is yellows plus
reds per match, both teams (ESPN box score); fouls, corners and shots are per
team per match; clean sheet / failed to score is per team-appearance;
first-half goals is per match, both sides. Penalties are penalty kicks taken
(scored, saved or missed) in ESPN's key events. No xG exists for this
competition in ESPN's record: **no divisional xG line, none estimated.**

---

## UEFA Nations League D — first carded on f1 (Gibraltar – Andorra)

Every League D group match in ESPN's record, 96 in four editions. Goal counts
from key events reconcile against the official score on 96 of 96; every
match has a two-team box score; no match went to extra time. The 2024–25
figures below reproduce the League D 2024–25 context line in
baselines_0926.md exactly.

**Format, 2026–27 (Wikipedia's 2026–27 League D page; Andorra Esportiu):**
six teams in two groups of three, four matches per side, home and away. This
is the last League D edition before the competition drops to three leagues in
2028–29, and all six sides are promoted to League C whatever their finish.
Group D1: Malta, Andorra, Gibraltar. Group D2: Lithuania, Azerbaijan,
Liechtenstein. Lithuania and Azerbaijan come down from League C (the two
lowest fourth-placed sides of 2024–25); Gibraltar and Malta stay after losing
the March 2026 C/D play-offs (Gibraltar 0–1 and 0–1 to Latvia); Andorra and
Liechtenstein stay as third-placed League D sides.

### 2024–25 League D (12 matches — the primary line on every League D card)
Group stage only, two groups of three, four matches per side: D1 San Marino,
Gibraltar, Liechtenstein; D2 Moldova, Malta, Andorra. The March 2026 C/D
play-offs are not in the line.
Four of the six are in 2026–27 League D (Gibraltar, Liechtenstein, Malta,
Andorra). Today's Group D1 has three of them: Malta (second in D2), Andorra
(third in D2), Gibraltar (second in D1).
- goals per game 1.58; over 2.5 16.7%; BTTS 25.0%; home win 41.7%; draw 33.3%; away win 25.0%
- clean sheet / failed to score 45.8% per team-appearance; under 1.5 goals 58.3% of matches; two 0–0s; final margin within one goal in 9 of 12
- first-half goals 0.58 per match; level at half-time in 6 of 12
- cards per game 7.42 (3.71 per team; 86 yellows, 3 reds); home side 3.42, away side 4.00; fouls 16.58 per team (home 14.25, away 18.92); 4.47 fouls per card
- corners 3.08 per team (home 2.67, away 3.50; home side won more in 3 of 12)
- shots 9.38 per team; shots on target 2.88 per team
- penalty kicks 0.75 per match (9 in 12, 6 scored)

### 2022–23 League D (18 matches — cross-check, not the card line)
D1 Latvia, Moldova, Andorra, Liechtenstein; D2 Estonia, Malta, San Marino.
- goals per game 2.44; over 2.5 44.4%; BTTS 38.9%; home win 44.4%; draw 11.1%; away win 44.4%
- clean sheet / failed to score 33.3% per team-appearance; under 1.5 goals 16.7%; one 0–0
- first-half goals 0.94 per match
- cards per game 3.94 (69 yellows, 2 reds); fouls 12.81 per team; 6.49 fouls per card; corners 4.39 per team
- shots 10.83 per team; shots on target 3.53 per team
- penalty kicks 0.50 per match (9 in 18)

### 2020–21 League D (18 matches — cross-check, not the card line)
D1 Faroe Islands, Malta, Latvia, Andorra; D2 Gibraltar, Liechtenstein, San Marino.
- goals per game 1.78; over 2.5 16.7%; BTTS 38.9%; home win 22.2%; draw 50.0%; away win 27.8%
- clean sheet / failed to score 41.7%; under 1.5 goals 44.4%; four 0–0s
- first-half goals 0.94 per match
- cards per game 5.72 (100 yellows, 3 reds); fouls 15.67 per team; 5.48 fouls per card; corners 4.00 per team
- shots 10.06 per team; shots on target 3.03 per team
- penalty kicks 0.28 per match (5 in 18)

### 2018–19 League D (48 matches — a sixteen-team division, not comparable in membership)
Four groups of four; members included Georgia, North Macedonia, Kosovo,
Belarus, Luxembourg, Armenia, Kazakhstan and Azerbaijan alongside today's sides.
- goals per game 2.52; over 2.5 41.7%; BTTS 35.4%; home win 43.8%; draw 31.2%; away win 25.0%
- first-half goals 1.06; cards per game 4.25; fouls 14.19 per team; 6.68 fouls per card; corners 5.11 per team; penalty kicks 0.19 per match

### 2022–23 and 2024–25 pooled (30 matches)
- goals per game 2.10; over 2.5 33.3%; BTTS 33.3%; home win 43.3%; draw 20.0%
- clean sheet / failed to score 38.3%; under 1.5 goals 33.3%
- first-half goals 0.80; cards per game 5.33; fouls 14.32 per team; 5.37 fouls per card; corners 3.87 per team; penalty kicks 0.60 per match

### 2020–21 to 2024–25 pooled (48 matches, the three six- or seven-team editions)
- goals per game 1.98; over 2.5 27.1%; BTTS 35.4%; home win 35.4%; draw 31.2%
- under 1.5 goals 37.5%; first-half goals 0.85; cards per game 5.48; fouls 14.82 per team; 5.41 fouls per card; corners 3.92 per team; penalty kicks 0.48 per match

**League D is not steady on anything.** Between 2022–23 and 2024–25 goals per
match fell from 2.44 to 1.58, over 2.5 from 44.4% to 16.7%, first-half goals
from 0.94 to 0.58, and cards rose from 3.94 to 7.42 on fouls up from 12.81 to
16.58 per team; 2020–21 sits between them on cards (5.72) and near 2024–25 on
goals (1.78). Every edition is 12 to 18 matches between six or seven sides, so
one group's matches move the line. The 2024–25 line is printed because it is
the most recent edition and four of its six sides are in 2026–27.

### 2026–27 League D so far (2 matches — not a baseline)
Andorra 1–2 Malta (Encamp, 24 September) and Liechtenstein 0–2 Lithuania
(Vaduz, 24 September): 2.50 goals per match, one over 2.5 and one BTTS,
first-half goals 1.00, cards 4.50 per match (9 yellows, no red), fouls 16.25
per team, corners 3.25 per team, one penalty kick (missed). Lithuania –
Azerbaijan (Kaunas, 27 September, 15:00) had not finished when this line was
written and is not in it.

### Gibraltar in League D (context line, not a baseline — added on f1)
Every Gibraltar League D group match, 14 in three editions (2018–19 Group D4,
2020–21 Group D2, 2024–25 Group D1): W5 D5 L4, 12–19; over 2.5 28.6%; BTTS
35.7%; clean sheet 42.9%, failed to score 35.7%; first-half goals 0.43 scored
and 0.50 conceded; cards 3.21 per match against their opponents' 3.50 (6.71
per match), on 11.57 fouls committed and 14.71 suffered; corners 3.43 won and
5.36 conceded; penalty kicks 3 for and 3 against.
- At home: 7 matches, W3 D2 L2, 9–12; over 2.5 42.9%; BTTS 57.1%; failed to
  score 14.3%; cards 2.71 against their visitors' 4.43 (7.14 per match); fouls
  11.57 committed and 16.86 suffered; corners 4.14 won and 4.43 conceded, won
  more in 5 of 7. The five at Victoria Stadium (2018–19, 2020–21) and two at
  Europa Point Stadium (2024–25: 2–2 Liechtenstein, 15 cards; 1–0 San Marino,
  11 cards).

### Andorra in League D (context line, not a baseline — added on f1)
Every Andorra League D group match, 23 in five editions (2018–19 D1, 2020–21
D1, 2022–23 D1, 2024–25 D2, 2026–27 D1 to date): W2 D9 L12, 10–33; over 2.5
34.8%; BTTS 30.4%; clean sheet 30.4%, failed to score 65.2%; first-half goals
0.17 scored and 0.57 conceded; level at half-time in 12 of 23; cards 3.17 per
match against their opponents' 2.48 (5.65 per match), on 19.26 fouls committed
and 15.17 suffered (6.07 fouls per card); corners 2.57 won and 4.83 conceded;
penalty kicks 1 for and 8 against; reds 3 for and 5 against.
- Away: 11 matches, W1 D3 L7, 4–19; over 2.5 45.5%; BTTS 18.2%; failed to score
  72.7%; clean sheet 36.4%; first-half goals 0.27 scored and 0.73 conceded;
  cards 3.27 against their hosts' 2.09; fouls 20.00 committed and 14.82
  suffered; corners 1.82 won and 4.45 conceded; penalty kicks 0 for and 5
  against. The one away win is 2–0 in Vaduz (September 2022).
- 2020–21 onwards (the six- and seven-team editions): 17 matches, W2 D5 L10,
  8–24; away 8, W1 D2 L5, 4–12.

## Sources for the League D lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={201809,201810,201811,202009,202010,202011,202206,202209,202409,202410,202411,202609,202610,202611}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 96 League D group matches and the two 2026–27 matches, read 27 September 2026.
- ESPN standings `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2018,2020,2022,2024,2026}` for group membership, finishing positions and movement between divisions.
- Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_D (format, groups, matchday-one results); Andorra Esportiu https://www.andorraesportiu.com/la-nations-torna-a-posar-andorra-a-prova (promotion secured by the format change); logged in sources_0927.md under f1.

---

## UEFA Nations League A — first carded on f2 (Serbia – Netherlands)

Recomputed for this slate from the same 96 ESPN League A group summaries as
the League A entries in baselines_0924.md, baselines_0925.md and
baselines_0926.md, with the counting conventions above. **Zero baseline
searches spent.** Goal counts from key events reconcile against the official
score on 96 of 96; no match went to extra time; every match has a two-team box
score. **Every figure matches the 0926 entry** (2024–25 cards per game 4.125,
printed 4.13; over 2.5 56.25%, printed 56.3%; 2022–23 goals per game 2.625,
printed 2.63). No xG exists for this competition in ESPN's record: **no
divisional xG line, none estimated.**

**Format, 2026–27 (Wikipedia's 2026–27 League A page, citing UEFA's
regulations and its 15 September 2026 promotion/relegation note):** four
groups of four, six matches per side. The top two in each group go to the
March 2027 quarter-finals. The two worst last-placed sides are relegated
directly; the two best last-placed and the two worst third-placed sides play
League B's runners-up in March 2027 play-offs. This replaces the rule under
which every last-placed side went down, and is new to this edition (the
competition moves to three leagues of 18 in 2028–29).

### 2024–25 League A (48 matches — the primary line on every League A card)
Group stage only, four groups of four, six matches per side: A1 Portugal,
Croatia, Scotland, Poland; A2 France, Italy, Belgium, Israel; A3 Germany,
Netherlands, Hungary, Bosnia-Herzegovina; A4 Spain, Denmark, Serbia,
Switzerland. The March 2025 quarter-finals and A/B play-offs and the June 2025
Finals are not in the line.
Ten of the sixteen are in 2026–27 League A. Today's Group A2 (Netherlands,
Greece, Germany, Serbia) has three of them: Germany (first in A3), the
Netherlands (second in A3) and Serbia (third in A4, kept their place by beating
Austria in the A/B play-off, 1–1 in Vienna and 2–0 in Belgrade). Greece come up
from League B through the A/B play-off (second in B2, then beat Scotland).
- goals per game 2.94; over 2.5 56.3%; BTTS 58.3%; home win 43.8%; draw 29.2%; away win 27.1%
- clean sheet / failed to score 26.0% per team-appearance; under 1.5 goals 22.9% of matches; five 0–0s
- first-half goals 1.33 per match; level at half-time in 18 of 48; final margin within one goal in 30 of 48
- cards per game 4.13 (2.06 per team; 188 yellows, 10 reds); fouls 11.39 per team (22.77 per match); 5.52 fouls per card; corners 4.75 per team
- shots 12.93 per team; shots on target 4.48 per team
- penalty kicks 0.42 per match (20 in 48)

### 2022–23 League A (48 matches — cross-check, not the card line)
A1 Croatia, Denmark, France, Austria; A2 Spain, Portugal, Switzerland,
Czechia; A3 Italy, Hungary, Germany, England; A4 Netherlands, Belgium,
Poland, Wales. Group stage only.
- goals per game 2.63; over 2.5 45.8%; BTTS 52.1%; home win 39.6%; draw 22.9%; away win 37.5%
- clean sheet / failed to score 25.0% per team-appearance; under 1.5 goals 25.0%; one 0–0
- first-half goals 1.02 per match; level at half-time in 22 of 48; final margin within one goal in 33 of 48
- cards per game 3.33 (1.67 per team; 159 yellows, 1 red); fouls 11.01 per team (22.02 per match); 6.61 fouls per card; corners 4.68 per team
- shots 11.38 per team; shots on target 4.18 per team
- penalty kicks 0.23 per match (11 in 48)

### Both editions pooled (96 matches)
- goals per game 2.78; over 2.5 51.0%; BTTS 55.2%; home win 41.7%; draw 26.0%
- first-half goals 1.18; cards per game 3.73; fouls 11.20 per team; 6.01 fouls per card; corners 4.71 per team; penalty kicks 0.32 per match

**League A moved between editions on goals and cards, not on fouls or
corners**: goals rose by 0.31 per match, over 2.5 by 10.4 points and
first-half goals by 0.31, and cards by 0.79 per match on almost the same foul
count. The 2024–25 line is printed because it is the most recent edition and
shares ten of its sixteen sides with 2026–27.

### 2026–27 League A so far (8 matches — not a baseline)
Matchday 1, 24–26 September: Netherlands 1–1 Germany, Norway 3–2 Denmark,
Portugal 1–0 Wales, Serbia 1–2 Greece, Italy 0–2 Belgium, Türkiye 0–1 France,
Czechia 1–2 Croatia, England 2–3 Spain. 2.75 goals per match; over 2.5 4 of 8;
BTTS 5 of 8; home side W2 D1 L5; first-half goals 1.25; level at half-time in 2
of 8; cards 4.00 per match (30 yellows, 2 reds); fouls 11.56 per team; 5.78
fouls per card; corners 5.06 per team; one penalty kick in 8.

### Sides that stayed in League A hosting sides that also stayed (context line, not a baseline — added on f2)
Recomputed from the same 96 ESPN League A rows, zero searches: every 2022–23 and
2024–25 League A match in which both the home side and the visitor were in
League A the previous edition (neither promoted). 48 matches (24 in each
edition). Home side W18 D14 L16 (1.42 points per match), 1.62 scored and 1.29
conceded (78–62); 2.92 goals per match; over 2.5 50.0%; BTTS 58.3%; under 1.5
goals in 13 of 48; home side kept a clean sheet 27.1%, failed to score 16.7%;
first-half goals 1.17 per match; at half-time the home side led in 13, was level
in 20 (17 at 0–0) and trailed in 15; home side won by two or more in 9, lost by
two or more in 6, and 33 of 48 finished within one goal. Box score: cards 3.94
per match (home 1.96, visitor 1.98; 7 reds); fouls 11.40 per team; 5.79 fouls
per card; corners 5.33 won and 4.31 conceded by the home side, which won more in
28 of 48; shots 14.10 and 10.46; home possession 50.5%; penalty kicks 0.38 per
match (18). **By edition:** 2022–23 home W8 D7 L9, 2.58 goals, over 2.5 37.5%,
BTTS 50.0%, cards 3.54, level at half-time 12 of 24; 2024–25 home W10 D7 L7,
3.25 goals, over 2.5 62.5%, BTTS 66.7%, cards 4.33, level at half-time 8 of 24.
Matchday 1 of 2026–27 had two such matches: Netherlands 1–1 Germany, Italy 0–2
Belgium. Serbia, who stayed through the play-off rather than a top-three group
finish, have no match in this line (they were in League B in 2022–23).

### Netherlands away in League A, all editions (context line, not a baseline — added on f2)
Every Netherlands League A group match away from home, 11 in four editions, from
ESPN's summaries (2018–19 A1: France, Germany in Gelsenkirchen; 2020–21 A1:
Bosnia-Herzegovina, Italy in Bergamo, Poland in Chorzów; 2022–23 A4: Belgium,
Wales, Poland; 2024–25 A3: Hungary, Germany, Bosnia-Herzegovina). W4 D5 L2,
16–11 (1.45 scored, 1.00 conceded); 2.45 goals per match; over 2.5 45.5%; BTTS
72.7%; clean sheet 18.2%, failed to score 18.2%; first-half goals 0.36 scored
and 0.55 conceded, half-time led 3, level 4 (three 0–0), trailed 4; 12 of their
16 goals after half-time; final margin within one goal in 9 of 11 (the
exceptions 4–1 in Brussels and 2–0 in Warsaw, both wins). Box score: cards 1.09
per match against their hosts' 1.91 (3.00 per match; one Dutch red, van Dijk's
second yellow in Budapest); fouls 12.18 committed and 13.27 suffered; corners
4.91 won and 4.00 conceded, won more in 6 of 11; shots 11.55 and 9.45;
possession 56.4%; penalty kicks 1 for and 0 against. The two away defeats were
1–2 in Paris (2018) and 0–1 in Munich (2024).

### Serbia at home in League A (context line, not a baseline — added on f2)
Serbia's only League A editions are 2024–25 and 2026–27 (League C in 2018–19,
League B in 2020–21 and 2022–23). Four home group matches: 0–0 Spain and 1–2
Greece at Rajko Mitić, 2–0 Switzerland and 0–0 Denmark at Dubočica, Leskovac.
W1 D2 L1, 3–2; 1.25 goals per match; over 2.5 1 of 4; BTTS 1 of 4; half-time led
2, level 2, trailed 0; cards 5.25 per match (Serbia 3.00, visitors 2.25; one
Serbian red); fouls 11.75 committed and 9.50 suffered; corners 3.50 won and 6.25
conceded, won more in 1 of 4; shots 11.75 and 16.50; possession 37.1%; penalty
kicks 0 for and 1 against.

### Sides that stayed in League A hosting promoted sides (context line, not a baseline — added on f3)
Recomputed on f3 from the same 96 ESPN League A group summaries, zero searches:
every 2022–23 and 2024–25 League A match with a home side that was in League A
the edition before and a visitor promoted from League B (2022–23: Austria,
Czechia, Hungary, Wales; 2024–25: Scotland, Israel, Bosnia-Herzegovina, Serbia).
24 matches (12 in each edition). It reproduces, from the host's side, the
promoted-away line in baselines_0926.md (promoted visitors W4 D3 L17, 0.96
scored and 2.04 conceded, corners 2.79/6.38, shots 8.21/18.29).
- Home side W17 D3 L4 (2.25 points per match), 2.04 scored and 0.96 conceded (49–23); 3.00 goals per match; over 2.5 15 of 24 (62.5%); BTTS 12 of 24 (50.0%); home clean sheet 9 of 24 (the promoted visitor failed to score in 37.5%), home side failed to score 5 of 24.
- First-half goals 0.96 scored and 0.42 conceded (1.38 per match); at half-time the home side led 12, level 7, trailed 5; final margin within one goal in 12 of 24.
- Box score: cards 1.50 home, 1.88 visitor (3.38 per match); fouls 10.96 and 10.75; corners 6.38 won and 2.79 conceded, home side won more in 20 of 24; shots 18.29 and 8.21.
- By edition: 2022–23 home W9 D0 L3, 19–14, over 2.5 7 of 12, BTTS 5 of 12, corners 5.25/3.42; 2024–25 home W8 D3 L1, 30–9, over 2.5 8 of 12, BTTS 7 of 12, corners 7.50/2.17.

### Wales in League A, 2022–23 — their last promotion (context line, not a baseline — added on f3)
Group A4 (Netherlands, Belgium, Poland, Wales), from ESPN's summaries and the 2022
standings: W0 D1 L5, 6–11, fourth and relegated. Home: 1–2 Netherlands, 1–1
Belgium, 0–1 Poland. Away: 1–2 Poland, 2–3 Netherlands, 1–2 Belgium — all three
lost by one goal; 4–7 away; first-half goals 0.33 scored and 1.33 conceded away
(trailing at half-time twice, level once); Wales 2.67 cards per away match, hosts
1.00; fouls 10.67 committed and 13.67 suffered; corners 3.33 won and 5.00
conceded; shots 11.00 and 18.67.

### Denmark at home in League A, 2022–25 (context line, not a baseline — added on f3)
Six home group matches, all at Parken: 0–1 Croatia, 2–0 Austria, 2–0 France
(2022–23); 2–0 Switzerland, 2–0 Serbia, 1–2 Spain (2024–25). W4 D0 L2, 9–3; 2.00
goals per match; over 2.5 1 of 6; BTTS 1 of 6; clean sheets 4 of 6; first-half
goals 0.83 scored and 0.17 conceded, half-time led 3, level 2, trailed 1; cards
2.50 Denmark and 2.33 visitors; fouls 11.00 and 12.00; corners 7.83 won and 4.83
conceded, won more in 5 of 6; shots 13.67 and 9.67. The 2024–25 quarter-final
first leg (1–0 Portugal) is outside the group-stage line.

## Sources for the League A lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411,202609}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 96 League A group matches, the eight 2026–27 matchday-1 matches and the Netherlands' 2018–19 and 2020–21 away group matches (505528, 505510, 570737, 570709, 570637), read 27 September 2026.
- ESPN team schedules `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/teams/{449,6757}/schedule?season={2018,2020,2022}` for both sides' earlier Nations League editions.
- ESPN standings `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2018,2020,2022,2024,2026}` for group membership, finishing positions and movement between divisions.
- Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_A (raw wikitext; format section, team changes, Group 2 fixtures); logged in sources_0927.md under f2.
- Added on f3: the three League A context lines above, recomputed from the same 96 ESPN League A group summaries (scoreboards `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`, group membership from `…/uefa.nations/standings?season={2022,2024}`), read 27 September 2026. Zero searches.

---

## UEFA Nations League B — first carded on f4 (Austria – Kosovo)

Recomputed for this slate from the same 90 ESPN League B group summaries as
the League B entries in baselines_0924.md, baselines_0925.md and
baselines_0926.md, with the counting conventions above. **Zero baseline
searches spent.** Group membership from the 2022 and 2024 standings (the
four Russia fixtures of 2022–23 Group B2 were never played and are not in the
line). Wales 1–0 Montenegro (698976) again has no key events in ESPN's
record; its 36th-minute Wilson penalty is added from ESPN's commentary, as on
0924, 0925 and 0926, and goal counts then reconcile against the official
score on 90 of 90. No match went to extra time; every match has a two-team
box score. **Every figure matches the 0926 entry** (2024–25 goals 2.667,
printed 2.67; first-half goals 1.125, printed 1.12; cards 4.417, printed
4.42; 5.198 fouls per card, printed 5.20). No xG exists for this competition
in ESPN's record: **no divisional xG line, none estimated.**

**Format, 2026–27 (Wikipedia's 2026–27 League B page, citing UEFA):** four
groups of four, six matches per side. Group winners are promoted to League A
for 2028–29; runners-up play League A third- or fourth-placed sides in March
2027 promotion play-offs; fourth-placed sides play League C runners-up in
relegation play-offs. Today's Group B3: Israel (relegated from League A),
Austria (lost the 2025 A/B play-off to Serbia, stayed in League B), Republic
of Ireland (third in 2024–25 Group B2, stayed in League B), Kosovo (second in 2024–25
League C Group C2, promoted by beating Iceland 2–1 and 3–1 in the March 2025
B/C play-off; **Kosovo's first League B edition**).

### 2024–25 League B (48 matches — the primary line on every League B card)
Group stage only, four groups of four, six matches per side: B1 Czechia,
Ukraine, Georgia, Albania; B2 England, Greece, Finland, Republic of Ireland;
B3 Norway, Austria, Slovenia, Kazakhstan; B4 Türkiye, Wales, Iceland,
Montenegro. The March 2025 A/B and B/C play-offs are not in the line.
Five of the sixteen are in 2026–27 League B (Austria, Republic of Ireland,
Slovenia, Ukraine, Georgia). Today's fixture has one of them: Austria (second
in B3 on 11 points, 14–5).
- goals per game 2.67; over 2.5 50.0%; BTTS 43.8%; home win 45.8%; draw 18.8%; away win 35.4%
- clean sheet / failed to score 32.3% per team-appearance; under 1.5 goals 22.9% of matches; four 0–0s
- first-half goals 1.12 per match
- cards per game 4.42 (2.21 per team; 209 yellows, 3 reds); fouls 11.48 per team (22.96 per match); 5.20 fouls per card; corners 4.52 per team
- shots 12.68 per team; shots on target 4.19 per team
- penalty kicks 0.27 per match (13 in 48)

### 2022–23 League B (42 matches — cross-check, not the card line)
- goals per game 2.67; over 2.5 47.6%; BTTS 52.4%; home win 45.2%; draw 28.6%; away win 26.2%
- clean sheet / failed to score 26.2%; under 1.5 goals 21.4%; two 0–0s
- first-half goals 1.07 per match
- cards per game 4.57 (184 yellows, 8 reds); fouls 11.17 per team; 4.89 fouls per card; corners 4.77 per team
- shots 11.61 per team; shots on target 3.99 per team
- penalty kicks 0.21 per match (9 in 42)

### Both editions pooled (90 matches)
- goals per game 2.67; over 2.5 48.9%; BTTS 47.8%; home win 45.6%; draw 23.3%
- first-half goals 1.10; cards per game 4.49; fouls 11.33 per team; 5.05 fouls per card; corners 4.64 per team; penalty kicks 0.24 per match

**League B is steady on volume, not on outcome**, as on 0924–0926: goals,
first-half goals, cards, fouls and corners barely moved between editions;
BTTS, draws, away wins and reds did.

### 2026–27 League B so far (8 matches — not a baseline)
Matchday 1, 24–26 September: Austria 3–1 Israel, Kosovo 1–0 Republic of
Ireland, Georgia 0–1 Northern Ireland, Hungary 0–1 Ukraine, Poland 0–0
Bosnia-Herzegovina, Sweden 2–1 Romania, Slovenia 0–0 Scotland, North Macedonia
0–3 Switzerland. 1.63 goals per match; over 2.5 3 of 8; BTTS 2 of 8; home side
W3 D2 L3; first-half goals 0.88; cards 5.25 per match (2 reds); fouls 13.25
per team; 5.05 fouls per card; corners 2.88 per team; two penalty kicks.

### Sides that stayed in League B hosting sides promoted from League C (context line, not a baseline — added on f4)
From the same 90 League B rows, zero searches: every 2022–23 and 2024–25
League B match with a home side that was in League B the edition before
(neither promoted nor relegated from League A) and a visitor promoted from
League C (2022–23: Montenegro, Albania, Armenia, Slovenia; 2024–25: Georgia,
Greece, Kazakhstan, Türkiye). 15 matches (7 and 8). No promoted side in
either edition came up through a play-off; Kosovo are the first.
- Home side W9 D1 L5 (1.87 points per match), 1.80 scored and 1.13 conceded (27–17); 2.93 goals per match; over 2.5 8 of 15; BTTS 5 of 15; under 1.5 goals 3 of 15; home clean sheet 6 of 15, home side failed to score 5 of 15.
- First-half goals 1.00 scored and 0.20 conceded (1.20 per match); at half-time the home side led 8, level 6, trailed 1; final margin within one goal in 5 of 15 (home side won by two or more 6, lost by two or more 4).
- Box score: cards 2.07 home, 2.53 visitor (4.60 per match); fouls 10.93 and 10.13; corners 5.00 won and 3.47 conceded, home side won more in 7 of 15; shots 13.80 and 11.07; home possession 53.0%.
- By edition: 2022–23 home W5 D1 L1, 13–7, corners 6.14/2.57, possession 61.0%; 2024–25 home W4 D0 L4, 14–10, corners 4.00/4.25, possession 45.9% (Greece and Türkiye won away twice each).

### Sides promoted from League C, away in League B (context line, not a baseline — added on f4)
The same eight promoted sides' 23 away League B matches (all hosts), from the
visitor's side: W6 D4 L13 (0.96 points per match), 0.96 scored and 1.74
conceded (22–40); 2.70 goals per match; over 2.5 12 of 23; BTTS 9 of 23;
failed to score 10 of 23; first-half goals 0.22 scored and 0.87 conceded, at
half-time led 2, level 10, trailed 11; cards 2.83 against their hosts' 2.26
(5.09 per match); fouls 11.70 committed and 11.39 suffered; corners 3.61 won
and 6.00 conceded, won more in 8 of 23; shots 10.13 and 14.26; possession 44.9%.

## Sources for the League B lines
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411,202609}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 90 League B group matches and the eight 2026–27 matchday-1 League B matches; commentary of event 698976 for the Wilson penalty; read 27 September 2026.
- ESPN standings `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}` for group membership, promotion and relegation between editions.
- Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_B (raw wikitext; format, team changes, Group 3 fixtures); logged in sources_0927.md under f4.
