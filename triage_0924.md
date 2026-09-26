# triage_0924

Slate size: 8 fixtures (slate.8.xlsx, UEFA Nations League 2026–27, three
divisions: League A, League B, League D). Capacity: 8 (no capacity line
given, default).
T1: 8 · T2: 0 · T3: 0.
Estimated search spend against the ceiling: 8 fixtures at T1 depth
(~13 searches each, 21 where the promoted or manager-change ceiling
applies) = 104–168. The promoted ceiling applies to f3 (Greece), f4
(Norway), f5 (Wales) and f7 (Kosovo) for certain; the manager-change
ceiling is unknown for all sixteen sides and could apply widely in the
first window after the World Cup. Baselines: three divisions, three
baseline lookups; 0 searches if they are rebuilt from the ESPN pipeline
as on 0919 and 0920 (the 2024–25 edition of each division, since 2026–27
has no matches before today). Roughly 104–171 searches.

Separation: none needed. Capacity equals slate size, no fixture scores 0
or less, and no division is capped, so every fixture takes a T1 place
whatever its rank. Totals still separate into three bands (7, 6, 5), but
no tie-break was used and no tier depends on the order. Read the tiers as
"capacity covered the whole slate", not as findings.

Lookups: 0 of 6 spent. Matchday and promoted status both came free from
the standing ESPN pipeline (logged in sources_0924.md under a Triage
heading): the 2026–27 Nations League standings show every side on 0
matches played and today's eight fixtures are the first dated events of
the edition, so this is matchday 1 for all eight; the 2026–27 group lists
against the 2024–25, 2022–23 and 2020–21 lists give promoted, relegated
and returning sides. No fixture sits on a capacity cut, so a search
could not have moved a tier in any case. Manager or system change is
outside the budget and the archive holds no national-team card, so it is
unknown for all sixteen sides; that is the reason every row is
provisional.

Two sheet questions from Phase 1, settled by the same pull:
- "Ireland" is the Republic of Ireland. ESPN's 2026–27 Group B3 is Israel,
  Austria, Republic of Ireland, Kosovo, and today's event reads "Republic
  of Ireland at Kosovo". Northern Ireland is in Group B2 and does not play
  today. fixtures_0924.md and progress_0924.md are amended.
- Both League B fixtures (f6, f7) are Group B3.
- Kickoffs: ESPN gives 16:00Z and 18:45Z, which are 18:00 and 20:45 in
  Europe/Rome. The sheet's times are Italian time.

f1 | 18:00 | Andorra – Malta | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | capacity covers the slate; both sides in League D for a third straight edition, coach status unknown
f2 | 20:45 | Netherlands – Germany | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | capacity covers the slate; both sides in League A every edition since 2020–21, coach status unknown
f3 | 20:45 | Serbia – Greece | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Greece promoted via the 2025 A/B play-off and new to League A (C, C, B in the three prior editions)
f4 | 20:45 | Norway – Denmark | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Norway promoted as B3 winners and new to League A (B in all three prior editions)
f5 | 20:45 | Portugal – Wales | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Wales promoted as B4 winners, back after one edition out (A in 2022–23), so the returning fact does not score
f6 | 20:45 | Austria – Israel | coverage 3 | window 2 | distinct 0 (prov) | sample 0 | yield 0 | total 5 | T1 | capacity covers the slate; Israel relegated from League A after one edition, which none of the three facts scores
f7 | 20:45 | Kosovo – Republic of Ireland | coverage 3 | window 2 | distinct 2 (prov) | sample 0 | yield 0 | total 7 | T1 | Kosovo promoted via the 2025 B/C play-off and new to League B (D, C, C, C before)
f8 | 20:45 | Liechtenstein – Lithuania | coverage 3 | window 2 | distinct 1 (prov) | sample 0 | yield 0 | total 6 | T1 | Lithuania relegated and new to League D (C in all three prior editions)

