# -*- coding: utf-8 -*-
"""Update the Phase 3 board builder for the confirmed team sheets and for the
Elche coaching correction."""
import io, sys

fn = "build_board_0918.py"
PAIRS = [

("""HEADLINE = ("Five of tonight&rsquo;s ten clubs are run by a coach who was not in charge in May, "
            "and one of them took the job on Monday")""",
 """HEADLINE = ("Six of tonight&rsquo;s ten clubs are run by a coach who was not in charge in May, "
            "and one of them took the job on Monday")"""),

("""STANDFIRST = ("Five fixtures, one from each of Europe&rsquo;s top five leagues, parsed from the typed sheet "
              "slate.5.xlsx &mdash; all five cards built at full T1 depth.")""",
 """STANDFIRST = ("Five fixtures, one from each of Europe&rsquo;s top five leagues, parsed from the typed sheet "
              "slate.5.xlsx &mdash; all five cards built at full T1 depth, then revised against the "
              "confirmed team sheets, benches and injury lists.")"""),

("<strong>Five of the ten clubs have a head coach who was not in charge when last season ended</strong>: Mauro Lustrinelli took Union Berlin on 1 July, Ivan Juric took Monza on 1 July, Alberto Aquilani replaced Fabio Grosso at Sassuolo, Xabi Alonso took Chelsea on 1 July after being appointed in mid-May, and Lens have had three coaches this calendar year",
 "<strong>Six of the ten clubs have a head coach who was not in charge when last season ended</strong>: Mauro Lustrinelli took Union Berlin on 1 July, Ivan Juric took Monza on 1 July, Alberto Aquilani replaced Fabio Grosso at Sassuolo, Xabi Alonso took Chelsea on 1 July after being appointed in mid-May, Mart&iacute;n Anselmi took Elche on 13 June after Eder Sarabia stepped down of his own accord in late May, and Lens have had three coaches this calendar year"),

("Only Bayern, Brentford, Monaco, Espanyol and Elche start under the man who finished 2025&ndash;26, and Elche&rsquo;s Eder Sarabia is suspended from the bench.</p>",
 "Only Bayern, Brentford, Monaco and Espanyol start under the man who finished 2025&ndash;26. <strong>An earlier version of this board named Sarabia as Elche&rsquo;s coach and reported him suspended from the bench, on the word of a Spanish preview. That was wrong, it is corrected on the card rather than quietly removed, and it is the one factual error this board made.</strong></p>"),

("Those samples run from 27 matches to 59. Each strip therefore carries two baselines, and on several rows the gap between the two baselines is wider than the gap between the two clubs.</p>",
 """Those samples run from 27 matches to 59. Each strip therefore carries two baselines, and on several rows the gap between the two baselines is wider than the gap between the two clubs.</p>
<p>The confirmed team sheets, which arrived after the cards were written, settled four of the five questions each card had named as the one most likely to change its ratings, and settled three of them against the side already carrying the thinner evidence. <strong>Union are without both Friedrich and Nsoki, so two of the four centre-backs they bought this summer do not play and a third is a substitute. Chelsea are without Moises Ca&iuml;cedo and Jo&atilde;o Pedro, with Romeo Lavia only on the bench, so a midfield that had already sold Enzo Fern&aacute;ndez and Andrey Santos starts Jordan Henderson and Valent&iacute;n Barco. Yannick Cahuzac&rsquo;s first Lens team is a 4-2-3-1 that keeps the structure rather than reverting, with Sk&oacute;ra&#347;, Hazard and Ivanovi&#263; all in reserve.</strong> Only the Serie A card&rsquo;s open question &mdash; a published Serie A record for Daniele Perenzoni &mdash; is untouched by a team sheet. Three of the summer&rsquo;s largest signings across the board start on the bench: Bayern&rsquo;s two &euro;50m arrivals and Brentford&rsquo;s club-record midfielder.</p>"""),

("<strong>Contradictions are named on the card rather than resolved:</strong> whether Friedrich and Nsoki play for Union; whether Chris Bedia joined or left Union; whether Paul Pogba signed for Monaco or was released by it on 19 August; Monaco&rsquo;s net transfer balance; Takumi Minamino&rsquo;s diagnosis; Jonathan Gradit&rsquo;s fitness; and a Spanish preview that places the LaLiga fixture at the wrong ground.</div>",
 "<strong>Contradictions, and what the team sheets settled.</strong> Resolved by the confirmed lists: Friedrich and Nsoki are both out for Union and Imeri is fit; Takumi Minamino is fit and a substitute, which ends the cruciate-or-muscle dispute in the least severe direction; Jonathan Gradit is fit enough for the Lens bench; the LaLiga fixture is at the RCDE Stadium, as the fixture record said and one preview denied. Still unresolved and named on the cards: whether Chris Bedia joined or left Union; whether Paul Pogba signed for Monaco or was released by it on 19 August; Monaco&rsquo;s net transfer balance. <strong>One thing the team sheets did not resolve but corrected: Elche&rsquo;s head coach is Mart&iacute;n Anselmi, appointed 13 June 2026, not Eder Sarabia. The card said Sarabia and said he was suspended from the bench. Both were wrong.</strong> New absences the previews missed: Ansu Fati (calf) for Monaco and Yeferson Paz for Sassuolo.</div>"),

("<li><strong>The one normal fixture is Espanyol&ndash;Elche.</strong> It is the only match on the board where both clubs kept their head coach, both played in this division last season, and both have six league matches already played &mdash; the deepest current sample here. Everything else on this page is a club that changed coach, changed division, or has three or four matches on the clock.</li>",
 "<li><strong>There is no normal fixture on this board.</strong> Every one of the five contains at least one club whose head coach was not in charge in May. The closest is <strong>Espanyol&ndash;Elche</strong>, where both clubs played in this division last season and both have six league matches already played &mdash; the deepest current sample here &mdash; but Elche changed coach in June, which is a correction to what this page first said. Everything else is a club that changed coach, changed division, or has three or four matches on the clock.</li>"),

("<li><strong>Where the evidence is thinnest, and which part of the board to trust least.</strong> First, <strong>Bayern&ndash;Union</strong>: three league matches per club, the smallest sample on the slate, and each club&rsquo;s three contains one result that distorts every rate built on it &mdash; Bayern&rsquo;s 0&ndash;0 at Schalke and Union&rsquo;s 0&ndash;4 at Leverkusen. Second, <strong>the referees&rsquo; penalty rates, which are unpublished for all five officials</strong> in every source reached, so no Discipline row on this board can speak to contact in the box. Third, <strong>Monaco&ndash;Lens</strong>, where the away side&rsquo;s entire strip was produced under two coaches neither of whom will pick the team tonight, and where the divisional home-win rate of 27.8% over 36 matches contradicts 46.1% over 306.</li>",
 """<li><strong>Where the evidence is thinnest, and which part of the board to trust least.</strong> First, <strong>Bayern&ndash;Union</strong>: three league matches per club, the smallest sample on the slate, and each club&rsquo;s three contains one result that distorts every rate built on it &mdash; Bayern&rsquo;s 0&ndash;0 at Schalke and Union&rsquo;s 0&ndash;4 at Leverkusen, now compounded by both Friedrich and Nsoki being confirmed out. Second, <strong>the referees&rsquo; penalty rates, which are unpublished for all five officials</strong> in every source reached, so no Discipline row on this board can speak to contact in the box. Third, <strong>Monaco&ndash;Lens</strong>, where the away side&rsquo;s entire strip was produced under two coaches neither of whom picks the team tonight, and where the divisional home-win rate of 27.8% over 36 matches contradicts 46.1% over 306.</li>
<li><strong>What the confirmed team sheets changed, in one line per card.</strong> Bayern&ndash;Union: Neuer starts, closing the goalkeeping gap the card flagged, and Union&rsquo;s summer centre-back line is two out and one benched. Monza&ndash;Sassuolo: Monza name the eleven that was trailed; Aquilani resolves both selection questions the other way, with Bowie benched. Monaco&ndash;Lens: Monaco switch to a back three with Zakaria in it, Minamino and Salisu are fit substitutes, Ansu Fati is a new absence, and Cahuzac keeps the structure. Brentford&ndash;Chelsea: Ca&iuml;cedo and Jo&atilde;o Pedro out, Lavia benched, Chelsea in a 3-4-2-1, and Brentford&rsquo;s club-record signing starts on the bench. Espanyol&ndash;Elche: four of Espanyol&rsquo;s six summer loans are substitutes, Elche&rsquo;s injury list is one name, and the head coach on this card was wrong.</li>"""),

("League baselines: baselines_0918.md, whose 2025&ndash;26 lines are carried from baselines_0917.md and baselines_0916.md. Every source used is logged in full in sources_0918.md.",
 "League baselines: baselines_0918.md, whose 2025&ndash;26 lines are carried from baselines_0917.md and baselines_0916.md. <strong>Confirmed team sheets, benches and injury lists for all five fixtures were supplied by you after the cards were written, and the Elche coaching change was then verified independently against TeleElx, Infobae, eldesmarque and the club&rsquo;s own announcement.</strong> Every source used is logged in full in sources_0918.md."),
]

s = io.open(fn, encoding="utf-8").read()
for old, new in PAIRS:
    if old not in s:
        sys.exit("MISS: %s..." % old[:100])
    s = s.replace(old, new, 1)
io.open(fn, "w", encoding="utf-8").write(s)
print("patched %s (%d edits)" % (fn, len(PAIRS)))
