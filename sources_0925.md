# sources_0925

## Triage
- ESPN public scoreboard, uefa.nations, 20260925 (and 20260904–20260924 for prior 2026–27 events): https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925&limit=200 — pipeline pull, not a search.
- ESPN standings, uefa.nations, seasons 2026, 2024, 2022, 2020: https://site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season=2026 — group membership, matches played, prior-edition finishing positions. Pipeline pull, not a search.
- Searches spent: 0 of 6.

## f1 · Georgia – Northern Ireland (T1)

Searches spent: 8 — Georgia 2 (ceiling 5: no coach change inside the window, not promoted), Northern Ireland 3 (ceiling 9: promoted), 1 shared xG search, referee 2 (appointment, record); no separate preview search (preview pages came up in the team searches). Baseline: 0 searches, League B recomputed from ESPN and written to baselines_0925.md (matches the 0924 League B entry).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925` — event 401861049 ("Northern Ireland at Georgia"), kickoff 16:00Z, Boris Paichadze Dinamo Arena, Tbilisi; team ids Georgia 584, Northern Ireland 586.
- `…/uefa.nations/summary?event=401861049` — no rosters or officials published at 12:44 CEST. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{584,586}/schedule?season={2024,2025,2026}` — every Georgia and Northern Ireland match since September 2024; no September 2026 match before today for either.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly}/summary?event={id}` — 40 summaries (Georgia 20, Northern Ireland 20): box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens; goal counts reconciled against the final score in all 27 competitive matches. No extra-time match. No usable box score for Georgia's six friendlies or for four of Northern Ireland's seven (results only).
- `site.web.api.espn.com/apis/v2/sports/soccer/{uefa.nations?season={2020,2022,2024,2026}, fifa.worldq.uefa?season=2025}/standings` — Groups B1 and C3 2024–25, 2026–27 Group B2, WCQ Groups A and E, 2020–21 and 2022–23 placings; the sides promoted from League C into League B for 2022–23 and 2024–25.
- `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}` + 90 summaries — League B baselines and the eight promoted sides' League B records (46 matches, venue split, matchday-one results).
- `…/{uefa.champions, uefa.europa, uefa.europa.conf} 202407–202505, 202507–202605, 202607–202609; uefa.nations 202409–202411, 202503, 202506, 202603, 202609; fifa.worldq.uefa 202503, 202506, 202509–202511, 202603; fifa.world 202606–202607; uefa.super_cup 202408, 202508, 202608` scoreboards + 1,605 summaries (mostly cached from the 0924 runs) — Grinfeld's UEFA and international matches in ESPN's record (11 since July 2024). ESPN returned no Israeli league events (`isr.1`).

Web:
- Search "Georgia national team squad Nations League Northern Ireland September 2026 head coach call-ups injuries" → ESPN https://www.espn.com/soccer/story/_/id/50003532/georgia-vs-northern-ireland-nations-league-2026-tv-channel-how-watch-uk-kick-live-stream-referee-line-ups fetched (referee TBC; Northern Ireland out: Bradley, McCann, Lyons; Georgia no major injuries, 27-man squad, Mamageishvili the one uncapped player; predicted elevens incl. Dion Charles and Azarovi — contradicted by UEFA's list, not used); Sports Mole https://www.sportsmole.co.uk/football/northern-ireland/uefa-nations-league/preview/georgia-vs-northern-ireland-prediction-team-news-lineups_605651.html fetched (Kvaratskhelia captain, Dvali and Kharebashvili, predicted shapes; venue "Stadioni Ragbi Arena" contradicted, not used); UEFA.com https://www.uefa.com/uefanationsleague/match/2048014--georgia-vs-northern-ireland/lineups/ fetched (both 23-man lists, coaches; no elevens or officials); Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_B fetched (Group B2, venue, kickoff, referee Orel Grinfeld ISR; its "relegated from League A" for Georgia and Ukraine contradicted by ESPN's standings, not used); search summary (Sagnol appointed February 2021, continues).
- Search "Northern Ireland squad Nations League Georgia Tbilisi September 2026 Michael O'Neill injuries withdrawals" → Irish News https://www.irishnews.com/sport/soccer/georgia-vs-northern-ireland-tv-channel-kick-off-time-and-how-to-watch-nations-league-clash-45ODMFEZENB33GAVRYJLQU3OC4/ fetched (22 Sept: venue, kickoff, last meeting a 2008 friendly won 4–1 by Northern Ireland; the page's price lines were not carried); Newsletter pages https://www.newsletter.co.uk/sport/football/northern-ireland/northern-ireland-matchday-squad-confirmed-with-four-players-set-to-miss-out-on-georgia-selection-9177232 and https://www.newsletter.co.uk/sport/football/michael-oneill-asks-fans-not-to-put-pressure-on-young-northern-ireland-side-9173530 returned 403; search summary (28-man squad, average age 24, four teenagers, Bradley knee, McCann hamstring, Lyons and McDonnell knee).
- Search "Georgia v Northern Ireland Nations League 25 September 2026 referee appointed" → search summary (Orel Grinfeld); Wikipedia League B page as above.
- Search "Guram Kashia retires Georgia national team Sagnol squad September 2026 …" → Georgia Today https://georgiatoday.ge/guram-kashia-plays-final-match-for-georgia/ fetched (3 June 2026: Kashia's last match, v Romania, 129 caps); search summary (Kvaratskhelia captain; Mamageishvili the only newcomer). No source on Gvelesiani, Gocholeishvili or Azarovi.
- Search "Northern Ireland squad Georgia Hungary Ukraine O'Neill Dion Charles Jamie Reid left out Eoin Toal Bradley knee September 2026" → Irish FA https://www.irishfa.com/news/2026/september/northern-ireland-squad-for-unl-quadruple-header-named fetched (15 Sept: full 28-man squad with clubs, nine returnees, standby Southwood, Clarke, Reid; injured McCann, Lyons, Bradley; four fixtures and venues). 112.ua and lovebelfast results not opened.
- Search "Michael O'Neill Northern Ireland manager contract extension second spell appointed December 2022 Euro 2028" → search summary of Irish FA https://www.irishfa.com/news/2026/may/michael-o-neill-signs-four-year-extension-as-northern-ireland-manager (May 2026, four-year extension to 2032) and Irish Times https://www.irishtimes.com/sport/soccer/2022/12/07/the-right-man-for-the-job-michael-oneill-returns-as-northern-ireland-manager/ (return, 7 December 2022). Pages not opened.
- Search "Orel Grinfeld referee statistics yellow cards per game penalties Ligat Ha'Al 2025-26" → playerstats.football https://playerstats.football/referee/457 fetched (Ligat ha'Al 2024–25: 19 matches, 95 yellows; 2023–24: 19, 91; 2026–27: 3, 3 yellows, 71 fouls; career 442 fixtures, 1,969 yellows, 51 reds; tonight listed as next fixture; 2024–25 Champions League 2 and 2026–27 Europa and Conference League 1 each, contradicted by ESPN's record); worldfootball.net https://www.worldfootball.net/referee_summary/orel-grinfeld/ returned 402. WhoScored, BDFutbol, BeSoccer results not opened.
- Search "Georgia Northern Ireland expected goals xG per match World Cup qualifying 2025 …" (shared) → FotMob https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams fetched (Georgia 6.8 xG on 7 goals, Northern Ireland 5.1 on 7; matches counted not stated; no xGA table). Betting-preview results (Racing Post, Football Whispers, Sportsgambler, xGscore) not opened.

## f2 · Armenia – Latvia (T1)

Searches spent: 8. Armenia 3 (ceiling 5: coach appointed August 2025, outside the window; not promoted), Latvia 3 (ceiling 5), 1 shared preview search, 1 referee record search. No separate appointment search: the referee was named on the Wikipedia League C page reached through the second Latvia search, and playerstats.football lists the match as his next fixture. Baseline: 0 searches. League C was computed from ESPN and written to baselines_0925.md, the first League C entry in the archive.

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861050 ("Latvia at Armenia"), kickoff 16:00Z, Vazgen Sargsyan Republican Stadium; team ids Armenia 579, Latvia 456.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{579,456}/schedule?season={2024,2025,2026}`: every Armenia and Latvia match since August 2024. Armenia has no match after 9 June 2026. Latvia has no match after 31 March 2026.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly}/summary?event={id}`: 37 summaries (Armenia 19, Latvia 18). They supplied box scores, key events (goals, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the final score in all 30 competitive matches. No extra-time match. No usable box score for any of the seven friendlies.
- `site.api.espn.com/apis/v2/sports/soccer/fifa.worldq.uefa/standings?season=2025`: Groups F and K final tables.
- `…/uefa.nations/standings?season={2022,2024,2026}`: Group C4 2024–25 final table, 2026–27 Group C2, and movement between divisions.
- `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}` plus 96 summaries: the League C baselines. The commentary of event 698999 gave the Romania – Kosovo abandonment.
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607) and `uefa.super_cup` (202408, 202508, 202608), plus 1,605 summaries (cached from the f1 run). These covered Matoša's matches in ESPN's record: 758012 Rapid Vienna – Craiova and 758049 Shelbourne – Crystal Palace. The Slovenian league query (`svn.1`) returned HTTP 400.

Web:
- Search "Armenia national team squad Nations League Latvia September 2026 head coach call-ups injuries":
  - sportaran https://sportaran.com/en/post/sbornaya-armenii-obyavila-sostav-na-matchi-ligi-nacij-debyut-garibyana-i-vozvrashenie-terteryana/ fetched. 17 September: 29-man squad, Gharibyan's first call-up, Terteryan's return, eight injured players, four fixtures.
  - sportaran https://sportaran.com/en/post/sbornaya-armenii-nazvala-okonchatelnuyu-zayavku-na-match-s-latviej-v-spiske-23-futbolista/ fetched. Final 23; five omitted with no reason given.
  - UEFA.com https://www.uefa.com/uefanationsleague/match/2048017--armenia-vs-latvia/lineups/ fetched. Both 23-man lists and both coaches; no elevens and no officials.
  - Search summary: Mkrtchyan injured, replaced by Petrosyan.
- Search "Latvia national team squad Armenia Yerevan Nations League September 2026 coach injuries":
  - sportaran https://sportaran.com/en/post/latviya-poteryala-odnogo-iz-liderov-pered-matchem-s-armeniej/ fetched. Ikaunieks injured in RFS training; Čudars called up; Dašķevičs stays.
  - inbox.eu https://news.inbox.eu/150shu8-latvia-s-national-football-team-begins-its-uefa-nations-league-campaign-first-opponent-armenia?language=en fetched. Seven debutants, Grabovskis to miss the match, fixtures, six all-time meetings.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_C fetched. Group C2, venue, referee Martin Matoša (Slovenia); kickoff given as "18:00 CET", recorded as a contradiction.
  - Goal.com, beIN, 365scores and the betting-preview results were not opened.
- Search "Yeghishe Melikyan appointed Armenia head coach date contract Petrakov":
  - Search summary: appointed 6 August 2025, contract to November 2026, replaced John van 't Schip; Petrakov left 13 October 2024.
  - Wikipedia https://en.wikipedia.org/wiki/Yegishe_Melikyan fetched. 6 August 2025; Pyunik 2021–2025; no end date for van 't Schip.
  - Armradio https://en.armradio.am/2025/08/06/yeghishe-melikyan-appointed-head-coach-of-armenian-national-team/ and Armenpress were not opened.
- Search "Paolo Nicolato Latvia head coach appointed contract extension 2026":
  - Search summary: appointed 5 February 2024; short-term extension in December; extension to the end of 2027 in May 2026.
  - Baltic Football News https://balticfootballnews.com/paolo-nicolato-extends-latvia-contract-until-end-of-2027/ was not opened.
- Search "Martin Matoša referee statistics yellow cards per game penalties 2025-26":
  - playerstats.football https://playerstats.football/referee/1609 fetched. Season and competition table; career 111 fixtures, 478 yellows, 7 reds; tonight listed as his next fixture.
  - corner-stats https://corner-stats.com/martin-matoa/slovenia/referee/5532 fetched with no data table.
  - worldfootball.net, BeSoccer and football-lineups were not opened.
- Search "Armenia vs Latvia preview team news 25 September 2026 Nations League …" (shared):
  - Search summary only. Armenia's last win was 2–1 v Ireland; Mkrtchyan injured; six all-time meetings.
  - Every result was a betting-preview page, and none was opened.
- Search "Latvija izlase sastāvs Nāciju līga Armēnija Nicolato …":
  - sportacentrs https://sportacentrs.com/futbols/latvijas_izlase/25092026-latvijas_izlase_naciju_ligas_jauno_celien fetched. 26-man squad with clubs, Ikaunieks out, Cirkins available for the first two matches only. It dates the 2024–25 meetings to 2025, which ESPN contradicts.
  - sportacentrs https://sportacentrs.com/futbols/latvijas_izlase/21092026-nikolato_citati_neuzvaresana_man_ir_loti_ fetched. Nicolato: Šits and Kroļļis injured, a 3-4-3 base with 4-4-2 and 5-3-2 options, a shortage of centre-backs.
  - tv3.lv and jauns.lv were not opened.
- Search "Lucas Zelarayán Varazdat Haroyan Armenia national team 2026 retired not called up Melikyan":
  - Search summary of Canal Showsport https://canalshowsport.com.ar/lucas-zelarayan-no-jugara-mas-en-la-seleccion-de-armenia/ and sportaran. Zelarayán left the national team for personal reasons, confirmed by Melikyan; Haroyan retired in June 2025.
  - Pages were not opened.

## f3 · Italy – Belgium (T1)

Searches spent: 10. Italy 3 (ceiling 9: coach change, Mancini appointed 28 July 2026), Belgium 3 (ceiling 9: coach change, van Bommel appointed July 2026), 1 shared xG search, referee 2 (appointment, record). The shared preview (Sports Mole) and the Wikipedia League A page came through the first Italy search, so there was no separate preview search. Baseline: 0 searches. League A recomputed from ESPN and written to baselines_0925.md (matches the 0924 League A entry).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861052 ("Belgium at Italy"), kickoff 18:45Z, Olimpico, Roma; team ids Italy 162, Belgium 459.
- `…/uefa.nations/summary?event=401861052`: no rosters or officials published at 14:10 CEST. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{162,459}/schedule?season={2024,2025,2026}` plus monthly scoreboards `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly}/scoreboard?dates={202409–202411,202503,202506,202509–202511,202603,202606,202609}`: every Italy and Belgium match since September 2024. The schedule endpoint omitted Belgium 3–1 Israel (698897, 6 September 2024); the monthly scoreboard supplied it. No September 2026 match before today for either side.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/summary?event={id}`: 46 summaries (Italy 20, Belgium 26). They supplied box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the 90-minute score in all 40 competitive matches. Two matches went to extra time: Bosnia-Herzegovina – Italy (761952, shoot-out 4–1) and Belgium – Senegal (760493, 3–2 a.e.t.). For those, cards come from key events inside 90 minutes, fouls and corners from the commentary inside 90 minutes, and there is no 90-minute shot count. Every friendly has a box score.
- `…/uefa.nations/standings?season={2022,2024,2026}` (cached from f1/f2): Group A2 2024–25, 2026–27 Group A1, division history.
- `…/uefa.nations/scoreboard?dates={202206,202209,202409,202410,202411}` + 96 summaries: League A baselines.
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608) and `ger.1` (202408–202505, 202508–202605, 202608–202609), plus 2,253 summaries (mostly cached from earlier runs). These gave Siebert's 60 matches in ESPN's record since July 2024 (35 Bundesliga, 18 UEFA club, 7 international).

Web:
- Search "Italy national team squad Nations League Belgium September 2026 head coach call-ups injuries":
  - Sports Mole https://www.sportsmole.co.uk/football/italy/uefa-nations-league/preview/italy-vs-belgium-prediction-team-news-lineups_605669.html fetched. Coaches; Bastoni suspended; Dimarco, Cristante and Locatelli injured; Belgium absences; predicted shapes 4-3-3 and 4-2-3-1; four Italy wins in the last five meetings. Score predictions and any price lines were not carried.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_A fetched. Group A1, Stadio Olimpico, 20:45, referee Daniel Siebert (GER). Its "relegated from League A" for Belgium is contradicted by ESPN's play-off results and was not used.
  - Search summary: Mancini's first squad, ten players from outside Serie A, Ruggeri for Dimarco.
  - Yahoo, Khel Now and 101 Great Goals were not opened.
- Search "Belgium squad Nations League Italy Rome September 2026 coach call-ups injuries":
  - Football Italia https://football-italia.net/belgium-6-serie-a-players-nations-league-italy/ fetched. 28-man list with clubs, 18 September; it includes Trossard.
  - Search summary: van Bommel's first squad; Italy absences incl. Locatelli.
  - Yardbarker and The Hard Tackle were not opened.
- Search "Roberto Mancini appointed Italy coach again date Gattuso resigned 2026":
  - Euronews https://www.euronews.com/2026/07/28/roberto-mancini-returns-as-italy-coach-after-third-straight-world-cup-miss fetched. Appointed 28 July 2026; Gattuso resigned April 2026; Saudi Arabia from August 2023, Al-Sadd 2024. No June interim named.
  - CNN, Al Jazeera and FIFA pages were not opened.
- Search "Mark van Bommel appointed Belgium head coach date Rudi Garcia leaves 2026":
  - ESPN https://www.espn.com/soccer/story/_/id/49439835/belgium-name-mark-van-bommel-replace-rudi-garcia-manager fetched. Announced 24 July; Antwerp, Wolfsburg, PSV; World Cup quarter-final.
  - Search summary: beIN https://www.beinsports.com/en-us/soccer/fifa-world-cup-2026/articles/belgium-appoints-mark-van-bommel-as-new-head-coach-2026-07-25 dated 25 July; Garcia's contract ended 31 July; contract to Euro 2028. The two dates are not reconciled.
- Search "Mancini convocati Italia Belgio Turchia Nations League settembre 2026 lista Kayode Zoma Romano":
  - Tuttosport https://www.tuttosport.com/news/calcio/italia/2026/09/25-151449465/italia_la_lista_ufficiale_dei_23_convocati_di_mancini_contro_il_belgio_chi_sono_gli_11_in_tribuna fetched. Official 23 and the 11 left out, 25 September 09:55; Zaniolo out for fitness.
  - Search summary of Sky Sport https://sport.sky.it/calcio/nazionale/convocati-italia-mancini-nazionale-nations-league-settembre-2026 and Fanpage: 34 called, nine debutants; Fagioli, Zaniolo and Mandragora recalled; four autumn fixtures and venues. Pages not opened.
- Search "Belgium Trossard withdraws injured Van Bommel Courtois break Doku not selected Rode Duivels Italy":
  - FMT https://www.freemalaysiatoday.com/category/sports/2026/09/18/van-bommel-names-first-belgium-squad-with-eight-changes-from-world-cup fetched. Eight changes from the World Cup squad; uncapped goalkeepers; Doku and Onana injured; Meunier and Saelemaekers dropped; Witsel retired; Courtois excused.
  - Search summary of Goal.com https://www.goal.com/en-za/news/van-bommel-begins-his-mission-with-the-courtois-blow-belgium-s-squad-reveals-surprises/bltb940459e227723dc and napolimagazine/TMW https://www.napolimagazine.com/calcio/articolo/tmw-belgio-rifinitura-verso-l-italia-il-c-t-van-bommel-dovr-rinunciare-a-trossard-e-penders-24-09-2026: Trossard (bruised heel) and Penders (quadriceps) not travelling; Courtois agreement; van Bommel in charge from 15 August. Pages not opened.
- Search "Belgium World Cup 2026 expected goals xG per match team stats; Italy World Cup qualifying 2025 xG" (shared):
  - Opta Analyst https://theanalyst.com/articles/gennaro-gattuso-italy-world-cup-2026-play-offs fetched. Italy 140 qualifying shots, 0.11 xG per shot; Belgium 143 shots; Gattuso named June 2025; 4-4-2 in his first two matches.
  - RealGM xG tracker https://soccer.realgm.com/analysis/559/2026-FIFA-World-Cup-xG-Tracker-Results-Expected-Goals-Of-Every-Match returned 403.
  - Search summary: Belgium 1.35 xG v Egypt; source page not opened.
  - FotMob and FOX Sports results were not opened.
- Search "Daniel Siebert referee Italy Belgium Nations League Olimpico appointed UEFA":
  - Search summary of LaPresse https://uk.lapresse.it/sport-en/2026/09/23/nations-league-german-referee-siebert-to-take-charge-of-italy-v-belgium/ and Football Italia https://football-italia.net/german-referee-siebert-chosen-italy-vs-belgium/: UEFA appointment; assistants Seidel and Foltyn, VAR Dankert, AVAR Müller; 2025–26 Champions League final; Italy matches in 2019 and 2020. Pages not opened.
- Search "Daniel Siebert Schiedsrichter Statistik 2025/26 Bundesliga Gelbe Karten pro Spiel Elfmeter":
  - Search summary of Statz https://statz.ai/referee/daniel-siebert: 2025–26 Bundesliga 16 matches, 58 yellows, 2 reds, 20.88 fouls per match; no penalty figure.
  - kicker, weltfussball and fussballdaten were not opened.

## f4 · Turkiye – France (T1)

Searches spent: 8. Türkiye 4 (ceiling 9: promoted), France 2 (ceiling 9: coach change, Zidane appointed 28 July 2026), referee 2 (appointment, record). The shared preview (Sports Mole) came through the first Türkiye search, so there was no separate preview search. xG came from the FotMob qualifying tables opened directly, as on f1, not from a search. Baseline: 0 searches. League A read from baselines_0925.md (written on f3).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861053 ("France at Türkiye"), kickoff 18:45Z, Yildiz Entegre Kocaeli Stadyumu, Kocaeli; team ids Türkiye 465, France 478.
- `…/uefa.nations/summary?event=401861053`: no rosters or officials published when read. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{465,478}/schedule?season={2024,2025,2026}` plus monthly scoreboards `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/scoreboard?dates={202409–202411,202503,202506,202509–202511,202603,202606,202607,202609}`: every Türkiye and France match since September 2024. The schedule endpoint omitted France's first three 2024–25 Nations League matches (698898, 698918, 698943); the monthly scoreboards supplied them. No September 2026 match before today for either side.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/summary?event={id}`: 51 summaries (Türkiye 23, France 28). They supplied box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the 90-minute score in all 43 competitive matches. One match went to extra time: France – Croatia (723710, shoot-out); for it, cards come from key events inside 90 minutes, fouls and corners from the commentary inside 90 minutes, and there is no 90-minute shot count. Box-score and key-event card counts agree in every World Cup match. No usable box score for Türkiye's two June 2025 friendlies (results only).
- `…/uefa.nations/standings?season={2022,2024,2026}` (cached): Groups A2 and B4 2024–25, 2026–27 Group A1, and the League A finishes of the eight sides promoted from League B for 2022–23 and 2024–25.
- League A 2022–23 and 2024–25 match rows (96, from the f3 run): the promoted sides' League A record (48 matches, venue split, matchday-one results, corners).
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608) and `ger.1` (202408–202505, 202508–202605, 202608–202609), plus 2,253 summaries (cached from the f3 run). These gave Zwayer's 64 matches in ESPN's record since July 2024 (36 Bundesliga, 19 UEFA club, 9 international).

