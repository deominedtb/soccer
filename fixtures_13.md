# fixtures_13 — parsed from odds_13.xlsx (sheet internally named "odds_12"), 05-09-2026

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
  time serialization (e.g. `20:44:59.99999999997441975`); normalized to
  the nearest minute below, no source ambiguity.
- Workbook contains seven tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used), `odds_7` (sheetId 2, 28-08-2026 fixtures — not used, already
  consumed as fixtures_8), `odds_8` (sheetId 3, 29-08-2026 fixtures — not
  used, already consumed as fixtures_9), `odds_9` (sheetId 4, 30-08-2026
  fixtures — not used, already consumed as fixtures_10), `odds_10`
  (sheetId 5, 31-08-2026 fixtures — not used, already consumed as
  fixtures_11), `odds_11` (sheetId 6, 04-09-2026 fixtures — not used,
  already consumed as fixtures_12), and a seventh tab still internally
  named `odds_12` (sheetId 7) whose title row reads "MATCHES 05-09-2026 —
  odds read from screenshots" — today's slate, and the one read here. The
  file is named `odds_13.xlsx` and this is the thirteenth Phase-1 run
  overall; the internal tab label is stale (a leftover from copy/paste)
  and was not used for numbering — output numbered fixtures_13 /
  progress_13 per the file sequence, same lag pattern seen in
  odds_10.xlsx through odds_12.xlsx.
- 21 fixtures on this sheet (`A4:AJ24`). This is 15 more than the last
  slate (odds_12, 6 fixtures) and clears the >6-fixture threshold, so
  Phase 1.5 triage runs before Phase 2 on this slate.
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8 through fixtures_12.
  The goals line is 2.5 for every fixture here.
- `Win/+2 Home` and `Win/+2 Away` are empty for all 21 rows — recorded as
  not given throughout, not a per-fixture gap.
- No fixture is missing a 1X / 12 / X2 cell, an AH-line 3-way price, a
  corner-race price or a cards line this slate.
- Home/away card-split columns are present only for f1 (Fiorentina –
  Torino), f7 (Brentford – Sunderland), f8 (Brighton – Leeds United), f9
  (Fulham FC – Crystal Palace), f10 (Manchester City – Coventry City),
  f11 (Nottingham Forest – Tottenham), f15 (Hull City – Aston Villa) and
  f18 (Roma – Atalanta); empty for the other 13 fixtures — recorded as
  not given per fixture below, not guessed.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line, a 3-way corner-race market, and per-team card O/U lines where
  given.
- Team names are recorded exactly as typed in the source (e.g. "Union
  Berlino" = Union Berlin, "Friburgo" = Freiburg, "Lipsia" = Leipzig,
  "Werder Brema" = Werder Bremen, "Bayern Monaco" = Bayern Munich,
  "Nizza" = Nice — Italian-style naming carried over from earlier
  slates). "Borussia Mönchengladbach" and "Deportivo La Coruña" carry
  their diacritics correctly in the source file.
- All 21 fixtures share the same date, 05-09-2026, across competitions
  inferable from clubs (Serie A, Bundesliga, Premier League, LaLiga,
  Ligue 1) — league label left to Phase 2.

---

### f1 · Fiorentina – Torino
league: *(not given — research)* | kickoff: 05-09-2026 15:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.3 / 3.85
O2.5 / U2.5: 1.9 / 1.85
BTTS Y / N: 1.72 / 2.05
1X / 12 / X2: 1.25 / 1.32 / 1.75
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.75 / 3.85 / 1.75
Corner race 1/X/2: 1.47 / 9 / 2.95
Corners line, U/O: 8.5, 1.95 / 1.72
Cards line, U/O: 4.5, 1.8 / 1.8
Home card line, U/O: 2.5, 1.42 / 2.35
Away card line, U/O: 2.5, 1.65 / 1.93

### f2 · Bayer Leverkusen – Union Berlino
league: *(not given — research)* | kickoff: 05-09-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 1.37 / 5.25 / 7.5
O2.5 / U2.5: 1.35 / 2.95
BTTS Y / N: 1.5 / 2.4
1X / 12 / X2: 1.08 / 1.15 / 3.05
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 1.9 / 4.15 / 3.05
Corner race 1/X/2: 1.27 / 9.5 / 4.15
Corners line, U/O: 10.5, 1.68 / 2.05
Cards line, U/O: 3.5, 1.8 / 1.8
Home/Away card split: not given

