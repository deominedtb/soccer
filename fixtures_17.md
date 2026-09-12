# fixtures_17 — parsed from odds_17.xlsx (active sheet internally named "odds 17"), 12-09-2026

Header row read from file (no assumed positions). Fields present: Date, Time,
Home, Away, 1, X, 2, O/U Line, Under, Over, GG, NG, DC 1X, DC 12, DC X2.

**Flags**
- No `league` or `venue` columns in the source header — both fields are
  absent from every row below and must come from Phase 2 research, not
  invented here.
- The workbook is saved in strict-OOXML conformance, which the normal
  reader opened as zero sheets (same symptom logged for odds_14.xlsx,
  odds_15.xlsx and odds_16.xlsx) — read directly from the sheet XML
  instead.
- Narrower field set than the last several slates: no cards line, no
  corners, no corner race, no team corners, no Asian handicap of any kind
  this time — just 1X2, the 2.5 goals line, BTTS and double chance.
  `O2.5` is read from the `Over` column and `U2.5` from the `Under`
  column, matching the mapping used since fixtures_8; the goals line is
  2.5 for all 33 rows.
- Two kickoff slots only: `13:30:00.000` (clean) and
  `15:59:59.9999999999968050` (floating-point artifact), normalized to
  `16:00`. All 33 fixtures share the date 2026-09-12.
- Double chance (DC 1X/12/X2) is populated for 9 of 33 fixtures only
  (f1–f3, f15–f19, f26–f27) — empty for the other 24, recorded as not
  given per fixture below, not a blanket gap.
- Workbook holds 12 tabs: the active tab is named "odds 17" (sheetId 12,
  note the space, not an underscore) plus `odds_EXAMPLE` (template, sheetId
  1), `odds_7` through `odds_14` (sheetIds 2–9, already consumed through
  fixtures_15), `odds_16` (sheetId 10, already consumed as fixtures_16)
  and `Sheet1` (sheetId 11, unused). No `odds_15` or `odds_17` tab exists —
  consistent with each new slate's tab being renamed in place rather than
  duplicated, though this is the first slate where the renamed tab kept a
  space instead of an underscore.
- Cell A1 carries an author comment (destiny ofere): "Source: Screenshot
  2026-09-12 115142.png, Screenshot 2026-09-12 115215.png, Screenshot
  2026-09-12 115101.png, Screenshot 2026-09-12 115206.png, Screenshot
  2026-09-12 115111.png, Screenshot 2026-09-12 115128.png, uploaded
  2026-09-12" — logged for provenance though 1B mode does not re-derive
  from the images.
- Team names are recorded exactly as typed in the source, including
  suffixes ("Stockport County FC", "Tranmere Rovers FC", "Chesterfield
  FC", "York City FC", "Barnet FC", "Blackpool FC", "Bromley FC",
  "Bristol Rovers", "Bristol City").
- No fixture is missing a 1/X/2 price, an O2.5/U2.5 price or a BTTS
  price this slate. 33 fixtures, well above the 6-fixture triage
  threshold — Phase 1.5 applies to this slate.

---

### f1 · Bolton – Cardiff
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 2.55 / 3.6 / 2.5
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.45 / 2.6
DC 1X / 12 / X2: 1.5 / 1.25 / 1.48

### f2 · Derby County – Birmingham City
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 3.5 / 3.25 / 2.1
O2.5 / U2.5: 2 / 1.73
BTTS Y / N: 1.8 / 1.9
DC 1X / 12 / X2: 1.7 / 1.3 / 1.27

### f3 · West Bromwich – Queens Park Rangers
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 2.2 / 3.25 / 3.25
O2.5 / U2.5: 1.8 / 1.9
BTTS Y / N: 1.65 / 2.1
DC 1X / 12 / X2: 1.3 / 1.3 / 1.63

### f4 · Crawley – Cheltenham Town
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 2.45 / 3.5 / 2.55
O2.5 / U2.5: 1.57 / 2.25
BTTS Y / N: 1.47 / 2.4
DC 1X / 12 / X2: not given

### f5 · Grimsby Town – Bristol Rovers
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 2.35 / 3.5 / 2.65
O2.5 / U2.5: 1.7 / 2
BTTS Y / N: 1.58 / 2.15
DC 1X / 12 / X2: not given

### f6 · Leyton Orient – Wycombe Wanderers
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 2.35 / 3.45 / 2.7
O2.5 / U2.5: 1.68 / 2
BTTS Y / N: 1.58 / 2.2
DC 1X / 12 / X2: not given

### f7 · Notts County – Bradford City
league: *(not given — research)* | kickoff: 2026-09-12 13:30 | venue: *(not given — research)*
1 / X / 2: 3 / 3.25 / 2.25
O2.5 / U2.5: 2 / 1.7
BTTS Y / N: 1.8 / 1.88
DC 1X / 12 / X2: not given

### f8 · Sheffield Wednesday – Wigan
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.58 / 4.05 / 4.9
O2.5 / U2.5: 1.48 / 2.4
BTTS Y / N: 1.55 / 2.25
DC 1X / 12 / X2: not given

### f9 · Stockport County FC – Leicester City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.75 / 3.95 / 3.8
O2.5 / U2.5: 1.48 / 2.4
BTTS Y / N: 1.5 / 2.4
DC 1X / 12 / X2: not given

### f10 · Wimbledon – Doncaster Rovers
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.55 / 3.35 / 2.5
O2.5 / U2.5: 1.9 / 1.77
BTTS Y / N: 1.73 / 1.95
DC 1X / 12 / X2: not given

