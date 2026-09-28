# triage_0920

Slate size: 20 fixtures (slate.7.xlsx, five competitions). Capacity: 8
(no capacity line given, default).
T1: 8 · T2: 5 · T3: 7. T2 is five, not four: the fifth is the coverage
floor (Ligue 1, see below) and nothing was demoted to pay for it.
Estimated search spend against the ceiling: 8 fixtures at T1 depth
(~13 searches each, 21 where the promoted or manager-change ceiling
applies — it applies to all eight) = 104–168, + 5 at T2 depth (~8 each)
= 40, + baselines. Roughly 144–208 searches. Baselines: five
competitions, five baseline lookups; 0 searches if they are rebuilt from
the ESPN pipeline as on 0919 (2025–26 lines carried from
baselines_0919.md, 2026–27 lines recomputed), up to 5 if searched.

Separation: 3 fixtures were separated by score alone (f2, f7, f15 at
total 10, all T1). The other 17 fell to a tie-break: 4 on sample depth
(f13 out of T1 into T2, and f3, f11, f17 out of the T2 place into T3, all
on a side with only 4 competitive matches), and 13 on kickoff or sheet
order — the seven sample-2 fixtures at total 9 (f1, f6, f9, f10, f12 took
the five open T1 places on earlier kickoff; f16 and f19 went to T2 on
later kickoff) and the six sample-2 fixtures at total 8 (f4 took the one
open T2 place; f4, f5 and f8 all kick off at 15:00, so f4 won on sheet
order). Triage has mostly reproduced kickoff order at both the T1/T2 and
T2/T3 lines. Read those tiers as bookkeeping, not findings. Override
freely.

Lookups: 0 of 6 spent. Matchday and promoted status are the two things
the budget allows, and both came free from the ESPN standings pipeline
that sources_0919.md lists as "standing data pipeline, not a search"
(2026 against 2025 standings for the promoted sides; games played plus
one for the round). Manager or system change is outside the budget, so it
stays unknown for every club not already carded in the archive; that is
the reason four fixtures are marked provisional. The pulls are logged in
sources_0920.md under a Triage heading.

Matchday, from standings: Premier League matchweek 5, LaLiga jornada 7,
Serie A giornata 5, Bundesliga matchday 4, Ligue 1 journée 5. Several
clubs show one league match fewer than their division's round (Leverkusen,
Leipzig, Paderborn, Elversberg, Schalke and Hoffenheim on 3 in the
Bundesliga; Getafe, Málaga, Deportivo, Real Betis, Real Madrid, Atlético,
Valencia, Real Sociedad and Villarreal on 6 in LaLiga; Levante on 5): they
play today, so their counts are before this round. Phase 2 confirms the
matchday and says why where a club is behind its division.

