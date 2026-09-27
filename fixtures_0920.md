# fixtures_0920 — 2026-09-20 — typed sheet slate.7.xlsx (Phase 1B)
# source: the tab named "Slate 7" inside slate.7.xlsx (strict-OOXML workbook;
# opens as zero sheets in the normal reader, so the sheet XML was read directly;
# the other tabs are leftovers from prior sessions and were not read). 20 fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away Team.
# Column order is League / Home / Time / Away, read from the header, not assumed.
# Row 1 is the title cell "Today's Games". The sheet carries NO date: 2026-09-20 is
# taken from the file's save date and today's date, and is an assumption.
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (12:29:59.9999999999744, 20:44:59.9999999999744 and similar)
# are normalised to the clean minute.
# Venue: no column — left empty, recovered in Phase 2, not guessed here.
# Matchday: no column — left empty likewise.
# Team names carried as the sheet writes them: "Deportivo A Coruña", "Málaga",
# "Atlético Madrid", "PSG", "Man City", "Man United", "Milan", "Frosinone".
# Rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.

league | kickoff | venue | home | away | matchday | source
Italy - Serie A | 12:30 | | Fiorentina | Napoli | | typed:slate.7.xlsx
Spain - LaLiga | 14:00 | | Getafe | Málaga | | typed:slate.7.xlsx
France - Ligue 1 | 15:00 | | Auxerre | Brest | | typed:slate.7.xlsx
England - Premier League | 15:00 | | Bournemouth | Liverpool | | typed:slate.7.xlsx
England - Premier League | 15:00 | | Leeds | Crystal Palace | | typed:slate.7.xlsx
England - Premier League | 15:00 | | Man City | Sunderland | | typed:slate.7.xlsx
Italy - Serie A | 15:00 | | Frosinone | Como | | typed:slate.7.xlsx
Italy - Serie A | 15:00 | | Parma | Genoa | | typed:slate.7.xlsx
Germany - Bundesliga | 15:30 | | Leverkusen | RB Leipzig | | typed:slate.7.xlsx
Spain - LaLiga | 16:15 | | Atlético Madrid | Real Madrid | | typed:slate.7.xlsx
France - Ligue 1 | 17:15 | | Nice | Lille | | typed:slate.7.xlsx
England - Premier League | 17:30 | | Fulham | Man United | | typed:slate.7.xlsx
Germany - Bundesliga | 17:30 | | Schalke 04 | Elversberg | | typed:slate.7.xlsx
Italy - Serie A | 18:00 | | Juventus | Atalanta | | typed:slate.7.xlsx
Spain - LaLiga | 18:30 | | Deportivo A Coruña | Real Betis | | typed:slate.7.xlsx
Spain - LaLiga | 18:30 | | Villarreal | Levante | | typed:slate.7.xlsx
Germany - Bundesliga | 19:30 | | Paderborn | Hoffenheim | | typed:slate.7.xlsx
France - Ligue 1 | 20:45 | | Marseille | PSG | | typed:slate.7.xlsx
Italy - Serie A | 20:45 | | Milan | Lecce | | typed:slate.7.xlsx
Spain - LaLiga | 21:00 | | Valencia | Real Sociedad | | typed:slate.7.xlsx
