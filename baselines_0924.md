# baselines_0924

UEFA Nations League 2026–27, matchday 1. Three divisions on this slate
(League A, League B, League D); each division's line is written the first
time a fixture from it is carded, and read from this file afterwards.
2026–27 has no completed match in any division before today, so every
line is a completed earlier edition of the same division.

Method, as on 0919 and 0920: recomputed from ESPN's public match record,
not searched. Event lists from `site.web.api.espn.com/.../uefa.nations/scoreboard?dates=YYYYMM`
(the date-range form of that query now returns HTTP 400; monthly queries
work), each match then read from its own summary — boxscore for fouls,
yellow and red cards, corners and shots; key events for goal minute,
scoring side and penalty kicks. The goal-timing parser reconciled against
the official final score on 30 of 30 matches below. **Zero baseline
searches spent.**

Counting conventions match the earlier files: cards per game is yellows
plus reds per match, both teams (ESPN boxscore); fouls, corners and shots
are per team per match; clean sheet / failed to score is per
team-appearance; first-half goals is per match, both sides. Penalties are
penalty kicks taken (scored, saved or missed) in ESPN's key events.
No xG exists for this competition in ESPN's record, and Understat does not
cover national teams: **no divisional xG line, none estimated.**

---

## UEFA Nations League D — first carded on f1 (Andorra – Malta)

### 2024–25 League D (12 matches — the primary line on every League D card)
Groups D1 San Marino, Gibraltar, Liechtenstein; D2 Moldova, Malta, Andorra.
Four of the six (Gibraltar, Malta, Andorra, Liechtenstein) are in 2026–27
League D; San Marino and Moldova went up, Lithuania and Azerbaijan came
down from League C.
- goals per game 1.58; over 2.5 16.7%; BTTS 25.0%; home win 41.7%; draw 33.3%; away win 25.0%
- clean sheet / failed to score 45.8% per team-appearance; under 1.5 goals 58.3% of matches; two 0–0s
- first-half goals 0.58 per match
- cards per game 7.42 (3.71 per team); fouls 16.58 per team; corners 3.08 per team
- shots 9.38 per team; shots on target 2.88 per team
- penalty kicks 0.75 per match (9 in 12)

### 2022–23 League D (18 matches — cross-check, not the card line)
Groups D1 Latvia, Moldova, Andorra, Liechtenstein; D2 Estonia, Malta, San Marino.
- goals per game 2.44; over 2.5 44.4%; BTTS 38.9%; home win 44.4%; draw 11.1%; away win 44.4%
- clean sheet / failed to score 33.3% per team-appearance
- first-half goals 0.94 per match
- cards per game 3.94; fouls 12.81 per team; corners 4.39 per team
- shots 10.83 per team; shots on target 3.53 per team
- penalty kicks 0.50 per match

### Both editions pooled (30 matches)
- goals per game 2.10; over 2.5 33.3%; BTTS 33.3%; home win 43.3%; draw 20.0%
- first-half goals 0.80; cards per game 5.33; fouls 14.32 per team; corners 3.87 per team

**The division is not a fixed point.** The two editions differ on nearly
every line: goals 1.58 against 2.44, over 2.5 16.7% against 44.4%, draws
33.3% against 11.1%, and cards 7.42 against 3.94 per match on fouls 16.58
against 12.81 per team. Twelve and eighteen matches between six and seven
sides, with membership changing each edition, is the thinnest baseline
this board has used. The 2024–25 line is printed on the card because it is
the most recent edition and shares four of its six sides with 2026–27;
where the 2022–23 figure disagrees materially, the card says so.

## Sources for every line above
- ESPN scoreboard `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`.
- ESPN summaries `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}` — 30 matches.
- ESPN standings `site.web.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2022,2024,2026}` for group membership.

---

## UEFA Nations League A — first carded on f2 (Netherlands – Germany)

### 2024–25 League A (48 matches — the primary line on every League A card)
Group stage only, four groups of four, six matches per side: A1 Portugal,
Croatia, Scotland, Poland; A2 France, Italy, Belgium, Israel; A3 Germany,
Netherlands, Hungary, Bosnia-Herzegovina; A4 Spain, Denmark, Serbia,
Switzerland. The March 2025 quarter-finals and June 2025 Finals are not in
the line (two-legged and neutral-venue knockout ties, not group play).
Ten of the sixteen are in 2026–27 League A; Poland, Scotland, Israel,
Bosnia-Herzegovina, Hungary and Switzerland are not, and Türkiye, Greece,
England, Czechia, Norway and Wales are in.
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
- cards per game 3.33 (1 red in 48); fouls 11.01 per team; 6.61 fouls per card; corners 4.68 per team
- shots 11.38 per team; shots on target 4.18 per team
- penalty kicks 0.23 per match (11 in 48)