f1 | 12:30 | Fiorentina – Napoli | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T1 | tie at 9; earliest kickoff among the sample-2 group; both clubs changed coach in the window (Napoli July, Fiorentina September)
f2 | 14:00 | Getafe – Málaga | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Málaga promoted and back after two or more seasons out
f3 | 15:00 | Auxerre – Brest | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T3 | tie at 8; dropped on sample depth, both clubs on 4 matches (both changed coach, scored)
f4 | 15:00 | Bournemouth – Liverpool | coverage 4 | window 2 | distinct 1 | sample 2 | yield -1 | total 8 | T2 | tie at 8 (sample 2); first in sheet order at 15:00; Bournemouth carded in slate 0917 (fx_0917_f8.html)
f5 | 15:00 | Leeds – Crystal Palace | coverage 4 | window 2 | distinct 1 | sample 2 | yield -1 | total 8 | T3 | tie at 8 (sample 2); behind f4 in sheet order at 15:00; Crystal Palace carded in slate 0917 (fx_0917_f5.html)
f6 | 15:00 | Man City – Sunderland | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T1 | tie at 9; earlier kickoff than the T2 group; City coach change (29 June)
f7 | 15:00 | Frosinone – Como | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Frosinone promoted and back after two seasons out
f8 | 15:00 | Parma – Genoa | coverage 4 | window 2 | distinct 0 | sample 2 | yield 0 | total 8 | T3 | tie at 8 (sample 2); behind f4 in sheet order at 15:00; both coaches known unchanged, no promoted side
f9 | 15:30 | Leverkusen – RB Leipzig | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T1 | tie at 9; earlier kickoff than the T2 group; Leipzig coach change (24 June)
f10 | 16:15 | Atlético Madrid – Real Madrid | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T1 | tie at 9; earlier kickoff than the T2 group; Real Madrid coach change (11 June)
f11 | 17:15 | Nice – Lille | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T3 | tie at 8; dropped on sample depth, Nice on 4 matches (Lille coach change, 1 June, scored)
f12 | 17:30 | Fulham – Man United | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T1 | tie at 9; last open T1 place on kickoff; Fulham coach appointed 7 July
f13 | 17:30 | Schalke 04 – Elversberg | coverage 4 | window 2 | distinct 2 | sample 1 | yield 0 | total 9 | T2 | tie at 9; out of T1 on sample depth, both clubs on 4 matches; both promoted, both new to or back in the division
f14 | 18:00 | Juventus – Atalanta | coverage 4 | window 2 | distinct 1 | sample 2 | yield -1 | total 8 | T3 | tie at 8 (sample 2); out on kickoff; Juventus carded in slate 0917 (fx_0917_f6.html)
f15 | 18:30 | Deportivo A Coruña – Real Betis | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Deportivo promoted and back after two or more seasons out
f16 | 18:30 | Villarreal – Levante | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T2 | tie at 9; out of T1 on later kickoff; Villarreal coach change (1 June)
f17 | 19:30 | Paderborn – Hoffenheim | coverage 4 | window 2 | distinct 2 (prov) | sample 1 | yield -1 | total 8 | T3 | tie at 8; dropped on sample depth, Paderborn on 4 matches; Hoffenheim carded in slate 0917 (fx_0917_f2.html); Paderborn coach status unknown
f18 | 20:45 | Marseille – PSG | coverage 4 | window 2 | distinct 1 | sample 2 | yield -1 | total 8 | T2 | coverage floor: Ligue 1 would otherwise have no fixture at T2 or better; top of the Ligue 1 fixtures at 8 on sample depth; Marseille carded in slate 0917 (fx_0917_f3.html)
f19 | 20:45 | Milan – Lecce | coverage 4 | window 2 | distinct 1 | sample 2 | yield 0 | total 9 | T2 | tie at 9; out of T1 on later kickoff; Milan coach change (June)
f20 | 21:00 | Valencia – Real Sociedad | coverage 4 | window 2 | distinct 1 | sample 2 | yield -1 | total 8 | T3 | tie at 8 (sample 2); out on kickoff; Real Sociedad carded in slate 0917 (fx_0917_f8.html)

Signal notes.
- Coverage 4 for all five divisions: Premier League, LaLiga, Serie A,
  Bundesliga and Ligue 1 publish match-level xG, shot data, per-referee
  card records and complete fees. No division on the slate is capped.
- Window 2 on every row: every kickoff falls today, inside 72 hours of
  this run (run at 02:54 local; earliest kickoff 12:30 CEST).
- Sample is the thinner-played of the two sides, counted, not assumed:
  league matches played (ESPN standings) plus every completed competitive
  match in the ESPN cup and European records since 1 July (DFB-Pokal, EFL
  Cup, Coppa Italia, Champions League and its qualifying, Europa League
  and Conference League qualifying, and the UEFA, German, French and
  English super cups). Copa del Rey, Coupe de France, Italian Super Cup
  and Spanish Super Cup have no matches in the record. Counts by club,
  league + other, before today's round:
  Premier League: Bournemouth 4+2, Liverpool 4+2, Leeds 4+2, Crystal
  Palace 4+2, Man City 4+3, Sunderland 4+2, Fulham 4+2, Man United 4+2.
  LaLiga: Getafe 6+2, Málaga 6+0, Atlético 6+1, Real Madrid 6+1,
  Deportivo 6+0, Real Betis 6+1, Villarreal 6+1, Levante 5+0, Valencia
  6+0, Real Sociedad 6+1. Serie A: Fiorentina 4+2, Napoli 4+1, Frosinone
  4+2, Como 4+1, Parma 4+2, Genoa 4+2, Juventus 4+1, Atalanta 4+2, Milan
  4+1, Lecce 4+1. Bundesliga: Leverkusen 3+2, Leipzig 3+2, Schalke 3+1,
  Elversberg 3+1, Paderborn 3+1, Hoffenheim 3+2. Ligue 1: Auxerre 4+0,
  Brest 4+0, Nice 4+0, Lille 4+1, Marseille 4+1, PSG 4+3.
  Sample 1 fixtures are those with a side on exactly four competitive
  matches: f3 (Auxerre, Brest), f11 (Nice), f13 (Schalke, Elversberg),
  f17 (Paderborn). The counts do not include today's fixtures.