### f3 · Borussia Mönchengladbach – SV 07 Elversberg
league: *(not given — research)* | kickoff: 05-09-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 1.9 / 3.8 / 3.75
O2.5 / U2.5: 1.43 / 2.6
BTTS Y / N: 1.5 / 2.4
1X / 12 / X2: 1.25 / 1.25 / 1.88
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.1 / 4.2 / 1.88
Corner race 1/X/2: 1.62 / 8.5 / 2.55
Corners line, U/O: 9.5, 1.72 / 1.95
Cards line, U/O: 3.5, 1.85 / 1.75
Home/Away card split: not given

### f4 · Hoffenheim – Borussia Dortmund
league: *(not given — research)* | kickoff: 05-09-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 2.6 / 3.8 / 2.45
O2.5 / U2.5: 1.42 / 2.65
BTTS Y / N: 1.37 / 2.85
1X / 12 / X2: 1.55 / 1.25 / 1.48
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.55 / 4.7 / 4.45
Corner race 1/X/2: 1.85 / 8.5 / 2.15
Corners line, U/O: 9.5, 2 / 1.68
Cards line, U/O: 3.5, 2.05 / 1.6
Home/Away card split: not given

### f5 · SC Paderborn – Friburgo
league: *(not given — research)* | kickoff: 05-09-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 3.75 / 3.65 / 1.95
O2.5 / U2.5: 1.6 / 2.2
BTTS Y / N: 1.53 / 2.35
1X / 12 / X2: 1.85 / 1.27 / 1.25
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.85 / 4.05 / 3.35
Corner race 1/X/2: 1.95 / 8.5 / 2
Corners line, U/O: 9.5, 1.7 / 2
Cards line, U/O: 3.5, 2.05 / 1.6
Home/Away card split: not given

### f6 · Werder Brema – Lipsia
league: *(not given — research)* | kickoff: 05-09-2026 15:30 | venue: *(not given — research)*
1 / X / 2: 4.1 / 4.15 / 1.75
O2.5 / U2.5: 1.37 / 2.85
BTTS Y / N: 1.4 / 2.75
1X / 12 / X2: 2.05 / 1.22 / 1.22
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.05 / 4.15 / 2.75
Corner race 1/X/2: 2.25 / 8.5 / 1.75
Corners line, U/O: 9.5, 1.88 / 1.8
Cards line, U/O: 3.5, 1.7 / 1.9
Home/Away card split: not given

### f7 · Brentford – Sunderland
league: *(not given — research)* | kickoff: 05-09-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 1.73 / 3.8 / 4.75
O2.5 / U2.5: 1.8 / 1.95
BTTS Y / N: 1.72 / 2.05
1X / 12 / X2: 1.18 / 1.25 / 2.1
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.9 / 3.7 / 2.1
Corner race 1/X/2: 1.45 / 9 / 3
Corners line, U/O: 9.5, 1.97 / 1.72
Cards line, U/O: 3.5, 2 / 1.65
Home card line, U/O: 1.5, 1.73 / 1.8
Away card line, U/O: 2.5, 1.48 / 2.2

### f8 · Brighton – Leeds United
league: *(not given — research)* | kickoff: 05-09-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.5 / 3.6
O2.5 / U2.5: 1.75 / 2
BTTS Y / N: 1.62 / 2.2
1X / 12 / X2: 1.28 / 1.3 / 1.75
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.7 / 4 / 1.75
Corner race 1/X/2: 1.35 / 9.5 / 3.55
Corners line, U/O: 9.5, 2 / 1.68
Cards line, U/O: 4.5, 1.55 / 2.15
Home card line, U/O: 1.5, 2.1 / 1.53
Away card line, U/O: 2.5, 1.47 / 2.2