Web:
- Search "Türkiye squad Nations League France September 2026 Montella call-ups injuries":
  - Sports Mole https://www.sportsmole.co.uk/football/france/uefa-nations-league/preview/turkey-vs-france-prediction-team-news-lineups_605656.html fetched. Coaches; Çalhanoğlu and Yıldız injured; Saliba injured, Tchouaméni left out, Konaté withdrawn, Yoro as replacement; predicted elevens; six meetings, Türkiye W1 D1 L4. Score predictions and any price lines were not carried.
  - Daily Sabah https://www.dailysabah.com/sports/football/turkiye-face-nations-league-baptism-of-fire-against-tough-france fetched. Kökçü doubtful (toe); four first call-ups; Mbappé available after flu-like symptoms; first League A campaign; World Cup exits. Dates the match 24 September, contradicted by every other source.
  - Search summary: 29-man squad named 18 September, Okan Kocuk among the uncapped; Çalhanoğlu injured, Yıldız surgery on a fracture, Müldür and Rıdvan Yılmaz out, Söyüncü and Kaan Ayhan left out by choice; Yunus Akgün and Deniz Gül doubtful.
  - Khel Now, RotoWire, SI, WhoScored and tapmad results not opened.
- Search "France squad Nations League Türkiye September 2026 new head coach call-ups injuries":
  - Al Jazeera https://www.aljazeera.com/sports/2026/9/24/turkiye-vs-france-uefa-nations-league-teams-kickoff-time-lineups fetched. Kocaeli Stadium, 18:45 GMT; Deschamps's 14 years; six debutants; Mbappé captain; head to head.
  - Yahoo Sports https://sports.yahoo.com/articles/france-roster-2026-uefa-nations-114344432.html fetched. Full 23 with clubs and caps, named 18 September; omissions; Konaté (knee sprain) and Zaïre-Emery (replaced by Akliouche) withdrawals.
  - Goal.com https://www.goal.com/en/news/turkiye-france-uefa-nations-league-preview/blt6f487c5fe2ffedd2 fetched. Predicted elevens (4-2-3-1 and 4-3-3); Saliba back injury, Tchouaméni groin; "no injuries or suspensions confirmed" for Türkiye, superseded by later reports.
