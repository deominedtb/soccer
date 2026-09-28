# fixtures_9 — parsed from odds_8.xlsx (sheet "odds_8"), 29-08-2026

Header row read from file (no assumed positions). Fields present: Date, KO,
Home, Away, 1, X, 2, Goals line, Under, Over, GG, NG, 1X, 12, X2,
Win/+2 Home, Win/+2 Away, AH line, 1H, XH, 2H, Corn 1, Corn X, Corn 2,
Corn line, Corn U, Corn O, Cards line, Cards U, Cards O, Home crd line,
Home crd U, Home crd O, Away crd line, Away crd U, Away crd O.

**Flags**
- No `league` or `venue` columns in the source header — both fields are
  absent from every row below and must come from Phase 2 research, not
  invented here.
- KO times in the raw cells carry floating-point artifacts from Excel's
  time serialization (e.g. `20:45:00.0000000000031950`,
  `15:29:59.99999999999360325`); normalized to the nearest minute below,
  no source ambiguity.
- Workbook also contains tabs `odds_EXAMPLE` (sheetId 1) and `odds_7`
  (sheetId 2) — not used; `odds_8` (sheetId 3) is the one read, per the
  filename given. Note the file is named `odds_8.xlsx` but this is the
  ninth Phase-1 run (fixtures_8/progress_8 already exist from
  `odds_7.xlsx`) — output numbered fixtures_9 / progress_9 accordingly.
- All 22 rows have complete 1/X/2, O/U 2.5, BTTS, cards and corners
  fields — no "-" cells, no unreadable prices.
- `Win/+2 Home` and `Win/+2 Away` are empty for every row in this sheet
  — recorded as not given throughout, not a per-fixture gap.
- Extra markets beyond the standard template exist in this file: double
  chance (1X/12/X2), a 3-way handicap (`EH 3-way`, labelled per the
  header correction logged in fixtures_8.md — these are the three-way
  price on the `AH line`, not half-time 1X2), a 3-way corner-race market,
  and — for 9 of the 22 fixtures — per-team card O/U lines.
- Team names are recorded exactly as typed in the source (Italian
  bookmaker naming for several clubs, e.g. "Colonia" = Köln, "Lipsia" =
  Leipzig, "Amburgo" = Hamburg, "Union Berlino", "Eintracht Francoforte",
  "Siviglia" = Sevilla) — not translated here, per the no-re-verify rule.
- All 22 fixtures share the same date, 29-08-2026, across four
  competitions inferable from clubs (Premier League, Bundesliga,
  Championship, LaLiga, Serie A, Ligue 1) — league label left to Phase 2.

---

### f1 · Liverpool – Nottingham Forest
league: *(not given — research)* | kickoff: 29-08-2026 13:30 | venue: *(not given — research)*
1 / X / 2: 1.47 / 4.6 / 6.5
O2.5 / U2.5: 1.48 / 2.5
BTTS Y / N: 1.62 / 2.2
1X / 12 / X2: 1.1 / 1.19 / 2.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.15 / 3.9 / 2.65
Corner race 1/X/2: 1.23 / 9.5 / 4.6
Corners line, U/O: 10.5, 1.67 / 2.05
Cards line, U/O: 3.5, 1.7 / 1.9
Home card line, U/O: 1.5, 1.52 / 2.1
Away card line, U/O: 1.5, 2.3 / 1.43

### f2 · Colonia – Hoffenheim
league: *(not given — research)* | kickoff: 29-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 2.95 / 3.75 / 2.2
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.43 / 2.6
1X / 12 / X2: 1.65 / 1.25 / 1.4
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 6 / 5 / 1.4
Corner race 1/X/2: 2.35 / 8.5 / 1.7
Corners line, U/O: 10.5, 1.7 / 2
Cards line, U/O: 3.5, 1.8 / 1.85
Home/Away card split: not given

