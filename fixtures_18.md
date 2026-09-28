# fixtures_18 — parsed from odds_18.xlsx (active sheet internally named "Today Odds"), 13-09-2026

Header row read from file (no assumed positions). Fields present: Date, Time,
Home, Away, 1, X, 2, O/U Line, Under, Over, GG, NG, DC 1X, DC 12, DC X2.

**Flags**
- No `league` or `venue` columns in the source header — both fields are
  absent from every row below and must come from Phase 2 research, not
  invented here.
- The workbook is saved in strict-OOXML conformance, which the normal
  reader opened as zero sheets (same symptom logged for odds_14.xlsx
  through odds_17.xlsx) — read directly from the sheet XML instead.
- Same narrow field set as fixtures_17: no cards line, no corners, no
  corner race, no team corners, no Asian handicap — just 1X2, the 2.5
  goals line, BTTS and double chance. `O2.5` is read from the `Over`
  column and `U2.5` from the `Under` column, matching the mapping used
  since fixtures_8; the goals line is 2.5 for all 14 rows.
- All 14 fixtures share the date 2026-09-13. Several kickoff times are
  floating-point artifacts (e.g. `17:29:59.9999999999968050`,
  `18:59:59.9999999999968050`) normalized to the clean minute (`17:30`,
  `19:00`).
- Double chance (DC 1X/12/X2) is populated for 13 of 14 fixtures —
  Benfica – Gil Vicente is missing DC 1X only (source cell blank),
  recorded as not given for that one price, not the whole fixture.
- Workbook holds 13 tabs: the active tab is "Today Odds" (sheetId 13,
  new this slate) plus `odds 17` (sheetId 12, consumed as fixtures_17),
  `odds_EXAMPLE` (template, sheetId 1), `odds_7` through `odds_14`
  (sheetIds 2–9, already consumed), `odds_16` (sheetId 10, already
  consumed as fixtures_16) and `Sheet1` (sheetId 11, unused). No
  `odds_15`, `odds_17` or `odds_18` named tab exists — each new slate's
  data lands in a renamed/rotating tab rather than a tab matching the
  file number.
- Cell A1 carries an author comment (destiny ofere): "Source: Screenshot
  2026-09-13 153715.png, Screenshot 2026-09-13 153641.png, Screenshot
  2026-09-13 153654.png, Screenshot 2026-09-13 153743.png, Screenshot
  2026-09-13 153629.png, Screenshot 2026-09-13 153726.png, Screenshot
  2026-09-13 153705.png, uploaded 2026-09-13" — logged for provenance
  though 1B mode does not re-derive from the images.
- Team names are recorded exactly as typed in the source, including the
  Italianized spellings ("Bayern Monaco", "Sporting Lisbona") and
  "Deportivo La Coruña" (UTF-8 confirmed at the byte level).
- No fixture is missing a 1/X/2 price, an O2.5/U2.5 price or a BTTS
  price this slate. 14 fixtures, above the 6-fixture triage threshold —
  Phase 1.5 applies to this slate.

---

### f1 · Levante – Barcelona
league: *(not given — research)* | kickoff: 2026-09-13 16:15 | venue: *(not given — research)*
1 / X / 2: 13 / 8 / 1.17
O2.5 / U2.5: 1.2 / 4
BTTS Y / N: 1.63 / 2.15
DC 1X / 12 / X2: 4.95 / 1.07 / 1.02

### f2 · Zwolle – Feyenoord
league: *(not given — research)* | kickoff: 2026-09-13 16:45 | venue: *(not given — research)*
1 / X / 2: 6 / 4.85 / 1.43
O2.5 / U2.5: 1.35 / 2.95
BTTS Y / N: 1.5 / 2.4
DC 1X / 12 / X2: 2.7 / 1.16 / 1.11

### f3 · Le Mans FC – Lens
league: *(not given — research)* | kickoff: 2026-09-13 17:15 | venue: *(not given — research)*
1 / X / 2: 5.1 / 4.1 / 1.62
O2.5 / U2.5: 1.53 / 2.35
BTTS Y / N: 1.55 / 2.3
DC 1X / 12 / X2: 2.25 / 1.22 / 1.16

