# -*- coding: utf-8 -*-
"""Third lineup patch: the remaining stale coaching claims in f5."""
import io, sys

fn = "fx_0918_f5.html"
PAIRS = [
 ("RCDE Stadium, Barcelona &middot; the only fixture on tonight&rsquo;s board where neither club changed head coach &mdash; but Elche sold their &euro;25m forward and &euro;12m centre-back and signed twelve, Espanyol foul more than anyone on the slate, Elche changed head coach in June, and the referee is making his fourth appearance in Primera</p>",
  "RCDE Stadium, Barcelona &middot; the deepest current-season sample on tonight&rsquo;s board, six league matches each &mdash; but Elche changed head coach in June, sold their &euro;25m forward and &euro;12m centre-back and signed twelve, Espanyol foul more than anyone on the slate, and the referee is making his fourth appearance in Primera</p>"),

 ("<div class=\"mkt-why\">Both clubs have six league matches, both kept their head coach, and both have two full seasons of rates in the same division &mdash; the most continuous evidence on this board.",
  "<div class=\"mkt-why\">Both clubs have six league matches and two full seasons of rates in the same division &mdash; the deepest and most continuous club evidence on this board, even though Elche changed head coach in June and their twelve arrivals were assembled for Mart&iacute;n Anselmi rather than by him."),

 ("both rest on two full seasons of rates in the same division from two clubs with the same coaches, which nothing else on tonight's board can say.</li>",
  "both rest on two full seasons of rates in the same division and six matches of this one, which nothing else on tonight's board can say. Elche's coaching change qualifies that continuity without removing it: the rates are the club's, not Sarabia's.</li>"),
]

s = io.open(fn, encoding="utf-8").read()
for old, new in PAIRS:
    if old not in s:
        sys.exit("MISS: %s..." % old[:90])
    s = s.replace(old, new, 1)
io.open(fn, "w", encoding="utf-8").write(s)
print("patched %s (%d edits)" % (fn, len(PAIRS)))
