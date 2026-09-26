# triage_0926

Slate size: 10 fixtures (slate.10.xlsx, UEFA Nations League 2026–27, three
divisions: League A, League B, League C). Capacity: 8 (no capacity line
given, default).
T1: 8 · T2: 2 · T3: 0.
Estimated search spend against the ceiling: 8 fixtures at T1 depth
(~13 searches each, 17 where one side is promoted, 21 where both sides
carry the promoted or manager-change ceiling) = 104–168, plus 2 fixtures
at T2 depth (~8 each) = 16. The promoted ceiling applies to f2 (San
Marino), f6 (Czechia), f7 (England), f8 (North Macedonia) and f10
(Moldova) for certain; the manager-change ceiling is unknown for all
twenty sides and could apply widely in the first window after the World
Cup. Baselines: three divisions. All three lines already exist in
baselines_0925.md (2024–25 editions, rebuilt from the ESPN pipeline); by
the once-per-slate rule baselines_0926.md still needs its own entries, at
0 searches if they are rebuilt from the ESPN pipeline again. Roughly
120–184 searches.

Separation: 7 of the 8 T1 places were decided by score alone. Totals fall
in three bands (7 × 3, 6 × 4, 5 × 3), and the two upper bands fill seven
places. The eighth place sits inside the 5 band, where coverage and sample
depth are tied on every row; it went to f1 on earlier kickoff, a
tie-break that carries no evidence, so read f1's T1 as "first in line",
not as a finding. f3 and f4 are T2 because capacity ran out, tied with each
other on every signal including kickoff. Read the tiers as capacity
allocation, not as views on the games.

Lookups: 0 of 6 spent. Matchday and promoted status came free from the
standing ESPN pipeline (logged in sources_0926.md under a Triage
heading): the 2026–27 Nations League standings show every side on
today's slate on 0 matches played, and today's ten are these groups'
first dated events (scoreboard 20260904–20260926 carries no earlier match
for any of them), so this is matchday 1 for all ten; the 2026–27 group
lists against the 2024–25, 2022–23 and 2020–21 lists, plus the March 2025
relegation play-offs, give promoted, relegated and returning sides. No
lookup could have moved a tier: the only ties are inside the 5 band and
capacity fixes which of them fits, so a search would only have
re-ordered a tie-break. Manager or system change is outside the budget
and the archive holds no card on any of these twenty sides, so it is
unknown for all of them; that is the reason every row is provisional.

Sheet questions from Phase 1, settled by the same pull:
- The two "UEFA Nations League A" rows (f6, f7) are Group A3 (Spain,
  Croatia, England, Czechia). The two "UEFA Nations League B" rows (f1,
  f8) are Group B1 (Slovenia, Scotland, North Macedonia, Switzerland).
  Group C1: f2, f9. Group C3: f3, f10. Group C4: f4, f5, as the sheet
  labels them.
- Kickoffs: ESPN gives 13:00Z, 16:00Z and 18:45Z, which are 15:00, 18:00
  and 20:45 in Europe/Rome. The sheet's times are Italian time.

f1 | 15:00 | Slovenia – Scotland | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | 8th place by earlier kickoff after a coverage and sample tie; Scotland relegated via the play-off but were in B in 2020–21 and 2022–23, so nothing scores
f2 | 18:00 | San Marino – Finland | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | San Marino promoted as D1 winners and new to League C (D in all three prior editions)
f3 | 18:00 | Faroe Islands – Kazakhstan | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T2 | capacity spent; Kazakhstan relegated after one edition in B, so returning does not score; coach status unknown
f4 | 18:00 | Bulgaria – Luxembourg | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T2 | capacity spent; both sides in League C every edition since 2020–21, coach status unknown
f5 | 18:00 | Iceland – Estonia | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Iceland relegated after the B/C play-off and new to League C (A, B, B in the three prior editions)
f6 | 20:45 | Czechia – Croatia | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Czechia promoted as B1 winners; one edition in B after A in 2022–23, so returning does not score
f7 | 20:45 | England – Spain | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | England promoted as B2 winners; one edition in B after A in 2020–21 and 2022–23, so returning does not score
f8 | 20:45 | North Macedonia – Switzerland | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | North Macedonia promoted as C4 winners; both sides new to League B (C and A in the prior editions)
f9 | 20:45 | Albania – Belarus | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Albania relegated and back in League C after two editions in B
f10 | 20:45 | Slovakia – Moldova | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Moldova promoted as D2 winners and back in League C after two editions in D

