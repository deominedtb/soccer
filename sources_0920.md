# sources_0920

Slate of 20 fixtures across the top-five European leagues, 2026-09-20.
Phase 1 mode 1B from slate.7.xlsx (tab "Slate 7", read from the sheet XML).

## Triage

Searches spent: 0 of 6. Everything below is the standing ESPN data
pipeline (as in sources_0919.md), not a search.

- ESPN standings, `site.web.api.espn.com/apis/v2/sports/soccer/{eng.1,esp.1,ita.1,ger.1,fra.1}/standings?season={2026,2025,2024,2023}` — league matches played per club for 2026-27 (matchday and sample depth); the 2026 list against the 2025 list for promoted and relegated clubs; the 2024 and 2023 lists for how long each promoted club was out of the division.
- ESPN core events, `sports.core.api.espn.com/v2/sports/soccer/leagues/{slug}/events?dates=20260701-20260919` and each event's own competitor and status record, for slugs `ger.dfb_pokal`, `eng.league_cup`, `ita.coppa_italia`, `esp.copa_del_rey`, `fra.coupe_de_france`, `uefa.champions`, `uefa.champions_qual`, `uefa.europa`, `uefa.europa_qual`, `uefa.europa.conf`, `uefa.europa.conf_qual`, `uefa.super_cup`, `ger.super_cup`, `fra.super_cup`, `ita.super_cup`, `esp.super_cup`, `eng.charity` — competitive matches outside the league (604 completed events read). `esp.copa_del_rey`, `fra.coupe_de_france`, `uefa.europa.conf`, `ita.super_cup` and `esp.super_cup` returned no events in the range.
- `site.api.espn.com` scoreboard host not used.
- Archive read for the yield and coach-change signals: progress_0917.md to progress_0919.md; fx_0914_f1, f4, f5; fx_0915_f3, f5, f7; fx_0916_f1, f3, f7; fx_0917_f2, f3, f5, f6, f8; fx_8_f3, f5, f6; fx_9_f7, f9, f18; fx_10_f4, f6; fx_11_f1, f2, f3; fx_12_f3, f4; fx_13_f2, f3, f6, f7, f8, f9, f19; fx_14_f3, f4, f5; fx_15_f4, f5; fx_16_f1, f2, f3, f4 (Section A coach facts only); triage_0919.md for scoring conventions.

## f1 — Fiorentina – Napoli (T1)
- Standing ESPN pipeline (see baselines_0920.md) for every rate, result, corner, card, foul, shot and referee figure on the card: 45 Serie A 2026–27 matches, 380 Serie A 2025–26 matches, 604 cup/European matches, all read from `site.web.api.espn.com/.../summary?event={id}`.
- Understat `getLeagueData/Serie_A/{2025,2026}` — xG, npxG, xGA, PPDA, deep completions for both clubs, both seasons.
- Wikipedia, 2026–27 ACF Fiorentina season — full summer transfer list with fees, manager change dates (Grosso to 6 September, Vanoli from 7 September).
- Wikipedia, 2026–27 SSC Napoli season — full summer transfer list with fees, results, Allegri appointment.
- ESPN, "Napoli appoint Massimiliano Allegri as new manager, replaces Antonio Conte" (3 July 2026, three-year deal to 2029).
- Corriere dello Sport / Sky Sport / Firenze Post, Serie A giornata 5 designations (16 September 2026) — Doveri appointed, Gariglio on VAR.
- Football Italia / Goal.com / Yahoo Sports, 19–20 September 2026 — Napoli injury list (Meret, Buongiorno, Marianucci, McTominay, Alisson Santos, Giovane, Spinazzola), Anguissa recovered; Fiorentina's Parisi out.
- Taipei Times / Viola Nation, 8–9 September 2026 — Grosso dismissal and Vanoli return, and Vanoli's November 2025 first spell.

## f2 — Getafe – Málaga (T1)
- Standing ESPN pipeline for every rate, result, corner, card, foul, shot and referee figure: 64 LaLiga 2026–27 matches, 380 LaLiga 2025–26, 468 LaLiga 2 2025–26 (for Málaga's second-tier record and the LaLiga 2 baseline), 604 cup/European matches (Getafe's Conference League play-off v Partizan).
- Understat `getLeagueData/La_liga/{2025,2026}` — xG, npxG, xGA, PPDA, deep for Getafe both seasons and Málaga 2026–27. **No LaLiga 2 coverage exists, so Málaga have no 2025–26 xG.**
- ESPN standings `esp.2?season=2025` — LaLiga 2 final table: Racing Santander 82, Deportivo 77, Almería 74, Málaga 73 from 42 matches; Málaga promoted via play-off.
- Málaga CF official match page (malagacf.com, J7 v Getafe) — kickoff, venue, referee Javier Alberola Rojas, VAR Juan Luis Pulido Santana, 23-man squad named Saturday.
- Iusport, Primera División Sunday designations — Alberola Rojas confirmed for Getafe–Málaga.
- FútbolFantasy, Málaga mercado verano 2026 — full altas/bajas list with fees and status.
- Wikipedia / classementlaliga / LaLiga transfers — Getafe's window: Luis Milla €4m in, Rodrigo Gomes on loan from Wolves, Enes Ünal €5m to Beşiktaş, Juan Berrocal free to Málaga.
- Sports Mole / The Stats Zone match preview, 19–20 September 2026 — injury and suspension lists for both clubs, home/away run, league positions.
- Radio Marca Málaga / El Desmarque — Funes and Loren Juarros contract renewals after promotion.