- Search "Türkiye France Nations League 25 September 2026 referee appointed UEFA hakem":
  - Search summary: Felix Zwayer.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_A fetched. Group A1 fixtures and venues, Kocaeli Stadium, 20:45 CET, referee Felix Zwayer (GER); Türkiye promoted via the A/B play-off.
  - UEFA.com, FotMob, Yeni Şafak, 101 Great Goals and TFF results not opened.
- Search "Felix Zwayer referee statistics 2025-26 yellow cards per game penalties Türkiye matches":
  - Search summary (Statz, statshub, valuestats): 74 yellows in 16 Bundesliga matches 2025–26; 163 yellows, 9 reds, 21.27 fouls and 0.35 penalties per match across 2025–26. Not reconciled with ESPN's box scores.
  - Wikipedia https://en.wikipedia.org/wiki/Felix_Zwayer fetched. UEFA Elite; 2025 Europa League final, 2023 Nations League final, Euro 2024, World Cup 2026 (USA–Australia); 2005 Hoyzer case ban; no Türkiye match mentioned (ESPN's record has two).
  - WhoScored, playerstats.football, football-lineups, worldreferee, adamchoi and kickoffscore not opened.
- Search "Zinedine Zidane appointed France head coach date contract Deschamps final match July 2026":
  - Search summary of CNN https://www.cnn.com/2026/07/28/sport/zinedine-zidane-france-head-coach, Al Jazeera and Xinhua: announced 28 July 2026, four-year contract to the end of the 2030 World Cup. Pages not opened.
