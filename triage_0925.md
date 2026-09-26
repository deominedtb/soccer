# triage_0925

Slate size: 8 fixtures (slate.9.xlsx, UEFA Nations League 2026–27, three
divisions: League A, League B, League C). Capacity: 8 (no capacity line
given, default).
T1: 8 · T2: 0 · T3: 0.
Estimated search spend against the ceiling: 8 fixtures at T1 depth
(~13 searches each, 21 where the promoted or manager-change ceiling
applies) = 104–168. The promoted ceiling applies to f1 (Northern
Ireland), f4 (Türkiye) and f7 (Sweden, Romania) for certain; the
manager-change ceiling is unknown for all sixteen sides and could apply
widely in the first window after the World Cup. Baselines: three
divisions. League A and League B lines already exist in baselines_0924.md
(2024–25 edition, rebuilt from the ESPN pipeline); by the once-per-slate
rule baselines_0925.md still needs its own entries, at 0 searches if they
are rebuilt from the ESPN pipeline again. League C is new to the archive.
Roughly 104–171 searches.

Separation: none needed. Capacity equals slate size, no fixture scores 0
or less, and no division is capped, so every fixture takes a T1 place
whatever its rank. Totals separate into three bands (7, 6, 5), but no
tie-break was used and no tier depends on the order. Read the tiers as
"capacity covered the whole slate", not as findings.

Lookups: 0 of 6 spent. Matchday and promoted status came free from the
standing ESPN pipeline (logged in sources_0925.md under a Triage
heading): the 2026–27 Nations League standings show every side on
today's slate on 0 matches played and today's eight are these groups'
first dated events, so this is matchday 1 for all eight; the 2026–27
group lists against the 2024–25, 2022–23 and 2020–21 lists give promoted,
relegated and returning sides. No fixture sits on a capacity cut, so a
search could not have moved a tier in any case. Manager or system change
is outside the budget and the archive holds no card on any of these
sixteen sides, so it is unknown for all of them; that is the reason every
row is provisional.

Sheet questions from Phase 1, settled by the same pull:
- The two "UEFA Nations League A" rows (f3, f4) are Group A1. The two
  "UEFA Nations League C" rows (f2, f8) are Group C2.
- "Turkiye" is ESPN's "Türkiye"; "Bosnia and Herzegovina" is ESPN's
  "Bosnia-Herzegovina".
- Kickoffs: ESPN gives 16:00Z and 18:45Z, which are 18:00 and 20:45 in
  Europe/Rome. The sheet's times are Italian time.

f1 | 18:00 | Georgia – Northern Ireland | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Northern Ireland promoted as C3 winners, back in League B after two editions out
f2 | 18:00 | Armenia – Latvia | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | capacity covers the slate; both sides in League C for a second straight edition, coach status unknown
f3 | 20:45 | Italy – Belgium | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | capacity covers the slate; both sides in League A every edition since 2020–21, coach status unknown
f4 | 20:45 | Turkiye – France | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Türkiye promoted via the 2025 A/B play-off and new to League A (B, C, B in the three prior editions)
f5 | 20:45 | Hungary – Ukraine | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Hungary relegated and back in League B after two editions in A
f6 | 20:45 | Poland – Bosnia and Herzegovina | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Poland relegated and new to League B (A in all three prior editions)
f7 | 20:45 | Sweden – Romania | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | both sides promoted from League C, each back after one edition out, so the returning fact does not score
f8 | 20:45 | Montenegro – Cyprus | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Montenegro relegated and back in League C after two editions in B

Signal notes.
- Coverage 3 for all three divisions, scored from the division, not the
  game, on the same basis as triage_0924.md: ESPN publishes a full box
  score (shots, possession, fouls, cards, corners), key events, venue and
  referee for every Nations League tie from League A to League D. What
  keeps every division off 4: no match-level xG in the standing pipeline,
  referee records findable per official but not tabulated for this
  competition, and no transfer-fee layer. The RESEARCH SPEC's fee field
  has no national-team equivalent; squad turnover here means call-ups and
  post-World Cup retirements.
- Window 2 on every row: all eight kick off today, inside 72 hours of
  this run.
- Sample 0 on every row, counted, not assumed. ESPN's 2026–27 standings
  show 0 matches played for all sixteen sides; Groups A1, B2, B4 and C2
  open today. The World Cup belongs to 2025–26 and is not counted. By the
  spec this is not a demotion; section D has to say so on all eight.
- Distinct is scored on three facts, as on 0924: (1) a promoted side,
  from the 2026–27 groups against 2024–25; (2) a coach change inside the
  window, unknown for all sixteen sides; (3) either side new to the
  division or back after two or more editions out, checked against
  2024–25, 2022–23 and 2020–21. A promotion after one edition out scores
  (1) but not (3). Relegation is not a scored fact.
  Promoted into their division this edition, on this slate: Türkiye (B4
  runners-up 2024–25, won the A/B play-off; Hungary went down),
  Northern Ireland (C3 winners), Sweden (C1 winners), Romania (C2
  winners).
  Relegated into their division this edition, on this slate: Poland (A1
  fourth), Bosnia-Herzegovina (A3 fourth), Hungary (lost the A/B
  play-off), Montenegro (B4 fourth).
  Division history, 2020–21 / 2022–23 / 2024–25 / 2026–27:
  Italy A/A/A/A · Belgium A/A/A/A · France A/A/A/A · Türkiye B/C/B/A ·
  Georgia C/C/B/B · Northern Ireland B/C/C/B · Hungary B/A/A/B ·
  Ukraine A/B/B/B · Poland A/A/A/B · Bosnia-Herzegovina A/B/A/B ·
  Sweden A/B/C/B · Romania B/B/C/B · Armenia C/B/C/C · Latvia D/D/C/C ·
  Montenegro C/B/B/C · Cyprus C/C/C/C.
- Yield 0 on every row. No side on this slate appears in any prior
  progress_*.md or fx_*_f*.html as a carded team; the only national-team
  cards in the archive are 0924's, and none of its sixteen sides plays
  today.

Competitions on the slate:
- UEFA Nations League A: 2 fixtures (Group A1: f3, f4), both T1. One
  baseline (2024–25 League A).
- UEFA Nations League B: 4 fixtures (Group B2: f1, f5; Group B4: f6, f7),
  all T1. One baseline (2024–25 League B).
- UEFA Nations League C: 2 fixtures (Group C2: f2, f8), both T1. One
  baseline (2024–25 League C), new to the archive.
Three baselines in all. Each division's 2024–25 membership differs from
2026–27 by the promoted and relegated sides above, which the baseline
line should say.

Coverage floor: not needed. Every division has T1 fixtures.

Capped by low evidence coverage: none (all three divisions score 3).

Provisional distinctiveness (coach status unknown): all eight rows. None
of them can move a tier: every fixture is already T1 and there is no T2
or T3 to promote from.
