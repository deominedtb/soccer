# sources_0916

## Triage
- No searches spent (capacity 8 exceeds slate size 7; no tier could move).

## Slate integrity
- WebSearch: "UEFA Europa League 2026-27 league phase matchday 17 September 2026 fixtures Milan Benfica Sunderland AZ Leverkusen Celje" — league phase opens Wednesday 16 September 2026 (UEFA.com fixture list, Wikipedia).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Europa_League_league_phase — all seven fixtures confirmed as matchday 1 on 16 September 2026, 21:00 CEST; stadium and referee listed in each match box; Hapoel Be'er Sheva home match at Rapid-Giulești Stadium, Bucharest (neutral venue).

## Baseline · UEFA Europa League
- WebSearch: "UEFA Europa League 2025/26 season statistics goals per match cards per game corners average league phase" — aggregator figures (PerformanceOdds/FootyStats snippets: 4.38 cards, 9.32 corners over 271 matches incl. qualifying) not used.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_UEFA_Europa_League_league_phase — 144 match boxes counted: goals, O2.5, BTTS, home wins, failed-to-score, first-half goals from goal minutes.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_UEFA_Europa_League_knockout_phase — fetched, not used in the baseline (extra time in second legs).
- curl: https://www.fotmob.com/leagues/73/stats/europa-league — season ids (2025/26 = 28190).
- curl: https://data.fotmob.com/stats/73/season/28190/ (corner_taken_team, total_yel_card_team, total_red_card_team, fk_foul_lost_team, expected_goals_team, clean_sheet_team) — 189 matches, 378 team-appearances.
- Context baselines (no search): Wikipedia 2025–26 Serie A and 2025–26 Primeira Liga results grids (counted); FotMob Serie A 55/27044 and Liga Portugal 61/27181 team totals.

## f1 · Milan – Benfica (T1)
- WebSearch: "Milan calciomercato estate 2026 acquisti cessioni ufficiali Allegri stagione 2026-27" — calcioefinanza, Eurosport tabellone; Ramos, Gila, Diawara, Kostic, Guernier.
- WebSearch: "Benfica mercado verão 2026 contratações saídas oficiais Marco Silva treinador 2026-27" — RTP, slbenfica.pt (Marco Silva official, 9 June), A Bola, DAZN. Snippet conflated the 2025 window (Manu Silva, Ríos arrivals); Wikipedia 2026–27 ledger used instead.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_AC_Milan_season — manager Amorim; summer ledger with fees; Serie A match boxes (scorers, cards, referees).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Serie_A — managerial changes (Allegri sacked 25 May 2026, Amorim 16 June 2026; Allegri to Napoli 3 July 2026); results grid to 14 Sep.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Serie_A — results grid, Milan 5th 53–35, 70 pts; home/away split, O2.5, BTTS, CS, FTS counted.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_AC_Milan_season — fetched for context.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_S.L._Benfica_season — manager Marco Silva; summer ledger with fees; league and qualifying match boxes (scorers, cards, goal minutes).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_S.L._Benfica_season — league match boxes (first-half goals counted); Mourinho from 18 Sep 2025.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Primeira_Liga and /2025%E2%80%9326_Primeira_Liga — managerial changes (Mourinho signed by Real Madrid, Marco Silva 9 June 2026); grids (Benfica 2nd, 23-11-0, 74–25, 80 pts; 302 of 306 matches filled).
- curl: https://data.fotmob.com/stats/55/season/27044/ and /36072/ — Milan xG, corners, cards, fouls, clean sheets, possession, shots on target 2025–26 and 2026–27.
- curl: https://data.fotmob.com/stats/61/season/27181/ and /40067/ — Benfica same fields.
- curl: https://understat.com/getTeamData/AC_Milan/2025 and /2026 — shots for/against, goals by period (first half), goal situations, formation minutes.
- WebSearch: "Milan Benfica Europa League probabili formazioni Amorim indisponibili squalificati 16 settembre 2026" — ilsussidiario, LaPresse, Quotidiano Sportivo, PianetaMilan, Tuttosport (no Milan absentees; Hutchinson first start; Amorim ex-Benfica). Betting pages ignored.
- WebFetch: https://www.pianetamilan.it/partite/probabili-formazioni/probabili-formazioni-milan-benfica-le-scelte-di-amorim-e-silva-per-europa-league/ — probable XIs, Modrić/Rabiot rested, Trubin/Soares and Durán/Pavlidis doubts.
- WebSearch: "Benfica convocados Milan Liga Europa Marco Silva lesionados ausências Bah Trubin setembro 2026" — Record, A Bola, Bola na Rede, Futebol Divertido: 24 called up, Bah left out, Índio/Umeh/Neto/G. Moreira stayed home.
- WebSearch: "Jarred Gillett referee Milan Benfica Europa League appointment" — Football Italia, Yahoo, football360, Tribuna (appointment 14 Sep; first Australian in a European league phase).
- WebFetch: https://football-italia.net/referee-line-up-confirmed-milan-vs-benfica/ — Davies, Greenhalgh, Harrington, Atwell (VAR), Kwiatkowski (AVAR); no prior Milan/Benfica matches.
- WebSearch: "Jarred Gillett referee stats 2025/26 Premier League yellow cards per game penalties fouls" — statshub, statz.ai, footymetrics, Squawka; snippet figures mutually inconsistent, resolved by fetch.
- WebFetch: https://statz.ai/referee/jarred-gillett — 27 matches combined 25/26–26/27, 3.67 Y, 19.89 fouls (no season split; not used in the strip).
- WebFetch: https://www.footymetrics.com/referees/153-jarred-gillett — season/competition split used: PL 25/26 21 matches 78 Y 1 R 416 fouls 6 pens; PL 26/27 3 matches 13 Y 68 fouls 0 pens; PL 24/25 16 matches 68 Y 353 fouls 2 pens.
- Local, not a source of facts: fx_18_f9.html and fx_8_f4.html read for leads only; the Milan card's "Allegri continues" is contradicted by Wikipedia and the previews and was not used.