- Search "Vincenzo Montella Türkiye contract extension after World Cup 2026 stays head coach":
  - Search summary of Daily Sabah (two-year extension, June 2025) and Goal.com (TFF president Hacıosmanoğlu keeps Montella after the World Cup exit). Pages not opened.
  - Wikipedia https://en.wikipedia.org/wiki/Vincenzo_Montella fetched. Unveiled 21 September 2023; Euro 2024 quarter-final; A/B play-off 6–1 on aggregate; World Cup play-off wins over Romania and Kosovo; group-stage exit.
- Search "Montella A Milli Takım aday kadro Fransa İtalya Belçika Eylül 2026 …":
  - Milli Gazete https://www.milligazete.com.tr/a-milli-takim-uefa-uluslar-a-ligi-2026-aday-kadrosu-29-kisilik-kadroda-hangi-isimler-var fetched. Full 29 by position with clubs, dated 19 September; four first call-ups; Çalhanoğlu, Yıldız and Müldür absent, no reasons given.
  - One search summary dates the France match 26 September, contradicted by every other source. Fanatik, Akşam and other results not opened.
- Search "Türkiye Fransa maçı muhtemel 11 Orkun Kökçü parmak sakatlık Yunus Akgün Deniz Gül son durum Kocaeli":
  - Search summary: Kökçü not expected to play after missing Monday's and Tuesday's training (toe); Deniz Gül, Muhammed Şengezer and Yunus Akgün back in training; predicted elevens. NTVSpor, TGRT, haber7, Yeni Şafak, sporx and others not opened.
- FotMob, opened directly with no search: https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams and https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_conceded_team/world-cup-qualification-uefa-teams: Türkiye 11.8 xG on 19 goals, 9.7 xG conceded on 12; France 16.3 on 16, 3.4 on 4; match counts not shown.

## f5 · Hungary – Ukraine (T1)

Searches spent: 8. Hungary 3 (ceiling 5: no coach change, not promoted), Ukraine 2 (ceiling 9: coach change, Maldera appointed 18 May 2026), 1 shared preview search (head to head), referee 2 (appointment, record). The Sports Mole preview came through the first Hungary search. xG came from the FotMob qualifying tables opened directly, as on f1 and f4, not from a search. Baseline: 0 searches. League B read from baselines_0925.md (written on f1).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861054 ("Ukraine at Hungary"), kickoff 18:45Z, Puskás Aréna, Budapest; team ids Hungary 480, Ukraine 457.
- `…/uefa.nations/summary?event=401861054`: no rosters or officials published at 14:42 CEST. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{480,457}/schedule?season={2024,2025,2026}`, cross-checked against monthly scoreboards `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly,fifa.world}/scoreboard?dates={202409–202411,202503,202506,202509–202511,202603,202605,202606,202609}`: every Hungary and Ukraine match since September 2024; the two lists agree. No September 2026 match before today for either side.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly}/summary?event={id}`: 40 summaries (Hungary 20, Ukraine 20). They supplied box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the final score in all 29 competitive matches. No extra-time match. No usable box score for Hungary's June 2025 friendlies (Sweden, Azerbaijan) or for Ukraine's friendlies with Canada, New Zealand, Albania and Poland.
- `…/fifa.worldq.uefa/summary?event=724993`: key events for Sallai's red card (52').
- `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}`: 2020–21 and 2022–23 League A fourth places (the sides relegated into League B for 2022–23 and 2024–25), their League B group finishes, 2024–25 Groups A3 and B1, 2026–27 Group B2.
- League B 2022–23 and 2024–25 match rows (90, from the f1 run): the relegated sides' League B record (46 matches, venue split, matchday-one results, corners).
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202206, 202209, 202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608), `eng.1` (202408–202505, 202508–202605, 202608–202609), `eng.fa` (202408–202505, 202508–202605) and `eng.league_cup` (202408–202503, 202508–202603, 202608–202609), plus 3,070 summaries (partly cached from earlier runs). These gave Gillett's 49 matches in ESPN's record since July 2024 (42 Premier League, 3 FA Cup, 2 League Cup, 1 World Cup qualifier, 1 Europa League); cup matches without a box score are left out of every rate.

Web:
- Search "Hungary squad Nations League Ukraine September 2026 head coach call-ups injuries":
  - Sports Mole https://www.sportsmole.co.uk/football/hungary/uefa-nations-league/preview/hungary-vs-ukraine-prediction-team-news-lineups_605652.html fetched. Coaches (Maldera appointed May 2026); Sallai and Varga unavailable; Malinovskyi missing; predicted elevens in 4-2-3-1 (Ukraine's includes Shaparenko and Yaremchuk, neither in UEFA's 23). Score predictions and any price lines were not carried.
  - UEFA.com https://www.uefa.com/uefanationsleague/match/2048012--hungary-vs-ukraine/lineups/ fetched. Both 23-man lists and both coaches; no elevens and no officials.
  - 112.ua https://112.ua/en/ugorsina-ogolosila-zaavku-na-ligu-nacij-u-grupi-ukraina-pivnicna-irlandia-ta-gruzia-185919 fetched. Hungary's 26 named 18 September; no names on the page.
  - TNT Sports, 365Scores, Tips.GG, 7msport and FotMob results not opened.