### f11 · Rotherham United – Salford City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.55 / 3.6 / 2.4
O2.5 / U2.5: 1.7 / 2
BTTS Y / N: 1.58 / 2.15
DC 1X / 12 / X2: not given

### f12 · Shrewsbury Town – Northampton Town
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.55 / 3.1 / 2.7
O2.5 / U2.5: 2.25 / 1.55
BTTS Y / N: 1.92 / 1.72
DC 1X / 12 / X2: not given

### f13 · Walsall – Rochdale
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.7 / 3.65 / 4.35
O2.5 / U2.5: 1.67 / 2.05
BTTS Y / N: 1.65 / 2.05
DC 1X / 12 / X2: not given

### f14 · York City FC – Swindon Town
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.53 / 4.3 / 4.85
O2.5 / U2.5: 1.43 / 2.6
BTTS Y / N: 1.5 / 2.3
DC 1X / 12 / X2: not given

### f15 · Blackburn Rovers – Millwall
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.6 / 3.3 / 2.6
O2.5 / U2.5: 1.9 / 1.8
BTTS Y / N: 1.72 / 2
DC 1X / 12 / X2: 1.45 / 1.3 / 1.45

### f16 · Charlton Athletic – Portsmouth
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.7 / 3.15 / 2.65
O2.5 / U2.5: 2.1 / 1.65
BTTS Y / N: 1.85 / 1.85
DC 1X / 12 / X2: 1.45 / 1.33 / 1.43

### f17 · Middlesbrough – Norwich
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.85 / 3.85 / 3.75
O2.5 / U2.5: 1.55 / 2.3
BTTS Y / N: 1.53 / 2.35
DC 1X / 12 / X2: 1.25 / 1.23 / 1.9

### f18 · Preston North End – Lincoln City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.3 / 3.4 / 2.9
O2.5 / U2.5: 1.78 / 1.93
BTTS Y / N: 1.65 / 2.1
DC 1X / 12 / X2: 1.38 / 1.3 / 1.57

### f19 · Southampton – Bristol City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.65 / 4.1 / 4.45
O2.5 / U2.5: 1.55 / 2.3
BTTS Y / N: 1.6 / 2.2
DC 1X / 12 / X2: 1.18 / 1.2 / 2.15

### f20 · Barnet FC – Accrington Stanley
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.45 / 4.35 / 6
O2.5 / U2.5: 1.48 / 2.45
BTTS Y / N: 1.6 / 2.1
DC 1X / 12 / X2: not given

### f21 · Colchester United – Crewe Alexandra
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.6 / 3.15
O2.5 / U2.5: 1.63 / 2.15
BTTS Y / N: 1.53 / 2.25
DC 1X / 12 / X2: not given

### f22 · Gillingham – Tranmere Rovers FC
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.5 / 3 / 2.8
O2.5 / U2.5: 1.95 / 1.75
BTTS Y / N: 1.7 / 1.95
DC 1X / 12 / X2: not given

### f23 · Newport County – Fleetwood Town
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 3.1 / 3.5 / 2.05
O2.5 / U2.5: 1.77 / 1.92
BTTS Y / N: 1.65 / 2.05
DC 1X / 12 / X2: not given

### f24 · Oldham Athletic – Chesterfield FC
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.35 / 3.3
O2.5 / U2.5: 1.8 / 1.9
BTTS Y / N: 1.65 / 2.05
DC 1X / 12 / X2: not given

### f25 · Port Vale – Exeter City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.3 / 3.35
O2.5 / U2.5: 1.97 / 1.73
BTTS Y / N: 1.78 / 1.85
DC 1X / 12 / X2: not given

### f26 · Swansea – Burnley
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.05 / 3.4 / 3.5
O2.5 / U2.5: 1.83 / 1.87
BTTS Y / N: 1.7 / 2.05
DC 1X / 12 / X2: 1.28 / 1.3 / 1.72

### f27 · Watford – Stoke City
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.3 / 3.35 / 3
O2.5 / U2.5: 1.83 / 1.87
BTTS Y / N: 1.68 / 2.05
DC 1X / 12 / X2: 1.35 / 1.3 / 1.58

### f28 · Blackpool FC – Bromley FC
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.65 / 3.8 / 4.65
O2.5 / U2.5: 1.6 / 2.15
BTTS Y / N: 1.62 / 2.1
DC 1X / 12 / X2: not given

### f29 · Cambridge United – Reading FC
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 2.6 / 3.3 / 2.5
O2.5 / U2.5: 1.92 / 1.75
BTTS Y / N: 1.75 / 1.95
DC 1X / 12 / X2: not given

### f30 · Mansfield Town – Huddersfield
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 3.35 / 3.6 / 1.95
O2.5 / U2.5: 1.55 / 2.25
BTTS Y / N: 1.5 / 2.35
DC 1X / 12 / X2: not given

### f31 · Milton Keynes Dons – Peterborough United
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.9 / 3.8 / 3.4
O2.5 / U2.5: 1.5 / 2.4
BTTS Y / N: 1.47 / 2.45
DC 1X / 12 / X2: not given

### f32 · Oxford United – Burton Albion
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.8 / 3.7 / 3.8
O2.5 / U2.5: 1.67 / 2.05
BTTS Y / N: 1.63 / 2.1
DC 1X / 12 / X2: not given

### f33 · Plymouth Argyle – Barnsley
league: *(not given — research)* | kickoff: 2026-09-12 16:00 | venue: *(not given — research)*
1 / X / 2: 1.62 / 4.1 / 4.45
O2.5 / U2.5: 1.45 / 2.5
BTTS Y / N: 1.5 / 2.35
DC 1X / 12 / X2: not given
