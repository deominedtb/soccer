# fixtures_10 — parsed from odds_10.xlsx (sheet internally named "odds_9"), 30-08-2026

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
  time serialization (e.g. `17:29:59.9999999999968050`,
  `15:29:59.99999999999360325`); normalized to the nearest minute below,
  no source ambiguity.
- Workbook contains four tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used), `odds_7` (sheetId 2, 28-08-2026 fixtures — not used, already
  consumed as fixtures_8), `odds_8` (sheetId 3, 29-08-2026 fixtures — not
  used, already consumed as fixtures_9), and a fourth tab still internally
  named `odds_9` (sheetId 4) whose title row reads "MATCHES 30-08-2026" —
  today's slate, and the one read here. The file is named `odds_10.xlsx`
  and this is the tenth Phase-1 run overall; the internal tab label is
  stale (a leftover from copy/paste) and was not used for numbering —
  output numbered fixtures_10 / progress_10 per the file sequence.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8/9.
- `Win/+2 Home` and `Win/+2 Away` are empty for every one of the 15 rows —
  recorded as not given throughout, not a per-fixture gap.
- f6 (Real Madrid – Malaga) is also missing `1X` — the only double-chance
  cell absent anywhere in this sheet.
- f7 (Stade Rennes FC – Le Mans FC) has no cards market at all — `Cards
  line/U/O` and both home/away card splits are empty.
- Home/away card-split columns are present only for f1, f2, f3, f8, f10,
  f12, f13; empty for f4, f5, f6, f7, f9, f11, f14, f15 — recorded as not
  given per fixture below, not guessed.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line (`EH 3-way`), a 3-way corner-race market, and per-team card O/U
  lines where given.
- Team names are recorded exactly as typed in the source (e.g. "Friburgo"
  = Freiburg, "Amburgo"-style Italian naming appears in earlier slates but
  not this one; "Deportivo La Coruña" carries its correct accent from the
  source string; "Malaga" is spelled without its accent in the source,
  kept as typed).
- All 15 fixtures share the same date, 30-08-2026, across competitions
  inferable from clubs (Premier League, Bundesliga, Championship-adjacent
  EFL sides, LaLiga, Serie A, Ligue 1, Segunda) — league label left to
  Phase 2.

---

### f1 · Chelsea – Brighton
league: *(not given — research)* | kickoff: 30-08-2026 15:00 | venue: *(not given — research)*
1 / X / 2: 1.87 / 3.8 / 3.9
O2.5 / U2.5: 1.57 / 2.3
BTTS Y / N: 1.53 / 2.4
1X / 12 / X2: 1.25 / 1.25 / 1.9
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.15 / 4 / 1.9
Corner race 1/X/2: 1.6 / 8.5 / 2.6
Corners line, U/O: 10.5, 1.65 / 2.05
Cards line, U/O: 4.5, 1.7 / 1.9
Home card line, U/O: 2.5, 1.43 / 2.35
Away card line, U/O: 2.5, 1.52 / 2.1

### f2 · Leeds United – Brentford
league: *(not given — research)* | kickoff: 30-08-2026 15:00 | venue: *(not given — research)*
1 / X / 2: 2.75 / 3.3 / 2.55
O2.5 / U2.5: 1.82 / 1.92
BTTS Y / N: 1.62 / 2.2
1X / 12 / X2: 1.5 / 1.32 / 1.45
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.5 / 4.45 / 5
Corner race 1/X/2: 1.87 / 8.5 / 2.1
Corners line, U/O: 9.5, 2.05 / 1.68
Cards line, U/O: 3.5, 1.7 / 1.9
Home card line, U/O: 1.5, 1.77 / 1.77
Away card line, U/O: 1.5, 1.97 / 1.6

