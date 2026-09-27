# fixtures_0924 — 2026-09-24 — typed sheet slate.8.xlsx (Phase 1B)
# source: the tab named "Slate 8" inside slate.8.xlsx (strict-OOXML workbook;
# opens as zero sheets in the normal reader, so the sheet XML was read directly;
# the other tabs are leftovers from prior sessions and were not read). 8 fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away Team.
# Column order is League / Home / Time / Away, read from the header, not assumed.
# Row 1 is the title cell "Today's Games"; B1 carries the date 2026-09-24, taken
# as the slate date.
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (20:45:00.0000000000031950) are normalised to the clean
# minute.
# Venue: no column — left empty, recovered in Phase 2, not guessed here.
# Matchday: no column — left empty likewise.
# League labels carried as the sheet writes them. The two League B rows carry no
# group letter ("UEFA Nations League B"); the group is recovered in Phase 2.
# Team names carried as the sheet writes them, with one exception: the sheet's
# "Ireland" (away, f7) was ambiguous between the Republic of Ireland and Northern
# Ireland. Resolved in Phase 1.5 from the ESPN pipeline, not from memory: ESPN's
# 2026-27 Group B3 is Israel, Austria, Republic of Ireland, Kosovo, and today's
# event reads "Republic of Ireland at Kosovo". Row amended; sheet text kept below.
# Both League B rows are Group B3 (same source).
# Kickoff timezone, same source: ESPN gives 16:00Z and 18:45Z for today's eight,
# i.e. 18:00 and 20:45 Europe/Rome. The sheet's times are Italian time.
# Rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.
# The workbook was open in Excel at read time (lock file present); the saved copy
# (modified 2026-09-24 14:12 local) is what was read.

league | kickoff | venue | home | away | matchday | source
UEFA Nations League D - Group 1 | 18:00 | | Andorra | Malta | | typed:slate.8.xlsx
UEFA Nations League A - Group 2 | 20:45 | | Netherlands | Germany | | typed:slate.8.xlsx
UEFA Nations League A - Group 2 | 20:45 | | Serbia | Greece | | typed:slate.8.xlsx
UEFA Nations League A - Group 4 | 20:45 | | Norway | Denmark | | typed:slate.8.xlsx
UEFA Nations League A - Group 4 | 20:45 | | Portugal | Wales | | typed:slate.8.xlsx
UEFA Nations League B | 20:45 | | Austria | Israel | | typed:slate.8.xlsx
UEFA Nations League B | 20:45 | | Kosovo | Republic of Ireland | | typed:slate.8.xlsx (sheet: "Ireland")
UEFA Nations League D - Group 2 | 20:45 | | Liechtenstein | Lithuania | | typed:slate.8.xlsx
