# triage_0919

Slate size: 23 fixtures (slate.6.xlsx, five competitions). Capacity: 8
(no capacity line given, default).
T1: 8 · T2: 5 · T3: 10. T2 is five, not four: the fifth is the coverage
floor (Bundesliga, see below) and nothing was demoted to pay for it.
Estimated search spend against the ceiling: 8 fixtures at T1 depth
(~13 searches each, 21 where the promoted or manager-change ceiling
applies — it applies to all eight) = 104–168, + 5 at T2 depth (~8 each)
= 40, + baselines. Roughly 144–208 searches. Baselines: five
competitions, five baseline lookups; 0 searches if they are rebuilt from
the ESPN pipeline as on 0918 (2025–26 lines carried from
baselines_0918.md, 2026–27 lines recomputed), up to 5 if searched.

Separation: 15 fixtures were separated by score alone — the 8 T1 places
(totals 9–11) and the seven at total 7 (all T3). The other 8 tie at
total 8 for the four T2 places below the T1 line. Of those, 1 (f3) fell
on sample depth (Bologna on 4 competitive matches against 5 or more for
the rest), and the 4 T2 places among the remaining 7 went to the earlier
kickoffs — so 7 fixtures fell to the kickoff tie-break, 4 in (f1, f4, f9,
f12), 3 out (f14, f17, f23). The T1/T2 line is a score gap, 9 against 8,
and needs no tie-break. The T2/T3 line is mostly kickoff order: f3, f14
and f23 are T3 because they kick off later or have a thinner-played
side, not because their evidence is thinner in any way that matters.
Read those tiers as bookkeeping, not findings. Override freely.

Lookups: 0 of 6 spent. Matchday and promoted status are the two things
the budget allows, and both came free from the ESPN standings pipeline
that sources_0918.md already lists as "standing data pipeline, not a
search" (2026 against 2025 standings for the promoted sides; games
played plus one for the round). Manager or system change is outside the
budget, so it stays unknown for every club not already carded in the
archive; that is the reason most distinctiveness scores are marked
provisional. The pulls are logged in sources_0919.md under a Triage
heading.

Matchday, from standings: Premier League matchweek 5, LaLiga jornada 7,
Serie A giornata 5, Bundesliga matchday 4, Ligue 1 journée 5. Athletic
Club has 5 league matches played against 6 for Alavés — one of its
earlier league fixtures is outstanding; Phase 2 says why.

f1 | 13:30 | Tottenham – Aston Villa | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T2 | tie at 8 (sample 2); earlier kickoff than the T3 tied group
f2 | 14:00 | Osasuna – Rayo Vallecano | coverage 4 | window 2 | distinct 1 (prov) | sample 2 | yield 0 | total 9 | T1 | Rayo coach change since June (fx_0915_f2)
f3 | 15:00 | Bologna – Torino | coverage 4 | window 2 | distinct 1 (prov) | sample 1 | yield 0 | total 8 | T3 | tie at 8; dropped on sample depth, Bologna on 4 matches (Torino coach change scored)
f4 | 15:00 | Udinese – Cagliari | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T2 | tie at 8 (sample 2); earlier kickoff than the T3 tied group
f5 | 15:30 | M'gladbach – Mainz | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; both sides on 4 matches
f6 | 15:30 | Frankfurt – Freiburg | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; Frankfurt on 4 matches
f7 | 15:30 | Hamburger SV – Köln | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; both sides on 4 matches
f8 | 15:30 | Werder Bremen – Augsburg | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; both sides on 4 matches
f9 | 16:00 | Brighton – Arsenal | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T2 | tie at 8 (sample 2); earlier kickoff than the T3 tied group
f10 | 16:00 | Everton – Ipswich | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Ipswich promoted and changed coach (23 June)
f11 | 16:00 | Newcastle – Hull | coverage 4 | window 2 | distinct 3 | sample 2 | yield 0 | total 11 | T1 | Hull promoted and back after two seasons away, Newcastle changed coach (5 Aug); distinct at cap
f12 | 16:15 | Athletic Club – Deportivo Alavés | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T2 | tie at 8 (sample 2); earlier kickoff than the T3 tied group
f13 | 17:15 | Paris FC – Strasbourg | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; both sides on 4 matches
f14 | 18:00 | Roma – Inter | coverage 4 | window 2 | distinct 0 | sample 2 | yield 0 | total 8 | T3 | tie at 8; both coaches unchanged, no promoted side; out on kickoff
f15 | 18:30 | Celta Vigo – Racing Santander | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Racing promoted and back after a long absence
f16 | 18:30 | Nottm Forest – Coventry | coverage 4 | window 2 | distinct 2 (prov) | sample 2 | yield 0 | total 10 | T1 | Coventry promoted and back after a long absence
f17 | 18:30 | VfB Stuttgart – Dortmund | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T2 | coverage floor: Bundesliga would otherwise have no fixture at T2 or better; top-scoring Bundesliga fixture, out on kickoff in the tie
f18 | 20:45 | Venezia – Lazio | coverage 4 | window 2 | distinct 1 (prov) | sample 2 | yield 0 | total 9 | T1 | Venezia promoted
f19 | 20:45 | Angers – Troyes | coverage 4 | window 2 | distinct 2 (prov) | sample 1 | yield 0 | total 9 | T1 | Troyes promoted and back after a long absence
f20 | 20:45 | Le Mans – Lorient | coverage 4 | window 2 | distinct 2 (prov) | sample 1 | yield 0 | total 9 | T1 | Le Mans promoted and back after a long absence
f21 | 20:45 | Lyon – Rennes | coverage 4 | window 2 | distinct 1 | sample 2 | yield -2 | total 7 | T3 | both clubs already carded in full in slate 0916 (fx_0916_f2.html, fx_0916_f6.html)
f22 | 20:45 | Toulouse – Le Havre | coverage 4 | window 2 | distinct 0 (prov) | sample 1 | yield 0 | total 7 | T3 | no structural fact scored; both sides on 4 matches
f23 | 21:00 | Sevilla – Barcelona | coverage 4 | window 2 | distinct 0 (prov) | sample 2 | yield 0 | total 8 | T3 | tie at 8; out on kickoff

