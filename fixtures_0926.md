# fixtures_0926 — 2026-09-26 — typed sheet slate.10.xlsx (Phase 1B)
# source: the tab named "Slate 10" inside slate.10.xlsx (strict-OOXML workbook;
# opens as zero sheets in the normal reader, so the sheet XML was read directly;
# the other tabs are leftovers from prior sessions and were not read). 10 fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away Team.
# Column order is League / Home / Time / Away, read from the header, not assumed.
# Row 1 is the title cell "Today's Games"; B1 carries the date 2026-09-26, taken
# as the slate date. No price columns in the sheet.
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (20:44:59.99999999997441975) are normalised to the clean
# minute (20:45). Sanity check against ESPN's public scoreboard (uefa.nations,
# 20260926): 13:00Z, 16:00Z and 18:45Z, i.e. 15:00, 18:00 and 20:45 Europe/Rome,
# matching the sheet's times as Italian time. All ten events found; none extra,
# none missing.
# Venue: no column — left empty, recovered in Phase 2, not guessed here.
# Matchday: no column — left empty likewise.
# League labels carried as the sheet writes them. The "UEFA Nations League A" rows
# and the "UEFA Nations League B" rows carry no group; the group is recovered in
# Phase 2 (triage_0926.md records what ESPN's standings give).
# Team names carried as the sheet writes them; ESPN renders the same ten pairings.
# Rows sorted by kickoff; rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.

league | kickoff | venue | home | away | matchday | source
UEFA Nations League B | 15:00 | | Slovenia | Scotland | | typed:slate.10.xlsx
UEFA Nations League C - Group 1 | 18:00 | | San Marino | Finland | | typed:slate.10.xlsx
UEFA Nations League C - Group 3 | 18:00 | | Faroe Islands | Kazakhstan | | typed:slate.10.xlsx
UEFA Nations League C - Group 4 | 18:00 | | Bulgaria | Luxembourg | | typed:slate.10.xlsx
UEFA Nations League C - Group 4 | 18:00 | | Iceland | Estonia | | typed:slate.10.xlsx
UEFA Nations League A | 20:45 | | Czechia | Croatia | | typed:slate.10.xlsx
UEFA Nations League A | 20:45 | | England | Spain | | typed:slate.10.xlsx
UEFA Nations League B | 20:45 | | North Macedonia | Switzerland | | typed:slate.10.xlsx
UEFA Nations League C - Group 1 | 20:45 | | Albania | Belarus | | typed:slate.10.xlsx
UEFA Nations League C - Group 3 | 20:45 | | Slovakia | Moldova | | typed:slate.10.xlsx