### f3 · Lipsia – Borussia Mönchengladbach
league: *(not given — research)* | kickoff: 29-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 1.55 / 4.4 / 5.25
O2.5 / U2.5: 1.43 / 2.6
BTTS Y / N: 1.52 / 2.35
1X / 12 / X2: 1.15 / 1.2 / 2.4
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.35 / 3.95 / 2.4
Corner race 1/X/2: 1.35 / 9.5 / 3.5
Corners line, U/O: 9.5, 1.8 / 1.77
Cards line, U/O: 3.5, 1.65 / 1.95
Home/Away card split: not given

### f4 · Mainz – SC Paderborn
league: *(not given — research)* | kickoff: 29-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 1.55 / 4.25 / 5.5
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.6 / 2.2
1X / 12 / X2: 1.14 / 1.2 / 2.4
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.4 / 3.9 / 2.4
Corner race 1/X/2: 1.43 / 9 / 3.1
Corners line, U/O: 9.5, 1.88 / 1.8
Cards line, U/O: 3.5, 1.8 / 1.8
Home/Away card split: not given

### f5 · SV 07 Elversberg – Bayer Leverkusen
league: *(not given — research)* | kickoff: 29-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 5 / 4.25 / 1.6
O2.5 / U2.5: 1.43 / 2.6
BTTS Y / N: 1.5 / 2.4
1X / 12 / X2: 2.3 / 1.2 / 1.16
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.3 / 4 / 2.45
Corner race 1/X/2: 2.75 / 10 / 1.5
Corners line, U/O: 9.5, 1.85 / 1.83
Cards line, U/O: 3.5, 1.8 / 1.8
Home/Away card split: not given

### f6 · Union Berlino – Eintracht Francoforte
league: *(not given — research)* | kickoff: 29-08-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 2.6 / 3.5 / 2.55
O2.5 / U2.5: 1.6 / 2.2
BTTS Y / N: 1.47 / 2.5
1X / 12 / X2: 1.5 / 1.3 / 1.48
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.5 / 4.6 / 4.95
Corner race 1/X/2: 1.8 / 8.5 / 2.2
Corners line, U/O: 9.5, 1.9 / 1.78
Cards line, U/O: 3.5, 1.65 / 1.95
Home/Away card split: not given

### f7 · Bournemouth – Everton
league: *(not given — research)* | kickoff: 29-08-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 2.1 / 3.35 / 3.6
O2.5 / U2.5: 1.83 / 1.9
BTTS Y / N: 1.67 / 2.1
1X / 12 / X2: 1.28 / 1.32 / 1.72
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.85 / 4 / 1.72
Corner race 1/X/2: 1.5 / 9 / 2.8
Corners line, U/O: 10.5, 1.73 / 1.95
Cards line, U/O: 3.5, 2.05 / 1.6
Home card line, U/O: 1.5, 1.82 / 1.73
Away card line, U/O: 2.5, 1.48 / 2.2

### f8 · Coventry City – Hull City
league: *(not given — research)* | kickoff: 29-08-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 1.78 / 3.55 / 4.65
O2.5 / U2.5: 1.87 / 1.85
BTTS Y / N: 1.75 / 2
1X / 12 / X2: 1.18 / 1.28 / 2
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.1 / 3.7 / 2
Corner race 1/X/2: 1.48 / 9 / 2.9
Corners line, U/O: 9.5, 1.8 / 1.88
Cards line, U/O: 4.5, 1.52 / 2.2
Home card line, U/O: 1.5, 1.7 / 1.85
Away card line, U/O: 2.5, 1.7 / 1.85

### f9 · Levante – Real Betis
league: *(not given — research)* | kickoff: 29-08-2026 17:00 | venue: *(not given — research)*
1 / X / 2: 3.15 / 3.25 / 2.3
O2.5 / U2.5: 1.9 / 1.8
BTTS Y / N: 1.72 / 2
1X / 12 / X2: 1.6 / 1.33 / 1.35
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.6 / 4.1 / 4.5
Corner race 1/X/2: 1.88 / 8.5 / 2.1
Corners line, U/O: 9.5, 1.87 / 1.8
Cards line, U/O: 3.5, 1.9 / 1.75
Home/Away card split: not given

