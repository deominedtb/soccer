# fixtures_16 — parsed from odds_16.xlsx (sheet internally named "odds_16"), 11-09-2026

Header row read from file (no assumed positions). Fields present: Date, KO,
Home, Away, 1, X, 2, Goals line, Under, Over, GG, NG, 1X, 12, X2,
Win/+2 Home, Win/+2 Away, AH line, 1 H, X H, 2 H, Corn 1, Corn X, Corn 2,
Corn line, Corn U, Corn O, Cards line, Cards U, Cards O, Home crd line,
Home crd U, Home crd O, Away crd line, Away crd U, Away crd O.

**Flags**
- No `league` or `venue` columns in the source header — both fields are
  absent from every row below and must come from Phase 2 research, not
  invented here.
- The workbook is saved in strict-OOXML conformance, which the normal
  reader could not open (it returned zero sheets); read directly from the
  sheet XML instead. Same symptom as odds_14.xlsx and odds_15.xlsx.
- KO times: 2 of 4 rows carry a floating-point artifact
  (`20:44:59.99999712000295650`) — normalized to 20:45. The other two
  (`21:00:00.000`, `20:30:00.00000287999704350`) are clean or near-clean.
- Workbook contains ten tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used), `odds_7` through `odds_14` (sheetIds 2–9, already consumed as
  fixtures_8 through fixtures_15), and `odds_16` (sheetId 10) — this
  slate. Unlike odds_10.xlsx through odds_15.xlsx, the active tab's
  internal name matches the file number this time; no `odds_15` tab
  remains, consistent with that tab having been renamed in place rather
  than duplicated. Title row reads "MATCHES 11-09-2026 — odds read from
  screenshots", matching today's date.
- 4 fixtures on this sheet (rows 3–6, one title row and one header row
  above, two blank rows below). Below the ≤6-fixture threshold, so Phase
  1.5 triage is skipped this slate — research everything.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8 through fixtures_15.
  The goals line is 2.5 for every fixture here.
- `Win/+2 Home` and `Win/+2 Away` are empty for all 4 rows — recorded as
  not given throughout, not a per-fixture gap.
- Home/away card-split lines are present only for f2 (Venezia –
  Fiorentina); missing for f1, f3 and f4 — recorded as not given per
  fixture below.
- No fixture is missing a 1/X/2 price, an AH-line 3-way price, a corner
  race price or a cards line this slate.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line, a 3-way corner-race market, and per-team card O/U lines where
  given.
- Team names are recorded exactly as typed in the source (e.g. "Siviglia"
  = Sevilla, "Union Berlino" = Union Berlin, "Marsiglia" = Marseille) —
  Italian-style naming carried over from earlier slates.
- All 4 fixtures share the same date, 11-09-2026, across three kickoff
  slots (20:30, 20:45 ×2, 21:00); league label left to Phase 2 per
  fixture.

---

### f1 · Union Berlino – Schalke 04
league: *(not given — research)* | kickoff: 11-09-2026 20:30 | venue: *(not given — research)*
1 / X / 2: 2.4 / 3.5 / 2.8
O2.5 / U2.5: 1.57 / 2.25
BTTS Y / N: 1.45 / 2.6
1X / 12 / X2: 1.42 / 1.3 / 1.55
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.5 / 4.5 / 1.55
Corner race 1/X/2: 1.63 / 8.5 / 2.5
Corners line, U/O: 9.5, 1.85 / 1.8
Cards line, U/O: 4.5, 1.65 / 1.95
Home card line, U/O: not given
Away card line, U/O: not given

### f2 · Venezia – Fiorentina
league: *(not given — research)* | kickoff: 11-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.75 / 3.35 / 2.5
O2.5 / U2.5: 1.6 / 2.25
BTTS Y / N: 1.47 / 2.55
1X / 12 / X2: 1.5 / 1.3 / 1.43
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.5 / 4.55 / 4.75
Corner race 1/X/2: 2 / 8 / 2
Corners line, U/O: 8.5, 1.78 / 1.9
Cards line, U/O: 4.5, 1.8 / 1.8
Home card line, U/O: 2.5, 1.53 / 2.1
Away card line, U/O: 2.5, 1.5 / 2.15

### f3 · Stade Rennes FC – Marsiglia
league: *(not given — research)* | kickoff: 11-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.8 / 3.25
O2.5 / U2.5: 1.45 / 2.6
BTTS Y / N: 1.4 / 2.75
1X / 12 / X2: 1.33 / 1.25 / 1.75
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.33 / 5.5 / 6.5
Corner race 1/X/2: 1.7 / 8.5 / 2.35
Corners line, U/O: 9.5, 1.97 / 1.72
Cards line, U/O: 4.5, 1.57 / 2.1
Home card line, U/O: not given
Away card line, U/O: not given

### f4 · Siviglia – Valencia
league: *(not given — research)* | kickoff: 11-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.92 / 3.25 / 4.35
O2.5 / U2.5: 2.15 / 1.62
BTTS Y / N: 2 / 1.75
1X / 12 / X2: 1.2 / 1.33 / 1.85
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.6 / 3.65 / 1.85
Corner race 1/X/2: 1.53 / 9 / 2.7
Corners line, U/O: 8.5, 1.8 / 1.8
Cards line, U/O: 5.5, 1.8 / 1.78
Home card line, U/O: not given
Away card line, U/O: not given
