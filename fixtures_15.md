# fixtures_15 — parsed from odds_15.xlsx (sheet internally named "odds_14"), 10-09-2026

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
  sheet XML instead (namespace swapped to transitional OOXML to parse).
  No effect on the values below, same symptom as odds_14.xlsx.
- KO times in the raw cells are clean (`18:45:00.000`, `21:00:00.000`) —
  no floating-point artifact to normalize this slate.
- Workbook contains nine tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used) and `odds_7` through `odds_14` (sheetIds 2–9, already
  consumed as fixtures_8 through fixtures_14). The ninth tab is still
  internally named `odds_14` (stale, leftover from copy/paste — same lag
  pattern as odds_10.xlsx through odds_14.xlsx) but its title row reads
  "MATCHES 10-09-2026 — odds read from screenshots" and it is the active
  tab — today's slate, and the one read here. The file is named
  `odds_15.xlsx` and this is the fifteenth Phase-1 run overall; output
  numbered fixtures_15 / progress_15 per the file sequence.
- 6 fixtures on this sheet (`A4:AJ9`, one blank spacer row at r=2). This
  is at the ≤6-fixture threshold, so Phase 1.5 triage is skipped this
  slate — research everything.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8 through fixtures_14.
  The goals line is 2.5 for every fixture here.
- `Win/+2 Home` and `Win/+2 Away` are empty for all 6 rows — recorded as
  not given throughout, not a per-fixture gap.
- f3 (Bayern Monaco – Bodø Glimt) and f5 (Manchester United – Sabah
  Masazir) are each missing the 1X double-chance cell — recorded as not
  given per fixture below, not derived from the moneyline.
- No fixture is missing a 1/X/2 price, an AH-line 3-way price, a corner
  race price or a cards line this slate.
- Every fixture this slate carries a home/away card-split line.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line, a 3-way corner-race market, and per-team card O/U lines.
- Team names are recorded exactly as typed in the source (e.g. "Bayern
  Monaco" = Bayern Munich, "Lipsia" = RB Leipzig — Italian-style naming
  carried over from earlier slates).
- All 6 fixtures share the same date, 10-09-2026, in two kickoff slots
  (18:45 and 21:00) consistent with a UEFA continental matchday; league
  label left to Phase 2 per fixture.

---

### f1 · Fenerbahçe – Roma
league: *(not given — research)* | kickoff: 10-09-2026 18:45 | venue: *(not given — research)*
1 / X / 2: 3.5 / 3.6 / 2.05
O2.5 / U2.5: 1.55 / 2.3
BTTS Y / N: 1.47 / 2.55
1X / 12 / X2: 1.75 / 1.28 / 1.3
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.75 / 4.1 / 3.55
Corner race 1/X/2: 2.25 / 8.5 / 1.75
Corners line, U/O: 9.5, 1.78 / 1.9
Cards line, U/O: 4.5, 2.05 / 1.58
Home card line, U/O: 2.5, 1.65 / 1.9
Away card line, U/O: 2.5, 1.65 / 1.9

### f2 · PSV Eindhoven – Shakhtar Donetsk
league: *(not given — research)* | kickoff: 10-09-2026 18:45 | venue: *(not given — research)*
1 / X / 2: 1.5 / 4.7 / 5.75
O2.5 / U2.5: 1.42 / 2.7
BTTS Y / N: 1.5 / 2.45
1X / 12 / X2: 1.13 / 1.18 / 2.55
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.2 / 3.95 / 2.55
Corner race 1/X/2: 1.3 / 9.5 / 3.95
Corners line, U/O: 9.5, 1.93 / 1.75
Cards line, U/O: 3.5, 2.15 / 1.55
Home card line, U/O: 1.5, 1.83 / 1.7
Away card line, U/O: 2.5, 1.55 / 2.1

### f3 · Bayern Monaco – Bodø Glimt
league: *(not given — research)* | kickoff: 10-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.07 / 13 / 25
O2.5 / U2.5: 1.1 / 6
BTTS Y / N: 1.65 / 2.1
1X / 12 / X2: not given / 1.02 / 8.5
Win-or-+2 (Home/Away): not given
AH line: -3
EH 3-way (1/X/2 on AH line): 2.1 / 4.7 / 2.4
Corner race 1/X/2: 1.06 / 14 / 9
Corners line, U/O: 10.5, 1.8 / 1.85
Cards line, U/O: 2.5, 1.95 / 1.7
Home card line, U/O: 1.5, 1.32 / 2.65
Away card line, U/O: 1.5, 1.75 / 1.78

### f4 · Como – Lipsia
league: *(not given — research)* | kickoff: 10-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.73 / 4.1 / 4.35
O2.5 / U2.5: 1.43 / 2.65
BTTS Y / N: 1.42 / 2.7
1X / 12 / X2: 1.2 / 1.23 / 2.1
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.7 / 4 / 2.1
Corner race 1/X/2: 1.53 / 9 / 2.75
Corners line, U/O: 8.5, 1.95 / 1.7
Cards line, U/O: 3.5, 2.05 / 1.6
Home card line, U/O: 1.5, 2 / 1.58
Away card line, U/O: 1.5, 2.3 / 1.45

### f5 · Manchester United – Sabah Masazir
league: *(not given — research)* | kickoff: 10-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.08 / 11 / 27
O2.5 / U2.5: 1.18 / 4.25
BTTS Y / N: 1.97 / 1.75
1X / 12 / X2: not given / 1.03 / 7.75
Win-or-+2 (Home/Away): not given
AH line: -3
EH 3-way (1/X/2 on AH line): 2.35 / 4.5 / 2.15
Corner race 1/X/2: 1.22 / 10 / 4.75
Corners line, U/O: 9.5, 1.95 / 1.72
Cards line, U/O: 3.5, 1.5 / 2.25
Home card line, U/O: 1.5, 1.35 / 2.5
Away card line, U/O: 1.5, 2.1 / 1.52

### f6 · Slavia Praga – Lens
league: *(not given — research)* | kickoff: 10-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 2.65 / 3.5 / 2.5
O2.5 / U2.5: 1.6 / 2.2
BTTS Y / N: 1.47 / 2.5
1X / 12 / X2: 1.5 / 1.3 / 1.45
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.5 / 4.5 / 4.8
Corner race 1/X/2: 1.97 / 8.5 / 2
Corners line, U/O: 9.5, 2.05 / 1.67
Cards line, U/O: 4.5, 1.7 / 1.9
Home card line, U/O: 1.5, 2.25 / 1.47
Away card line, U/O: 2.5, 1.6 / 1.98
