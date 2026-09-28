# triage_17

Slate size: 33 fixtures | Capacity: 10 (no capacity line given, default applies)
T1: 10 | T2: 5 (4 scored + 1 override) | T3: 18
Estimated search spend: unchanged from the first pass — 8 of the 10 T1
fixtures carry a side newly promoted this season (~19 searches each), the
other 2 run at the standard ~11, and the 5 T2 fixtures (including the f32
override) run at ~6 each. ≈ (8×19) + (2×11) + (5×6) = 152 + 22 + 30 = 204.
Separated by score: 10 of 33 land on a unique or non-tied total (f1 alone
at 6; the nine-way tie at 4 exactly fills the remaining T1 slots, so no
tie-break was needed to seat T1 this run). Fell to tie-break: the total-3
cohort only (7 fixtures, resolved mostly by raw live-row count — see
below), plus the f32 override, which is not a score-based placement at
all.

**Rerun basis — 1X2 restored to scope, per instruction.** Live-row
scoring and the result-dead flag are computed on the full market set
fixtures_17.md carries (1X2, O2.5/U2.5, BTTS, DC where present), not the
forced BTTS+O2.5-only pass from the previous run.

- **Result-dead: N/A, but now for a clean, confirmed reason rather than
  an exclusion.** The shortest 1X2 price is ≥1.30 on all 33 fixtures —
  the tightest anywhere is Barnet FC – Accrington Stanley at 1.45, then
  York City – Swindon at 1.53 and Sheffield Wednesday – Wigan at 1.58.
  No fixture on this slate has a dead moneyline, so the "dead 1X2, live
  derived markets" rescue scenario you described doesn't actually arise
  in slate 17's data — there is nothing here for that flag to catch.
- **Live rows, recomputed properly, is a real (small) discriminator this
  time.** 1X2, O2.5/U2.5 and BTTS are live on all 33 fixtures (never in
  question), so the only source of variation is the 9 fixtures carrying
  DC. Each DC leg was scored as a genuine two-way market against its
  1X2 complement (DC-1X vs the "2" price, DC-12 vs "X", DC-X2 vs "1"),
  since DC has no listed complement of its own. Result: DC legs are
  mostly dead everywhere — combining any two outcomes into a double
  chance price pushes it under the 1.40 two-way floor for anything but
  a near-even three-way spread. Three fixtures keep 2 of 3 DC legs live
  because their 1X2 is unusually tight (Bolton – Cardiff 2.55/3.6/2.5,
  Blackburn – Millwall 2.6/3.3/2.6, Charlton – Portsmouth 2.7/3.15/2.65),
  putting them at 5 of 6 possible rows live — the 5–6 band, worth 2. The
  other 6 DC fixtures keep only 1 of 3 legs live (4 of 6 rows) and the 24
  fixtures without DC cap at 3 of 3 — both land in the "4 or fewer → 0"
  band. No fixture reaches the 7+ band this slate; the file's market
  breadth (3 well-formed rows, 6 at most with DC) is narrower than the
  bands were calibrated for (up to 10 on earlier slates), so most of the
  slate is still floored at 0 even though nothing is actually dead — a
  structural ceiling, not a finding about any one game.
