# fixtures_8 — parsed from odds_7.xlsx (sheet "odds_7"), 28-08-2026

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
  time serialization (e.g. `18:59:59.9999999999968050`); normalized to
  the nearest minute below, no source ambiguity.
- Sheet also contains a tab named `odds_EXAMPLE` (sheetId 1) — not used;
  `odds_7` (sheetId 2) is the one read, per file name given.
- All 6 rows have complete 1/X/2, O/U 2.5, BTTS, cards and corners
  fields — no "-" cells, no uncertain prices.
- Extra markets beyond the standard template exist in this file: double
  chance (1X/12/X2), win-or-+2-goals, Asian handicap line, half-time
  1X2, a 3-way corner-race market (Corn 1/X/2), and — for f4 and f5
  only — per-team card O/U lines. No dedicated "team corners" column
  is present in this file.

---

### f1 · Racing Santander – Elche
league: *(not given — research)* | kickoff: 28-08-2026 19:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.5 / 3.55
O2.5 / U2.5: 1.65 / 2.15
BTTS Y / N: 1.57 / 2.30
1X / 12 / X2: 1.30 / 1.30 / 1.75
Win-or-+2 (Home/Away): 1.98 / 3.4
AH line: -1
HT 1/X/2: 3.6 / 4.10 / 1.75
Corner race 1/X/2: 1.95 / 8.5 / 2.0
Corners line, U/O: 9.5, 1.77 / 1.90
Cards line, U/O: 4.5, 1.90 / 1.70
Home/Away card split: not given

### f2 · Bayern Monaco – Stoccarda
league: *(not given — research)* | kickoff: 28-08-2026 20:30 | venue: *(not given — research)*
1 / X / 2: 1.23 / 7.0 / 10.5
O2.5 / U2.5: 1.16 / 4.5
BTTS Y / N: 1.43 / 2.65
1X / 12 / X2: 1.04 / 1.09 / 4.15
Win-or-+2 (Home/Away): 1.2 / 9.5
AH line: -2
HT 1/X/2: 2.25 / 4.55 / 2.35
Corner race 1/X/2: 1.23 / 10.0 / 4.55
Corners line, U/O: 9.5, 1.95 / 1.73
Cards line, U/O: 3.5, 1.65 / 2.0
Home/Away card split: not given

### f3 · Lille – PSG
league: *(not given — research)* | kickoff: 28-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 5.0 / 3.8 / 1.7
O2.5 / U2.5: 1.72 / 2.0
BTTS Y / N: 1.68 / 2.1
1X / 12 / X2: 2.15 / 1.25 / 1.16
Win-or-+2 (Home/Away): not given
AH line: +1
HT 1/X/2: 2.15 / 3.75 / 2.8
Corner race 1/X/2: 2.6 / 9.5 / 1.57
Corners line, U/O: 9.5, 1.80 / 1.88
Cards line, U/O: 3.5, 1.55 / 2.15
Home/Away card split: not given

### f4 · Milan – Venezia
league: *(not given — research)* | kickoff: 28-08-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.47 / 4.35 / 7.1
O2.5 / U2.5: 1.68 / 2.1
BTTS Y / N: 1.85 / 1.9
1X / 12 / X2: 1.09 / 1.2 / 2.65
Win-or-+2 (Home/Away): 1.43 / 6.5
AH line: -1
HT 1/X/2: 2.25 / 3.65 / 2.65
Corner race 1/X/2: 1.3 / 9.5 / 3.85
Corners line, U/O: 9.5, 1.70 / 1.98
Cards line, U/O: 2.5, 2.10 / 1.60
Home card line, U/O: 1.5, 1.35 / 2.6
Away card line, U/O: 1.5, 1.90 / 1.65

### f5 · Crystal Palace – Manchester City
league: *(not given — research)* | kickoff: 28-08-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 4.8 / 4.0 / 1.68
O2.5 / U2.5: 1.68 / 2.1
BTTS Y / N: 1.65 / 2.15
1X / 12 / X2: 2.15 / 1.25 / 1.17
Win-or-+2 (Home/Away): 4.5 / 1.63
AH line: +1
HT 1/X/2: 2.15 / 3.75 / 2.75
Corner race 1/X/2: 3.55 / 8.5 / 1.37
Corners line, U/O: 9.5, 1.75 / 1.85
Cards line, U/O: 3.5, 1.83 / 1.77
Home card line, U/O: 1.5, 2.05 / 1.55
Away card line, U/O: 1.5, 1.90 / 1.65

### f6 · Alavés – Villarreal
league: *(not given — research)* | kickoff: 28-08-2026 21:30 | venue: *(not given — research)*
1 / X / 2: 3.2 / 3.5 / 2.2
O2.5 / U2.5: 1.75 / 2.0
BTTS Y / N: 1.63 / 2.2
1X / 12 / X2: 1.65 / 1.3 / 1.35
Win-or-+2 (Home/Away): 3.05 / 2.1
AH line: +1
HT 1/X/2: 1.65 / 4.1 / 4.1
Corner race 1/X/2: 1.8 / 8.5 / 2.2
Corners line, U/O: 9.5, 1.75 / 1.92
Cards line, U/O: 4.5, 1.90 / 1.70
Home/Away card split: not given
