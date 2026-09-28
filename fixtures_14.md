# fixtures_14 — parsed from odds_14.xlsx (sheet internally named "odds_13"), 09-09-2026

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
  sheet XML instead. No effect on the values below, noted only in case a
  future run hits the same empty-sheet symptom on this file.
- KO times in the raw cells are clean (`18:45:00.000`, `21:00:00.000`) —
  no floating-point artifact to normalize this slate, unlike odds_13.
- Workbook contains eight tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used) and `odds_7` through `odds_13` (sheetIds 2–8, already
  consumed as fixtures_8 through fixtures_13). The eighth tab is still
  internally named `odds_13` (stale, leftover from copy/paste — same lag
  pattern as odds_10.xlsx through odds_13.xlsx) but its title row reads
  "MATCHES 09-09-2026 — odds read from screenshots" and it is the active
  tab — today's slate, and the one read here. The file is named
  `odds_14.xlsx` and this is the fourteenth Phase-1 run overall; output
  numbered fixtures_14 / progress_14 per the file sequence.
- 6 fixtures on this sheet (`A4:AJ9`, one blank spacer row at r=2). This
  is at the ≤6-fixture threshold, so Phase 1.5 triage is skipped this
  slate — research everything.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8 through fixtures_13.
  The goals line is 2.5 for every fixture here.
- `Win/+2 Home` and `Win/+2 Away` are empty for all 6 rows — recorded as
  not given throughout, not a per-fixture gap.
- f1 (Barcellona – Feyenoord) and f5 (PSG – Slovan Bratislava) are each
  missing one or both of the double-chance cells (1X and/or 12) — recorded
  as not given per fixture below, not derived from the moneyline.
- No fixture is missing a 1/X/2 price, an AH-line 3-way price, a corner
  race price or a cards line this slate.
- Every fixture this slate carries a home/away card-split line — unlike
  odds_13, where only 8 of 21 fixtures had one.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line, a 3-way corner-race market, and per-team card O/U lines.
- Team names are recorded exactly as typed in the source (e.g.
  "Stoccarda" = Stuttgart, "Sporting Lisbona" = Sporting CP — Italian-style
  naming carried over from earlier slates).
- All 6 fixtures share the same date, 09-09-2026, in two kickoff slots
  (18:45 and 21:00) consistent with a UEFA continental matchday; league
  label left to Phase 2 per fixture.

---

### f1 · Barcellona – Feyenoord
league: *(not given — research)* | kickoff: 09-09-2026 18:45 | venue: *(not given — research)*
1 / X / 2: 1.07 / 13 / 25
O2.5 / U2.5: 1.14 / 5
BTTS Y / N: 1.8 / 1.9
1X / 12 / X2: not given / 1.02 / 8.5
Win-or-+2 (Home/Away): not given
AH line: -3
EH 3-way (1/X/2 on AH line): 2.2 / 4.55 / 2.3
Corner race 1/X/2: 1.08 / 12 / 8
Corners line, U/O: 10.5, 1.67 / 2.05
Cards line, U/O: 2.5, 1.85 / 1.7
Home card line, U/O: 0.5, 2 / 1.57
Away card line, U/O: 1.5, 2.05 / 1.55

### f2 · Stoccarda – Viking FK
league: *(not given — research)* | kickoff: 09-09-2026 18:45 | venue: *(not given — research)*
1 / X / 2: 1.25 / 6.5 / 10
O2.5 / U2.5: 1.23 / 3.85
BTTS Y / N: 1.53 / 2.4
1X / 12 / X2: 1.04 / 1.1 / 3.9
Win-or-+2 (Home/Away): not given
AH line: -2
EH 3-way (1/X/2 on AH line): 2.4 / 4.35 / 2.2
Corner race 1/X/2: 1.16 / 10 / 5.75
Corners line, U/O: 10.5, 1.72 / 1.97
Cards line, U/O: 3.5, 2 / 1.65
Home card line, U/O: 1.5, 1.65 / 1.9
Away card line, U/O: 2.5, 1.55 / 2.1

### f3 · Liverpool – Atletico Madrid
league: *(not given — research)* | kickoff: 09-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.73 / 4 / 4.6
O2.5 / U2.5: 1.53 / 2.4
BTTS Y / N: 1.52 / 2.4
1X / 12 / X2: 1.19 / 1.25 / 2.1
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.75 / 3.9 / 2.1
Corner race 1/X/2: 1.4 / 9.5 / 3.25
Corners line, U/O: 9.5, 1.75 / 1.93
Cards line, U/O: 3.5, 1.85 / 1.75
Home card line, U/O: 1.5, 1.5 / 2.15
Away card line, U/O: 2.5, 1.52 / 2.1

### f4 · Napoli – Arsenal
league: *(not given — research)* | kickoff: 09-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 5.75 / 3.85 / 1.62
O2.5 / U2.5: 1.87 / 1.87
BTTS Y / N: 1.93 / 1.8
1X / 12 / X2: 2.3 / 1.25 / 1.13
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.3 / 3.55 / 2.65
Corner race 1/X/2: 2.45 / 9 / 1.63
Corners line, U/O: 8.5, 2.05 / 1.67
Cards line, U/O: 3.5, 1.55 / 2.1
Home card line, U/O: 1.5, 1.78 / 1.75
Away card line, U/O: 1.5, 1.7 / 1.85

### f5 · PSG – Slovan Bratislava
league: *(not given — research)* | kickoff: 09-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.03 / 20 / 30
O2.5 / U2.5: 1.14 / 5
BTTS Y / N: 2.65 / 1.43
1X / 12 / X2: not given / not given / 12
Win-or-+2 (Home/Away): not given
AH line: -4
EH 3-way (1/X/2 on AH line): 2.75 / 5.25 / 1.85
Corner race 1/X/2: 1.03 / 14 / 11
Corners line, U/O: 10.5, 1.98 / 1.7
Cards line, U/O: 2.5, 1.9 / 1.7
Home card line, U/O: 0.5, 1.92 / 1.65
Away card line, U/O: 1.5, 2.15 / 1.5

### f6 · Sporting Lisbona – Galatasaray
league: *(not given — research)* | kickoff: 09-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.7 / 4 / 4.65
O2.5 / U2.5: 1.53 / 2.35
BTTS Y / N: 1.53 / 2.35
1X / 12 / X2: 1.18 / 1.25 / 2.15
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.7 / 3.85 / 2.15
Corner race 1/X/2: 1.48 / 9 / 2.9
Corners line, U/O: 9.5, 1.95 / 1.72
Cards line, U/O: 4.5, 1.7 / 1.9
Home card line, U/O: 1.5, 2 / 1.58
Away card line, U/O: 2.5, 1.72 / 1.82