## f2 · Anderlecht – Lyon (T1)
- WebSearch: "Anderlecht transferts été 2026 arrivées départs entraîneur saison 2026-27 officiel" — Foot Mercato tableau, DH, Walfoot, BeSoccer; coach not settled in snippet (Vítor Bruno mentioned).
- WebSearch: "OL Lyon mercato été 2026 arrivées départs officiels entraîneur Fonseca saison 2026-27" — dicodusport, Foot Mercato, Maxifoot, Lyonfoot (Bidstrup €10.5m; Fofana, Moreira, Satriano out).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Belgian_Pro_League — managerial changes (Taravel caretaker spell ended 24 May 2026; Vítor Bruno appointed 23 June 2026); Anderlecht 3-1-2, 4–5 after six.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Belgian_Pro_League — regular-season grid (Anderlecht 6th, 12-8-10, 43–39, 44 pts; 240 matches: 2.62 goals, 46.7% O2.5, 53.8% BTTS, 40.8% home wins), champions' play-off table (Anderlecht 4th, 3-2-5, 16–23), Hasi dismissed 1 Feb 2026.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_RSC_Anderlecht_season — season summary (Still interim, Taravel caretaker 9 Feb), 40 league match boxes (O2.5, BTTS, CS, FTS, first-half goals counted), Belgian Cup final 1–3 v Union SG.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_RSC_Anderlecht_season — stale (updated 10 July); Bruno appointment date confirmed only.
- curl: https://www.fotmob.com/teams/8635/fixtures/anderlecht — 2026–27 results: Pro League six, Europa League qualifying v Hammarby, PAOK, Kairat.
- curl: https://www.fotmob.com/teams/8635/squad — positions; Hey out until early January 2027; Camara, Sardella day to day.
- WebFetch: https://www.footmercato.net/club/rsc-anderlecht/tableau/ — Anderlecht 2026–27 arrivals and departures with fees (single source for fees).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Olympique_Lyonnais_season — manager Fonseca; summer ledger with fees.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Olympique_Lyonnais_season — Europa League 2025–26 results (7 of 8 league-phase wins; last-16 exit to Celta Vigo; De Burgos Bengoetxea refereed Lyon 4–2 PAOK, 29 Jan 2026).
- curl: https://www.fotmob.com/teams/9748/fixtures/lyon and /squad — 2026–27 results (Champions League qualifying v Sparta Prague and Fenerbahçe; Ligue 1 four); keepers, no injuries listed.
- curl: https://understat.com/getTeamData/Lyon/2025 and /2026; https://understat.com/getLeagueData/Ligue_1/2025 and /2026 — Lyon xG, shots, first-half goals, formation minutes; Ligue 1 table (Lyon 4th, 18-6-10, 53–40, 60 pts) and league goal rates (306 matches: 2.82, 52.6% O2.5, 50.7% BTTS, 46.1% home wins).
- curl: https://data.fotmob.com/stats/40/season/27152/ and /37803/ (Pro League), /53/season/27212/ and /37298/ (Ligue 1), /73/season/28190/ (Europa League) — xG, corners, cards, fouls, possession, clean sheets.
- WebSearch: "Anderlecht Lyon Europa League 16 septembre 2026 compositions probables absents blessés Vitor Bruno Fonseca" — titrespresse, BeFoot, AfricaFoot, Foot Mercato live: probable XIs; Hey, Sardella, Camara, Biancone injured, Koutsoupias not registered; Lyon full squad; Duranville's academy club. Betting-preview pages ignored.
- WebSearch: "De Burgos Bengoetxea árbitro estadísticas temporada 2025-26 LaLiga tarjetas por partido penaltis" — career 365 matches, 4.37 yellows (snippet, not used in strip).
- WebSearch: "Anderlecht Lyon arbitre De Burgos Bengoetxea Ligue Europa désignation" — olympique-et-lyonnais.com, Lyonfoot, DH: full Spanish team (De Francisco, Masso Granado, Cordero, Soto Grado VAR, Muñiz Ruiz AVAR); previous Lyon–PAOK match. DH headline: Omobamidele for Biancone, Aasgaard surprise, Mata and Openda start.
- WebFetch (403): https://valuestats.com/en/referee/18637-ricardo-de-burgos-bengoetxea
- WebFetch: https://playerstats.football/referee/432 — season/competition split used (LaLiga 25/26 19 matches 3.95 Y 0.05 R 22.63 fouls; UEL 25/26 4 matches; UCL 25/26 2; LaLiga 24/25 19 matches 3.42 Y 0.21 R 21.84 fouls). 2026–27 lines internally inconsistent, not used.
- WebFetch: https://www.dhnet.be/sports/football/europe/c2/2026/09/16/qui-est-burgos-bengoetxea-... — background only (FIFA since 2018); no Anderlecht history, no statistics.