Signal notes.
- Coverage 4 for all five divisions: Premier League, LaLiga, Serie A,
  Bundesliga and Ligue 1 publish match-level xG, shot data, per-referee
  card records and complete fees. No division on the slate is capped.
- Window 2 on every row: every kickoff falls today, inside 72 hours of
  this run.
- Sample is the thinner-played of the two sides, counted, not assumed:
  league matches played (ESPN standings) plus every competitive match in
  the ESPN cup and European scoreboards since 1 July (DFB-Pokal, EFL Cup,
  Coppa Italia, Champions League and its qualifying, Europa League and
  Conference League qualifying, and the UEFA, German and French Super
  Cups). Copa del Rey and Coupe de France have no matches in the record
  yet. Counts by club, league + other:
  Premier League: Tottenham 4+2, Aston Villa 4+3, Brighton 4+3, Arsenal
  4+2, Everton 4+2, Ipswich 4+2, Newcastle 4+2, Hull 4+2, Nottm Forest
  4+1, Coventry 4+2. LaLiga: Osasuna 6+0, Rayo 6+0, Athletic 5+0, Alavés
  6+0, Celta 6+1, Racing Santander 6+0, Sevilla 6+0, Barcelona 6+1.
  Serie A: Bologna 4+0, Torino 4+2, Udinese 4+2, Cagliari 4+2, Roma 4+1,
  Inter 4+1, Venezia 4+2, Lazio 4+1. Bundesliga: M'gladbach 3+1, Mainz
  3+1, Frankfurt 3+1, Freiburg 3+3, Hamburger SV 3+1, Köln 3+1, Bremen
  3+1, Augsburg 3+1, Stuttgart 3+2, Dortmund 3+3. Ligue 1: Paris FC 4+0,
  Strasbourg 4+0, Angers 4+0, Troyes 4+0, Le Mans 4+0, Lorient 4+0, Lyon
  4+5, Rennes 4+1, Toulouse 4+0, Le Havre 4+0.
  Sample 1 fixtures are those with a side on exactly four competitive
  matches: f3 (Bologna), f5, f6, f7, f8 (all Bundesliga), f13, f19, f20,
  f22 (Ligue 1). These counts do not include this weekend's fixtures.
- Distinct is scored on three facts: (1) a promoted side, from the 2026
  against 2025 standings; (2) a coach change since 1 June 2026, known
  only from archived cards; (3) either club back after two or more
  seasons out of the division (absent from the 2024–25 standings too),
  so a promotion after one season away scores (1) but not (3).
  Promoted this season: Premier League Coventry, Hull, Ipswich; LaLiga
  Deportivo, Málaga, Racing Santander; Serie A Frosinone, Monza, Venezia;
  Bundesliga Paderborn, Elversberg, Schalke; Ligue 1 Le Mans, Troyes.
  Of those on this slate, Coventry, Hull, Racing, Troyes and Le Mans
  score (3) as well; Ipswich and Venezia do not (both were in their
  division in 2024–25).
  Coach change known from archived cards: Torino (Abate, appointed 12
  June, fx_0914_f2), Rayo Vallecano (San José, 18 June, fx_0915_f2),
  Ipswich (O'Neil, 23 June, fx_0915_f6), Lyon (Vítor Bruno, 23 June,
  fx_0916_f2), Newcastle (Jaissle, 5 August, fx_0914_f4). Known
  unchanged in the window: Roma, Inter, Udinese (fx_0914), Arsenal
  (fx_0915_f6), Alavés (fx_0915_f3); Tottenham and Rennes changed coach
  before 1 June, so outside the window. The other 34 clubs' coach status
  was not looked up.