### f9 · Fulham FC – Crystal Palace
league: *(not given — research)* | kickoff: 05-09-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 2.15 / 3.25 / 3.6
O2.5 / U2.5: 1.9 / 1.85
BTTS Y / N: 1.68 / 2.1
1X / 12 / X2: 1.28 / 1.33 / 1.7
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4 / 4 / 1.7
Corner race 1/X/2: 1.5 / 9 / 2.85
Corners line, U/O: 9.5, 1.97 / 1.72
Cards line, U/O: 3.5, 1.85 / 1.75
Home card line, U/O: 1.5, 1.8 / 1.73
Away card line, U/O: 1.5, 2.2 / 1.5

### f10 · Manchester City – Coventry City
league: *(not given — research)* | kickoff: 05-09-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 1.18 / 7.5 / 13
O2.5 / U2.5: 1.35 / 3
BTTS Y / N: 2 / 1.75
1X / 12 / X2: 1.02 / 1.08 / 4.75
Win-or-+2 (Home/Away): not given
AH line: -2
EH 3-way (1/X/2 on AH line): 2.3 / 4.1 / 2.45
Corner race 1/X/2: 1.12 / 11 / 6.5
Corners line, U/O: 10.5, 1.67 / 2.05
Cards line, U/O: 2.5, 2.05 / 1.6
Home card line, U/O: 0.5, 2.55 / 1.35
Away card line, U/O: 1.5, 1.95 / 1.6

### f11 · Nottingham Forest – Tottenham
league: *(not given — research)* | kickoff: 05-09-2026 16:00 | venue: *(not given — research)*
1 / X / 2: 2.5 / 3.4 / 2.8
O2.5 / U2.5: 1.75 / 2
BTTS Y / N: 1.6 / 2.25
1X / 12 / X2: 1.43 / 1.3 / 1.52
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 4.85 / 4.4 / 1.52
Corner race 1/X/2: 1.95 / 8.5 / 2
Corners line, U/O: 10.5, 1.68 / 2.05
Cards line, U/O: 3.5, 1.7 / 1.9
Home card line, U/O: 1.5, 1.58 / 2
Away card line, U/O: 1.5, 2.2 / 1.47

### f12 · Athletic Bilbao – Atletico Madrid
league: *(not given — research)* | kickoff: 05-09-2026 16:15 | venue: *(not given — research)*
1 / X / 2: 3 / 3.3 / 2.4
O2.5 / U2.5: 1.85 / 1.85
BTTS Y / N: 1.62 / 2.15
1X / 12 / X2: 1.55 / 1.32 / 1.38
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.55 / 4.25 / 4.7
Corner race 1/X/2: 1.77 / 8.5 / 2.25
Corners line, U/O: 9.5, 1.98 / 1.7
Cards line, U/O: 4.5, 1.6 / 2.05
Home/Away card split: not given

### f13 · Lens – Lorient
league: *(not given — research)* | kickoff: 05-09-2026 17:15 | venue: *(not given — research)*
1 / X / 2: 1.55 / 4.35 / 5.5
O2.5 / U2.5: 1.6 / 2.2
BTTS Y / N: 1.68 / 2.05
1X / 12 / X2: 1.14 / 1.2 / 2.4
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.4 / 3.75 / 2.4
Corner race 1/X/2: 1.37 / 9.5 / 3.35
Corners line, U/O: 9.5, 2 / 1.68
Cards line, U/O: 3.5, 1.6 / 2.05
Home/Away card split: not given

### f14 · Inter – Napoli
league: *(not given — research)* | kickoff: 05-09-2026 18:00 | venue: *(not given — research)*
1 / X / 2: 1.67 / 3.75 / 5.5
O2.5 / U2.5: 1.85 / 1.9
BTTS Y / N: 1.85 / 1.9
1X / 12 / X2: 1.14 / 1.25 / 2.2
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.75 / 3.6 / 2.2
Corner race 1/X/2: 1.5 / 9 / 2.8
Corners line, U/O: 9.5, 1.68 / 2.05
Cards line, U/O: 3.5, 1.55 / 2.15
Home/Away card split: not given