## f3 · Leverkusen – Celje (T1)
- WebSearch: "Bayer Leverkusen Transfers Sommer 2026 Zugänge Abgänge Ablöse Trainer Saison 2026/27" — sportschau, SPORT1, neunzigplus, Sky; Carles Martínez from 1 July 2026, €157m spent.
- WebSearch: "NK Celje prestopi poletje 2026 okrepitve odhodi trener sezona 2026/27" — Planet Nogomet, Ekipa, 24ur, Sportklub, SN portal, Celje.info: Karničnik, Nieto, Iosifov out; Kramer, Žužek, Širvys, Diounkou, Dukuly in.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Bayer_04_Leverkusen_season — manager, summer ins/outs (fees undisclosed), Martínez appointed 1 July.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Bayer_04_Leverkusen_season — ten Hag until 1 Sep 2025, Hjulmand from 8 Sep; Champions League and DFB-Pokal results.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Bundesliga — Hjulmand sacked 4 June 2026, Martínez appointed 4 June; Elversberg promoted (Bundesliga debut).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Bundesliga — fetched; grid incomplete (Understat used instead).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Slovenian_PrvaLiga — Celje champions, 23-5-6, 85–32.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Slovenian_PrvaLiga — managerial changes (Campelos out 14 Sep 2026, Zeljković in 15 Sep; Koper replaced Zeljković 15 Sep); table to 13 Sep (Celje 7th, 3-2-3, 11–11).
- curl (404): https://en.wikipedia.org/wiki/2026%E2%80%9327_NK_Celje_season and 2025–26.
- curl: https://www.fotmob.com/api/data/search/suggest?term=celje — Celje team id 4622, league 173.
- curl: https://www.fotmob.com/teams/4622/fixtures/celje and /squad — 2026–27 results (league, Champions League qualifying v Egnatia, Ararat-Armenia, Slovan Bratislava); positions; Pišek out to mid-January 2027.
- curl: https://www.fotmob.com/leagues/173/fixtures/prva-liga?season=2025/2026 and 2026/2027 — Slovenian results lists: Celje O2.5/BTTS/CS/FTS/home-away counted; league 2025–26 162 matches, 3.09 goals, 65.4% O2.5, 58.6% BTTS, 49.4% home wins.
- curl: https://data.fotmob.com/stats/173/season/27222/ and /38006/ — goals, clean sheets, reds only (no xG, cards, corners, fouls published).
- curl: https://www.fotmob.com/match/5787771, 5787783, 5954866, 5954876, 5987801, 5987808 — Celje qualifier match stats (possession, shots, corners all six; xG, cards, fouls only the two Slovan matches); first-half goals from match events.
- curl: https://www.fotmob.com/teams/8178/fixtures/leverkusen and /squad — 2026–27 results (DFB-Pokal, three Bundesliga); injuries (Tella, Culbreath, Maza, Eichhorn, Ben Seghir); keepers.
- curl: https://data.fotmob.com/stats/54/season/26891/ and /40040/ — Leverkusen xG, corners, cards, fouls, possession, clean sheets.
- curl: https://understat.com/getTeamData/Bayer_Leverkusen/2025 and /2026; https://understat.com/getLeagueData/Bundesliga/2025 and /2026 — shots, first-half goals, formation minutes; Leverkusen 6th, 59 pts, 68–47; Bundesliga 2025–26 3.24 goals, 63.7% O2.5, 61.8% BTTS, 43.8% home wins.
- WebFetch: https://neunzigplus.de/bundesliga/leverkusens-transfersommer-2026-im-detail-157-millionen-ausgegeben-37-millionen-minus — fees (Doué €30m, Moreira €29.5m, Diaby €28m, Gutiérrez €26m, Medina €23m from Marseille, Eichhorn €9m; Hincapié €40m, Alajbegović €32m, Palacios €22.5m, Grimaldo €15m, Kovář €5m). Conflicts logged: Medina's previous club (Wikipedia: Lens); Moreira's fee (Lyon Wikipedia: €33.6m).
- WebSearch: "Celje Vítor Campelos razrešen Zoran Zeljković novi trener Leverkusen liga Evropa" — 24ur, kicker, RTV SLO, Planet Nogomet, Tagesspiegel/dpa: Campelos dismissed Monday after four defeats in five; Zeljković from Koper, Celje assistant 2017–18; one training session.
- WebSearch: "Leverkusen Celje Europa League Aufstellung Personal Ausfälle Carles Martínez 16. September 2026" — kicker line-up page (listed XIs), bundesliga.com, baykusen: Boniface, Hofmann, Oermann, Eichhorn not registered; Tella, Culbreath injured.
- WebFetch: https://www.bundesliga.com/en/bundesliga/news/bayer-leverkusen-celje-live-europa-league-blog-preview-report-diaby-maza-39119 — Maza doubtful (cold), Flekken starts; Celje lost play-off to Slovan 3–2 on aggregate after extra time.
- WebSearch: "Jasper Vergoote scheidsrechter statistieken 2025-26 gele kaarten per wedstrijd strafschoppen Jupiler Pro League" — nl.wikipedia (Pro League since 2019, FIFA since 2022), voetbaluitslagen.be, WhoScored.
- WebFetch: https://voetbaluitslagen.be/voetbalcompetities/belgie/jupiler-pro-league/scheidsrechters/ — 2026–27: 4 matches, 11 Y, 2 R, 1 pen, 50 fouls; league 2.95 Y per match. No 2025–26 view.
- WebSearch: "Vergoote Schiedsrichter Leverkusen Celje Europa League" — Sofascore preview.
- WebFetch: https://www.sofascore.com/news/bayer-leverkusen-vs-nk-celje-europa-league-preview-at-bayarena — Vergoote career 181 matches, 689 Y, 18 Y-R, 25 R; Kotnik suspended; first competitive meeting. Form-trend lines on the page not used.