- Search "Andrea Maldera appointed Ukraine head coach date Rebrov leaves 2026":
  - Wikipedia https://en.wikipedia.org/wiki/Andrea_Maldera fetched. Appointed 18 May 2026; assistant posts at Milan, Ukraine under Shevchenko (2016–2021), Brighton and Marseille under De Zerbi; no previous head-coaching post; Ukraine's first foreign coach.
  - Search summary of Rubryka https://rubryka.com/en/2026/05/18/zbirna-ukrayiny-otrymala-novogo-trenera-andrea-maldera-pidpysav-dvorichnyj-kontrakt/, Ukrinform and Interfax: two-year contract with an option; Rebrov's departure announced by Shevchenko on 21 April. Pages not opened.
- Search "Ukraine squad Maldera Nations League Hungary Budapest September 2026 Malinovskyi Mudryk Dovbyk Zinchenko injured not called":
  - 112.ua https://112.ua/en/pered-matcem-ligi-nacij-ukraina-proti-ugorsini-trener-maldera-povidomiv-pro-travmi-gravciv-187169 fetched. Ponomarenko ill but expected fit; Yaremchuk knee discomfort; nine absent (Mudryk, Zinchenko, Malinovskyi, Yarmoliuk, Konoplia, Hutsuliak, Dovbyk, Stepanov, Andriievskyi); seven on standby. The page dates itself 24 September 2024, contradicted by the match date.
  - Mezha https://mezha.net/eng/news/1e332010_ukraine_names_23-player/ fetched. Final 23 and the seven left out (Mykhailichenko, Mykhavko, Shaparenko, Varfolomeyev, Pikhalionok, Veleten, Yaremchuk).
  - Search summary: Dovbyk injured at his club; "financial constraints" on calling up foreign-based players, not confirmed by any page read and not used. UNN and other 112.ua results not opened.
- Search "Marco Rossi Hungary contract after World Cup qualifying failure stays coach 2026 Sallai Varga injured keret szeptember":
  - Daily News Hungary https://dailynewshungary.com/marco-rossi-hungarian-football-team-ireland/ fetched. 25 November 2025: resignation offered after the Ireland defeat, rejected by the MLSZ board; contract to 2030.
  - Hungary Today https://hungarytoday.hu/291550-2/ fetched. July 2024 confirmation of Rossi; in charge since summer 2018.
  - FIFA, Wikipedia and sportaran results not opened.
- Search "Rossi keret Nemzetek Ligája Ukrajna Észak-Írország 2026 szeptember Sallai Varga Barnabás sérült Dibusz Négo Szalai hiányzik":
  - Index https://index.hu/sport/futball/2026/09/24/nemzetek-ligaja-2026-2027-b-liga-magyar-valogatott-marco-rossi-keret-ukrajna-georgia-eszak-irorszag fetched. Sallai, Varga and Styles injured; possible move from 4-2-3-1 to 4-3-2-1; four fixtures and dates. Its mention of a "József Szalai" as a forward option is not matched in UEFA's 23.
  - Index https://index.hu/sport/futball/2026/09/15/magyar-labdarugo-valogatott-kerethirdetes-nemzetek-ligaja-b-marco-rossi-telki-sajtotajekoztato/ fetched. Squad of 26 on 15 September; five newcomers; Dibusz out injured; Yaakobishvili left out after a transfer; Rossi on Alex Tóth.
  - Search summary: Dibusz "rested for fatigue", contradicting Index; Rossi on Ukraine's back four. Magyar Nemzet, Origo, 10perc, Esti Hírlap and Pénzcentrum not opened.
- Search "Hungary v Ukraine Nations League 25 September 2026 referee appointed játékvezető":
  - Sofascore https://www.sofascore.com/news/hungary-vs-ukraine-preview-nations-league-group-b2-opener-at-puskas-arena fetched. Referee Jarred Gillett (340 matches, 1,370 yellows, 28 reds); Varga (thigh) and Malinovskyi (knee) out; shapes 4-2-3-1 and 4-1-4-1.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_B fetched. Group B2 fixtures and venues, Puskás Aréna, 20:45, referee Jarred Gillett (England); Ukraine's home matches in Trnava.
  - Flashscore, beIN, VAVEL, 365Scores and the betting-preview results were not opened.
- Search "Jarred Gillett referee statistics 2025-26 Premier League yellow cards per game penalties fouls":
  - Statshub https://www.statshub.com/referee/gillett-jarred/138289 fetched. Career by competition (Premier League 90 matches, 3.86 yellows; Champions League 1, Conference League 2).
  - Wikipedia https://en.wikipedia.org/wiki/Jarred_Gillett fetched. Australian-born; FIFA list for Australia 2013–2019 and for England since 2023; first Premier League match September 2021; no Hungary or Ukraine match mentioned.
  - Search summary: five Premier League penalties "this season" (season not stated; ESPN's record differs). Squawka and the Wikipedia season pages not opened.
- Search "Hungary vs Ukraine head to head history previous meetings last met friendly 2026 Nations League preview" (shared):
  - Sky Sports https://www.skysports.com/football/hungary-vs-ukraine/553991 fetched. No head-to-head listed.
  - Search summary: two 1992 meetings won by Hungary; not confirmed by any page read, not used. AiScore, Tips.GG, Ratingbet and scores24 results not opened.
- FotMob, opened directly with no search: https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams and https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_conceded_team/world-cup-qualification-uefa-teams: Hungary 8.3 xG on 11 goals, 10.5 xG conceded on 10; Ukraine 8.4 on 11, 12.5 on 14; match counts not shown.

## f6 · Poland – Bosnia and Herzegovina (T1)

Searches spent: 8. Poland 3 (ceiling 9: coach change, Urban appointed 16 July 2025), Bosnia and Herzegovina 3 (ceiling 5: no coach change, not promoted), referee 2 (appointment, record). No separate shared preview search: the Sofascore, Khel Now and Goal.com previews came through the team searches, and the competitive head to head came from ESPN. xG came from the FotMob qualifying tables opened directly, as on f1, f4 and f5, not from a search. Baseline: 0 searches. League B read from baselines_0925.md (written on f1).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861055 ("Bosnia-Herzegovina at Poland"), kickoff 18:45Z, PGE Narodowy; team ids Poland 471, Bosnia-Herzegovina 452.
- `…/uefa.nations/summary?event=401861055`: no rosters or officials published when read. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{471,452}/schedule?season={2024,2025,2026}`: every Poland and Bosnia match since June 2024. No September 2026 match before today for either side.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/summary?event={id}`: 44 summaries (Poland 20, Bosnia 24). They supplied box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the final score in all 36 competitive matches. The play-off ties Wales – Bosnia (761381) and Bosnia – Italy (761952) went to extra time; their 90-minute cards come from key events, and their fouls and corners from commentary. Friendlies with Moldova, New Zealand, Slovenia and Malta have no box score; those in 2026 have empty ones.
- `site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/teams/{471,452}/roster`: squads for this window (Poland 25, Bosnia 28).
- `…/uefa.nations/scoreboard?dates={202009,202010}`: the 2020–21 League A meetings (570754, 570707).
- `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2024,2026}`: 2024–25 Groups A1 and A3 finishes; 2026–27 League B membership.
- League B 2022–23 and 2024–25 match rows (90, from the f1 run): the relegated sides' League B record at home and away (23 each), matchday-one results, and Bosnia's 2022–23 Group B3 run.
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202206, 202209, 202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608) and `gre.1` (202408–202505, 202508–202605, 202608–202609), plus 2,260 summaries (partly cached from earlier runs). These gave Papapetrou's 49 matches in ESPN's record since June 2022 (36 Greek Super League, 13 UEFA club and international). `gre.cup` returned HTTP 400 for every month and is not in the record. His Greek box scores carry no cards for 19 of 36 matches, so league cards are counted from key events.