### f3 · Sunderland – Fulham FC
league: *(not given — research)* | kickoff: 30-08-2026 15:00 | venue: *(not given — research)*
1 / X / 2: 2.4 / 3.25 / 3.05
O2.5 / U2.5: 2 / 1.75
BTTS Y / N: 1.75 / 2
1X / 12 / X2: 1.37 / 1.33 / 1.55
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.8 / 4.15 / 1.55
Corner race 1/X/2: 1.8 / 8.5 / 2.2
Corners line, U/O: 9.5, 1.88 / 1.8
Cards line, U/O: 3.5, 2 / 1.65
Home card line, U/O: 1.5, 1.9 / 1.65
Away card line, U/O: 1.5, 2.3 / 1.43

### f4 · Paris FC – Nizza
league: *(not given — research)* | kickoff: 30-08-2026 15:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.3 / 3.75
O2.5 / U2.5: 1.95 / 1.77
BTTS Y / N: 1.77 / 1.95
1X / 12 / X2: 1.25 / 1.32 / 1.75
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.85 / 3.85 / 1.75
Corner race 1/X/2: 1.7 / 8.5 / 2.35
Corners line, U/O: 9.5, 1.92 / 1.75
Cards line, U/O: 3.5, 2 / 1.65
Home/Away card split: not given

### f5 · Friburgo – Werder Brema
league: *(not given — research)* | kickoff: 30-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 1.82 / 3.65 / 4.25
O2.5 / U2.5: 1.68 / 2.05
BTTS Y / N: 1.6 / 2.2
1X / 12 / X2: 1.2 / 1.27 / 1.95
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.1 / 3.85 / 1.95
Corner race 1/X/2: 1.58 / 9 / 2.6
Corners line, U/O: 9.5, 1.75 / 1.92
Cards line, U/O: 3.5, 1.85 / 1.75
Home/Away card split: not given

### f6 · Real Madrid – Malaga
league: *(not given — research)* | kickoff: 30-08-2026 17:00 | venue: *(not given — research)*
1 / X / 2: 1.08 / 12 / 25
O2.5 / U2.5: 1.22 / 3.85
BTTS Y / N: 2.15 / 1.63
1X / 12 / X2: not given / 1.02 / 8
Win-or-+2 (Home/Away): not given
AH line: -3
EH 3-way (1/X/2 on AH line): 2.5 / 4.5 / 2.1
Corner race 1/X/2: 1.11 / 11 / 7
Corners line, U/O: 9.5, 2 / 1.7
Cards line, U/O: 3.5, 1.7 / 1.9
Home/Away card split: not given

### f7 · Stade Rennes FC – Le Mans FC
league: *(not given — research)* | kickoff: 30-08-2026 17:15 | venue: *(not given — research)*
1 / X / 2: 1.42 / 4.85 / 6.75
O2.5 / U2.5: 1.53 / 2.35
BTTS Y / N: 1.68 / 2.05
1X / 12 / X2: 1.09 / 1.17 / 2.8
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.1 / 3.8 / 2.8
Corner race 1/X/2: 1.3 / 9.5 / 3.95
Corners line, U/O: 9.5, 1.98 / 1.7
Cards line, U/O: not given (no cards market for this fixture)
Home/Away card split: not given

### f8 · Manchester United – Ipswich Town
league: *(not given — research)* | kickoff: 30-08-2026 17:30 | venue: *(not given — research)*
1 / X / 2: 1.38 / 5.1 / 7.75
O2.5 / U2.5: 1.47 / 2.55
BTTS Y / N: 1.68 / 2.1
1X / 12 / X2: 1.07 / 1.16 / 3.05
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 1.95 / 3.95 / 3.05
Corner race 1/X/2: 1.25 / 9.5 / 4.3
Corners line, U/O: 9.5, 1.93 / 1.75
Cards line, U/O: 3.5, 1.85 / 1.75
Home card line, U/O: 1.5, 1.52 / 2.1
Away card line, U/O: 2.5, 1.5 / 2.15

### f9 · Augsburg – Schalke 04
league: *(not given — research)* | kickoff: 30-08-2026 17:30 | venue: *(not given — research)*
1 / X / 2: 2.2 / 3.4 / 3.25
O2.5 / U2.5: 1.68 / 2.05
BTTS Y / N: 1.55 / 2.3
1X / 12 / X2: 1.33 / 1.3 / 1.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.05 / 4.2 / 1.65
Corner race 1/X/2: 1.75 / 8.5 / 2.3
Corners line, U/O: 9.5, 1.9 / 1.7
Cards line, U/O: 3.5, 2.05 / 1.6
Home/Away card split: not given