## f4 · Hapoel Be'er Sheva – Dinamo Zagreb (T1)
- WebSearch: "Hapoel Beer Sheva 2026-27 summer transfers signings departures coach Israeli Premier League" — FotMob team summary (Kozuch; Forson, Ugarriza, Malede, Amador, João Victor in; Koren, Lopes, Eliasi, Kangwa, Elias out), footballtransfers, Tribuna.
- WebSearch: "Dinamo Zagreb transferi ljeto 2026 dolasci odlasci trener sezona 2026/27" — nogometne-vijesti (March planning piece), BeSoccer; Kovačević coach. Completed ledger taken from Wikipedia.
- curl: https://www.fotmob.com/api/data/search/suggest — team ids (Be'er Sheva 9754, league 127; Dinamo 10156, league 252).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_GNK_Dinamo_Zagreb_season — manager, summer ledger with fees, league, cup and qualifying match boxes.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_GNK_Dinamo_Zagreb_season — manager; Europa League results; 23 league boxes with goal minutes (first-half goals counted, partial).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Israeli_Premier_League and /2026%E2%80%9327_Israeli_Premier_League — champions; managerial-changes tables (no Be'er Sheva change either season); championship round table (24-7-5, 79–38).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Hapoel_Be%27er_Sheva_F.C._season — no match boxes; 2026–27 page 404.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Croatian_Football_League and /2026%E2%80%9327_Croatian_Football_League — fetched for context.
- curl: https://www.fotmob.com/teams/9754/fixtures and /squad; https://www.fotmob.com/teams/10156/fixtures and /squad — 2026–27 results; coaches; injuries (Rotman, Ventura, Zlatanović; Goda, Dani Rodríguez, Stojaković); squad membership of reported arrivals.
- curl: https://www.fotmob.com/leagues/127/fixtures/ligat-haal?season=2025/2026, 2026/2027 and /leagues/252/fixtures/hnl?season=2025/2026, 2026/2027 — results lists: club O2.5/BTTS/CS/FTS/home-away counted; Israel 2025–26 240 matches 2.97 goals, 55.0% O2.5, 54.6% BTTS, 40.4% home wins; Croatia 180 matches 2.66, 48.9%, 52.2%, 45.6%.
- curl: https://data.fotmob.com/stats/127/season/1000000248/ and /1000000453/; /252/season/27123/ and /36345/ — corners, fouls, possession, clean sheets, shots on target, cards (Israeli yellow cards and both leagues' xG unavailable).
- curl: https://data.fotmob.com/stats/73/season/28190/ — Dinamo 2025–26 Europa League xG, corners, cards, fouls, possession.
- curl: https://www.fotmob.com/match/5787769, 5787781, 5954867, 5954877, 5987802, 5987809 (Be'er Sheva) and 5787768, 5787780, 5954862, 5954872, 5987800, 5987807 (Dinamo) — qualifier stats and first-half goals; xG/cards/fouls only where published (2 and 4 matches).
- WebSearch: "Hapoel Beer Sheva Dinamo Zagreb Bucharest Europa League preview team news suspended injured" — Yahoo, Sports Mole, WhoScored, 365scores; Be'er Sheva lost 6–4 on aggregate to Sabah; head-to-head 5–0 (2018–19). Betting-tip pages ignored.
- WebFetch: https://www.sportsmole.co.uk/football/hapoel-beer-sheva/europa-league/preview/h-beer-sheva-vs-dinamo-zagreb-prediction-team-news-lineups_605091.html — Diop and Peretz suspended; Biton heart problem; Levy, Stoyanov left out; Dinamo absentees and non-selected; Beljo 31 league goals last season, 7 goals 3 assists in five this season; probable XIs. Prediction section ignored.
- WebSearch: "John Brooks referee 2025/26 Premier League stats yellow cards per game fouls penalties" — aggregator snippet: 10 PL matches, 3.80 Y, 0.30 R, 20.80 fouls, 0.40 pens (conflict logged).
- WebFetch: https://playerstats.football/referee/227 — season/competition split used (PL 25/26 13 matches 4.15 Y 0.15 R 20.77 fouls; PL 24/25 16 matches 5.69 Y 0.06 R 22.63 fouls; UEL 25/26 2, 24/25 4; PL 26/27 3).
- WebSearch: "\"John Brooks\" referee Hapoel Beer Sheva Dinamo Zagreb Europa League" — Net.hr appointment ("John Brooks sudi Hapoel Be'er Sheva - Dinamo"); venue named Superbet Arena-Giulești, 22:00 local; UEFA top category, PL debut December 2021.