Signal notes.
- Coverage 3 for all three divisions, scored from the division, not the
  game, on the same basis as triage_0924.md and triage_0925.md: ESPN
  publishes a full box score (shots, possession, fouls, cards, corners),
  key events, venue and referee for every Nations League tie from League A
  to League D. What keeps every division off 4: no match-level xG in the
  standing pipeline, referee records findable per official but not
  tabulated for this competition, and no transfer-fee layer. The RESEARCH
  SPEC's fee field has no national-team equivalent; squad turnover here
  means call-ups and post-World Cup retirements. No competition scores 2 or
  less, so no cap applies. San Marino, Faroe Islands and Kazakhstan have
  the thinnest press coverage on the slate, and Phase 2 should say so if a
  field comes up empty, but that is a team fact, not a division score.
- Window 2 on every row: all ten kick off today, inside 72 hours of this
  run.
- Sample 0 on every row, counted, not assumed. ESPN's 2026–27 standings
  show 0 matches played for all twenty sides; Groups A3, B1, C1, C3 and C4
  open today. The World Cup belongs to 2025–26 and is not counted. By the
  spec this is not a demotion; section D has to say so on all ten.
- Distinct is scored on three facts, as on 0924 and 0925: (1) a promoted
  side, from the 2026–27 groups against 2024–25; (2) a coach change inside
  the window, unknown for all twenty sides; (3) either side new to the
  division or back after two or more editions out, checked against
  2024–25, 2022–23 and 2020–21. Each fact scores once per fixture however
  many sides carry it. A promotion after one edition out scores (1) but not
  (3). Relegation is not a scored fact.
  Promoted into their division this edition, on this slate: Czechia (B1
  winners 2024–25), England (B2 winners), North Macedonia (C4 winners),
  San Marino (D1 winners), Moldova (D2 winners).
  Relegated into their division this edition, on this slate: Scotland
  (A1 third, lost the relegation play-off to Greece 3–1 on aggregate),
  Switzerland (A4 fourth), Finland (B2 fourth), Albania (B1 fourth),
  Kazakhstan (B3 fourth), Iceland (B4 third, lost the relegation play-off
  to Kosovo 5–2 on aggregate).
  Stayed in the same division: Croatia, Spain (A); Slovenia (B, survived
  the play-off against Slovakia 1–0 on aggregate); Belarus, Faroe Islands,
  Slovakia, Bulgaria, Luxembourg, Estonia (C).
  Division history, 2020–21 / 2022–23 / 2024–25 / 2026–27:
  Czechia B/A/B/A · Croatia A/A/A/A · England A/A/B/A · Spain A/A/A/A ·
  Slovenia C/B/B/B · Scotland B/B/A/B · North Macedonia C/C/C/B ·
  Switzerland A/A/A/B · San Marino D/D/D/C · Finland B/B/B/C ·
  Albania C/B/B/C · Belarus C/C/C/C · Faroe Islands D/C/C/C ·
  Kazakhstan C/C/B/C · Slovakia B/C/C/C · Moldova C/D/D/C ·
  Bulgaria B/C/C/C · Luxembourg C/C/C/C · Iceland A/B/B/C ·
  Estonia C/D/C/C.
- Yield 0 on every row. No side on this slate appears in any prior
  progress_*.md or as a card title in any fx_*_f*.html; the national-team
  cards in the archive are 0924's and 0925's, and none of their
  thirty-two sides plays today. Several of today's sides appear inside
  those cards as opponents' history, which is not a card on them.

Competitions on the slate:
- UEFA Nations League A: 2 fixtures (Group A3: f6, f7), both T1. One
  baseline (2024–25 League A).
- UEFA Nations League B: 2 fixtures (Group B1: f1, f8), both T1. One
  baseline (2024–25 League B).
- UEFA Nations League C: 6 fixtures (Group C1: f2, f9; Group C3: f3, f10;
  Group C4: f4, f5), four T1 (f2, f5, f9, f10) and two T2 (f3, f4). One
  baseline (2024–25 League C).
Three baselines in all. Each division's 2024–25 membership differs from
2026–27 by the promoted and relegated sides above, which the baseline line
should say.

Coverage floor: not needed. Every division has T1 fixtures.

Capped by low evidence coverage: none (all three divisions score 3).

Provisional distinctiveness (coach status unknown): all ten rows. Only f3
and f4 could move a tier: they sit at T2 on a tie and Phase 2 may promote
one to T1 if its first search finds a coach change or other structural fact
that contradicts the triage assumption, saying so in that run's
confirmation line and amending progress_0926.md.