- The known-status asymmetry is real: a fixture whose clubs were carded
  earlier this week gets its coach fact scored and one whose clubs were
  not does not. That is why the provisional list below is long, and it
  can move a fixture by one point — enough to cross the T2/T3 line among
  the tied eight.
- Yield: Lyon and Rennes both received full T1 cards in slate 0916
  (fx_0916_f2.html, fx_0916_f6.html), so f21 scores −2. No other club on
  this slate appears in slates 0916, 0917 or 0918. Older cards outside
  the three-slate window, for information only: Torino, Roma, Inter,
  Udinese, Newcastle (slate 0914); Rayo Vallecano, Alavés, Ipswich,
  Arsenal, Tottenham (slate 0915).
- ESPN's site.api scoreboard host returned 403 from this machine today,
  so today's fixture data was not re-pulled; nothing in triage depends on
  it. Standings and cup data came from the core and web hosts.

Competitions on the slate:
- Premier League: 5 fixtures — T1 f10, f11, f16; T2 f1, f9. One baseline.
- LaLiga: 4 fixtures — T1 f2, f15; T2 f12; T3 f23. One baseline.
- Serie A: 4 fixtures — T1 f18; T2 f4; T3 f3, f14. One baseline.
- Bundesliga: 5 fixtures — T2 f17 (coverage floor); T3 f5, f6, f7, f8. One
  baseline.
- Ligue 1: 5 fixtures — T1 f19, f20; T3 f13, f21, f22. One baseline.
Five baselines in all. baselines_0918.md already carries all five
competitions, so the 2025–26 lines are reused without a search and only
the 2026–27 lines need refreshing.

Coverage floor: applied once. The Bundesliga had no fixture at T2 or
better, so its highest-scoring fixture, f17 VfB Stuttgart – Dortmund
(total 8, tied with seven others and out on kickoff), was promoted to
T2. Every other division already had a T1 or T2 fixture.

Capped by low evidence coverage: none (all five divisions score 4).

Provisional distinctiveness (coach status unknown for at least one club
whose status could still raise the score): f1, f2, f3, f4, f5, f6, f7,
f8, f9, f10, f12, f13, f15, f16, f17, f18, f19, f20, f22, f23. Not
provisional: f11 (score at the cap of 3), f14 (both clubs known
unchanged, no promoted side) and f21 (both clubs known). Phase 2 may
promote one provisional fixture to T1 when its first search contradicts
the triage assumption, for instance an unreported coach change, and will
say so in that run's confirmation line and amend progress_0919.md.

Phase 2 promotion: f12 Athletic Club – Deportivo Alavés promoted from T2 to
T1. Its first search contradicted the triage assumption — **Athletic Club
changed head coach, Edin Terzić announced on 5 May 2026 to replace Ernesto
Valverde**, which triage had scored as unknown and marked provisional. With
that fact the fixture scores distinct 1 and totals 9, above the T1 cut.
No fixture was demoted to pay for it; estimated spend rises by about 5
searches. Slate now T1: 9 · T2: 4 · T3: 10.

Phase 2 corrections (no re-tier). Two further coaching changes triage had
recorded as unknown are now on record and neither moves a tier, because both
fixtures were already T1: **Osasuna — Luis Miguel Ramis appointed about 10
June 2026** to replace Alessio Lisci (f2), and **Nottingham Forest — Oliver
Glasner appointed July 2026** from Crystal Palace (f16). Also confirmed as
unchanged, against the provisional assumption: Everton (Moyes), Hull
(Jakirović, extended 4 September 2026), Coventry (Lampard), Brighton
(Hürzeler), Arsenal (Arteta), Aston Villa (Emery), Udinese (Runjaić),
Cagliari (Pisacane), Alavés (Sánchez Flores).

Override (yours), received during Phase 2: all ten T3 fixtures raised to T1
— f3, f5, f6, f7, f8, f13, f14, f21, f22, f23 — to be researched at full
RESEARCH SPEC depth with sections A–E. Taken as given; the slate is not
re-scored and no fixture was demoted to pay for it. The scored tier stays
visible beside the override on each progress line. Estimated spend rises by
roughly 130–210 searches; slate now T1: 19 (10 of them yours) · T2: 4 · T3: 0.

Amendment to the override above, same session: at 18:20 CEST fourteen of the
twenty-three fixtures had kicked off (f1–f12 at full time, f13 at half-time,
f14 in progress), so the override is applied only to the three unstarted
fixtures it still reaches — f21, f22 and f23 — which are researched at full
RESEARCH SPEC depth with sections A–E. The seven started T3 fixtures (f3, f5,
f6, f7, f8, f13, f14) are not built: a pre-match context card cannot be
written for a match already under way. Their progress lines record that
rather than a tier. Nine fixtures remain unstarted and all nine are carded.
