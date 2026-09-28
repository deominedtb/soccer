# Scorecard — context engine verdicts against results

Updated 2026-09-28 · slates 0914, 0915, 0916, 0917, 0918, 0919, 0920, 0926, 0927 · 87 fixtures settled, 65 league fixtures in the lean audit.

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
Well-suited | 75 | 63% | 52% | +11 pts | ±9
OK | 326 | 57% | 50% | +7 pts | ±5
Dangerous | 53 | 49% | 50% | -1 pts | ±11
_of which Split_ | 167 | 53% | 50% | +2 pts | ±6

## By verdict, all eight families

verdict | tests | hit | prior | edge | ±90%
--- | --- | --- | --- | --- | ---
Well-suited | 75 | 63% | 52% | +11 pts | ±9
OK | 362 | 56% | 50% | +6 pts | ±4
Dangerous | 135 | 47% | 46% | +1 pts | ±7
_of which Split_ | 169 | 53% | 50% | +3 pts | ±6

## By family

family | Well-suited | OK | Dangerous | all
--- | --- | --- | --- | ---
1X2 | – | 47% vs 38% (n=19) | 40% vs 38% (n=45) | 42% vs 38% (n=64)
AH / DNB | – | 41% vs 53% (n=17) | 54% vs 51% (n=37) | 50% vs 51% (n=54)
Totals | 56% vs 54% (n=18) | 52% vs 51% (n=42) | 60% vs 52% (n=5) | 54% vs 52% (n=65)
BTTS | 67% vs 51% (n=12) | 65% vs 50% (n=46) | 67% vs 50% (n=6) | 66% vs 50% (n=64)
Team goals | 67% vs 52% (n=12) | 52% vs 50% (n=112) | 17% vs 55% (n=6) | 52% vs 51% (n=130)
Halves | 86% vs 51% (n=7) | 61% vs 51% (n=46) | 33% vs 47% (n=12) | 58% vs 51% (n=65)
Discipline | 67% vs 52% (n=9) | 56% vs 50% (n=48) | 50% vs 48% (n=8) | 57% vs 50% (n=65)
Corners | 53% vs 50% (n=17) | 66% vs 50% (n=32) | 62% vs 50% (n=16) | 62% vs 50% (n=65)

Each cell: hit vs prior (tests). Team goals counts two tests per fixture, one per side.

## Your picks

verdict on the card | picks | W–L–P | hit | staked | profit | ROI
--- | --- | --- | --- | --- | --- | ---
Well-suited | 2 | 1–1–0 | 50% | – | – | –
OK | 26 | 17–8–1 | 68% | 3.0 | +1.96 | 65%
Dangerous | 1 | 1–0–0 | 100% | 1.0 | +0.57 | 57%
