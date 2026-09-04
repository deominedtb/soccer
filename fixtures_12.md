# fixtures_12 — parsed from odds_12.xlsx (sheet internally named "odds_11"), 04-09-2026

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
  time serialization (e.g. `18:59:59.9999999999968050`); normalized to
  the nearest minute below, no source ambiguity.
- Workbook contains six tabs: `odds_EXAMPLE` (sheetId 1, template row —
  not used), `odds_7` (sheetId 2, 28-08-2026 fixtures — not used, already
  consumed as fixtures_8), `odds_8` (sheetId 3, 29-08-2026 fixtures — not
  used, already consumed as fixtures_9), `odds_9` (sheetId 4, 30-08-2026
  fixtures — not used, already consumed as fixtures_10), `odds_10`
  (sheetId 5, 31-08-2026 fixtures — not used, already consumed as
  fixtures_11), and a sixth tab still internally named `odds_11`
  (sheetId 6) whose title row reads "MATCHES 04-09-2026" — today's slate,
  and the one read here. The file is named `odds_12.xlsx` and this is the
  twelfth Phase-1 run overall; the internal tab label is stale (a leftover
  from copy/paste) and was not used for numbering — output numbered
  fixtures_12 / progress_12 per the file sequence, same lag pattern seen
  in odds_10.xlsx and odds_11.xlsx.
- Only 6 fixtures on this sheet (`A4:AJ9`).
- `O2.5` below is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used for fixtures_8/9/10/11. The goals
  line is 2.5 for every fixture here.
- `Win/+2 Home` and `Win/+2 Away` are empty for every one of the 6 rows —
  recorded as not given throughout, not a per-fixture gap.
- No fixture is missing a 1X / 12 / X2 cell this slate.
- Home/away card-split columns are present only for f3 (Genoa – Como) and
  f5 (Ipswich Town – Liverpool); empty for f1, f2, f4, f6 — recorded as
  not given per fixture below, not guessed.
- Extra markets beyond the standard template exist in this file, same as
  prior slates: double chance (1X/12/X2), a 3-way price on the handicap
  line, a 3-way corner-race market, and per-team card O/U lines where
  given.
- Team names are recorded exactly as typed in the source (e.g. "Lione" =
  Lyon, "Stoccarda" = Stuttgart, "Colonia" = Koln — Italian-style naming
  carried over from earlier slates).
- All 6 fixtures share the same date, 04-09-2026, across competitions
  inferable from clubs (Ligue 1, Bundesliga, Serie A, LaLiga, Premier
  League) — league label left to Phase 2.

---

### f1 · Lione – Auxerre
league: *(not given — research)* | kickoff: 04-09-2026 19:00 | venue: *(not given — research)*
1 / X / 2: 1.45 / 4.5 / 7
O2.5 / U2.5: 1.6 / 2.25
BTTS Y / N: 1.77 / 1.97
1X / 12 / X2: 1.09 / 1.19 / 2.75
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.15 / 3.8 / 2.75
Corner race 1/X/2: 1.38 / 9.5 / 3.35
Corners line, U/O: 9.5, 1.98 / 1.7
Cards line, U/O: 3.5, 1.85 / 1.75
Home/Away card split: not given

### f2 · Stoccarda – Colonia
league: *(not given — research)* | kickoff: 04-09-2026 20:30 | venue: *(not given — research)*
1 / X / 2: 1.48 / 4.85 / 5.75
O2.5 / U2.5: 1.33 / 3.1
BTTS Y / N: 1.45 / 2.6
1X / 12 / X2: 1.13 / 1.17 / 2.6
Win-or-+2 (Home/Away): not given
AH line: -1
EH 3-way (1/X/2 on AH line): 2.15 / 4.15 / 2.6
Corner race 1/X/2: 1.33 / 9.5 / 3.6
Corners line, U/O: 10.5, 1.75 / 1.95
Cards line, U/O: 3.5, 1.7 / 1.9
Home/Away card split: not given

### f3 · Genoa – Como
league: *(not given — research)* | kickoff: 04-09-2026 20:45 | venue: *(not given — research)*
1 / X / 2: 5.25 / 3.35 / 1.77
O2.5 / U2.5: 2 / 1.75
BTTS Y / N: 1.87 / 1.87
1X / 12 / X2: 2.05 / 1.3 / 1.15
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.05 / 3.6 / 3.05
Corner race 1/X/2: 3.05 / 9 / 1.45
Corners line, U/O: 8.5, 1.8 / 1.8
Cards line, U/O: 3.5, 2 / 1.63
Home card line, U/O: 1.5, 2.15 / 1.5
Away card line, U/O: 1.5, 2.1 / 1.55

### f4 · Real Betis – Real Madrid
league: *(not given — research)* | kickoff: 04-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 6.25 / 5 / 1.43
O2.5 / U2.5: 1.35 / 3
BTTS Y / N: 1.52 / 2.4
1X / 12 / X2: 2.8 / 1.16 / 1.11
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.8 / 4.1 / 2.05
Corner race 1/X/2: 3.15 / 9 / 1.43
Corners line, U/O: 10.5, 1.75 / 1.95
Cards line, U/O: 4.5, 1.75 / 1.85
Home/Away card split: not given

### f5 · Ipswich Town – Liverpool
league: *(not given — research)* | kickoff: 04-09-2026 21:00 | venue: *(not given — research)*
1 / X / 2: 5.75 / 4.7 / 1.5
O2.5 / U2.5: 1.37 / 2.9
BTTS Y / N: 1.48 / 2.5
1X / 12 / X2: 2.55 / 1.18 / 1.13
Win-or-+2 (Home/Away): not given
AH line: +1
EH 3-way (1/X/2 on AH line): 2.55 / 4.05 / 2.2
Corner race 1/X/2: 3.25 / 9.5 / 1.4
Corners line, U/O: 9.5, 2 / 1.7
Cards line, U/O: 4.5, 1.57 / 2.15
Home card line, U/O: 2.5, 1.55 / 2.1
Away card line, U/O: 1.5, 2 / 1.6

### f6 · PSG – Monaco
league: *(not given — research)* | kickoff: 04-09-2026 21:05 | venue: *(not given — research)*
1 / X / 2: 1.35 / 5.5 / 7.5
O2.5 / U2.5: 1.32 / 3.15
BTTS Y / N: 1.57 / 2.3
1X / 12 / X2: 1.08 / 1.14 / 3.15
Win-or-+2 (Home/Away): not given
AH line: -2
EH 3-way (1/X/2 on AH line): 3 / 4.4 / 1.87
Corner race 1/X/2: 1.3 / 9.5 / 3.95
Corners line, U/O: 9.5, 1.8 / 1.85
Cards line, U/O: 3.5, 1.8 / 1.8
Home/Away card split: not given