### Both editions pooled (96 matches)
- goals per game 2.78; over 2.5 51.0%; BTTS 55.2%; home win 41.7%; draw 26.0%
- first-half goals 1.18; cards per game 3.73; fouls 11.20 per team; corners 4.71 per team; penalty kicks 0.32 per match

**League A is steadier than League D but not fixed.** Fouls (11.39 against
11.01 per team) and corners (4.75 against 4.68) barely moved between
editions. Goals rose by 0.31 per match, over 2.5 by 10.4 points, first-half
goals by 0.31, and cards by 0.79 per match on almost the same foul count,
with ten reds against one. Penalty kicks nearly doubled. The 2024–25 line is
printed because it is the most recent edition and shares ten of its sixteen
sides with 2026–27.

Method as above: ESPN scoreboard `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`,
League A group membership from `…/uefa.nations/standings?season={2022,2024,2026}`,
and 96 summaries. One 2024–25 match (Scotland 2–3 Poland) carries every
goal, card and penalty twice in ESPN's key events; key events were
de-duplicated on type, minute, team and player, after which the
goal-timing parser reconciled against the official score on 96 of 96.
Penalty kicks are counted once per award. **Zero baseline searches spent.**

---

## UEFA Nations League B — first carded on f6 (Austria – Israel)

### 2024–25 League B (48 matches — the primary line on every League B card)
Group stage only, four groups of four, six matches per side: B1 Czechia,
Ukraine, Georgia, Albania; B2 England, Greece, Finland, Republic of Ireland;
B3 Norway, Austria, Slovenia, Kazakhstan; B4 Türkiye, Wales, Iceland,
Montenegro. The March 2025 A/B and B/C play-offs are not in the line
(two-legged promotion/relegation ties, not group play).
Five of the sixteen are in 2026–27 League B (Austria, Republic of Ireland,
Slovenia, Ukraine, Georgia); the other eleven are Israel, Kosovo,
Switzerland, Scotland, North Macedonia, Hungary, Northern Ireland,
Bosnia-Herzegovina, Sweden, Poland and Romania.
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
Slovenia, Serbia. Group stage only. Eight of these sides are in 2026–27
League B, three more than in the 2024–25 line.
- goals per game 2.67; over 2.5 47.6%; BTTS 52.4%; home win 45.2%; draw 28.6%; away win 26.2%
- clean sheet / failed to score 26.2% per team-appearance; under 1.5 goals 21.4%; two 0–0s
- first-half goals 1.07 per match
- cards per game 4.57 (2.29 per team; 184 yellows, 8 reds); fouls 11.17 per team; 4.89 fouls per card; corners 4.77 per team
- shots 11.61 per team; shots on target 3.99 per team
- penalty kicks 0.21 per match (9 in 42)

### Both editions pooled (90 matches)
- goals per game 2.67; over 2.5 48.9%; BTTS 47.8%; home win 45.6%; draw 23.3%
- first-half goals 1.10; cards per game 4.49; fouls 11.33 per team; 5.05 fouls per card; corners 4.64 per team; penalty kicks 0.24 per match

**League B is the steadiest of the three divisions on this slate on
volume, not on outcome.** Goals per match (2.67 in both), first-half goals
(1.12 against 1.07), cards (4.42 against 4.57), fouls (11.48 against 11.17
per team) and corners (4.52 against 4.77) barely moved between editions.
The split of outcomes did: BTTS 43.8% against 52.4%, draws 18.8% against
28.6%, away wins 35.4% against 26.2%, reds 3 against 8. It books more than
League A on the same foul count (4.42 cards per match at 5.20 fouls per
card, against League A's 4.13 at 5.52) and awards fewer penalty kicks
(0.27 against 0.42). The 2024–25 line is printed because it is the most
recent edition; it shares five of its sixteen sides with 2026–27, fewer
than the 2022–23 edition does (eight).

Method as above: ESPN scoreboard `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}`,
League B group membership from `…/uefa.nations/standings?season={2022,2024,2026}`,
and 90 summaries. Key events de-duplicated on type, period, minute, team
and participants. The goal-timing parser reconciled against the official
score on 89 of 90: Wales 1–0 Montenegro (698976, November 2024) has no key
events in ESPN's record, and its 36th-minute Wilson penalty was taken from
ESPN's commentary (goal, first-half goal and penalty kick added).
**Zero baseline searches spent.**