### f10 · Strasburgo – Lens
league: *(not given — research)* | kickoff: 29-08-2026 17:15 | venue: *(not given — research)*
1 / X / 2: 3.75 / 3.6 / 1.93
O2.5 / U2.5: 1.6 / 2.2
BTTS Y / N: 1.52 / 2.35
1X / 12 / X2: 1.85 / 1.28 / 1.25
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.85 / 4.05 / 3.35
Corner race 1/X/2: 2.3 / 8.5 / 1.7
Corners line, U/O: 9.5, 1.8 / 1.87
Cards line, U/O: 4.5, 1.6 / 2.05
Home/Away card split: not given

### f11 · Fiorentina – Frosinone
league: *(not given — research)* | kickoff: 29-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 1.65 / 4 / 5.1
O2.5 / U2.5: 1.72 / 2.05
BTTS Y / N: 1.75 / 2
1X / 12 / X2: 1.16 / 1.25 / 2.2
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.7 / 3.65 / 2.2
Corner race 1/X/2: 1.48 / 9 / 2.9
Corners line, U/O: 9.5, 1.83 / 1.77
Cards line, U/O: 4.5, 1.6 / 2
Home card line, U/O: 1.5, 2 / 1.6
Away card line, U/O: 2.5, 1.62 / 1.95

### f12 · Monza – Udinese
league: *(not given — research)* | kickoff: 29-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 3 / 3 / 2.55
O2.5 / U2.5: 2.2 / 1.62
BTTS Y / N: 1.85 / 1.87
1X / 12 / X2: 1.5 / 1.38 / 1.38
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.5 / 4.15 / 5.5
Corner race 1/X/2: 1.98 / 8 / 2
Corners line, U/O: 8.5, 1.92 / 1.75
Cards line, U/O: 3.5, 2.05 / 1.6
Home card line, U/O: 1.5, 2.25 / 1.45
Away card line, U/O: 1.5, 2.05 / 1.55

### f13 · Sassuolo – Torino
league: *(not given — research)* | kickoff: 29-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 2.25 / 3.2 / 3.3
O2.5 / U2.5: 2 / 1.75
BTTS Y / N: 1.72 / 2.05
1X / 12 / X2: 1.32 / 1.35 / 1.62
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.4 / 3.95 / 1.62
Corner race 1/X/2: 1.63 / 8.5 / 2.5
Corners line, U/O: 8.5, 2.05 / 1.67
Cards line, U/O: 3.5, 1.7 / 1.9
Home card line, U/O: 1.5, 1.8 / 1.73
Away card line, U/O: 1.5, 1.92 / 1.65

### f14 · Tottenham – Newcastle United
league: *(not given — research)* | kickoff: 29-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 2.15 / 3.65 / 3.15
O2.5 / U2.5: 1.6 / 2.25
BTTS Y / N: 1.5 / 2.45
1X / 12 / X2: 1.35 / 1.27 / 1.68
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.85 / 4.2 / 1.68
Corner race 1/X/2: 1.55 / 9 / 2.65
Corners line, U/O: 10.5, 1.8 / 1.85
Cards line, U/O: 4.5, 1.65 / 2
Home card line, U/O: 2.5, 1.43 / 2.3
Away card line, U/O: 2.5, 1.45 / 2.3

### f15 · Borussia Dortmund – Amburgo
league: *(not given — research)* | kickoff: 29-08-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 1.35 / 5.25 / 7.5
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.8 / 1.9
1X / 12 / X2: 1.08 / 1.15 / 3.1
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 1.95 / 3.85 / 3.1
Corner race 1/X/2: 1.19 / 9.5 / 5.25
Corners line, U/O: 9.5, 1.97 / 1.72
Cards line, U/O: 4.5, 1.6 / 2.05
Home/Away card split: not given

