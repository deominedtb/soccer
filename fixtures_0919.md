# fixtures_0919 — 2026-09-19 — typed sheet slate.6.xlsx (Phase 1B)
# source: the tab named "Slate 6" inside slate.6.xlsx (the workbook is
# strict-OOXML and opens as zero sheets in the normal reader, so the sheet
# XML was read directly; the other tabs are leftovers from prior sessions
# and were not read). 23 fixtures.
# Header row (row 4, read from the file): League, Home, Away, Kick-off, Venue.
# Row 1 is the title cell "Today's Slate"; row 2 reads "Matchday: 19 September
# 2026" and is taken as the slate date. This is a date, not a matchday number:
# the matchday column stays empty.
# Kickoffs: the Kick-off column carries no timezone; none assumed. Values with
# floating-point residue (15:59:59.9999999999968050, 20:45:00.0000000000031950
# and similar) are normalised to the clean minute; the three Premier League
# 15:59:59.99… values read 16:00.
# Venue: every cell reads "N/A" — treated as missing, left empty, recovered in
# Phase 2, not guessed here. Matchday: no column — left empty likewise.
# Team names: the source stores "Deportivo Alavés" and "Köln" cleanly; carried as
# written. "M'gladbach", "Nottm Forest" and "Racing Santander" are carried as the
# sheet renders them.
# Rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.

league | kickoff | venue | home | away | matchday | source
England - Premier League | 13:30 | | Tottenham | Aston Villa | | typed:slate.6.xlsx
Spain - LaLiga | 14:00 | | Osasuna | Rayo Vallecano | | typed:slate.6.xlsx
Italy - Serie A | 15:00 | | Bologna | Torino | | typed:slate.6.xlsx
Italy - Serie A | 15:00 | | Udinese | Cagliari | | typed:slate.6.xlsx
Germany - Bundesliga | 15:30 | | M'gladbach | Mainz | | typed:slate.6.xlsx
Germany - Bundesliga | 15:30 | | Frankfurt | Freiburg | | typed:slate.6.xlsx
Germany - Bundesliga | 15:30 | | Hamburger SV | Köln | | typed:slate.6.xlsx
Germany - Bundesliga | 15:30 | | Werder Bremen | Augsburg | | typed:slate.6.xlsx
England - Premier League | 16:00 | | Brighton | Arsenal | | typed:slate.6.xlsx
England - Premier League | 16:00 | | Everton | Ipswich | | typed:slate.6.xlsx
England - Premier League | 16:00 | | Newcastle | Hull | | typed:slate.6.xlsx
Spain - LaLiga | 16:15 | | Athletic Club | Deportivo Alavés | | typed:slate.6.xlsx
France - Ligue 1 | 17:15 | | Paris FC | Strasbourg | | typed:slate.6.xlsx
Italy - Serie A | 18:00 | | Roma | Inter | | typed:slate.6.xlsx
Spain - LaLiga | 18:30 | | Celta Vigo | Racing Santander | | typed:slate.6.xlsx
England - Premier League | 18:30 | | Nottm Forest | Coventry | | typed:slate.6.xlsx
Germany - Bundesliga | 18:30 | | VfB Stuttgart | Dortmund | | typed:slate.6.xlsx
Italy - Serie A | 20:45 | | Venezia | Lazio | | typed:slate.6.xlsx
France - Ligue 1 | 20:45 | | Angers | Troyes | | typed:slate.6.xlsx
France - Ligue 1 | 20:45 | | Le Mans | Lorient | | typed:slate.6.xlsx
France - Ligue 1 | 20:45 | | Lyon | Rennes | | typed:slate.6.xlsx
France - Ligue 1 | 20:45 | | Toulouse | Le Havre | | typed:slate.6.xlsx
Spain - LaLiga | 21:00 | | Sevilla | Barcelona | | typed:slate.6.xlsx
