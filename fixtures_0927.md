# fixtures_0927 — 2026-09-27 — typed sheet slate.11.xlsx (Phase 1B)
# source: the tab named "Slate 11" inside slate.11.xlsx (strict-OOXML workbook;
# opens as zero sheets in the normal reader, so the sheet XML was read directly;
# the other tabs are leftovers from prior sessions and were not read). 7 fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away Team.
# Column order is League / Home / Time / Away, read from the header, not assumed.
# Row 1 is the title cell "Today's Games"; B1 carries the date 2026-09-27, taken
# as the slate date. No price columns in the sheet.
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (20:44:59.99999999997441975) are normalised to the clean
# minute (20:45). Sanity check against ESPN's public scoreboard (uefa.nations,
# 20260927): 16:00Z and 18:45Z, i.e. 18:00 and 20:45 Europe/Rome, matching the
# sheet's times as Italian time. All seven sheet fixtures found on ESPN. ESPN
# carries one event the sheet does not: Lithuania – Azerbaijan, 15:00 — not added,
# the sheet is the slate.
# Venue: no column — left empty, recovered in Phase 2, not guessed here.
# Matchday: no column — left empty likewise.
# League labels carried as the sheet writes them. The "UEFA Nations League B"
# rows carry no group; the group is recovered in Phase 2.
# Team names carried as the sheet writes them. ESPN renders "Ireland" as
# "Republic of Ireland"; the other six pairings match.
# Rows sorted by kickoff; rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.
# No triage (7 fixtures, triage waived by instruction): every fixture is T1.

league | kickoff | venue | home | away | matchday | source
UEFA Nations League D - Group 1 | 18:00 | | Gibraltar | Andorra | | typed:slate.11.xlsx
UEFA Nations League A - Group 2 | 18:00 | | Serbia | Netherlands | | typed:slate.11.xlsx
UEFA Nations League A - Group 4 | 18:00 | | Denmark | Wales | | typed:slate.11.xlsx
UEFA Nations League B | 18:00 | | Austria | Kosovo | | typed:slate.11.xlsx
UEFA Nations League A - Group 2 | 20:45 | | Germany | Greece | | typed:slate.11.xlsx
UEFA Nations League A - Group 4 | 20:45 | | Norway | Portugal | | typed:slate.11.xlsx
UEFA Nations League B | 20:45 | | Israel | Ireland | | typed:slate.11.xlsx