### f10 · Napoli – Como
league: *(not given — research)* | kickoff: 30-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 2.55 / 3.05 / 3
O2.5 / U2.5: 2.2 / 1.62
BTTS Y / N: 1.87 / 1.87
1X / 12 / X2: 1.38 / 1.37 / 1.5
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 5.5 / 4.15 / 1.5
Corner race 1/X/2: 1.75 / 8.5 / 2.3
Corners line, U/O: 8.5, 1.75 / 1.92
Cards line, U/O: 4.5, 1.57 / 2.1
Home card line, U/O: 1.5, 1.97 / 1.6
Away card line, U/O: 2.5, 1.58 / 2

### f11 · Deportivo La Coruña – Valencia
league: *(not given — research)* | kickoff: 30-08-2026 19:30 | venue: *(not given — research)*
1 / X / 2: 2.55 / 2.95 / 3.05
O2.5 / U2.5: 2.4 / 1.5
BTTS Y / N: 1.95 / 1.77
1X / 12 / X2: 1.35 / 1.4 / 1.5
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 5.5 / 4.1 / 1.5
Corner race 1/X/2: 1.83 / 8.5 / 2.15
Corners line, U/O: 8.5, 2.05 / 1.65
Cards line, U/O: 3.5, 2 / 1.65
Home/Away card split: not given

### f12 · Cagliari – Inter
league: *(not given — research)* | kickoff: 30-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 7.75 / 4.6 / 1.42
O2.5 / U2.5: 1.75 / 2
BTTS Y / N: 1.95 / 1.8
1X / 12 / X2: 2.85 / 1.19 / 1.07
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.85 / 3.55 / 2.15
Corner race 1/X/2: 3.25 / 9.5 / 1.4
Corners line, U/O: 9.5, 1.7 / 1.98
Cards line, U/O: 3.5, 1.65 / 2
Home card line, U/O: 1.5, 2 / 1.58
Away card line, U/O: 1.5, 1.65 / 1.92

### f13 · Lazio – Genoa
league: *(not given — research)* | kickoff: 30-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.25 / 3 / 3.75
O2.5 / U2.5: 2.45 / 1.5
BTTS Y / N: 2 / 1.75
1X / 12 / X2: 1.27 / 1.38 / 1.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.6 / 3.75 / 1.65
Corner race 1/X/2: 1.55 / 9 / 2.7
Corners line, U/O: 8.5, 1.92 / 1.75
Cards line, U/O: 3.5, 1.9 / 1.7
Home card line, U/O: 1.5, 2.1 / 1.55
Away card line, U/O: 1.5, 1.98 / 1.6

### f14 · Monaco – Marsiglia
league: *(not given — research)* | kickoff: 30-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.2 / 3.6 / 3.1
O2.5 / U2.5: 1.57 / 2.25
BTTS Y / N: 1.47 / 2.5
1X / 12 / X2: 1.35 / 1.28 / 1.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.95 / 4.25 / 1.65
Corner race 1/X/2: 2 / 8 / 1.97
Corners line, U/O: 9.5, 1.83 / 1.85
Cards line, U/O: 3.5, 2.05 / 1.6
Home/Away card split: not given

### f15 · Celta Vigo – Athletic Bilbao
league: *(not given — research)* | kickoff: 30-08-2026 21:30 | venue: *(not given — research)*
1 / X / 2: 2.65 / 3.15 / 2.75
O2.5 / U2.5: 2.05 / 1.68
BTTS Y / N: 1.77 / 1.95
1X / 12 / X2: 1.45 / 1.35 / 1.45
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 5.75 / 4.35 / 1.45
Corner race 1/X/2: 1.98 / 8 / 2
Corners line, U/O: 8.5, 1.85 / 1.82
Cards line, U/O: 4.5, 1.67 / 1.95
Home/Away card split: not given