## f5 · Olympiacos – Jagiellonia Białystok (T1)
- WebSearch: "Ολυμπιακός μεταγραφές καλοκαίρι 2026 αποκτήσεις αποχωρήσεις προπονητής σεζόν 2026-27" — Sportal, SKAI, betting-site transfer lists (not used); no completed ledger in snippet.
- WebSearch: "Jagiellonia Białystok transfery lato 2026 przyszli odeszli trener sezon 2026/27" — mecze24, Meczyki, Gol24, FotMob; Siemieniec coach. Snippet arrivals (Szmyt, Konstantopoulos, Leiva, Bazdar, Montoia) not matched to FotMob's 2026 window; not used.
- curl: https://www.fotmob.com/api/data/search/suggest — Olympiacos 8638 (league 135), Jagiellonia 1957 (league 196).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Olympiacos_F.C._season — Mendilibar until 9 Sep 2026, Alguacil from 10 Sep; summer ledger with fees (€76.1m / €78.75m).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Super_League_Greece — managerial change (Mendilibar 9 Sep, 3rd; Alguacil 10 Sep).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Olympiacos_F.C._season — 18 league match boxes with goal minutes (first-half goals counted, partial); Champions League path.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Jagiellonia_Bia%C5%82ystok_season — 34 league boxes (33 with complete minutes; first-half goals counted); 2026–27 page 404.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Ekstraklasa, /2026%E2%80%9327_Ekstraklasa, /2025%E2%80%9326_Super_League_Greece — managerial tables (no Jagiellonia change).
- curl: https://www.fotmob.com/teams/8638/fixtures, /squad, /transfers and https://www.fotmob.com/teams/1957/fixtures, /squad, /transfers — 2026–27 results; injuries (El Kaabi out for season, Roca, Yazıcı; Sow); Jagiellonia summer moves with positions (fees not listed).
- curl: https://www.fotmob.com/leagues/135/fixtures/super-league?season=2025/2026, 2026/2027 and /leagues/196/fixtures/ekstraklasa?season=2025/2026, 2026/2027 — results lists and tables: Olympiacos 2nd (19-9-4, 51–17; regular season 17-7-2, 45–11), Jagiellonia 3rd (15-11-8, 56–41, 56 pts); club O2.5/BTTS/CS/FTS counted; Greece 236 matches 2.57 goals, 49.6% O2.5, 48.7% BTTS, 41.1% home wins; Poland 306 matches 2.74, 52.0%, 57.5%, 45.1%.
- curl: https://data.fotmob.com/stats/135/season/27184/ and /44734/; /196/season/27045/ and /37304/ — xG, corners, cards, fouls, possession, clean sheets.
- curl: https://www.fotmob.com/match/5954868, 5954878 (Olympiacos v NEC) and 5955032, 5955033, 5987960, 5987972 (Jagiellonia v Rangers, Iberia 1999) — qualifier possession, shots, corners, xG/cards where published, first-half goals.
- WebSearch: "Ολυμπιακός Γιαγκελόνια Αλγουασίλ αποστολή απουσίες Europa League 16 Σεπτεμβρίου" — Gazzetta, newsit, Fosonline, sport-fm, thrylos24, Newsbeast: 22-man squad; Fortounis suspended (Champions League qualifying red card); Gustavo Sá injured; Yaremchuk included.
- WebSearch: "Olympiakos Jagiellonia Liga Europy skład kontuzje Siemieniec zapowiedź sędzia Osmers" — Polsat Sport, Interia, Gol24, transfery.info: Kobayashi (centre-back) did not travel, long absence; Rangers 2:1/1:1, Iberia 4:0/2:1.
- WebSearch: "Harm Osmers Schiedsrichter Statistik 2025/26 Bundesliga Gelbe Karten pro Spiel Elfmeter" — fussballtransfers.com snippet: 4.6 yellows per match 2025–26 Bundesliga (4th); kicker, DFB Datencenter.
- WebFetch: https://www.fussballtransfers.com/deutschland/bundesliga/schiedsrichterstatistik — shows 2026–27 only; Osmers not in visible table.
- WebFetch (404): https://playerstats.football/referee/ ; WebFetch (403): weltfussball.de Osmers page; curl kicker Osmers page blocked (769 bytes).
- curl: https://datencenter.dfb.de/datencenter/personen/harm-osmers/schiedsrichter — Bundesliga since 2016, 138 Bundesliga matches, FIFA since 2020.
- WebSearch: "Όσμερς διαιτητής Ολυμπιακός Γιαγκελόνια Europa League" — Ta Nea, Sport24, in.gr, Onsports, sport-fm: appointment with Gittelmann, Dietz, Exner, Storks (VAR), Müller (AVAR). Betcosmos (betting) not used.
- WebFetch: https://www.sport-fm.gr/article/podosfairo/EuropaLeague/o-gnwrimos-osmers-sto-olumpiakos-giagkelonia/5147793 — team confirmed; no history details.
- WebFetch: https://www.tanea.gr/2026/09/14/sports/football/olympiakos-giagkelonia-o-osmers-diaititis-stin-premiera-tou-europa-league/ — eight Greek Super League matches incl. AEK 2–1 Panathinaikos (title-clinching); PAOK–Dinamo Zagreb, Conference League 2024.

