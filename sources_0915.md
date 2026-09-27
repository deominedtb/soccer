# sources_0915

## Triage

- Web search: "Serie A 2026-27 promoted teams from Serie B" — confirmed
  Venezia, Frosinone, Monza promoted; none on this slate.
- Web search: "LaLiga 2026-27 promoted teams from Segunda Division" —
  confirmed Málaga (playoff) plus two others promoted; none on this
  slate's LaLiga fixtures.
- Web search: "Premier League 2026-27 promoted teams from Championship"
  — confirmed Coventry City, Ipswich Town, Hull City promoted; West Ham
  United, Burnley, Wolverhampton Wanderers relegated. Ipswich Town
  (f6, promoted) and West Ham United (f5, relegated) both on this
  slate.
- Web search: "EFL Championship 2026-27 promoted teams from League One"
  — confirmed Lincoln City, Cardiff City, Bolton Wanderers promoted;
  Peterborough (f4), Barnsley (f4) and Reading (f8) remain League One.
- Web search: "Serie A manager sacked new coach September 2026 Como
  Parma Torino Roma Inter Udinese" — confirmed Fiorentina sacked Fabio
  Grosso, appointed Paolo Vanoli (f9). Also surfaced Roma (De Rossi to
  Juric) and Torino (Baroni to D'Aversa) manager changes — both on
  fixtures already dropped as stale (see fixtures_0915.md header).
- Web search: "Leeds United Newcastle Reading Villarreal Real Betis
  manager change September 2026" — no manager change found for Reading,
  Villarreal or Real Betis. Confirmed via this search that Leeds–
  Newcastle and Villarreal–Real Betis were already played on
  2026-09-14, which is what surfaced the stale-row problem in the
  typed sheet.
- Web search: "EFL Cup second round fixtures 15 September 2026 West Ham
  Ipswich Liverpool Reading Peterborough" — confirmed Reading–Brentford,
  Ipswich–Arsenal, Liverpool–Tottenham, Peterborough–Barnsley and West
  Ham–Fulham are genuinely scheduled for 2026-09-15 (Carabao Cup third
  round; William Hill preview names all five as "Tuesday 15th September
  2026"). Spent to confirm slate integrity, not a triage signal.
- Web search: "Coppa Italia round of 32 fixtures September 2026 Genoa
  Fiorentina" — confirmed Genoa–Südtirol and Fiorentina–Pisa are
  genuinely scheduled for 2026-09-15 (17:00/20:00 UK = 18:00/21:00
  Europe/Rome, consistent with the typed sheet). Spent to confirm slate
  integrity, not a triage signal.

## Correction to Triage log
- The triage search on Serie A manager changes returned a summary conflating seasons. Verified in Phase 2 against Wikipedia 2026–27 Serie A: Roma's De Rossi-to-Juric change is from 2024, not 2026; Torino's 2026–27 coach is Ignazio Abate (appointed 12 June 2026); Fiorentina's Grosso-to-Vanoli change (6–7 September 2026) is confirmed.

## Baseline · Coppa Italia
- WebSearch: "Coppa Italia 2025-26 statistiche gol per partita media cartellini calci d'angolo vittorie casa" — 111 goals / 45 = 2.47 (Wikipedia).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Coppa_Italia — 44 match boxes counted: O2.5 19, BTTS 20, home wins 26, 12 penalty shoot-outs.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Coppa_Italia — first-stage results, no extra time, 5 of 24 to penalties; Genoa–Südtirol and Fiorentina–Pisa boxes.
- curl: https://data.fotmob.com/stats/141/season/27177/ and /38626/ (corner_taken_team, total_yel_card_team, total_red_card_team, fk_foul_lost_team) — Coppa Italia team totals 2025–26 and 2026–27.
- Context baselines (no search): Wikipedia 2025–26 Serie A and Serie B results grids (counted); FotMob Serie A 55/27044 and Serie B 86/27577 team totals.

## f1 · Genoa – Südtirol (T1)
- WebSearch: "Genoa Südtirol Coppa Italia 15 settembre 2026 probabili formazioni arbitro" — Ferraris 18:00, Manganiello, probable XIs (fantamaster, tuttosport, calciogenoa, pianetagenoa1893, genoaoggi). Betting-site results ignored.
- WebFetch: https://www.pianetagenoa1893.net/primo-piano/genoa-sudtirol-coppa-italia-larbitro-e-manganiello-var-e-giua/ — Manganiello (Pinerolo), Politi, Regattieri, Galipò, Giua, Del Giovane; "Genoa sempre vincente in Coppa Italia" headline.
- WebFetch: https://www.tuttosport.com/news/calcio/coppa-italia/2026/09/15-151256847/genoa-sudtirol_probabili_formazioni_e_diretta_dove_si_vede_in_tv_e_streaming — probable XIs (Vitinha–Meichtry; Südtirol 3-4-2-1). Its summary described Genoa–Frosinone as a defeat; the Wikipedia grid and FotMob both record 1–1, used instead.
- WebFetch: https://www.fantamaster.it/probabili-formazioni-genoa-sudtirol-coppa-italia-2026-2027/ — probable XIs (El Shaarawy–Vitinha "inedito"; Südtirol 4-2-3-1).
- WebFetch: https://www.genoaoggi.it/coppa-italia/genoa-i-convocati-per-la-sfida-di-coppa-italia-col-sud-tirol/ — 25 convocati; no extra time, penalties if level.
- WebSearch: "Genoa calciomercato estate 2026 acquisti cessioni allenatore stagione 2026-27" — De Rossi; Sow, Meichtry, Traorè, Mitaj.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Genoa_CFC_season — full transfer table with fees, squad, results.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Serie_A — results grid (Genoa 16th, 41–51), managerial changes (Vieira out 1 Nov 2025, Murgita caretaker, De Rossi 6 Nov 2025).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Serie_A — grid to 14 Sep (Genoa 1–1 Frosinone), managerial changes.
- curl: https://understat.com/getTeamData/Genoa/2025 and /2026 — xG, shots for/against, formation minutes, goals by 15-minute period (first-half goals), set-piece goals.
- curl: https://www.fotmob.com/teams/10233/stats/genoa/teams — season IDs, fixture dates (Frosinone 12 Sep; Parma 20 Sep).
- curl: https://data.fotmob.com/stats/55/season/27044/ and /36072/ — Genoa corners, cards, fouls, xG, possession, clean sheets 2025–26 and 2026–27.
- WebFetch: https://www.espn.com/soccer/stats/_/league/ITA.1/season/2025/view/discipline — Serie A 2025–26 discipline (Genoa 61 Y 3 R), matches FotMob totals.
- WebSearch: "Genoa 2025-26 Serie A statistiche squadra calci d'angolo per partita falli commessi tiri media" — pointed to FotMob.
- WebFetch: https://www.corrieredellosport.it/squadra/calcio/genoa/statistiche/t990 — zero rows, unusable.
- WebFetch (404): https://footystats.org/clubs/genoa-cfc-521
- WebSearch: "Südtirol calciomercato estate 2026 acquisti cessioni allenatore Serie B 2026-27" — Possanzini; Lopes, Varnier, Pyyhtiä, Stivanello, Plizzari; Mallamo out.
- WebFetch: https://sport.virgilio.it/tabellone-calciomercato-serie-b-movimenti-acquisti-e-cessioni-estate-2025-913013 — Südtirol in/out list, updated 1 Sep 2026, no fees.
- curl (raw wikitext): https://en.wikipedia.org/wiki/FC_S%C3%BCdtirol — squad at 1 Sep 2026 (Giorgini listed; Rispoli on loan from Como).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Serie_B — grid (Südtirol 16th, 38–48), play-out v Bari 0–0 agg, longest winless run 13.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Serie_B — grid to 13 Sep, Castori out 23 Jun, Possanzini 24 Jun 2026.
- WebSearch: "Südtirol Serie B 2026-27 risultati giornate Benevento Catanzaro Modena Entella Possanzini" — matchday order, Modena 12 Sep, record-equalling 8 points (agenziagiornalisticaopinione, ntr24).
- curl: https://data.fotmob.com/stats/86/season/27577/ and /45720/ — Südtirol corners, cards, fouls, xG, possession 2025–26 and 2026–27.
- WebSearch: "FC Südtirol Serie B 2025-26 statistiche calci d'angolo cartellini falli media partita squadra" — nothing usable beyond FotMob.
- WebSearch: "Gianluca Manganiello arbitro statistiche 2025-26 cartellini gialli media rigori Serie A" — 2024–25: 17 matches, 48 Y, 3 R, 3 penalties, 412 fouls; career 3.78 Y / 0.09 R (pianetafanta, valuestats snippets).
- WebFetch: https://sport.virgilio.it/calcio/arbitri/gianluca-manganiello/ — 2026–27: 1 Serie A match, 4 Y, 0 R, 19 fouls, 0 pens; match list.
- WebFetch: https://www.pianetafanta.it/statistiche-arbitri.asp?NomeArbitro=Manganiello+G.&tipolink=100 — form page only, no data.
- WebFetch (403): https://it.whoscored.com/regions/108/tournaments/5/seasons/10732/stages/24500/refereestatistics/italia-serie-a-2025-2026

## Baseline · LaLiga
- WebSearch: "LaLiga 2025-26 season statistics goals per game over 2.5 BTTS cards per game corners home win percentage" — no league aggregate usable (Footiqo, Squawka, FootyStats pointers).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_La_Liga — results grid, 378 of 380 matches counted: 2.69 goals, 49.7% O2.5, 56.3% BTTS, 48.7% home wins; managerial changes.
- curl: https://data.fotmob.com/stats/87/season/27233/ — team totals: 1,612 Y + 107 R, 3,672 corners, fouls 12.6 per team.

## f2 · Rayo Vallecano – Espanyol (T1)
- WebSearch: "Rayo Vallecano Espanyol previa alineaciones probables árbitro 15 septiembre 2026" — Butarque 19:00, jornada 6, absences (De Frutos suspended; Batalla, Isi, Luiz Felipe, Vertrouwd; Kike García), probable XIs (sportaragon, eldesmarque, futeros, lagrada). Betting-site results ignored.
- curl: https://www.fotmob.com/matches/rayo-vallecano-vs-espanyol/2dbblq — referee listing (Díaz de Mera Escuderos, 39-match stats), stadium, predicted XIs and coaches, unavailable players, H2H.
- WebSearch: "árbitro Rayo Vallecano Espanyol jornada 6 LaLiga designación CTA septiembre 2026 VAR" — no official designation found.
- WebSearch: "Díaz de Mera Escuderos árbitro estadísticas temporada 2025-26 tarjetas por partido penaltis LaLiga" — career 6.02 Y / 0.18 R, 76 penalties (statshub snippet).
- WebFetch: https://estadisticaslaliga.es/arbitros.php — 2026–27: 3 matches, 15 Y, 0 R, 57 fouls, 0 penalties.
- WebFetch: https://www.futbolfantasy.com/laliga/arbitros — no jornada-6 designations; 3 matches, 4.7 Y pg.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_La_Liga and Template:2026–27_La_Liga_table — stadiums (Rayo at Estadio Ontime Butarque), results grid to 14 Sep, managerial changes (Pérez out 29 May; San José 18 Jun 2026), discipline leaders (Espanyol 17 Y; Rayo 2 R), lowest attendance 4,280.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Rayo_Vallecano_season — 8th, Conference League runners-up (W10 D1 L4), De Frutos 10 league goals.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_RCD_Espanyol_season — 11th, Manolo González.
- WebSearch: "Rayo Vallecano juega en Butarque temporada 2026-27 estadio de Vallecas obras motivo" — Comunidad de Madrid ended concession after audit (elespanol.com, infobae).
- WebSearch: "Rayo Vallecano fichajes verano 2026 Chavarría Chelsea Nobel Mendy Hull Beñat San José Butarque altas bajas" — arrivals/departures (futbolfantasy, fichajes.com, vavel); Vertrouwd €1.5m claim.
- WebFetch: https://www.futbolfantasy.com/laliga/equipos/rayo-vallecano/mercado-fichajes/verano-2026 — Belaid, Audero, Sadick, Bouaré (€600k, 50%), Pedrosa, Morro, Eto'o. Two entries marked "agreement" only (Aitor Fernández, Álex Moreno) not carried.
- curl: https://www.fotmob.com/teams/8370/overview/x — fixtures and dates, summer transfer list with fees (Chavarría €19m, Mendy €25m).
- WebSearch: "Espanyol fichajes verano 2026 altas bajas Calatrava Moscardo Bryan Zaragoza Manolo González balance mercado" — altas/bajas list.
- WebFetch: https://www.futbolfantasy.com/mercado-de-fichajes-del-espanyol-altas-bajas/verano-2026 — table with fees, loan returns (Romero, Ngonge, Terrats, Pickel), net −€2m.
- curl: https://www.fotmob.com/teams/8558/overview/x — fixtures and dates, transfer list (Terrats to Getafe €2.5m — conflicts with FútbolFantasy).
- curl: https://data.fotmob.com/stats/87/season/27233/ and /38843/ — Rayo and Espanyol corners, cards, fouls, xG, possession, clean sheets.
- curl: https://understat.com/getTeamData/Rayo_Vallecano/2025, /2026; Espanyol/2025, /2026 — shots, first-half goals, formations, home/away xG, match list.

## f3 · Deportivo Alavés – Valencia (T1)
- WebSearch: "Alavés Valencia previa jornada 6 alineaciones probables árbitro Mendizorroza 15 septiembre 2026" — 20:00 Mendizorroza; Alavés 10 pts, Valencia 1 pt; Corberán dismissed, Óscar Sánchez interim; absences (futbolfantasy, comunio, sportaragon, eldesmarque, futeros). Betting-site results ignored.
- WebSearch: "Valencia CF destituye Corberán septiembre 2026 Óscar Sánchez interino nuevo entrenador" — dismissal 13 Sep, first in LaLiga this season; Ron Gourlay and staff also removed (noticiasdealava, actualidadvalencia, vavel, valenciacf.com).
- curl: https://www.fotmob.com/matches/deportivo-alaves-vs-valencia/3cobnt — Sesma Espinosa listed with 23-match stats; stadium; predicted XIs and coaches; unavailable players; H2H.
- WebSearch: "Sesma Espinosa árbitro Alavés Valencia designación jornada 6 LaLiga" — designation reported; March 2026 debut report (deportevalenciano); iusport, lagrada.
- WebFetch: https://nortexpres.com/previa-alaves-valencia-el-mejor-arbitro-uno-de-los-peores-var/ — Sesma referee, Valentín Pizarro VAR; five Alavés matches last season, five Alavés wins.
- WebFetch: https://estadisticaslaliga.es/arbitros.php — Sesma 2026–27: 3 matches, 81 fouls, 2 penalties, 12 Y, 2 R.
- WebSearch: "Alavés fichajes verano 2026 Miguel Rodríguez Utrecht Valentini Koski Parada Spartak Diarra Quique Sánchez Flores" — Miguel Rodríguez €5m; Valentini replacing Parada; Villalibre out; net −€7m (futbolfantasy).
- WebSearch: "Valencia CF fichajes verano 2026 Harvey Elliott Arnau Martínez Sato Özkaçar balance mercado altas bajas" — Arnau Martínez €5m largest; Elliott loan; Guido renewed; Danjuma and Hugo Duro stayed (jornadaperfecta, tuayudantefantasy, eldesmarque).
- curl: https://www.fotmob.com/teams/9866/overview/x and /10267/overview/x — fixtures with dates, transfer lists with fees (Parada €5m, Diarra €1.2m, Mikel Rodríguez €2m, Özkaçar €1.75m, Sato €4m, Dieng €0.5m).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Deportivo_Alav%C3%A9s_season — 14th, Copa QF, Coudet to Sánchez Flores 3 Mar, Toni Martínez 14.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Valencia_CF_season — 9th, Copa QF, Hugo Duro 10.
- curl: https://data.fotmob.com/stats/87/season/27233/ and /38843/ — Alavés and Valencia corners, cards, fouls, xG, possession, shots on target.
- curl: https://understat.com/getTeamData/Alaves/2025, /2026; Valencia/2025, /2026 — shots, first-half goals, formations, match list.

## Baseline · EFL Cup
- WebSearch: "EFL Cup 2025-26 statistics goals per game cards per game corners home wins penalties shootouts" — 254 goals / 93 = 2.73 (Wikipedia).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_EFL_Cup — 92 match boxes counted: 47 O2.5, 50 BTTS, 37 home wins, 20 level, 20 to penalties.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_EFL_Cup — rounds one and two, 66 boxes; Peterborough and Barnsley results.
- curl: https://data.fotmob.com/stats/133/season/27199/ and /37889/ — EFL Cup corners, cards, fouls team totals.

## f4 · Peterborough United – Barnsley (T2)
- WebSearch: "Peterborough United v Barnsley Carabao Cup third round preview team news referee September 2026" — Weston Homes Stadium 19:30 BST; absences Adebisi, Hughes, Frith, Garbett; cup results (sportsmole, peterboroughtoday, goal.com). Betting-site results ignored.
- curl: https://www.fotmob.com/matches/barnsley-vs-peterborough-united/2dmy2t — published team sheets, coaches, Garbett out, referee listing (Thomas Parsons, 34-match stats), stadium, H2H.
- curl: https://www.fotmob.com/teams/8677/overview/x and /8283/overview/x — fixtures with dates, summer transfer lists (no fees).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_EFL_League_One and 2026–27 — results grids (2025–26 records; 2026–27 to 12 Sep), managerial changes (Ferguson out 25 Oct 2025, Williams 29 Oct 2025; Hourihane out 2 May 2026, Stendel 12 May 2026).
- curl: https://data.fotmob.com/stats/108/season/27196/ and /38071/ — corners, cards, fouls, xG, possession for both clubs; League One per-team averages.

## f5 · West Ham United – Fulham (T1)
- WebSearch: "West Ham v Fulham Carabao Cup third round preview team news referee 15 September 2026" — London Stadium 19:45 BST; Gavin Ward; West Ham top of Championship after 6–0 v Wrexham; Fulham 18th under Arbeloa (whufc.com, Yahoo Sports, claretandhugh). Betting-site results ignored.
- WebFetch: https://www.whufc.com/en/news/west-ham-united-v-fulham-or-all-you-need-to-know-sep-2026 — ticketing page only, no match facts.
- WebFetch: https://uk.sports.yahoo.com/news/west-ham-vs-fulham-preview-071000843.html — Veltman doubt, Souček out, Cairney out; Nuno and Arbeloa; Fulham 57.3% possession.
- Search result title only: https://www.whufc.com/en/news/match-officials-confirmed-for-fulham-carabao-cup-derby — officials confirmed (Gavin Ward per preview).
- WebSearch: "Gavin Ward referee statistics 2025-26 yellow cards per game penalties Premier League Championship" — 22 matches, 64 Y, 3 R, 2 penalties (KickoffScore / PlayerStats snippets).
- curl: https://www.fotmob.com/matches/west-ham-united-vs-fulham/2u9b5i — published team sheets, coaches, unavailable, referee 50-match stats, stadium, H2H.
- curl: https://www.fotmob.com/teams/8654/overview/x and /9879/overview/x — fixtures with dates, summer transfer lists with fees.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Premier_League — results grid (West Ham 18th, Fulham 11th), managerial changes (Potter out / Nuno 27 Sep 2025).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Premier_League — grid to 14 Sep, managerial changes (Silva out 2 Jun, Arbeloa 7 Jul 2026).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_EFL_Championship — grid (West Ham 7 matches, 20–9).
- curl: https://data.fotmob.com/stats/47/season/27110/, /47/season/36781/, /48/season/38070/, /133/season/37889/ — corners, cards, fouls, xG, possession.
- curl: https://understat.com/getTeamData/West_Ham/2025; Fulham/2025, /2026 — shots, first-half goals, formations, set-piece goals.

## f6 · Ipswich Town – Arsenal (T1)
- WebSearch: "Ipswich Town v Arsenal Carabao Cup third round preview team news referee 15 September 2026 Portman Road" — 20:00 BST Portman Road; Peter Bankes; Kepa expected in goal; Emersonn doubtful, Taylor out, Matusiwa doubtful; last two meetings (Yahoo Sports, justarsenal, lastwordonsports, paininthearsenal). Betting-site results ignored.
- curl: https://www.fotmob.com/matches/arsenal-vs-ipswich-town/37uw12 — referee listing and 47-match stats, stadium, last starting elevens (not tonight's), unavailable players, H2H.
- WebSearch: "Peter Bankes referee statistics 2025-26 Premier League yellow cards per game penalties fouls" — career 302 matches, 1,191 Y, 30 R, 17 second yellows, 69 penalties, 115 PL matches (StatsHub snippet).
- curl: https://www.fotmob.com/teams/9902/overview/x and /9825/overview/x — fixtures with dates (Arsenal Community Shield, Napoli UCL 9 Sep), summer transfer lists with fees.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_EFL_Championship — grid (Ipswich 2nd, 80–47, 84 pts).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Premier_League — managerial changes (McKenna resigned 10 Jun, O'Neil 23 Jun 2026), grid to 14 Sep.
- curl: https://data.fotmob.com/stats/48/season/27195/ (Ipswich 2025–26), /47/season/27110/ and /36781/ (Arsenal, Ipswich) — corners, cards, fouls, xG, possession, clean sheets.
- curl: https://understat.com/getTeamData/Ipswich/2026; Arsenal/2025, /2026 — shots, first-half goals, formations, set-piece goals.

## f7 · Liverpool – Tottenham Hotspur (T1)
- WebSearch: "Liverpool v Tottenham Carabao Cup third round preview team news referee Anfield 15 September 2026 Iraola De Zerbi" — 20:00 BST Anfield; Mamardashvili to start; Bradley, Chiesa, Ekitike, Leoni out; Kitchen fourth official; no VAR in round three; straight to penalties if level (thisisanfield, liverpoolfc.com, Yahoo Sports).
- WebFetch (403): https://www.thisisanfield.com/2026/09/liverpool-vs-tottenham-carabao-cup-injuries-team-selection-tv-info/
- WebSearch: "Andy Madley referee Liverpool Tottenham Carabao Cup September 2026 statistics yellow cards per game 2025-26" — Madley appointed; 3.07 Y / 0.07 R pg; 412 matches, 1,263 Y, 29 R, 15 second yellows (StatsHub, sportsmole snippets); another source 3.74 Y.
- curl: https://www.fotmob.com/matches/tottenham-hotspur-vs-liverpool/2gg3ek — published team sheets, coaches, unavailable, referee 43-match stats, stadium, H2H.
- curl: https://www.fotmob.com/teams/8650/overview/x and /8586/overview/x — fixtures with dates (Liverpool v Atlético 9 Sep; Tottenham 5–1 Charlton), summer transfer lists with fees.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Premier_League — grid (Liverpool 5th, Tottenham 17th); managerial changes (Frank out 11 Feb, Tudor 14 Feb–29 Mar, De Zerbi 31 Mar 2026).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Premier_League — Slot out 30 May, Iraola 4 Jun 2026; grid to 14 Sep.
- curl: https://data.fotmob.com/stats/47/season/27110/ and /36781/ — corners, cards, fouls, xG, possession, clean sheets.
- curl: https://understat.com/getTeamData/Liverpool/2025, /2026; Tottenham/2025, /2026 — shots, first-half goals, formations, set-piece goals.

## f8 · Reading – Brentford (T2)
- WebSearch: "Reading v Brentford Carabao Cup third round preview team news referee 15 September 2026 Select Car Leasing Stadium" — 20:00 BST; Tom Nield; penalties if level; Stokes returns; Furo operation; Fredrick available (brentfordfc.com, Yahoo Sports, vavel, onefootball).
- curl: https://www.fotmob.com/matches/reading-vs-brentford/37y9ut — published team sheets, coaches, Brentford unavailable, referee 45-match stats, stadium, H2H.
- curl: https://www.fotmob.com/teams/9798/overview/x and /9937/overview/x — fixtures with dates (Reading EFL Cup 6–5 Bromley, 3–0 Stevenage, Trophy 4–2 Wycombe; Brentford 6–1 Birmingham; Chelsea 18 Sep), transfer lists.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_EFL_League_One and 2026–27 — Reading grids; Hunt out 26 Oct 2025, Richardson 28 Oct 2025.
- curl: https://data.fotmob.com/stats/108/season/27196/ and /38071/ (Reading), /47/season/27110/ and /36781/ (Brentford), /133/season/37889/ (EFL Cup) — corners, cards, fouls, xG, possession.
- curl: https://understat.com/getTeamData/Brentford/2025, /2026 — first-half goals, formations.