Web:
- Search "Poland squad Nations League Bosnia September 2026 head coach call-ups injuries":
  - Sofascore https://www.sofascore.com/news/poland-vs-bosnia-herzegovina-warsaw-showdown-kicks-off-their-nations-league-campaigns fetched. Referee Papapetrou (219 matches, 880 yellows, 17 reds); Benedyczak, Rózga and Grabara out; lists Lewandowski as unavailable, contradicted by UEFA's 23 and three previews; predicted elevens (Bosnia's includes Vasilj and Džeko); head to head. Any score predictions were not carried.
  - Extratimetalk https://extratimetalk.com/poland-uefa-nations-league-squad-2026/ fetched. Squad by position with clubs, dated 22 September; withdrawals (Grabara cruciate ligament, Drągowski, Rózga, Benedyczak) and replacements (Abramowicz, Reguła).
  - Goal.com https://www.goal.com/en-us/news/watch-poland-v-bosnia-and-herzegovina-live-stream-online-tv-channel/blt691df01e9108e5a0 fetched. Venue; predicted elevens; "no injury concerns" for Bosnia and Bosnia "atop Group 4", both contradicted.
  - Football Faithful, Football Whispers, Toffeeweb and Dailysports results (betting previews) not opened.
- Search "Bosnia and Herzegovina squad Nations League Poland September 2026 coach Džeko call-ups":
  - Khel Now https://khelnow.com/football/bosnia-herzegovina-squad-september-october-uefa-nations-league-fixtures-202609 fetched. Barbarez's squad of 24 plus four on standby, 7 September; Džeko's statement that the Sweden match on 2 October is his last.
  - Khel Now https://khelnow.com/football/poland-vs-bosnia-herzegovina-preview-uefa-nations-league-202609 fetched. Referee Papapetrou; coaches; calls every player fit and Džeko available (contradicted); head to head 2W 1D in three.
  - FotMob, UEFA.com World Cup page, ESPN squad page and Telecomasia results not opened.
- Search "Jan Urban Poland coach contract after play-off defeat Sweden March 2026 stays Nations League":
  - PZPN https://pzpn.pl/en/national-teams/national-team-a/news/2026-03-31/head-coach-jan-urban-s-contract-to-be-extended fetched. Kulesza's extension announcement, 31 March 2026; length not stated.
  - Wikipedia https://en.wikipedia.org/wiki/Jan_Urban fetched. Appointed 16 July 2025, replacing Probierz after the Lewandowski dispute; extension announced minutes after the Sweden defeat.
  - FIFA https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/poland-jan-urban fetched; page returned no content. Orla.fm, Extratimetalk and Flashscore results not opened.
- Search "Barbarez Bosnia contract after World Cup 2026 Dedić injury Džeko joins squad later Poland match":
  - Wikipedia https://en.wikipedia.org/wiki/Sergej_Barbarez fetched. Appointed 19 April 2024, four-year contract; qualifying route; nothing after the World Cup.
  - beIN, Yahoo, Olympics.com, FourFourTwo and FIFA World Cup squad pages not opened.
- Search "Lewandowski Polska Bośnia 25 września 2026 kadra Urban kontuzja Grabara skład Liga Narodów":
  - Search summary (WP, Weszło, Stolica Sportu): 20:45 at PGE Narodowy; Urban's 26 including Lewandowski; Benedyczak, Grabara and Drągowski out, Reguła and Abramowicz in. Pages not opened.
  - UEFA.com https://www.uefa.com/uefanationsleague/teams/109--poland/squad/ opened directly: Poland's 23, Lewandowski included; Monka and Wojtuszek not in it.
- Search "Džeko Dedić povreda Poljska Varšava Liga nacija reprezentacija BiH Barbarez septembar 2026":
  - Reprezentacija.ba https://reprezentacija.ba/532653-poljska-bih-tv-prijenos-izjave-statistika-sudija fetched. Dedić, Busuladžić and Vasilj injured; Barbarez's aim of a top-two finish.
  - Sportske https://sportske.ba/clanak/poljska-bih-bez-dzeke-vasilja-i-dedica-nakon-86-dana-zmajevi-traze-pobjedu-u-varsavi/ fetched. Without Džeko, Vasilj and Dedić; 86 days since the last match (ESPN's dates give 85); predicted eleven names a goalkeeper "Jurkas" who is in no squad list, not used.
  - SC Sport https://scsport.raport.ba/edin-dzeko-nece-biti-uz-zmajeve-protiv-poljske-evo-kako-je-prosao-posljednji-mec-bez-dijamanta fetched. Džeko rested for the first two matches, returns against Sweden on 2 October; dates the Canada draw 18 June (ESPN 12 June).
  - Search summary: Tahirović, Malić, Hasić and Đurić called in for Dedić and Busuladžić. Visoko.ba, Sportski puls, Hayat and Magazin Plus not opened.
- UEFA.com Bosnia squad page tried at https://www.uefa.com/uefanationsleague/teams/57166--bosnia-and-herzegovina/squad/ with no search; it returned Ukraine's squad and was not used.
- Search "Anastasios Papapetrou referee Poland Bosnia Nations League 25 September 2026 appointed sędzia":
  - Interia https://sport.interia.pl/pilka-nozna/reprezentacija-polski/news-uefa-oglasza-kluczowa-decyzja-ws-meczu-polakow-w-lidze-narod,nId,23547860 fetched. UEFA appointment; all-Greek team (Petropoulos, Patras, Polychronis; VAR Papadopoulos, Zabalas); Legia – Flora (2021) and Raków – Sporting (2023). The page dates itself September 2024, contradicted by the fixture.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_B fetched. Group B4 opener at Stadion Narodowy, 20:45, referee Papapetrou (Greece). Its summary says Bosnia went down through a play-off, which ESPN's standings contradict (fourth place, direct).
  - Search summary: Papapetrou 41, no previous Poland national-team match. Stolica Sportu, worldfootball.net and the Nations League A page not opened.
