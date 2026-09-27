# triage_0915

Slate size: 10 fixtures (5 stale rows removed from the typed sheet — see
fixtures_0915.md header — before this triage ran).
Capacity: 8 (no capacity line given, default).
T1: 8 · T2: 2 · T3: 0.
Estimated search spend against ceiling: 8 fixtures at full T1 depth
(~13 searches each, 21 where the promoted/manager-change ceiling
applies) + 2 at T2 depth (~8 each) + baseline searches for Coppa
Italia, LaLiga and EFL Cup the first time each appears.

Separation: all 10 fixtures separated cleanly by score. The T1/T2 cut
fell exactly on a score gap (7 vs 6) — no fixture needed a tie-break
against the capacity line. 0 fixtures fell to a tie-break.

f1 | 18:00 | Genoa – Südtirol | coverage 3 | window 2 | distinct 1 | sample 1 | yield 0 | total 7 | T1 | Coppa Italia coverage capped below league level
f2 | 19:00 | Rayo Vallecano – Espanyol | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T1 | full LaLiga public record
f3 | 20:00 | Deportivo Alavés – Valencia | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T1 | full LaLiga public record
f4 | 20:30 | Peterborough – Barnsley | coverage 2 | window 2 | distinct 1 | sample 1 | yield -1 | total 5 | T2 | Peterborough already carded T1 in slate 17 (MK Dons v Peterborough United)
f5 | 20:45 | West Ham – Fulham | coverage 3 | window 2 | distinct 1 | sample 1 | yield 0 | total 7 | T1 | West Ham newly relegated to Championship — confirmed, not provisional
f6 | 21:00 | Ipswich – Arsenal | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T1 | Ipswich newly promoted this season — confirmed, not provisional
f7 | 21:00 | Liverpool – Tottenham | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T1 | full Premier League public record on both sides
f8 | 21:00 | Reading – Brentford | coverage 3 | window 2 | distinct 1 | sample 1 | yield -1 | total 6 | T2 | one club (Reading) already carded T1 in slate 17 — Cambridge United v Reading
f9 | 21:00 | Fiorentina – Pisa | coverage 3 | window 2 | distinct 1 | sample 1 | yield 0 | total 7 | T1 | Fiorentina manager change confirmed (Grosso out, Vanoli in) — not provisional
f10 | 21:30 | Elche – Real Madrid | coverage 4 | window 2 | distinct 1 | sample 1 | yield 0 | total 8 | T1 | full LaLiga public record

Competitions on the slate:
- Italy — Coppa Italia Round of 32: 2 fixtures, both T1. Coverage capped
  at 3 (cup-tie referee/discipline records not tabulated even for two
  Serie A sides). One baseline search this slate.
- Spain — LaLiga: 3 fixtures, all T1. Coverage 4. One baseline search.
- England — EFL Cup: 5 fixtures, 3 T1 + 2 T2. Coverage 2–3 depending on
  the weaker side's division. One baseline search.

Capped by low evidence coverage: Genoa – Südtirol and Fiorentina – Pisa
(Coppa Italia, capped 3 — cup discipline record not tabulated);
Peterborough – Barnsley (EFL Cup, capped 2 — both League One, no
referee record); Reading – Brentford (EFL Cup, capped 3 — Reading side
patchier than Brentford's).

Provisional distinctiveness (promotion ruled out for these by search,
manager-change not checked — still capped at 1, could move in Phase 2
if a manager change surfaces): Genoa – Südtirol, Rayo Vallecano –
Espanyol, Deportivo Alavés – Valencia, Peterborough – Barnsley,
Liverpool – Tottenham, Reading – Brentford, Elche – Real Madrid.
Confirmed (not provisional): West Ham – Fulham (relegation), Ipswich –
Arsenal (promotion), Fiorentina – Pisa (manager change).

Search spend this run: 8 (over the nominal 6-search Phase 1.5 ceiling —
2 of the 8 were spent confirming a data-integrity problem in the typed
sheet, not on triage signals themselves; see fixtures_0915.md header).
Logged to sources_0915.md under "Triage."