## f4 — Bournemouth – Liverpool (T2, researched at full T1 depth on your instruction)
- Standing ESPN pipeline: 46 Premier League 2026–27 matches, 380 2025–26, 604 cup/European matches (Bournemouth's EFL Cup tie and Europa League win at Real Sociedad; Liverpool's EFL Cup tie and Champions League win over Atlético).
- Understat `getLeagueData/EPL/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Sports Mole, "Liverpool summer transfers and net spend" — full ins/outs with fees; £246.9m spend, £700k income.
- Sports Mole, "Bournemouth summer transfers and net spend" — full ins/outs with fees; £54m spend, £0 income.
- Wikipedia, Marco Rose — appointment as Bournemouth head coach, work began 1 June 2026, backroom staff.
- ESPN match preview (Bournemouth v Liverpool, 2026–27 MW5) — kickoff, venue, referee Michael Oliver, VAR Craig Pawson, injury lists and predicted lineups for both clubs.
- Empire of the Kop / This Is Anfield, 14–19 September 2026 — referee appointment confirmation and assistants.
- **Unresolved contradiction logged:** the Bournemouth window records Enes Ünal leaving free to Getafe; the Getafe window records Ünal leaving for Beşiktaş at €5m in the same summer. Both are reported on the card; neither is preferred.

## f6 — Man City – Sunderland (T1)
- Standing ESPN pipeline: 46 Premier League 2026–27, 380 2025–26, 604 cup/European matches (City's Champions League win at Porto, EFL Cup v Norwich, Community Shield v Arsenal; Sunderland's EFL Cup v Hull and Europa League v AZ Alkmaar).
- Understat `getLeagueData/EPL/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Sports Mole, "Man City summer transfers and net spend" — full ins/outs with fees; £455.8m spend, £307.2m income.
- Sports Mole, "Sunderland summer transfers and net spend" — full ins/outs with fees; £58.3m spend, £26.9m income, 5 in and 20 out.
- Sunderland Echo / OneFootball — Le Bris's stated target of three or four signings, and the £161m/15-player promotion window of summer 2025 for contrast.
- Last Word on Sports / Sports Mole / mancity.com team news, 19 September 2026 — referee Robert Jones, Foden's three-match ban, Sunderland's Diarra and Mundle out and Reinildo suspended.
- Maresca's appointment (29 June 2026, three years, ~£17m compensation to Chelsea) carried from this board's own card fx_8_f5, not re-sourced.