## f6 · Sturm Graz – Rennes (T1)
- WebSearch: "SK Sturm Graz Transfers Sommer 2026 Zugänge Abgänge Ablöse Trainer Saison 2026/27" — weltfussball.at, 90minuten, sturmnetz.at (Mitchell €8m record defender sale; Karić, Lavalée out).
- WebSearch: "Stade Rennais mercato été 2026 arrivées départs officiels entraîneur saison 2026-27" — Maxifoot, dicodusport, Stade Rennais Online, titrespresse: Haise's contract extended; Jacquet to Liverpool, Brassier to Frankfurt; Dia, Cresswell, Thomasson, Lemaître in.
- curl: https://www.fotmob.com/api/data/search/suggest — Sturm 10014 (league 38), Rennes 9851 (league 53).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_SK_Sturm_Graz_season — manager Ingolitsch; summer ledger with fees; league, cup and qualifying boxes (first-half goals counted).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_SK_Sturm_Graz_season — 14 league boxes with minutes (partial first-half count).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Austrian_Football_Bundesliga — Säumel left 22 Dec 2025 (3rd), Ingolitsch appointed 29 Dec 2025 from Altach.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Austrian_Football_Bundesliga — no Sturm change this season.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Stade_Rennais_FC_season and /2025%E2%80%9326_Stade_Rennais_FC_season — Haise; Beye until 9 Feb 2026, Tambouret caretaker, Haise from 18 Feb; Jacquet £60m; Ligue 1 boxes (first-half goals counted).
- curl: https://www.fotmob.com/teams/10014/transfers, /squad and https://www.fotmob.com/teams/9851/transfers, /squad — summer moves with positions; injuries (Grgić, Soglo, Jatta); keepers.
- curl: https://www.fotmob.com/leagues/38/fixtures/bundesliga?season=2025/2026, 2026/2027 — Austrian results lists and table (Sturm 1st regular season 12-2-8, 2nd overall 16-8-8, 51–35); league 2.70 goals, 51.3% O2.5, 55.4% BTTS, 43.1% home wins.
- curl: https://data.fotmob.com/stats/38/season/27185/ and /38611/; /53/season/27212/ and /37298/; /73/season/28190/ — xG, corners, cards, fouls, possession, clean sheets; Sturm 2025–26 Europa League.
- curl: https://understat.com/getLeagueData/Ligue_1/2025 and /2026; https://understat.com/getTeamData/Rennes/2025 and /2026 — Rennes 6th, 59 pts, 59–50; shots and first-half goals 2025–26. Understat's 2026–27 Rennes log (6–3) disagrees with the published results (8–5) and was not used.
- WebSearch: "Sturm Graz Rennes Europa League Vorschau Ausfälle Ingolitsch Trainer seit" — 5min.at, ligaportal, ORF, Sports Mole, OneFootball: Ingolitsch since the winter; Jatta, Grgić, Weiper injured, Kayombo and Włodarczyk not registered, Diakité not ready to start (5min.at).
- WebSearch: "Sturm Graz Rennes Ligue Europa compos probables absents Haise 16 septembre 2026" — nothing relevant.
- WebFetch: https://www.sportsmole.co.uk/football/sturm-graz/europa-league/preview/sturm-graz-vs-rennes-prediction-team-news-lineups_605097.html — Grgić, Soglo injured, Jatta doubtful; Geyrhofer, Włodarczyk, Kayombo unregistered; Rennes no absentees; Rennes 6th and Lens's cup win; probable XIs (Rennes XI includes Frankowski, whose loan ended — not relied on; "no away European win in 10" contradicted by the 2–0 at Hearts — not used).
- WebSearch: "Manfredas Lukjančukas referee statistics cards per game UEFA 2025/26 A lyga penalties" — career 223 matches, 1,015 Y, 24 R (search summary).
- WebSearch: "Lukjančukas Schiedsrichter Sturm Graz Rennes Europa League" — kicker/weltfussball: Mirauskas, Stepanovas, Paulauskas, Ruperti (VAR), Manschot (AVAR).
- WebFetch: https://playerstats.football/referee/447 — UEFA splits: 2025–26 UEL 3 (5.00), UECL 3 (4.33), UCL 1 (1.00); 2024–25 UEL 2, UECL 2, UCL 4, Nations League 2.

