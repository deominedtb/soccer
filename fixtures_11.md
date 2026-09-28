# fixtures_11 — parsed from odds_11.xlsx (sheet internally named "odds_10"), 31-08-2026

Header row read from file (no assumed positions). Fields present: Date, KO,
Home, Away, 1, X, 2, Goals line, Under, Over, GG, NG, 1X, 12, X2,
Win/+2 Home, Win/+2 Away, AH line, 1 H, X H, 2 H, Corn 1, Corn X, Corn 2,
Corn line, Corn U, Corn O, Cards line, Cards U, Cards O, Home crd line,
Home crd U, Home crd O, Away crd line, Away crd U, Away crd O.

**Flags**
- No `league` or `venue` columns in the source header — both fields are
  absent from every row below and must come from Phase 2 research, not
  invented here.
- KO times in the raw cells carry floating-point artifacts from Excel's
  time serialization (e.g. `18:30:00.0000000000031950`); normalized to
  the nearest minute below, no source ambiguity.
- Workbook contains five tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used), `odds_7` (sheetId 2, 28-08-2026 fixtures — not used, already
  consumed as fixtures_8), `odds_8` (sheetId 3, 29-08-2026 fixtures — not
  used, already consumed as fixtures_9), `odds_9` (sheetId 4, 30-08-2026
  fixtures — not used, already consumed as fixtures_10), and a fifth tab
  still internally named `odds_10` (sheetId 5) whose title row reads
  "MATCHES 31-08-2026" — today's slate, and the one read here. The file
  is named `odds_11.xlsx` and this is the eleventh Phase-1 run overall;
  the internal tab label is stale (a leftover from copy/paste) and was
  not used for numbering — output numbered fixtures_11 / progress_11 per
  the file sequence, same lag pattern seen in odds_10.xlsx.
- Only 5 fixtures on this sheet (`A4:AJ8`), fewer than the 15-fixture
  slates in fixtures_8/9/10.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8/9/10.
- `Win/+2 Home` and `Win/+2 Away` are empty for every one of the 5 rows —
  recorded as not given throughout, not a per-fixture gap.
- f5 (Barcellona – Rayo Vallecano) is also missing `1X` — the only double-
  chance cell absent anywhere in this sheet.
- Home/away card-split columns are present only for f1, f3, f4; empty for
  f2, f5 — recorded as not given per fixture below, not guessed.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line (`EH 3-way`), a 3-way corner-race market, and per-team card O/U
  lines where given.
- Team names are recorded exactly as typed in the source (e.g.
  "Barcellona" = Barcelona, Italian-style naming carried over from earlier
  slates).
- All 5 fixtures share the same date, 31-08-2026, across competitions
  inferable from clubs (Serie A, LaLiga, Premier League) — league label
  left to Phase 2.

---

### f1 · Lecce – Roma
league: *(not given — research)* | kickoff: 31-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 7.25 / 4.25 / 1.47
O2.5 / U2.5: 1.97 / 1.77
BTTS Y / N: 2.2 / 1.6
1X / 12 / X2: 2.65 / 1.2 / 1.08
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.65 / 3.4 / 2.35
Corner race 1/X/2: 2.75 / 10 / 1.5
Corners line, U/O: 9.5, 1.7 / 2
Cards line, U/O: 3.5, 1.6 / 2
Home card line, U/O: 1.5, 1.9 / 1.65
Away card line, U/O: 1.5, 1.7 / 1.85

### f2 · Osasuna – Getafe
league: *(not given — research)* | kickoff: 31-08-2026 19:30 | venue: *(not given — research)*
1 / X / 2: 2.2 / 2.8 / 4.1
O2.5 / U2.5: 3 / 1.35
BTTS Y / N: 2.35 / 1.53
1X / 12 / X2: 1.23 / 1.42 / 1.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.75 / 3.6 / 1.65
Corner race 1/X/2: 1.6 / 8.5 / 2.6
Corners line, U/O: 8.5, 1.9 / 1.75
Cards line, U/O: 4.5, 1.9 / 1.7
Home/Away card split: not given

### f3 · Atalanta – Bologna
league: *(not given — research)* | kickoff: 31-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.95 / 3.6 / 3.85
O2.5 / U2.5: 1.87 / 1.85
BTTS Y / N: 1.75 / 2
1X / 12 / X2: 1.25 / 1.28 / 1.85
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.5 / 3.75 / 1.85
Corner race 1/X/2: 1.57 / 9 / 2.6
Corners line, U/O: 9.5, 1.73 / 1.95
Cards line, U/O: 2.5, 2 / 1.65
Home card line, U/O: 1.5, 1.47 / 2.25
Away card line, U/O: 1.5, 1.63 / 1.95

### f4 · Aston Villa – Arsenal
league: *(not given — research)* | kickoff: 31-08-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 6 / 4.3 / 1.53
O2.5 / U2.5: 1.72 / 2.05
BTTS Y / N: 1.8 / 1.93
1X / 12 / X2: 2.5 / 1.2 / 1.12
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.5 / 3.65 / 2.4
Corner race 1/X/2: 2.6 / 9.5 / 1.57
Corners line, U/O: 9.5, 1.8 / 1.87
Cards line, U/O: 3.5, 1.9 / 1.7
Home card line, U/O: 1.5, 2 / 1.6
Away card line, U/O: 1.5, 2.05 / 1.55

### f5 · Barcellona – Rayo Vallecano
league: *(not given — research)* | kickoff: 31-08-2026 21:30 | venue: *(not given — research)*
1 / X / 2: 1.1 / 10 / 20
O2.5 / U2.5: 1.23 / 3.75
BTTS Y / N: 2.05 / 1.68
1X / 12 / X2: not given / 1.04 / 6.75
Win-or-+2 (Home/Away): not given
AH line: -3
EH 3-way (1/X/2 on AH line): 2.75 / 4.55 / 1.92
Corner race 1/X/2: 1.16 / 10 / 5.75
Corners line, U/O: 10.5, 2 / 1.7
Cards line, U/O: 3.5, 1.7 / 1.9
Home/Away card split: not given