- Distinct is scored on three facts: (1) a promoted side, from the 2026
  against 2025 standings; (2) a coach change since 1 June 2026, known
  only from archived cards; (3) either club new to the division or back
  after two or more seasons out (absent from the 2024–25 standings too),
  so a promotion after one season away scores (1) but not (3).
  Promoted this season, ESPN 2026 list against 2025: Premier League
  Coventry, Hull, Ipswich; LaLiga Deportivo, Málaga, Racing Santander;
  Serie A Frosinone, Monza, Venezia; Bundesliga Paderborn, Elversberg,
  Schalke; Ligue 1 Le Mans, Troyes. On this slate: Málaga (f2), Frosinone
  (f7), Schalke and Elversberg (f13), Deportivo (f15), Paderborn (f17).
  All six score (3) as well: none was in its division in 2024–25, and
  Frosinone's last top-flight season was 2023–24.
  Coach change inside the window, from archived cards: Fiorentina (new
  head coach appointed early September, "two managers in four days",
  fx_16_f2), Napoli (July, fx_14_f4), Auxerre (Will Still, 12 June,
  fx_9_f18), Brest (Julien Lachuer, 27 June, fx_13_f19), Bournemouth
  (Marco Rose, June, fx_9_f7), Liverpool (Iraola from Bournemouth, summer,
  fx_9_f7 and fx_14_f3), Crystal Palace (appointed June, fx_0917_f5),
  Man City (Maresca, 29 June, fx_8_f5), RB Leipzig (Demichelis, 24 June,
  fx_15_f4), Real Madrid (Mourinho, announced 11 June, fx_10_f6), Lille
  (Davide Ancelotti, 1 June, fx_8_f3), Fulham (Arbeloa, 7 July, fx_0915_f5),
  Atalanta (Sarri, announced 15 June, fx_11_f3), Villarreal (Íñigo Pérez,
  1 June, fx_0914_f5), Marseille (Génésio, summer, third coach in five
  months, fx_0917_f3 and fx_16_f3), Milan (Amorim, June, fx_0916_f1),
  Valencia (Corberán dismissed 13 September, interim coach, fx_0915_f3).
  Known unchanged, or changed before the window: Leeds (fx_13_f8),
  Sunderland (Le Bris, extended, fx_13_f7), Como and Parma (fx_0914_f1),
  Genoa (fx_12_f3), Atlético (Simeone), Schalke (Muslić, fx_16_f1),
  Elversberg (fx_13_f3), Real Betis (Pellegrini, fx_12_f4), Hoffenheim
  (fx_13_f4), PSG (fx_14_f5), Lecce (Di Francesco, fx_11_f1), Man United
  (Carrick since January, made permanent in the summer — a status change,
  not a change of coach, fx_15_f5), Juventus (Spalletti since 30 October
  2025, fx_0917_f6), Levante (Castro since December 2025, fx_9_f9), Real
  Sociedad (since December 2025, fx_0917_f8), Leverkusen (new coach in May,
  before the window, fx_13_f2). Nice changed coach per fx_10_f4, date not
  established; it moves nothing, because Lille already scores the coach
  fact in f11. Unknown: Getafe (Bordalás named in fx_11_f2, never stated
  as unchanged), Málaga, Frosinone, Deportivo, Paderborn.