### f4 · Manchester United – Manchester City
league: *(not given — research)* | kickoff: 2026-09-13 17:30 | venue: *(not given — research)*
1 / X / 2: 3 / 3.75 / 2.2
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.42 / 2.65
DC 1X / 12 / X2: 1.65 / 1.25 / 1.38

### f5 · SV 07 Elversberg – Bayern Monaco
league: *(not given — research)* | kickoff: 2026-09-13 17:30 | venue: *(not given — research)*
1 / X / 2: 14 / 8.5 / 1.15
O2.5 / U2.5: 1.11 / 5.5
BTTS Y / N: 1.47 / 2.5
DC 1X / 12 / X2: 5.25 / 1.06 / 1.01

### f6 · Napoli – Bologna
league: *(not given — research)* | kickoff: 2026-09-13 18:00 | venue: *(not given — research)*
1 / X / 2: 1.87 / 3.55 / 4.15
O2.5 / U2.5: 1.85 / 1.85
BTTS Y / N: 1.75 / 1.97
DC 1X / 12 / X2: 1.22 / 1.28 / 1.9

### f7 · Getafe – Deportivo La Coruña
league: *(not given — research)* | kickoff: 2026-09-13 18:30 | venue: *(not given — research)*
1 / X / 2: 2.7 / 2.8 / 3.05
O2.5 / U2.5: 2.8 / 1.38
BTTS Y / N: 2.2 / 1.6
DC 1X / 12 / X2: 1.37 / 1.42 / 1.45

### f8 · Arouca – Santa Clara
league: *(not given — research)* | kickoff: 2026-09-13 19:00 | venue: *(not given — research)*
1 / X / 2: 2.55 / 2.95 / 2.9
O2.5 / U2.5: 2.15 / 1.62
BTTS Y / N: 1.85 / 1.85
DC 1X / 12 / X2: 1.38 / 1.35 / 1.47

### f9 · Benfica – Gil Vicente
league: *(not given — research)* | kickoff: 2026-09-13 19:00 | venue: *(not given — research)*
1 / X / 2: 1.11 / 9 / 17
O2.5 / U2.5: 1.37 / 2.85
BTTS Y / N: 2.25 / 1.57
DC 1X / 12 / X2: not given / 1.04 / 6

### f10 · PSV Eindhoven – Sparta Rotterdam
league: *(not given — research)* | kickoff: 2026-09-13 20:00 | venue: *(not given — research)*
1 / X / 2: 1.13 / 9 / 13
O2.5 / U2.5: 1.13 / 5.25
BTTS Y / N: 1.52 / 2.35
DC 1X / 12 / X2: 1.01 / 1.04 / 5.5

### f11 · Brest – PSG
league: *(not given — research)* | kickoff: 2026-09-13 20:45 | venue: *(not given — research)*
1 / X / 2: 10 / 6.75 / 1.23
O2.5 / U2.5: 1.33 / 3.1
BTTS Y / N: 1.75 / 1.95
DC 1X / 12 / X2: 4.05 / 1.09 / 1.04

### f12 · Sassuolo – Juventus
league: *(not given — research)* | kickoff: 2026-09-13 20:45 | venue: *(not given — research)*
1 / X / 2: 5.5 / 3.85 / 1.63
O2.5 / U2.5: 1.72 / 2
BTTS Y / N: 1.72 / 2
DC 1X / 12 / X2: 2.25 / 1.25 / 1.14

### f13 · Real Sociedad – Atletico Madrid
league: *(not given — research)* | kickoff: 2026-09-13 21:00 | venue: *(not given — research)*
1 / X / 2: 3.3 / 3.55 / 2.1
O2.5 / U2.5: 1.57 / 2.25
BTTS Y / N: 1.47 / 2.5
DC 1X / 12 / X2: 1.7 / 1.28 / 1.32

### f14 · Famalicao – Sporting Lisbona
league: *(not given — research)* | kickoff: 2026-09-13 21:30 | venue: *(not given — research)*
1 / X / 2: 6.5 / 4.5 / 1.45
O2.5 / U2.5: 1.75 / 1.98
BTTS Y / N: 1.95 / 1.77
DC 1X / 12 / X2: 2.65 / 1.18 / 1.09