## f7 — Frosinone – Como (T1)
- Standing ESPN pipeline: 45 Serie A 2026–27, 380 2025–26, 390 Serie B 2025–26 (Frosinone's second-tier record and the Serie B baseline), 604 cup/European matches (Frosinone's two Coppa Italia ties; Como's 4–1 Champions League win over RB Leipzig).
- ESPN standings `ita.2?season=2025` — Serie B final table: Venezia 82, Frosinone 81, Monza 76 from 38; Frosinone promoted as runners-up.
- Understat `getLeagueData/Serie_A/{2025,2026}` — Como both seasons, Frosinone 2026–27 only. **No Serie B coverage, so Frosinone have no 2025–26 xG.**
- Il Fatto Quotidiano / Lottomatica Sport guide to Frosinone 2026–27 — Alvini retained after promotion; full signing list by position (Desplanches, Akpoguma, Cittadini, Calvani, Fayed, Grillitsch, Schmid, Raimondo, Hasa, Zerbin, El Azzouzi, Masini) and departures.
- Calciomercato.com / Sky Sport — Como's window: Kean €10m loan with €25m obligation plus €5m bonuses to 2031, Chalobah €30m+, Nico Paz €60m permanent from Real Madrid, Liberali €6m, four paid loans.
- Eurosport / TuttoFantacalcio / PazziDiFanta, 19–20 September 2026 — probable lineups, venue Stadio Benito Stirpe, 15:00 kickoff, no suspensions, Grillitsch and Terzić out for Frosinone, Addai out for Como.
- Corriere dello Sport / Sky Sport, Serie A giornata 5 designations (16 September 2026) — Chiffi appointed.

## f9 — Bayer Leverkusen – RB Leipzig (T1)
- Standing ESPN pipeline: 33 Bundesliga 2026–27, 306 2025–26, 604 cup/European matches (both clubs' DFB-Pokal ties; Leverkusen's Europa League win over Celje; Leipzig's 1–4 at Como).
- Understat `getLeagueData/Bundesliga/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Bundesliga.com official announcement — **Carles Martínez Novell appointed 4 June 2026, two-year deal to June 2028, starting 1 July, from Toulouse, replacing Kasper Hjulmand after nine months and 48 matches.** This resolves the archive conflict flagged in triage_0920.md: fx_13_f2 wrongly named Ole Werner as Leverkusen's departing coach; Werner was Leipzig's, as fx_15_f4 recorded.
- Demichelis's appointment (24 June 2026, €2.5m release clause at Mallorca, contract to June 2028) carried from this board's own card fx_15_f4, not re-sourced.
- DFB Datencenter / fussballtransfers.com referee listing — Robert Schröder appointed, Johann Pfeifer VAR, Harm Osmers fourth official.
- Yahoo Sports / FotMob preview, 19–20 September 2026 — injury lists for both clubs and predicted lineups; venue BayArena, 15:30 kickoff.
- OneFootball / betinf Bundesliga transfer listings — Leverkusen: Hincapié €40m to Arsenal, Grimaldo €20m to Atlético, Doué ~€30m (to €37.5m) from Strasbourg, Gutiérrez €26m from Napoli, Moreira €29.5m from Lyon; Leipzig: Gruda, Reitz, Thomas, Koné, Sani named.
- **Gap logged:** no published fee was obtainable for any RB Leipzig summer arrival, nor their outgoing list. Nothing estimated.

## f10 — Atlético Madrid – Real Madrid (T1)
- Standing ESPN pipeline: 64 LaLiga 2026–27, 380 2025–26, 604 cup/European matches (Atlético's 1–2 at Liverpool and Real Madrid's 2–1 v Inter, both Champions League matchday 1).
- Understat `getLeagueData/La_liga/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- VAVEL / Prensa Libre / Teleprensa, 19 September 2026 — referee Miguel Ángel Ortiz Arias (Madrid committee), the first ever appointed to this derby after the CTA broke its territoriality rule; venue Riyadh Air Metropolitano, 16:15 kickoff.
- Yahoo Sports / Al Jazeera / Forbes match previews, 19 September 2026 — injury and doubt lists (Julián Álvarez, Sørloth, Barrios for Atlético; Militão, Rodrygo, Mendy for Real Madrid), expected lineups, Mbappé on seven league goals.
- DAZN / Fichajes.com transfer listings — Atlético in: Hjulmand (~€40m from Sporting, to 2031), Cristian Romero, Kang-In Lee, Grimaldo (€20m from Leverkusen); out: Griezmann free to Orlando City, Molina, Ruggeri, Almada. Real Madrid in: Konaté (released by Liverpool), Cucurella, Dumfries, Bernardo Silva (free from Manchester City).
- Mourinho's appointment (Arbeloa dismissed 9 June 2026, Mourinho announced 11 June on a deal to 2029) carried from this board's own card fx_10_f6, not re-sourced.
- **Gap logged:** no fee obtainable for Cucurella, Dumfries or Cristian Romero, nor for most of Atlético's departures. Nothing estimated.

## f12 — Fulham – Manchester United (T1)
- Standing ESPN pipeline: 46 Premier League 2026–27, 380 2025–26, 604 cup/European matches (Fulham's two EFL Cup ties; United's 4–0 Champions League win over Sabah and 2–3 EFL Cup exit to Brighton from 2–0 up).
- Understat `getLeagueData/EPL/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Sports Mole, "Man United summer transfers and net spend" — full ins/outs with fees; £163m spend, £38m income; Baleba £70m, Santos £50m, Tielemans £35m in, Højlund £38m to Napoli.
- Sports Mole, "Fulham summer transfers and net spend" — full ins/outs with fees; £78.1m spend, £0 income; Gonzalo García £34.3m, Shea Charles £30m, Palacios £8.6m; Arbeloa replaced Marco Silva.
- Read Man Utd / Al Jazeera / RotoWire preview, 18–19 September 2026 — referee Peter Bankes, assistants Cook and James, fourth official Chris Kavanagh; injury lists for both clubs; venue Craven Cottage, 16:30 BST.
- Arbeloa's 7 July 2026 Fulham appointment carried from this board's own card fx_0915_f5; his 9 June dismissal by Real Madrid from fx_10_f6. Carrick's January 2026 arrival and permanent contract from fx_15_f5.

## f13 — Schalke 04 – SV Elversberg (T2, researched at full T1 depth on your instruction)
- Standing ESPN pipeline: 33 Bundesliga 2026–27, 306 2. Bundesliga 2025–26 (both clubs' promotion seasons and the 2. Bundesliga baseline), 604 cup matches (both clubs' DFB-Pokal ties).
- ESPN standings `ger.2?season=2025` — Schalke 70, Elversberg 62, Paderborn 62 from 34; Schalke champions, Elversberg runners-up.
- Understat `getLeagueData/Bundesliga/2026` — xG, npxG, xGA, PPDA, deep for both clubs, 2026–27 only. **No 2. Bundesliga coverage, so neither club has any 2025–26 xG.**
- DFB Datencenter match page (Bundesliga 2026-27, 4. Spieltag) — referee Dr. Robin Braun, VAR Patrick Hanslbauer, assistants Heft and Osmanagic, fourth official Dr. Florian Exner; Veltins-Arena, 17:30.
- Sportschau / neunzigplus / schalketotal transfer summaries — Schalke: Tanaka €1m, Dina Ebimbe €800k, Adamu €800k, Wöber free, Gosens and Hwang on loan; €200k income. Elversberg: €12.1m invested, Cole Campbell €6m (club record, from Dortmund), Krattenmacher €2m, Poręba €1.6m.
- Wikipedia, Horst Steffen / neunzigplus "Fünf Klubs, fünf neue Trainer" — Vincent Wagner, 40, remains Elversberg head coach after the promotion; Muslić remains at Schalke (corroborating fx_16_f1).
- **Gap logged:** no injury or suspension information was obtainable for either club from any source reached. Nothing invented.

## f15 — Deportivo A Coruña – Real Betis (T1)
- Standing ESPN pipeline: 64 LaLiga 2026–27, 380 2025–26, 468 LaLiga 2 2025–26 (Deportivo's promotion season and the LaLiga 2 baseline), 604 cup/European matches (Betis's 3–2 Champions League win at Lille).
- ESPN standings `esp.2?season=2025` — Racing Santander 82, Deportivo 77 from 42; Deportivo promoted automatically as runners-up.
- Understat `getLeagueData/La_liga/{2025,2026}` — Betis both seasons, Deportivo 2026–27 only. **No LaLiga 2 coverage, so Deportivo have no 2025–26 xG.**
- Riazor.org / Jornada Perfecta / Iusport — referee César Soto Grado (Rioja), VAR José López Toca (Cantabria); 18:30 kickoff at Estadio Abanca-Riazor.
- El Español (Quincemil) / Betfair / VAVEL — Deportivo's window: Leo Román €9m from Mallorca (GK), Aubameyang ~€1m from Marseille, Angeliño on loan from Roma, José María Giménez, Adama Traoré, Marc Casadó, Amatucci (Fiorentina), Asp Jensen, Gijselhart, Ede Bright; Antonio Hidalgo's contract renewed automatically on promotion.
- La Nación / Bolavip preview, 19 September 2026 — Angeliño sent off v Sevilla on Wednesday and suspended; league positions.
- **Gaps logged:** Real Betis's entire summer 2026 transfer ledger was not obtainable from any source reached; no injury list beyond Angeliño's suspension was found for either club; fees undisclosed for four Deportivo arrivals and all departures. Nothing estimated.

## f16 — Villarreal – Levante (T2, researched at full T1 depth on your instruction)
- Standing ESPN pipeline: 64 LaLiga 2026–27, 380 2025–26, 604 cup/European matches (Villarreal's 2–3 Champions League defeat at Borussia Dortmund).
- Understat `getLeagueData/La_liga/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- VAVEL España, "El Levante UD visita Villarreal: convocatoria y árbitro" (19 September 2026) — referee Mateo Busquets Ferrer (Balearic), VAR Álvaro Moreno, full officiating team; Levante's 25-man squad and the three absentees (Etta Eyong, Sotelo, Primo).
- Comuniate / Comunio / Jornada Perfecta / Betfair previews — 18:30 kickoff at Estadio de la Cerámica, Villarreal's probable XI, Sotelo's knee sprain and Etta Eyong's rectus femoris injury.
- Fichajes.com / FútbolFantasy — Villarreal out: Terrats €2.5m to Getafe (8 July), Pedraza free to Lazio (3 July), Etta Eyong to Levante, Requena on loan to Levante (17 July); in: Andero Kaares, plus loan returns Akhomach and Rafa Marín; Parejo and Partey not replaced.
- FútbolFantasy, Héctor Rodas market summary (2 September 2026) — Levante's salary-limit-constrained window; in: Etta Eyong, Vencedor, Raghouber, Abed, Ryan, Ratkov and others; out: Cabello, Víctor Fernández, Paco Cortés, Lozano, Pastor and others.
- Íñigo Pérez's 1 June 2026 appointment carried from this board's own card fx_0914_f5; Luís Castro's December 2025 appointment from fx_9_f9.
- **Gaps logged:** no fee obtainable for any Levante transfer, in or out, nor for Etta Eyong's move; no Villarreal injury list found; Villarreal's incoming business beyond one named signing and two loan returns could not be established. Nothing estimated.

## f18 — Marseille – Paris Saint-Germain (T2, coverage floor; researched at full T1 depth on your instruction)
- Standing ESPN pipeline: 42 Ligue 1 2026–27, 305 of 306 2025–26 (the known ESPN gap, see baselines_0920.md), 604 cup/European matches (PSG's UEFA Super Cup, Trophée des Champions and 6–1 Champions League win; Marseille's 1–4 Europa League defeat at Beşiktaş).
- Understat `getLeagueData/Ligue_1/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Foot Africa / Football Club de Marseille / Paris-Supporters, 15–19 September 2026 — referee François Letexier, assistants Mugnier and Rahmouni, VAR Bastien Dechepy and Wilfried Bien; 20:45 kickoff at the Orange Vélodrome.
- CulturePSG / Paris-Supporters, 18 September 2026 — "at least four" PSG absences, Hakimi's right-thigh lesion sustained at Brest; Marseille's Kondogbia and Nnadi injured since late August.
- Dicodusport / CulturePSG / PSG Fanzone transfer tables — PSG in: Akliouche €50m (Monaco, 6 August), Ferran Torres €48.5m (Barcelona), Godts €45m (Ajax), Digne €7m (Aston Villa), Longoni free (Milan); out: Gonçalo Ramos (Milan), Kang-in Lee (Atlético), Kolo Muani (Juventus), €38–70m aggregate; Luis Enrique extended to 2030.
- Maxifoot, Marseille transfer table — €126.9m of confirmed departures (Greenwood €39m, Medina €23m, Timber €20m, Weah €14.4m, Traoré €7.7m, Rulli €3.5m, Balerdi on loan); **no confirmed arrival listed**.
- Génésio's appointment as Marseille's third coach in five months carried from this board's own cards fx_0917_f3 and fx_16_f3.
- **Gaps and contradictions logged:** Marseille's incoming window could not be established at all; PSG's absence list beyond Hakimi was not obtainable; the €38–70m departure figure is an aggregate range, not split per player; and the same Marseille source records Timothy Weah leaving for Juventus on 1 July while this weekend's published probable XI names him at right-back. Nothing estimated or resolved by preference.

## f19 — Milan – Lecce (T2, researched at full T1 depth on your instruction)
- Standing ESPN pipeline: 45 Serie A 2026–27, 380 2025–26, 604 cup/European matches (Milan's 0–2 Europa League defeat to Benfica at San Siro; Lecce's 0–2 Coppa Italia exit at Palermo).
- Understat `getLeagueData/Serie_A/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- AC Milan official announcement / Il Post / Sky Sport / ESPN (16 June 2026) — Rúben Amorim appointed on a three-year contract to 30 June 2029 after leaving Manchester United, replacing Allegri.
- Calcio e Finanza, "Quanto ha speso il Milan sul mercato 2026" (2 September 2026) — ~€81.13m of new-signing costs against ~€74.75m outgoing effect, net −€6.38m; Leão €38m with ~€27m capital gain.
- PianetaMilan / MilanNews24 transfer tables — Gonçalo Ramos ~€70m from PSG to 2031, Mario Gila ~€30m with bonuses from Lazio, Kostic, Diawara, Moreira, Guernier; out Füllkrug, Bennacer, Odogu, Athekame.
- CalcioLecce / US Lecce / PianetaLecce — Lecce's €7.40m outlay on ten players, the lowest in Serie A; in Bleve, Ilić, Dembélé, Fatah (three on loan with option from Torino), Monteiro, Geubbels; out Früchtl and Samooja.
- Eurosport / TuttoFantacalcio / MilanNews, 19–20 September 2026 — probable lineups, 20:45 kickoff at the Meazza; Milan no injuries and no suspensions, Lecce missing Berisha, Gandelman and Geubbels.
- Corriere dello Sport / Sky Sport, Serie A giornata 5 designations (16 September 2026) — La Penna appointed.
- Di Francesco's continuity at Lecce carried from this board's own card fx_11_f1.

────────────────────────────────────────────────
OVERRIDE BATCH — the seven T3 fixtures, raised to T1* on your instruction
and researched at full RESEARCH SPEC depth.

## f3 — AJ Auxerre – Stade Brestois (T3 → T1*, yours)
- Standing ESPN pipeline: 42 Ligue 1 2026–27, 305 of 306 2025–26, 604 cup/European matches (neither club appears in any — both have played league football only).
- Understat `getLeagueData/Ligue_1/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Ligue1.com "Les arbitres de la 5e journée" / AJA official — referee Guillaume Paradis, assistants Durand and Rodrigues, fourth official Benchabane, VAR Guenaoui and Zmyslony; 15:00 at the Abbé-Deschamps.
- TeamAJA "Bilan mercato estival 2026" / ICI Bourgogne / Dicodusport — Auxerre's ~€17.6m club-record outlay; Archer and Tuanzebe announced 1 September, Makosso from Luton, Labeau-Lascary on loan from Lens; Sinayoko out; Will Still's stated plan.
- Will Still's 12 June 2026 appointment carried from fx_9_f18; Julien Lachuer's 27 June promotion after Éric Roy's death from fx_13_f19; Del Castillo's €1m move to Osasuna from fx_0919_f2.
- **Gaps logged:** Brest's entire summer 2026 transfer ledger was not obtainable; no injury or suspension information exists for either club in anything reached. Nothing estimated.

## f5 — Leeds United – Crystal Palace (T3 → T1*, yours)
- Standing ESPN pipeline: 46 Premier League 2026–27, 380 2025–26, 604 cup/European matches (Leeds's two EFL Cup ties including the 3–6 at Chelsea; Palace's EFL Cup tie and 4–0 Europa League win over Lech Poznań).
- Understat `getLeagueData/EPL/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Yorkshire Evening Post / The Leeds Press / Yahoo Sports, 18–19 September 2026 — **referee Adam Herczeg making his Premier League debut**, 34 Championship matches to date, assistants Wood and Long, fourth official Hallam; injury lists for both clubs and Disasi's three-match ban.
- leedsunited.com "Summer 2026 transfers ins and outs" / ESPN / NBC Sports Premier League transfer lists — Leeds: Trafford £40m, Hincapié £25m, Tzolis £34m, Elvedi, Muharemović, Wilson and Meslier free; out Trossard £15.3m, Kiwior, Hein. Palace: Eze £60m rising to £67m to Arsenal, Lacroix reported £52m out; Pino and Canvot in.
- Palace's June 2026 coaching change and rebuilt defence carried from fx_0917_f5; Glasner's July move to Nottingham Forest from triage_0920.md.
- **Gaps and contradictions logged:** no Premier League referee record exists at all, so the entire referee block of the spec is empty and nothing is imported from the Championship; the Leeds ledger records Hincapié joining from Leverkusen for £25m while the Leverkusen window on card f9 records him joining Arsenal for €40m; Palace's head coach could not be named; no VAR appointment was published.

## f8 — Parma – Genoa (T3 → T1*, yours)
- Standing ESPN pipeline: 45 Serie A 2026–27, 380 2025–26, 604 cup matches (both clubs' two Coppa Italia ties).
- Understat `getLeagueData/Serie_A/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Corriere dello Sport / Sky Sport, Serie A giornata 5 designations (16 September 2026) — Maurizio Mariani appointed.
- SportParma / PazziDiFanta / TuttoSport / FantaMaster, 18–19 September 2026 — probable lineups, 15:00 at the Tardini, **Vásquez suspended for Genoa**, De Rossi's 3-5-2; Bernabé reported both as out and as expected to start.
- SportParma / Eurosport Serie A transfer boards — Parma 2026 moves that could be dated: Nicolussi Caviglia (Venezia), Cremaschi (Inter Miami), Scaglione (Genoa), Ordoñez in; Mateo Pellegrino to Fiorentina €25m plus €5m, recorded from the buying side on card f1.
- Cuesta's continuity from fx_0914_f1; De Rossi's from fx_12_f3; Genoa's "dozen summer arrivals and a sold centre-forward" from fx_0915_f1.
- **Gaps and contradictions logged:** no itemised 2026 fee list for Genoa; the Parma sources conflate the 2025 and 2026 windows, so only datable moves are stated and the rest omitted rather than reported uncertainly; the Bernabé fitness reports contradict each other and both are printed.

## f11 — OGC Nice – LOSC Lille (T3 → T1*, yours)
- Standing ESPN pipeline: 42 Ligue 1 2026–27, 305 of 306 2025–26, 604 cup/European matches (Lille's 2–3 Champions League defeat to Real Betis; Nice appear in none).
- Understat `getLeagueData/Ligue_1/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Ligue1.com "Les arbitres de la 5e journée" — referee Willy Delajod, assistants Finjean and Evrard, fourth official Leleu, VAR Gringore and Beyer; 17:15 at the Allianz Riviera.
- Sud Radio / Maxifoot / Les Transferts — **Olivier Pantaloni appointed at Nice on 17 June 2026** after Franck Haise left and Claude Puel's emergency spell was not continued; Nice's relegation play-off survival against Saint-Étienne and lost Coupe de France final.
- Sud Radio / Livefoot — Davide Ancelotti appointed at Lille on 1 June 2026 to replace Bruno Génésio, who went to Marseille (card f18); Meunier and Mandi out at contract end, Srdanovic and Nianzou in as numerical replacements, Önal from Nijmegen.
- Ancelotti's 1 June appointment and Lille's seven-in/twelve-out summer carried from fx_8_f3; the Nice coaching change from fx_10_f4, dated here for the first time.
- **Gaps and contradictions logged:** Nice's entire summer 2026 transfer ledger was not obtainable; no injury or suspension information for either club; **the Bouaddi fee is reported at £86m by Manchester City's own ledger (card f6) and at close to €130m by the French press — the two are not reconcilable at any exchange rate and neither is preferred.**

## f14 — Juventus – Atalanta (T3 → T1*, yours)
- Standing ESPN pipeline: 45 Serie A 2026–27, 380 2025–26, 604 cup/European matches (Juventus's 5–0 Europa League win over NEC Nijmegen; Atalanta's two Conference League play-off legs against Hapoel Tel Aviv).
- Understat `getLeagueData/Serie_A/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- Corriere dello Sport / Sky Sport, Serie A giornata 5 designations (16 September 2026) — Luca Zufferli appointed.
- Fanpage calciomercato live (1 September 2026) / FotMob / FootballTransfers — Juventus: nine signings under Spalletti, Woltemade on a €4m loan from Newcastle, Pape Matar Sarr on a €2m loan; Atalanta: Jonathan Rowe on a €5m loan from Bologna.
- Spalletti's 30 October 2025 appointment and 15-9-5 subsequent record carried from fx_0917_f6; Sarri's 15 June 2026 announcement and Atalanta's heavy defensive outflow with no published fee from fx_11_f3; João Mário's and Di Gregorio's loans out recorded from the receiving clubs on cards f1 and f4.
- **Gaps logged:** no injury or suspension information for either club; no itemised 2026 fee list for Atalanta beyond the Rowe loan, nor their outgoing list; fees for seven of Juventus's nine signings. Nothing estimated.

## f17 — SC Paderborn 07 – TSG Hoffenheim (T3 → T1*, yours)
- Standing ESPN pipeline: 33 Bundesliga 2026–27, 306 2. Bundesliga 2025–26 (Paderborn's promotion season and the 2. Bundesliga baseline), 604 cup/European matches (both clubs' DFB-Pokal ties; Hoffenheim's 0–2 Europa League defeat at OFI Crete).
- ESPN standings `ger.2?season=2025` — Schalke 70, Elversberg 62, Paderborn 62 from 34; Paderborn promoted in third.
- Understat `getLeagueData/Bundesliga/2026` — Hoffenheim both seasons, Paderborn 2026–27 only. **No 2. Bundesliga coverage, so Paderborn have no 2025–26 xG.**
- DFB Datencenter referee schedule — Daniel Schlager appointed, assistants Waschitzki-Günther and Fritsch, fourth official Bickel, VAR Nicolas Winter, VAR assistant Christian Fischer; 19:30.
- neunzigplus "Transferbilanz SC Paderborn im Sommer 2026" / LigaInsider / Sky Sport / Bundesliga.com official transfer market — **Paderborn 18 arrivals and 11 departures for about €8.7m, most expensive €3m, eight free, three on loan, and three of those loans from Hoffenheim**; Mika Baur to Celtic €6.3m; Hoffenheim 20 in and 22 out for about €65m, Nathan De Cat €20m from Anderlecht, Bazoumana Touré to Newcastle €47m.
- Paderborn's dismantled promotion spine carried from fx_9_f4; Hoffenheim's retained coach from fx_13_f4 and the Touré sale, reported there at €50m, from fx_0917_f2.
- **Gaps logged: Paderborn's head coach could not be identified from any source reached and is not named** — the point triage flagged as provisional; no injury or suspension information for either club; **the eligibility of the three Hoffenheim loanees to face their parent club is not stated anywhere reached**; the names of those three loanees were not obtainable; the Touré fee is reported at €47m here and €50m on the earlier card, and both are printed.

## f20 — Valencia – Real Sociedad (T3 → T1*, yours)
- Standing ESPN pipeline: 64 LaLiga 2026–27, 380 2025–26, 604 cup/European matches (Real Sociedad's 1–2 Europa League defeat to Bournemouth, carded in full on 17 September).
- Understat `getLeagueData/La_liga/{2025,2026}` — xG, npxG, xGA, PPDA, deep for both clubs, both seasons.
- FútbolFantasy / Jornada Perfecta / Infobae / Betfair, 19 September 2026 — **referee José Luis Munuera Montero**; 21:00 at Mestalla; Valencia's seven absentees (Canós, Diego López, Copete, Foulquier, Diakhaby, Tárrega, Sadiq) with Rioja doubtful; **Óscar Sánchez continuing as interim coach**.
- FútbolFantasy mercado verano 2026, Valencia and Real Sociedad — Valencia in: Arnau Martínez €5m, Ryunosuke Sato; out: Cenk Özkacar. Real Sociedad in: Kazunari Kita €1.5m; out: Brais Méndez, Carlos Fernández, Jon Karrikaburu.
- Corberán's 13 September dismissal alongside the football CEO carried from fx_0915_f3; Valencia's net-negative window from fx_16_f4; Sergio Francisco's 14 December 2025 sacking and the retained-manager characterisation from fx_0917_f8.
- **Gaps logged:** no injury or suspension information for Real Sociedad; the identity of their head coach since December 2025 could not be established and is not named; fees undisclosed for Sato in, Özkacar out and all three Real Sociedad departures; whether Óscar Sánchez continues beyond this fixture is unknown. Nothing estimated.

────────────────────────────────
REVISION — full re-check after you flagged that Ünal is still at Getafe.

Four transfer contradictions that the first build logged as unresolved were
chased down and all four are now settled. Each resolved against one of this
board's own cards, so four cards were corrected.

1. Enes Ünal — YOUR CATCH, and the source error was on card f2.
   He did not leave Getafe for Beşiktaş. He REJOINED Getafe from
   Bournemouth on a free transfer on 13 August 2026, permanently, to 2029.
   No fee passed because Bournemouth still owed Getafe from the 2023 deal
   that took him to England for €16.5m; Bournemouth keep a 20% sell-on and
   up to €1.5m in bonuses.
   Sources: Sofascore, comuniate.com, footballtransfers, cryptobriefing,
   ysscores, all August 2026.
   Knock-on: the whole Getafe transfer bullet on f2 was wrong, not just this
   line. The club's actual window was 14 in and 14 out for a net outlay of
   about €5m — Satriano €6.5m from Lyon, Zaid Romero €5m from Brugge, Mario
   Martín €3.5m from Real Madrid, Terrats €2.5m from Villarreal, Boselli
   €1.5m from River, plus Mojica and Ünal — and Luis Milla was a DEPARTURE to
   Como for €6m, not a €4m arrival from Granada. Bordalás renewed for two
   more seasons. Every sentence on f2 that rested on "sold its striker and
   did not replace him" has been rewritten.
   Source: FutbolFantasy / Fichajes / ingeniospodcast Getafe 2026-27 window.

2. Piero Hincapié — error was on card f5.
   He did not join Leeds for £25m. Arsenal converted his season-long loan
   from Bayer Leverkusen into a permanent transfer on 1 July 2026 for a
   reported £34.5m plus add-ons, five years to 2031. Card f9 had it right.
   He is removed from Leeds's arrivals.
   Sources: arsenal.com official, Goal.com, FootballTransfers, Sky Sports.

3. Timothy Weah — error was on card f18, and the direction was reversed.
   He did not leave Marseille for Juventus. He moved Juventus to Marseille
   on a loan with an obligation to buy, which was triggered, making him a
   permanent Marseille player. He is an ARRIVAL, not a departure, and he is
   in this weekend's probable eleven at right-back. Marseille's confirmed
   departure total therefore falls from €126.9m to €112.5m, and the card no
   longer says the club confirmed no arrivals.
   Sources: juventus.com official, NBC New York, OneFootball, ESPN.

4. Ayyoub Bouaddi's fee — the French press figure was wrong.
   £86m, being £81.3m fixed plus £4.3m in add-ons, five years to 2031,
   confirmed August 2026 — a Premier League record for a teenager. Not the
   "close to €130m" reported in France. Manchester City's own ledger on card
   f6 was right; card f11 is corrected.
   Sources: Sky Sports, ESPN, FOX Sports, all August 2026.

Still genuinely open: Parma's Adrián Bernabé is listed as out by one preview
and as expected to start by another. Both readings stay printed on f8.

SUPERLATIVE AUDIT. Separately, every board-wide comparative claim on all
twenty cards was re-checked mechanically against the counted dataset
(boardstats.json, built from the same ESPN and Understat figures as the
cards). Roughly thirty claims were wrong and have been corrected. The
pattern was systematic rather than random: most were true when written
against a part-built board and became false as later cards were added —
for example, Frosinone's 16.50 fouls was the highest on the board when f7
was written and stayed so, but Juventus's 16.00 was described as the
highest when f14 was written later. Others were wrong at the time, such as
Deportivo's 1.08 xG being called the lowest on the board when Málaga's 0.83
was already carded. Each claim is now stated at its true rank or softened
to a verified range. The divisional comparisons, which come straight from
baselines_0920.md, were unaffected — they were never the fragile part.