- Archive conflict to resolve in Phase 2 (f9): fx_13_f2 says Leverkusen
  replaced Ole Werner with Carles Martínez in May, and fx_15_f4 says
  Leipzig dismissed Ole Werner and appointed Demichelis on 24 June. Both
  cards name Werner. Neither changes a score (Leipzig's change is dated
  and in the window; Leverkusen's is before it), but one of the two is
  wrong.
- Yield: window is the last three slates, 0917, 0918 and 0919. Bournemouth
  (fx_0917_f8), Crystal Palace (fx_0917_f5), Juventus (fx_0917_f6),
  Hoffenheim (fx_0917_f2), Marseille (fx_0917_f3) and Real Sociedad
  (fx_0917_f8) each got a full T1 card there, so f4, f5, f14, f17, f18 and
  f20 score -1. No fixture has both clubs in the window, so none scores -2.
  No club on this slate appears in slates 0918 or 0919. Older cards
  outside the window, for information only: Liverpool (slate 0915),
  Leeds, Como, Parma (slate 0914), Fulham, Genoa, Valencia (slate 0915),
  Sunderland, Leverkusen, Milan (slate 0916), and the numbered slates 8–18
  for most of the rest.
- ESPN's site.api scoreboard host was not used; the standings and cup
  records came from site.web.api and sports.core.api, which answered
  normally today. Nothing in triage depends on the scoreboard.

Competitions on the slate:
- Premier League: 4 fixtures — T1 f6, f12; T2 f4; T3 f5. One baseline.
- LaLiga: 5 fixtures — T1 f2, f10, f15; T2 f16; T3 f20. One baseline.
- Serie A: 5 fixtures — T1 f1, f7; T2 f19; T3 f8, f14. One baseline.
- Bundesliga: 3 fixtures — T1 f9; T2 f13; T3 f17. One baseline.
- Ligue 1: 3 fixtures — T2 f18 (coverage floor); T3 f3, f11. One baseline.
Five baselines in all. baselines_0919.md already carries all five
competitions, so the 2025–26 lines are reused without a search and only
the 2026–27 lines need refreshing.

Coverage floor: applied once. Ligue 1 had no fixture at T2 or better, so
its highest-scoring fixture, f18 Marseille – PSG (total 8, tied with f3
and f11, ahead of them on sample depth), was promoted to T2. Marseille
was carded at full depth three days ago (fx_0917_f3.html), which is why
it scores -1 on yield; the floor takes the top Ligue 1 fixture whatever
its yield. Override if you would rather spend that T2 slot elsewhere.
Every other division already had a T1 or T2 fixture.

Capped by low evidence coverage: none (all five divisions score 4).

Provisional distinctiveness (coach status unknown for a club whose status
could still raise the score): f2, f7, f15, f17. f2, f7 and f15 are already
T1 at total 10, so a coach fact could not move their tier. f17 is the one
that can move: at 8 it sits on the T2/T3 line, and a Paderborn coach change
inside the window would lift it to 9 and take the fourth score-ranked T2
place from f4 (f4 would then fall to T3). Not provisional: every other
fixture is final at its score, because the promoted, coach and returning
facts are all known or already at the cap for that row.
Phase 2 may promote one provisional fixture to T1 when its first search
contradicts the triage assumption and will say so in that run's
confirmation line and amend progress_0920.md.

────────────────────────────────────────────────
OVERRIDE (yours), received after Phase 2 and Phase 3 completed

All seven T3 fixtures raised to T1 — f3, f5, f8, f11, f14, f17 and f20 —
to be researched at full RESEARCH SPEC depth with sections A–E. Taken as
given; the slate is not re-scored, no fixture was re-tiered that you did
not name, and nothing was demoted to pay for it. The scored tier stays
visible beside the override on every progress line, as "T3 → T1* (yours)".

Combined with the earlier instruction that the five T2 fixtures be
researched at full T1 depth, this means **every fixture on the slate is
now researched at full depth**: T1 as scored 8, T2 raised to full depth 5,
T3 raised to T1* 7 — twenty of twenty.

Estimated spend rises by roughly 90–150 searches for the seven, on top of
the ~144–208 already estimated, for a slate total of roughly 235–360.
Baselines are unaffected: all five competitions were already built in
baselines_0920.md from the ESPN pipeline at a cost of zero searches, and
the 2. Bundesliga, Serie B and LaLiga 2 lines needed for the promoted
clubs are already in that file too.

Note on what the override does not change. The triage scores stand as
recorded above: f3, f11 and f17 were separated out on sample depth (a side
on four competitive matches), f5, f14 and f20 on a club having received a
full card within the last three slates, and f8 on scoring zero for a
structural separator. Those reasons remain true and are stated on each
card, because they describe how much evidence the research could draw on —
which is now a property of the card rather than of the selection.