- Search "Anastasios Papapetrou referee statistics 2025-26 yellow cards per game penalties Super League Greece":
  - Statshub https://www.statshub.com/referee/papapetrou-anastasios/89007 fetched. Career by competition: Super League 155 matches, 4.08 yellows, 0.17 reds, 47 penalties; Nations League 4, 5.00 yellows; World Cup qualifying 5, 3.60.
  - Search summary: 13 Super League matches and 31 yellows in 2025–26 (ESPN's key events give 80 cards in 17); 2024–25 22 matches, 94 yellows, 488 fouls. Neither is used. SLGR, worldfootball.net, WhoScored, BDFutbol and football-lineups not opened.
- FotMob, opened directly with no search: https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams and https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_conceded_team/world-cup-qualification-uefa-teams: Poland 16.1 xG on 18 goals, 11.1 xG conceded on 11; Bosnia 17.6 on 19, 11.9 on 9; match counts not shown.

## f7 · Sweden – Romania (T1)

Searches spent: 9. Sweden 4 (ceiling 9: promoted, coach change — Potter appointed 20 October 2025), Romania 3 (ceiling 9: promoted, coach change — Hagi appointed April 2026), referee 2 (appointment, record). No separate shared preview search: the Sports Mole preview came through the first Sweden search, and the head to head came from the Swedish FA's match guide. xG came from the FotMob qualifying tables opened directly, as on f1, f4, f5 and f6, not from a search. Baseline: 0 searches. League B read from baselines_0925.md (written on f1).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861051 ("Romania at Sweden"), kickoff 18:45Z, Friends Arena, Stockholm; team ids Sweden 466, Romania 473.
- `…/uefa.nations/summary?event=401861051`: no rosters or officials published when read. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{466,473}/schedule?season={2024,2025,2026}`, cross-checked against monthly scoreboards `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/scoreboard?dates={202409–202411,202503,202506,202509–202511,202603,202605,202606,202609}`: every Sweden and Romania match since September 2024; the two lists agree. No September 2026 match before today for either side. `…/all/teams/466/schedule?season={2003…2023}` lists no Sweden–Romania meeting.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.world,fifa.friendly}/summary?event={id}`: 44 summaries (Sweden 24, Romania 20). They supplied box scores, key events (goal minute, side and scorer, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the final score in all 33 competitive matches except Romania – Kosovo (698999), abandoned at 0–0 and awarded 3–0, counted as played as in the League C baseline. No extra-time match. No usable box score for Sweden's 2025 friendlies or for Romania's friendlies with Canada, Moldova, Slovakia and Georgia (the last two empty).
- `site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/teams/{466,473}/roster`: Sweden 26 (matches the Swedish FA's squad after changes); Romania 41 (a stale preliminary list, not used for the 23).
- League B 2022–23 and 2024–25 match rows (90, from the f1 run): the promoted sides' League B record at home and away (23 each), matchday-one results, and the check that no two promoted sides shared a group.
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202206, 202209, 202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608) and `fifa.friendly` (202409–202411, 202503, 202506, 202509–202511, 202603, 202605, 202606, 202609), plus 2,304 summaries (mostly cached from earlier runs). These gave Berka's 12 matches in ESPN's record since July 2024 (8 UEFA club, 3 international, 1 friendly without card data). `cze.1` returned no events, so his Czech league matches are not in the record.

Web:
- Search "Sweden squad Nations League Romania September 2026 head coach call-ups injuries":
  - Sports Mole https://www.sportsmole.co.uk/football/sweden/uefa-nations-league/preview/sweden-vs-romania-prediction-team-news-lineups_605686.html fetched. Coaches (Hagi appointed April 2026); Elanga, Lagerbielke, Hien and Widell Zetterström out; predicted elevens (Romania's includes Bîrligea, contradicted by Digi24 and UEFA). Score predictions and any price lines were not carried.
  - Search summary: Svanberg withdrew 18 September; predicted 3-5-2. Khel Now, FotMob, Flashscore, Football Whispers, Ratingbet and Dailysports results not opened.
- Search "Romania squad Nations League Sweden September 2026 head coach call-ups injuries":
  - Romania Insider https://www.romania-insider.com/romania-football-team-sweden-nations-league-sept-2026 returned 429. Search summary only: Hagi coach; a side listing Drăguș, Moruțan and Marius Marin (contradicted); "fully fit squad" (contradicted). Not used for names.
  - Sportskeeda, Tips.GG and Ratingbet results not opened.
- Search "Gheorghe Hagi appointed Romania national team coach 2026 Lucescu replaced date contract":
  - ESPN https://www.espn.com/soccer/story/_/id/48554996/romania-great-gheorghe-hagi-returns-coach-national-team fetched. Announced 21 April 2026; contract to the 2030 World Cup; Lucescu fell ill and stepped down after the Türkiye play-off, died 7 April aged 80; 2001 spell of three months.
  - Search summary of Romania Insider https://www.romania-insider.com/gheorghe-hagi-coach-romania-football-team-2026 (appointment 20 April, four-year contract) and the Washington Post (21 April). Pages not opened.
- Search "lotul României Hagi Suedia Liga Națiunilor septembrie 2026 convocați accidentați Drăguș":
  - Digi24 https://www.digi24.ro/stiri/sport/fotbal/liga-natiunilor-selectionerul-gica-hagi-a-stabilit-lotul-pentru-meciul-cu-suedia-9-dintre-cei-32-de-tricolori-lasati-acasa-3962205 fetched. 24 September: the 32 with clubs and the nine left at Mogoșoaia; six-match group schedule.
  - Search summary (Digi Sport, Cotidianul, ziare.com): 33 called, Drăguș withdrew injured. Pages not opened.
- UEFA.com https://www.uefa.com/uefanationsleague/match/2048015--sweden-vs-romania/lineups/ opened directly with no search: both 23-man lists and both coaches; no elevens or officials. The match page itself showed no officials.
- Search "Potter truppen Sverige Rumänien Nations League september 2026 Lagerbielke skadad Svanberg Hien Elanga":
  - svenskfotboll.se https://www.svenskfotboll.se/nyheter/landslag/2026/09/herr-matchguide-rumanien-hemma/ fetched. Withdrawals (Ali, Nilsson, Svanberg) and replacements (Abraham, Larsson, Swedberg); Lagerbielke minor injury, Mellberg added; head to head 12 meetings, Sweden W6 D3 L3, 24–12; calls the World Cup exit round of 16 (ESPN: round of 32).
  - svenskfotboll.se https://www.svenskfotboll.se/nyheter/landslag/2026/09/trupp-nations-league/ fetched. Squad of 16 September; Hien, Elanga and Widell Zetterström injured; Nordfeldt left out, with Potter's comment.
  - Telgenytt, EM-fotboll, hurbra.se (predicted 4-4-2) and SVT not opened.
- Search "Graham Potter appointed Sweden head coach date Tomasson sacked contract extended after World Cup 2026":
  - Search summary (FootballTransfers, Soccerway): appointed 20 October 2025 after Tomasson's sacking (one point from four qualifiers); original deal to the end of the World Cup.
  - FIFA https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/graham-potter-sweden-contract fetched; page returned no content.
- Search "Graham Potter förlänger kontrakt förbundskapten Sverige 2026 till 2028":
  - Search summary: extension to 2030 (svenskfotboll.se https://www.svenskfotboll.se/nyheter/landslag/2026/03/graham-potter-forlanger/, Sveriges Radio, GP); SvenskaFans 12 March 2026; Kvartal headline "till 2028" (contradiction). Pages not opened.
- Search "Sverige Rumänien 25 september 2026 domare UEFA Nations League arbitru Suedia România":
  - Search summary: referee "TBA" in the results read. beIN, UEFA fixtures page and Tips.GG not opened.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_B fetched. Group B4 matchday 1 at Nationalarenan, Solna, 20:45 CET, referee Ondřej Berka (Czech Republic). Its seeding and standings lines are not used.
- Search "Ondřej Berka rozhodčí statistiky žluté karty 2025/26 Švédsko Rumunsko Liga národů delegace":
  - Eurofotbal https://www.eurofotbal.cz/clanky/berka-opakovane-chybuje-presto-ma-duveru-podle-dat-patri-mezi-sudimi-do-prumeru-824828/ fetched. 18 May 2026: 193 league matches in 11 seasons; about 3.1 yellows per match over two seasons against about 4.0 for the league; 2.8 career; "tolerant" style; no penalty or foul figures.
  - FAČR, fotbalpraha, chanceliga, csfotbal, eurofotbal card tables and worldfootball.net not opened.
- FotMob, opened directly with no search: https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams and https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_conceded_team/world-cup-qualification-uefa-teams: Sweden 9.6 xG on 10 goals, 11.7 xG conceded on 15; Romania 16.6 on 19, 9.2 on 11; match counts not shown.

## f8 · Montenegro – Cyprus (T1)

Searches spent: 9. Montenegro 3 (ceiling 5: Vučinić appointed 19 September 2025, outside the window; relegated, not promoted), Cyprus 3 (ceiling 5: Mantzios appointed January 2025; not promoted), 1 shared preview search (head to head), referee 2 (appointment, record). The Sports Mole preview came through the first Montenegro search. The referee was named on the Wikipedia League C page, opened after the appointment search returned no name. xG came from the FotMob qualifying tables opened directly, as on f1 and f4–f7, not from a search. Baseline: 0 searches. League C read from baselines_0925.md (written on f2).

Standing ESPN pipeline (not searches):
- `site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/scoreboard?dates=20260925`: event 401861056 ("Cyprus at Montenegro"), kickoff 18:45Z, Podgorica City Stadium; team ids Montenegro 6775, Cyprus 445.
- `…/uefa.nations/summary?event=401861056`: rosters empty and no officials published when read. Price fields in the same response were not read.
- `site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/{6775,445}/schedule?season={2024,2025,2026}`: every Montenegro and Cyprus match since November 2023. No September 2026 match before today for either side. Older season parameters return the same current list, so no head to head before 2024 comes from this endpoint.
- `…/{uefa.nations,fifa.worldq.uefa,fifa.friendly}/summary?event={id}`: 40 summaries (Montenegro 20, Cyprus 20). They supplied box scores, key events (goals, cards, penalty kicks), officials, venues, formations and starting elevens. Goal counts reconcile against the final score in 27 of 28 competitive matches. The exception is Wales 1–0 Montenegro (698976), which has no key events; its 36th-minute Wilson penalty is added from ESPN's commentary, as in the League B baseline. No extra-time match. No usable box score for any friendly (results only or empty for each side).
- `…/uefa.nations/scoreboard?dates={202009,202010,202011}` and summaries 570775 and 570654: the two 2020–21 meetings (Cyprus 0–2 Montenegro, GSP Stadium; Montenegro 4–0 Cyprus, Podgorica City Stadium).
- `site.api.espn.com/apis/v2/sports/soccer/uefa.nations/standings?season={2020,2022,2024,2026}`: 2020–21 and 2022–23 League B fourth places (the sides relegated into League C for 2022–23 and 2024–25), 2024–25 Groups B4 and C2, 2026–27 Group C2.
- `site.api.espn.com/apis/v2/sports/soccer/fifa.worldq.uefa/standings?season=2025`: Groups H and L final tables.
- `site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/teams/{6775,445}/roster`: Montenegro 28 (the wider squad), Cyprus 38 (a stale list, not used).
- League C 2022–23 and 2024–25 match rows (96, from the f2 run): the relegated sides' League C record (42 matches, venue split, matchday-one results, corners).
- Scoreboards for `uefa.champions, uefa.europa, uefa.europa.conf` (202407–202505, 202507–202605, 202607–202609), `uefa.nations` (202409–202411, 202503, 202506, 202603, 202609), `fifa.worldq.uefa` (202503, 202506, 202509–202511, 202603), `fifa.world` (202606–202607), `uefa.super_cup` (202408, 202508, 202608), `fifa.friendly` (202409–202411, 202503, 202506, 202509–202511, 202603, 202605, 202606, 202609), `ita.1` and `ita.coppa_italia` (202408–202505, 202508–202605, 202608–202609), plus 3,084 summaries (partly cached from earlier runs). These gave Chiffi's 39 matches in ESPN's record since August 2024 (34 Serie A, 1 Coppa Italia, 2 Conference League, 1 Nations League, 1 friendly). Atalanta – Genoa (5 October 2024) carries no cards in its box score or key events and is left out of his card and penalty rates.

Web:
- Search "Montenegro squad Nations League Cyprus September 2026 head coach call-ups injuries":
  - Sports Mole https://www.sportsmole.co.uk/football/cyprus/uefa-nations-league/preview/montenegro-vs-cyprus-prediction-team-news-lineups_605653.html fetched. Coaches; Cyprus's three first call-ups; Pikis left out; predicted elevens (including Hakšabanović and Sielis, both out); five meetings. It dates the match 23 September and places the 2020–21 wins at the opposite venues, both contradicted by ESPN. Score predictions and any price lines were not carried.
  - UEFA.com https://www.uefa.com/uefanationsleague/match/2048016--montenegro-vs-cyprus/lineups/ fetched. Both 23-man lists and both coaches; no elevens or officials.
  - Search summary: Vučinić coach; Krstović included. Al Jazeera, Sportskeeda, scores24, Ratingbet, The Stats Zone and FotMob results not opened.
- Search "Cyprus national team squad Nations League Montenegro Podgorica September 2026 coach call-ups injuries":
  - sportaran https://sportaran.com/en/post/kipr-obyavil-sostav-na-matchi-ligi-nacij-27-futbolistov-i-tri-debyutanta-pered-igroj-s-armeniej/ fetched. 18 September: squad with clubs, three debutants, Pikis omitted, four fixtures.
  - Search summary: four matches in 11 days; preparations from 21 September. Cyprus FA and FotMob results not opened.
- Search "Mirko Vučinić appointed Montenegro head coach date Prosinečki contract":
  - FSCG https://fscg.me/en/news/13972/mirko-vucinic-takes-over-the-falcons/ fetched. 19 September 2025: Prosinečki dismissed, Vučinić appointed; on the national-team staff since January 2022; no contract length.
  - Search summary: Prosinečki in charge 2024–2025; Kyrgyzstan from December 2025. Yahoo, OneFootball, Wikipedia and playmakerstats not opened.
- Search "Akis Mantzios appointed Cyprus national team coach date contract extension":
  - Search summary of Cyprus FA https://www.cfa.com.cy/En/news/50334 and Parikiaki https://www.parikiaki.com/2025/01/apostolos-mantzios-officially-takes-over-cyprus-mens-national-football-team/: announced 9 January 2025, two-year contract, in charge from 21 January 2025. A Facebook headline reports an extension; not opened, no date or length.
  - Wikipedia https://en.wikipedia.org/wiki/Akis_Mantzios fetched. Cyprus 2025–; no dates or extension.
- Search "Εθνική Κύπρου Μαυροβούνιο Μαντζιός αποστολή Ποντγκόριτσα Nations League τραυματισμός Σιέλης Λαϊφής":
  - Politis Gipedo https://gipedo.politis.com.cy/podosfairo/kypros/ethnikes-omades/1035761/h-ananeomeni-ethniki-psakhnei-to-spoydaio-ksekinima-stin-pontghkoritsa fetched. Sielis injured and stayed in Cyprus; Laifis travelled on an individual programme and will not feature; the 27 who travelled.
  - AlphaNews https://www.alphanews.live/sports/oloklironei-me-ena-erotimatiko-enopsei-mavrovouniou-i-ethniki-mas/ fetched. 24 September: Laifis doubtful, expected to be protected for Latvia.
  - Ant1, ShootandGoal, ekirikas, Nomisma and the betting-preview result not opened.
- Search "Vučinić spisak Crna Gora Kipar Liga nacija septembar 2026 Hakšabanović povreda Krstović":
  - CG Sport https://cgsport.me/2026/09/08/mirko-vucinic-objavio-spisak-ovo-je-26-igraca-za-start-lige-nacija/ fetched. The 26 of 8 September with clubs by position.
  - CG Sport https://cgsport.me/2026/09/21/vucinic-kompletirao-spisak-perovic-prekomandovan-iz-u-21-poziv-i-dresaju/ fetched. 21 September: Perović and Drešaj added; Hakšabanović misses the matches (injury, per a linked article).
  - Search summary: fixtures and venues. Antena M, Portal Analitika, Standard, Cetinjski List, Adria TV and Montenegro Magazin not opened.
- Search "Montenegro Cyprus Nations League 25 September 2026 referee sudija Crna Gora Kipar":
  - Search summary: no referee named. Sports Mole match guide, FOX Sports, Goal.com and betting-preview results not opened.
  - Wikipedia https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_C fetched. Group C2 fixtures and venues; referee Daniele Chiffi (Italy); pots. The page as read also carried a result line for this unplayed match, which was not used.
- Search "Daniele Chiffi arbitro statistiche 2025-26 Serie A cartellini gialli a partita rigori falli":
  - Italian Wikipedia https://it.wikipedia.org/wiki/Daniele_Chiffi fetched. FIFA list from 1 January 2022; Serie A debut 2014; 100 Serie A matches by October 2024; no statistics.
  - PianetaFanta https://www.pianetafanta.it/statistiche-arbitri.asp?NomeArbitro=Chiffi+D.&tipolink=100 returned HTTP 500.
  - Search summary: 10 Serie A matches in 2025–26, contradicted by ESPN's 15. Virgilio, Tuttocampo, ArbitroMaledetto, BeSoccer and calvar not opened.
- Search "Montenegro vs Cyprus head to head all-time meetings history Crna Gora Kipar međusobni dueli" (shared):
  - Search summary of 11v11 https://www.11v11.com/teams/montenegro/tab/opposingTeams/opposition/Cyprus/ and AiScore: five meetings since 6 June 2009, Montenegro W2 D3, nine goals; another source counts six (W2 D4). Pages not opened. Tips.GG, footlive, livescores.biz and FotMob not opened.
- FotMob, opened directly with no search: https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_team/world-cup-qualification-uefa-teams and https://www.fotmob.com/en-GB/leagues/10195/stats/season/24488/teams/expected_goals_conceded_team/world-cup-qualification-uefa-teams: Montenegro 11.8 xG on 8 goals, 15.3 xG conceded on 17; Cyprus 13.9 on 11, 11.5 on 11; match counts not shown.