Signal notes.
- Coverage 3 for all three divisions, scored from the division, not the
  game. ESPN publishes the same match record for every Nations League tie
  from League A to League D: a full box score (shots, shots on target,
  possession, fouls, yellow and red cards, corners), key events, venue
  and the appointed referee. Checked on eight 2024–25 ties across all
  four leagues (Andorra, Malta, Liechtenstein and Lithuania among them):
  identical 28-field box score in every one. What keeps every division
  off 4: no match-level xG in the standing pipeline (Understat does not
  cover national teams; other sources are partial at best), referee
  records findable per official but not tabulated for this competition,
  and no transfer-fee layer at all. The RESEARCH SPEC's fee field has no
  national-team equivalent; squad turnover here means call-ups and
  post-World Cup retirements, which federations publish as squad lists.
  League D is not scored lower than A or B: its box scores are complete,
  and the referees on the 2024–25 League D sample were established
  officials with findable records (one was a Premier League referee).
- Window 2 on every row: all eight kick off today, inside 72 hours of
  this run (run at 16:00 Europe/Rome; earliest kickoff 18:00). UEFA
  appointments for a matchday-1 fixture are normally published by now.
- Sample 0 on every row, counted, not assumed. ESPN's 2026–27 standings
  show 0 matches played for all 48 sides in Leagues A to D, and today's
  eight are the first dated events of the edition. The 2026–27
  national-team season is taken to open with this matchday; the World
  Cup, which ended on 19 July, belongs to 2025–26 and is not counted.
  By the spec this is not a demotion: nothing on any card can be checked
  against 2026–27 play, and section D has to say so on all eight.
- Distinct is scored on three facts: (1) a promoted side, from the
  2026–27 groups against 2024–25; (2) a coach change inside the window,
  unknown for all sixteen sides; (3) either side new to the division or
  back after two or more editions out, checked against 2024–25, 2022–23
  and 2020–21. A promotion after one edition out scores (1) but not (3),
  as on 0920.
  Promoted into their division this edition, on this slate: Greece (B2
  runners-up 2024–25, won the A/B play-off; Scotland went down), Norway
  (B3 winners), Wales (B4 winners), Kosovo (C2 runners-up 2024–25, won the
  B/C play-off; Iceland went down). Serbia kept its League A place
  through the play-off against Austria, which stays in League B.
  Relegated into their division this edition, on this slate: Israel (A2
  fourth, 2024–25, back in B after one edition up) and Lithuania (C2
  fourth, 2024–25, in League D for the first time in the editions ESPN
  covers). Relegation is not one of the scored facts, so Israel scores
  nothing; Lithuania scores (3) only.
  Division history, 2020–21 / 2022–23 / 2024–25 / 2026–27:
  Netherlands A/A/A/A · Germany A/A/A/A · Serbia B/B/A/A ·
  Greece C/C/B/A · Norway B/B/B/A · Denmark A/A/A/A · Portugal A/A/A/A ·
  Wales B/A/B/A · Austria B/A/B/B · Israel B/B/A/B · Kosovo C/C/C/B
  (D in 2018–19) · Republic of Ireland B/B/B/B · Andorra D/D/D/D ·
  Malta D/D/D/D · Liechtenstein D/D/D/D · Lithuania C/C/C/D.
- Yield 0 on every row. No national team appears in any prior
  progress_*.md or fx_*_f*.html; the archive is club football only.

Competitions on the slate:
- UEFA Nations League A: 4 fixtures (Group A2: f2, f3; Group A4: f4, f5),
  all T1. One baseline (2024–25 League A).
- UEFA Nations League B: 2 fixtures (Group B3: f6, f7), both T1. One
  baseline (2024–25 League B).
- UEFA Nations League D: 2 fixtures (Group D1: f1; Group D2: f8), both
  T1. One baseline (2024–25 League D). League D ran two groups of three
  in 2024–25 and runs two groups of three again, so its baseline rests on
  12 matches, the thinnest line on the slate.
Three baselines in all. No baselines_N.md carries any Nations League
line, so all three are new. Each division's 2024–25 membership differs
from 2026–27 by the promoted and relegated sides above, which the
baseline line should say.

Coverage floor: not needed. Every division has T1 fixtures.

Capped by low evidence coverage: none (all three divisions score 3).

Provisional distinctiveness (coach status unknown for sides whose status
could still raise the score): all eight rows. None of them can move a
tier: every fixture is already T1 and there is no T2 or T3 to promote
from. The Phase 2 rule allowing one provisional fixture to be promoted to
T1 has nothing to act on.
