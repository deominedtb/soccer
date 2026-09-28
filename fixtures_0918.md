# fixtures_0918 — 2026-09-18 — typed sheet slate.5.xlsx (Phase 1B)
# source: the tab named "Slate 5" inside slate.5.xlsx (the workbook is
# strict-OOXML and opens as zero sheets in the normal reader, so the sheet
# XML was read directly; the other tabs are leftovers from prior sessions
# and were not read). Five fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away
# Team. Row 1 is the title cell "Today's Games". No date column: the slate
# date is taken from the run date, 2026-09-18 (file saved that day).
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (20:29:59.9999999999968050, 20:45:00.0000000000031950)
# are normalised to the clean minute (20:30, 20:45).
# Team name: the source cell reads "Bayern M?nchen" with a corrupted
# character stored in the file itself; carried here as "Bayern München".
# Rows at the same kickoff keep the sheet's row order.
# venue and matchday: not in the source — left empty, recovered in Phase 2,
# not guessed here.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.

league | kickoff | venue | home | away | matchday | source
Germany - Bundesliga | 20:30 | | Bayern München | Union Berlin | | typed:slate.5.xlsx
Italy - Serie A | 20:45 | | Monza | Sassuolo | | typed:slate.5.xlsx
France - Ligue 1 | 20:45 | | Monaco | Lens | | typed:slate.5.xlsx
England - Premier League | 21:00 | | Brentford | Chelsea | | typed:slate.5.xlsx
Spain - LaLiga | 21:00 | | Espanyol | Elche | | typed:slate.5.xlsx