## f7 · Sunderland – AZ Alkmaar (T1)
- WebSearch: "Sunderland summer 2026 transfers ins outs fees Europa League squad Le Bris 2026-27" — Sports Mole, Sunderland Echo, OneFootball, FotMob (Le Bris extension; 7th with 54 pts; record £161m 2025 window).
- WebSearch: "AZ Alkmaar transfers zomer 2026 aankopen vertrekkers transfersom trainer seizoen 2026/27" — goalscore.nl, voetbal.com, Voetbalkrant: Parrott to Betis €16m; Natali €2.2m; De Grand €1.5m.
- curl: https://www.fotmob.com/api/data/search/suggest — Sunderland 8472 (league 47), AZ 10229 (league 57).
- curl (raw wikitext): https://en.wikipedia.org/wiki/2026%E2%80%9327_Sunderland_A.F.C._season and /2025%E2%80%9326_Sunderland_A.F.C._season — Le Bris; 2025–26 7th, FA Cup fifth round, EFL Cup second round.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_AZ_Alkmaar_season — 7th; KNVB Cup winners (5–1 v NEC, 19 April 2026); Conference League quarter-finals (Shakhtar); 34 league boxes (first-half goals counted); 2026–27 page 404.
- curl (raw wikitext): https://en.wikipedia.org/wiki/2025%E2%80%9326_Eredivisie and /2026%E2%80%9327_Eredivisie — Martens left 18 Jan 2026 (8th); Echteld interim, permanent 8 May 2026.
- curl: https://www.fotmob.com/teams/8472/fixtures, /transfers, /squad and https://www.fotmob.com/teams/10229/fixtures, /transfers, /squad — 2026–27 results; summer moves with positions; injuries (Diarra, Mundle; Kasius, Resink); coaches.
- curl: https://www.fotmob.com/leagues/57/fixtures/eredivisie?season=2025/2026, 2026/2027 — AZ rates and table (7th, 52 pts, 58–51); Eredivisie 2025–26 309 entries, 3.17 goals, 61.5% O2.5, 62.8% BTTS, 44.7% home wins.
- curl: https://understat.com/getLeagueData/EPL/2025 and /2026; https://understat.com/getTeamData/Sunderland/2025 and /2026 — Sunderland 7th, 54 pts, 42–48; shots, first-half goals; EPL 2025–26 2.75 goals, 55.0% O2.5, 56.1% BTTS, 42.6% home wins.
- curl: https://data.fotmob.com/stats/47/season/27110/ and /36781/; /57/season/27131/ and /36577/ — xG, corners, cards, fouls, possession, clean sheets, shots on target.
- curl: https://www.fotmob.com/match/5781699, 5781707, 5781716, 5781724, 5781736, 5781742 (AZ) and 5795366, 5795433, 5795436, 5795453 (Sunderland) — 2026–27 league corners for/against, shots, first-half goals; Reinildo red card v Arsenal.
- WebSearch: "Sunderland AZ Alkmaar Europa League team news injuries Le Bris press conference 16 September 2026" — Yahoo (Le Bris press conference: Diarra and Mundle only injuries, minimal changes), Last Word on Sports, Sports Mole.
- WebFetch: https://www.sportsmole.co.uk/football/sunderland/europa-league/preview/sunderland-vs-az-prediction-team-news-lineups_605105.html — omitted squad players; Reinildo's ban domestic only; AZ injuries (Smit, Kasius, Resink) and Verhulst ineligible; AZ second, KNVB Cup route; AZ 3 wins in 22 v English clubs; probable XIs. Prediction ignored.
- WebSearch: "Jérémie Pignard arbitre statistiques 2025-26 Ligue 1 cartons par match penaltys" — statshub summary: 152 matches, 644 Y, 25 R, 22 second yellows, 74 penalties.
- WebFetch: https://playerstats.football/referee/63 — season/competition splits used (Ligue 1 25/26 17 matches 76 cards 397 fouls; Ligue 1 24/25 18 at 4.39, 21.22 fouls; UECL 25/26 3 at 5.00, 17.00 fouls; UCL 25/26 1; 26/27 Ligue 1 2, Super Cup 1, UECL 2).
- WebSearch: "Pignard referee Sunderland AZ Alkmaar Europa League officials appointed" — Sunderland Echo, OneFootball, safc.com: full French team (Drouet, Zakrani, Lissorgue, Dechepy VAR; Zebec AVAR); only English-club match Chelsea 2–0 Servette (2024).
- WebFetch: https://www.sportsmole.co.uk/football/sunderland/transfer-talk/feature/sunderland-summer-transfers-all-confirmed-ins-and-outs-for-2026_599274.html — fees (Méthalie £24m, Fofana £25.7m, Ahoka £8.6m; Mayenda £18.9m, Patterson £8m); updated 3 Sep 20:45, before Danso. Conflicts logged: Fofana fee (Lyon Wikipedia €35m); Adingra loan vs free (FotMob).