### f15 · Hull City – Aston Villa
league: *(not given — research)* | kickoff: 05-09-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 4 / 3.6 / 1.9
O2.5 / U2.5: 1.85 / 1.9
BTTS Y / N: 1.75 / 2
1X / 12 / X2: 1.88 / 1.28 / 1.25
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.88 / 3.8 / 3.4
Corner race 1/X/2: 2.8 / 10 / 1.48
Corners line, U/O: 9.5, 1.68 / 2
Cards line, U/O: 3.5, 1.8 / 1.8
Home card line, U/O: 1.5, 2.15 / 1.5
Away card line, U/O: 1.5, 1.75 / 1.78

### f16 · Rayo Vallecano – Racing Santander
league: *(not given — research)* | kickoff: 05-09-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 2 / 3.5 / 3.75
O2.5 / U2.5: 1.65 / 2.1
BTTS Y / N: 1.55 / 2.3
1X / 12 / X2: 1.25 / 1.3 / 1.8
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 3.5 / 4.05 / 1.8
Corner race 1/X/2: 1.43 / 9 / 3.1
Corners line, U/O: 10.5, 1.72 / 1.97
Cards line, U/O: 5.5, 1.6 / 2.05
Home/Away card split: not given

### f17 · Schalke 04 – Bayern Monaco
league: *(not given — research)* | kickoff: 05-09-2026 18:30 | venue: *(not given — research)*
1 / X / 2: 14 / 8.5 / 1.15
O2.5 / U2.5: 1.2 / 4.2
BTTS Y / N: 1.65 / 2.1
1X / 12 / X2: 5.25 / 1.06 / 1.01
Win-or-+2 (Home/Away): not given
AH line: +2
EH 3-way (1/X/2 on AH line): 2.75 / 4.45 / 1.98
Corner race 1/X/2: 5 / 7.75 / 1.25
Corners line, U/O: 9.5, 1.85 / 1.8
Cards line, U/O: 3.5, 1.85 / 1.75
Home/Away card split: not given

### f18 · Roma – Atalanta
league: *(not given — research)* | kickoff: 05-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.7 / 3.8 / 4.9
O2.5 / U2.5: 1.65 / 2.15
BTTS Y / N: 1.62 / 2.2
1X / 12 / X2: 1.17 / 1.25 / 2.15
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.75 / 3.75 / 2.15
Corner race 1/X/2: 1.5 / 9 / 2.8
Corners line, U/O: 9.5, 1.65 / 2.05
Cards line, U/O: 3.5, 1.85 / 1.75
Home card line, U/O: 1.5, 1.7 / 1.85
Away card line, U/O: 1.5, 2.35 / 1.43

### f19 · Le Havre AC – Brest
league: *(not given — research)* | kickoff: 05-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 2.7 / 3.25 / 2.65
O2.5 / U2.5: 1.9 / 1.8
BTTS Y / N: 1.72 / 2
1X / 12 / X2: 1.47 / 1.33 / 1.45
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 1.47 / 4.45 / 5.5
Corner race 1/X/2: 1.85 / 8.5 / 2.15
Corners line, U/O: 9.5, 1.67 / 2.05
Cards line, U/O: 3.5, 2 / 1.65
Home/Away card split: not given

### f20 · Nizza – Le Mans FC
league: *(not given — research)* | kickoff: 05-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 1.75 / 3.75 / 4.5
O2.5 / U2.5: 1.75 / 1.97
BTTS Y / N: 1.65 / 2.1
1X / 12 / X2: 1.19 / 1.25 / 2.05
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.95 / 3.75 / 2.05
Corner race 1/X/2: 1.37 / 9.5 / 3.35
Corners line, U/O: 9.5, 1.98 / 1.7
Cards line, U/O: 4.5, 1.65 / 2
Home/Away card split: not given

### f21 · Villarreal – Deportivo La Coruña
league: *(not given — research)* | kickoff: 05-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 1.48 / 4.6 / 6.25
O2.5 / U2.5: 1.65 / 2.15
BTTS Y / N: 1.72 / 2
1X / 12 / X2: 1.11 / 1.19 / 2.65
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.25 / 3.7 / 2.65
Corner race 1/X/2: 1.35 / 9.5 / 3.5
Corners line, U/O: 10.5, 1.7 / 2
Cards line, U/O: 4.5, 1.7 / 1.9
Home/Away card split: not given