### f16 · Real Sociedad – Espanyol
league: *(not given — research)* | kickoff: 29-08-2026 19:00 | venue: *(not given — research)*
1 / X / 2: 1.8 / 3.7 / 4.25
O2.5 / U2.5: 1.8 / 1.9
BTTS Y / N: 1.68 / 2.05
1X / 12 / X2: 1.2 / 1.25 / 1.98
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.15 / 3.7 / 1.98
Corner race 1/X/2: 1.47 / 9 / 2.95
Corners line, U/O: 9.5, 1.85 / 1.82
Cards line, U/O: 4.5, 1.9 / 1.7
Home/Away card split: not given

### f17 · Juventus – Parma
league: *(not given — research)* | kickoff: 29-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.23 / 6.1 / 13
O2.5 / U2.5: 1.72 / 2.05
BTTS Y / N: 2.35 / 1.53
1X / 12 / X2: 1.02 / 1.12 / 4.15
Win-or-+2 (Home/Away): not given
AH line: -2
EH 3-way (1/X/2 on AH line): 2.9 / 3.8 / 2.05
Corner race 1/X/2: 1.15 / 10 / 6
Corners line, U/O: 9.5, 1.93 / 1.75
Cards line, U/O: 3.5, 1.7 / 1.85
Home card line, U/O: 1.5, 1.5 / 2.2
Away card line, U/O: 2.5, 1.43 / 2.3

### f18 · Auxerre – Angers
league: *(not given — research)* | kickoff: 29-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2 / 3.4 / 3.8
O2.5 / U2.5: 1.9 / 1.8
BTTS Y / N: 1.8 / 1.9
1X / 12 / X2: 1.25 / 1.3 / 1.8
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.7 / 3.85 / 1.8
Corner race 1/X/2: 1.45 / 9 / 2.95
Corners line, U/O: 9.5, 1.75 / 1.9
Cards line, U/O: 3.5, 2 / 1.62
Home/Away card split: not given

### f19 · Brest – Tolosa FC
league: *(not given — research)* | kickoff: 29-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.65 / 3.3 / 2.65
O2.5 / U2.5: 1.9 / 1.8
BTTS Y / N: 1.65 / 2.1
1X / 12 / X2: 1.47 / 1.32 / 1.47
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.47 / 4.45 / 5.5
Corner race 1/X/2: 1.95 / 8.5 / 2
Corners line, U/O: 9.5, 1.75 / 1.92
Cards line, U/O: 4.5, 1.7 / 1.9
Home/Away card split: not given

### f20 · Lione – Le Havre AC
league: *(not given — research)* | kickoff: 29-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.47 / 4.5 / 6.5
O2.5 / U2.5: 1.72 / 2
BTTS Y / N: 1.87 / 1.83
1X / 12 / X2: 1.1 / 1.19 / 2.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.3 / 3.6 / 2.65
Corner race 1/X/2: 1.3 / 9.5 / 3.95
Corners line, U/O: 9.5, 1.92 / 1.75
Cards line, U/O: 4.5, 1.55 / 2.1
Home/Away card split: not given

### f21 · Lorient – Troyes
league: *(not given — research)* | kickoff: 29-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.85 / 3.55 / 4.25
O2.5 / U2.5: 2 / 1.72
BTTS Y / N: 1.85 / 1.85
1X / 12 / X2: 1.2 / 1.28 / 1.93
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.35 / 3.6 / 1.93
Corner race 1/X/2: 1.7 / 8.5 / 2.35
Corners line, U/O: 8.5, 1.98 / 1.7
Cards line, U/O: 4.5, 1.62 / 2
Home/Away card split: not given

### f22 · Siviglia – Atletico Madrid
league: *(not given — research)* | kickoff: 29-08-2026 21:30 | venue: *(not given — research)*
1 / X / 2: 4.1 / 3.35 / 1.95
O2.5 / U2.5: 2 / 1.72
BTTS Y / N: 1.8 / 1.9
1X / 12 / X2: 1.83 / 1.3 / 1.23
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.83 / 3.75 / 3.6
Corner race 1/X/2: 2.05 / 8 / 1.95
Corners line, U/O: 9.5, 1.77 / 1.9
Cards line, U/O: 4.5, 1.8 / 1.85
Home/Away card split: not given