- **On weighting toward BTTS/O2.5 structural richness specifically:** I
  can't produce that within this phase. "Attacking transfers, weak
  defensive sample, high open-game style" is team-level research, and
  the standing budget reserves that for Phase 2 — spending it here across
  33 fixtures would blow the 6-search Phase 1.5 cap by a wide margin, and
  I'm not willing to guess at transfer activity or style to fill the gap
  (that's exactly the kind of invented fact the RESEARCH SPEC bans). The
  only budget-legal proxy available at this phase is squad churn via
  promoted/relegated status, which is already what's driving the
  distinct-signal column below — a newly promoted or newly relegated
  side is the one thing I can say, on record, without a team-level
  search, correlates with an unsettled defence. What I can commit to
  instead: for every T1/T2 card built in Phase 2, section C and E should
  foreground BTTS and Totals suitability ahead of 1X2, DC, or any other
  market this slate, since those are the two you're actually playing —
  that's an instruction Phase 2 can act on directly without more
  research now.
- Discipline window remains a constant 2 (every kickoff is today) and
  marginal yield remains 0 for all 33 (rechecked; no change from the
  first pass — see sources_17.md).

**T1 membership changed from the first triage pass as a direct result of
restoring 1X2/DC**, not from the BTTS/O2.5 weighting request: Sheffield
Wednesday – Wigan (f8) and Stockport County – Leicester City (f9) drop
from T1 to T2 (total 3, no live-row credit — neither carries a DC
column), replaced by Blackburn Rovers – Millwall (f15) and Charlton
Athletic – Portsmouth (f16), which pick up the 2-point live-row credit
above. Bolton – Cardiff (f1) is the clear top fixture on the sheet at
total 6 — the only fixture combining a promoted-side distinctiveness
score with the live-row bonus.

---

f1 | 13:30 | Bolton – Cardiff | live 5/6→2 | window 2 | distinct 2 | yield 0 | total 6 | T1 | both sides promoted, tightest 1X2 spread on the sheet keeps 2 of 3 DC legs live
f2 | 13:30 | Derby County – Birmingham City | live 4/6→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | Championship, neither side new to the division
f3 | 13:30 | West Bromwich – Queens Park Rangers | live 4/6→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | Championship, neither side new to the division
f4 | 13:30 | Crawley – Cheltenham Town | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor, see prior note
f5 | 13:30 | Grimsby Town – Bristol Rovers | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f6 | 13:30 | Leyton Orient – Wycombe Wanderers | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League One, neither side new to the division
f7 | 13:30 | Notts County – Bradford City | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | Notts County promoted from League Two this season
f8 | 16:00 | Sheffield Wednesday – Wigan | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | T2 | Sheffield Wednesday relegated from the Championship, no DC column to bank a live-row bonus
f9 | 16:00 | Stockport County FC – Leicester City | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | T2 | Leicester City relegated from the Championship, no DC column
f10 | 16:00 | Wimbledon – Doncaster Rovers | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League One, neither side new to the division
f11 | 16:00 | Rotherham United – Salford City | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | T2 | Rotherham relegated from League One, newly in League Two
f12 | 16:00 | Shrewsbury Town – Northampton Town | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | T3 | Northampton relegated from League One — tied the T2 cohort, lost the tie-break (see note)
f13 | 16:00 | Walsall – Rochdale | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | Rochdale promoted from the National League this season
f14 | 16:00 | York City FC – Swindon Town | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | York City promoted from the National League this season
f15 | 16:00 | Blackburn Rovers – Millwall | live 5/6→2 | window 2 | distinct 0 | yield 0 | total 4 | T1 | tight 1X2 spread (2.6/3.3/2.6) keeps 2 of 3 DC legs live
f16 | 16:00 | Charlton Athletic – Portsmouth | live 5/6→2 | window 2 | distinct 0 | yield 0 | total 4 | T1 | tight 1X2 spread (2.7/3.15/2.65) keeps 2 of 3 DC legs live
f17 | 16:00 | Middlesbrough – Norwich | live 4/6→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | Championship, neither side new to the division
f18 | 16:00 | Preston North End – Lincoln City | live 4/6→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | Lincoln City promoted from League One this season
f19 | 16:00 | Southampton – Bristol City | live 4/6→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | Championship, neither side new to the division
f20 | 16:00 | Barnet FC – Accrington Stanley | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f21 | 16:00 | Colchester United – Crewe Alexandra | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f22 | 16:00 | Gillingham – Tranmere Rovers FC | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f23 | 16:00 | Newport County – Fleetwood Town | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f24 | 16:00 | Oldham Athletic – Chesterfield FC | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League Two, neither side new to the division — thin-coverage floor
f25 | 16:00 | Port Vale – Exeter City | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | T3 | both sides relegated from League One — tied the T2 cohort, lost the tie-break (see note)
f26 | 16:00 | Swansea – Burnley | live 4/6→0 | window 2 | distinct 1 | yield 0 | total 3 | T2 | Burnley relegated from the Premier League; highest raw live-row count (4/6) of the total-3 cohort wins the tie-break outright
f27 | 16:00 | Watford – Stoke City | live 4/6→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | Championship, neither side new to the division
f28 | 16:00 | Blackpool FC – Bromley FC | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | Bromley promoted from League Two this season
f29 | 16:00 | Cambridge United – Reading FC | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | Cambridge United promoted from League Two this season
f30 | 16:00 | Mansfield Town – Huddersfield | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League One, neither side new to the division
f31 | 16:00 | Milton Keynes Dons – Peterborough United | live 3/3→0 | window 2 | distinct 2 | yield 0 | total 4 | T1 | MK Dons promoted from League Two this season
f32 | 16:00 | Oxford United – Burton Albion | live 3/3→0 | window 2 | distinct 1 | yield 0 | total 3 | scored T3 → T2 (mine) | Oxford United relegated from the Championship; tied the T2 cohort, demoted by tie-break alone last run — overridden regardless of this rerun, per instruction
f33 | 16:00 | Plymouth Argyle – Barnsley | live 3/3→0 | window 2 | distinct 0 | yield 0 | total 2 | T3 | League One, neither side new to the division

**Tie-break at total 3 (f8, f9, f11, f12, f25, f26 — f32 excluded, its
placement is an override, not a score outcome):** raw live-row count now
actually separates part of this cohort — f26 carries a live DC leg (raw
4/6) and wins the tie-break outright, no coin flip needed for that one
seat. The rest (f8, f9, f11, f12, f25) are genuinely tied at raw 3/3 with
no DC column to break on, and kickoff doesn't separate them either (all
16:00) — f8, f9 and f11 fill the remaining natural T2 seats by fixture
order in fixtures_17.md, which is an arbitrary cut for those three, not a
finding. f12 and f25 fall to T3 by that same arbitrary cut; unlike f32,
neither carries a standing override, but they are the next candidates in
line if you want to promote further.

**Competitions kept at T2 or better:** Championship (f1, f15, f16, f18 at
T1; f26 at T2), League One (f7, f28, f29, f31 at T1; f8, f9, f32 at T2),
League Two (f13, f14 at T1; f11 at T2). All three clear the coverage
floor without forcing a promotion.

**Result-dead fixtures:** none — every 1X2 on the sheet is live (see
note above).

**Provisional distinctiveness:** none in the strict sense, unchanged from
the first pass — every fixture has 2 of 3 structural bullets resolved,
manager-change pending Phase 2 throughout.

**Lower-division coverage note carries over unchanged from the first
pass:** the League Two T3 fixtures (f4, f5, f20–f24) sit at the floor
mainly because League Two sourcing is thin, not because the games are
duller — an override there is "worth a look despite weak sourcing." The
Championship T3 fixtures (f2, f3, f17, f19, f27) sit at the same floor
for the opposite reason: good coverage, genuinely settled fixtures.
