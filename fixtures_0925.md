# fixtures_0925 — 2026-09-25 — typed sheet slate.9.xlsx (Phase 1B)
# source: the tab named "Slate 9" inside slate.9.xlsx (strict-OOXML workbook;
# opens as zero sheets in the normal reader, so the sheet XML was read directly;
# the other tabs are leftovers from prior sessions and were not read). 8 fixtures.
# Header row (row 3, read from the file): League, Home Team, Time, Away Team.
# Column order is League / Home / Time / Away, read from the header, not assumed.
# Row 1 is the title cell "Today's Games"; B1 carries the date 2026-09-25, taken
# as the slate date.
# Kickoffs: the Time column carries no timezone; none assumed. Values with
# floating-point residue (20:45:00.0000000000031950) are normalised to the clean
# minute. Sanity check against ESPN's public scoreboard (uefa.nations, 20260925):
# 16:00Z and 18:45Z, i.e. 18:00 and 20:45 Europe/Rome, matching the sheet's times
# as Italian time. All eight events found; none extra, none missing.
# Venue: no column — left empty, recovered in Phase 2, not guessed here.
# Matchday: no column — left empty likewise.
# League labels carried as the sheet writes them. The two League A rows carry no
# group ("UEFA Nations League A") and the two League C rows likewise; the group is
# recovered in Phase 2.
# Team names carried as the sheet writes them ("Turkiye", "Bosnia and Herzegovina");
# ESPN renders these "Türkiye" and "Bosnia-Herzegovina", the same sides.
# Rows at the same kickoff keep the sheet's row order.
# No duplicate fixtures, no unparseable kickoffs, no malformed rows.

league | kickoff | venue | home | away | matchday | source
UEFA Nations League B - Group 2 | 18:00 | | Georgia | Northern Ireland | | typed:slate.9.xlsx
UEFA Nations League C | 18:00 | | Armenia | Latvia | | typed:slate.9.xlsx
UEFA Nations League A | 20:45 | | Italy | Belgium | | typed:slate.9.xlsx
UEFA Nations League A | 20:45 | | Turkiye | France | | typed:slate.9.xlsx
UEFA Nations League B - Group 2 | 20:45 | | Hungary | Ukraine | | typed:slate.9.xlsx
UEFA Nations League B - Group 4 | 20:45 | | Poland | Bosnia and Herzegovina | | typed:slate.9.xlsx
UEFA Nations League B - Group 4 | 20:45 | | Sweden | Romania | | typed:slate.9.xlsx
UEFA Nations League C | 20:45 | | Montenegro | Cyprus | | typed:slate.9.xlsx
