# Scorecard — context engine verdicts against results

Updated 2026-09-27 · slates 0914, 0915, 0916, 0917, 0918, 0919, 0920, 0926 · 80 fixtures settled, 58 league fixtures in the lean audit.

## How to read it
After each match, settle.py works out which way the pre-kickoff base rates leaned in each
family (both sides' rates against their own league line, ESPN records before kickoff) and
checks whether the match landed on that side. **Hit** is how often it did. **Prior** is how
often the same side lands across the league — what you would get without reading the card.
**Edge** is the difference. If the verdicts work, Well-suited should show the widest edge and
Dangerous the narrowest. ± is a rough 90% band on the hit rate: an edge inside it is noise.

The lean ignores the referee, injuries and lineups, which the cards do weigh — so this tests
the base-rate half of each verdict, not the whole of it. Cup and European ties are settled
but left out of the audit: their teams have no shared league line.

## By verdict — the six goal and stat families

The cleanest read. 1X2 and AH are left out here because their prior only knows home or away, so any strength-based lean beats it; read those two down their own column below.

verdict | tests | hit | prior | edge | ±90%
--- | --- | --- | --- | --- | ---
Well-suited | 73 | 63% | 52% | +11 pts | ±9
OK | 286 | 57% | 50% | +6 pts | ±5
Dangerous | 47 | 47% | 50% | -3 pts | ±12
_of which Split_ | 147 | 54% | 50% | +4 pts | ±7

## By verdict, all eight families

verdict | tests | hit | prior | edge | ±90%
--- | --- | --- | --- | --- | ---
Well-suited | 73 | 63% | 52% | +11 pts | ±9
OK | 312 | 56% | 50% | +6 pts | ±5
Dangerous | 126 | 48% | 46% | +2 pts | ±7
_of which Split_ | 149 | 55% | 50% | +5 pts | ±7

## By family

family | Well-suited | OK | Dangerous | all
--- | --- | --- | --- | ---
1X2 | – | 50% vs 38% (n=14) | 42% vs 38% (n=43) | 44% vs 38% (n=57)
AH / DNB | – | 42% vs 55% (n=12) | 56% vs 50% (n=36) | 52% vs 51% (n=48)
Totals | 56% vs 54% (n=18) | 53% vs 50% (n=38) | 50% vs 51% (n=2) | 53% vs 52% (n=58)
BTTS | 67% vs 51% (n=12) | 63% vs 51% (n=43) | 67% vs 54% (n=3) | 64% vs 51% (n=58)
Team goals | 67% vs 52% (n=12) | 51% vs 50% (n=98) | 17% vs 55% (n=6) | 51% vs 51% (n=116)
Halves | 86% vs 51% (n=7) | 59% vs 51% (n=39) | 33% vs 47% (n=12) | 57% vs 50% (n=58)
Discipline | 67% vs 52% (n=9) | 59% vs 50% (n=41) | 50% vs 48% (n=8) | 59% vs 50% (n=58)
Corners | 53% vs 49% (n=15) | 67% vs 50% (n=27) | 62% vs 50% (n=16) | 62% vs 50% (n=58)

Each cell: hit vs prior (tests). Team goals counts two tests per fixture, one per side.

## Your picks

verdict on the card | picks | W–L–P | hit | staked | profit | ROI
--- | --- | --- | --- | --- | --- | ---
OK | 6 | 6–0–0 | 100% | 3.0 | +1.96 | 65%
Dangerous | 1 | 1–0–0 | 100% | 1.0 | +0.57 | 57%
