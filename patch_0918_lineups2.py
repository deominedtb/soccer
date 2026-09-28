# -*- coding: utf-8 -*-
"""Second lineup patch: f4 and f5, plus a wording fix in f1."""
import io, sys

EDITS = {}
def E(fn, old, new):
    EDITS.setdefault(fn, []).append((old, new))

# ---------------------------------------------------------------- f1 wording
E("fx_0918_f1.html",
  "No suspensions for either side; Bayern's only listed absence is Tom Bischof's team-mate Tarek Buchmann (knee).</li>",
  "No suspensions for either side, and Bayern's only listed absence is Tarek Buchmann (knee) &mdash; Kompany starts Neuer, Stani&scaron;i&#263;, Upamecano, Tah and Davies behind Kimmich and Pavlovi&#263;, with Olise, Musiala and Luis D&iacute;az around Kane, and <strong>both &euro;50m summer signings, Saibari and Nathaniel Brown, on the bench</strong>.</li>")

# ---------------------------------------------------------------- f4
E("fx_0918_f4.html",
  "<strong>Chelsea list Moises Ca&iuml;cedo (calf), Marco Palestra (fitness), Emmanuel Emegha (fitness) and Jordan Henderson (wrist) as doubts, and Jo&atilde;o Pedro's involvement is described by Alonso only as \"a possibility\"</strong> after he withdrew from the Brazil squad during the international break. No suspensions are reported for either side. Ca&iuml;cedo's absence would leave a midfield that has already lost Enzo Fern&aacute;ndez and Andrey Santos without its remaining first-choice holder. Predicted elevens: <strong>Brentford</strong> &mdash; Kelleher; Kayode, Schuster, Ajer, Lewis-Potter; Janelt, Sangar&eacute;; Schade, Yarmolyuk, Anthony; Thiago. <strong>Chelsea</strong> &mdash; Mart&iacute;nez; Fofana, Lacroix, Colwill; Neto, Lavia, James, Chavarria; Palmer, Jo&atilde;o Pedro, Rogers.</li>",
  "<strong>Chelsea are confirmed without Moises Ca&iuml;cedo, Jo&atilde;o Pedro, Emmanuel Emegha and Marco Palestra</strong> &mdash; both of the doubts that mattered have resolved against playing. <strong>Ca&iuml;cedo's absence leaves a midfield that had already lost Enzo Fern&aacute;ndez and Andrey Santos without its remaining first-choice holder, and Romeo Lavia is only a substitute: Chelsea start Jordan Henderson and Valent&iacute;n Barco in central midfield, and Danny Welbeck at centre-forward in place of Jo&atilde;o Pedro.</strong> Henderson starts against the club that terminated his contract eight weeks ago. No suspensions for either side. <strong>Confirmed elevens &mdash; Brentford 4-2-3-1</strong>: Kelleher; Kayode, Schuster, Ajer, Lewis-Potter; Yarmoliuk, Janelt; Anthony, Damsgaard, Schade; Igor Thiago &mdash; with <strong>Mamadou Sangar&eacute;, the club-record signing, and El Hadji Malick Diouf, the &pound;35m defender, both on the bench</strong> alongside Callum Wilson. <strong>Chelsea 3-4-2-1</strong>: Mart&iacute;nez; Lacroix, Colwill, Chavarr&iacute;a; Neto, Henderson, Barco, Rogers; Palmer; Welbeck &mdash; a back three rather than the four trailed, with Est&ecirc;v&atilde;o, Gittens, Gusto, Hato, Lavia and Quenda in reserve. One name in the Chelsea eleven was not legible in the team-sheet graphic and is not guessed at here.</li>")

E("fx_0918_f4.html",
  "&mdash; and Jo&atilde;o Pedro is only \"a possibility\" tonight. The conceded halves of the family are better documented than the scored halves.",
  "&mdash; and Jo&atilde;o Pedro is confirmed out, with Danny Welbeck leading the line in his place. The conceded halves of the family are better documented than the scored halves.")

E("fx_0918_f4.html",
  "team goals depends on which of Chelsea's new forwards plays &mdash; Jo&atilde;o Pedro's involvement is described only as a possibility.</li>",
  "team goals depends on which of Chelsea's new forwards plays, and the confirmed answer is neither of the two who scored the goals &mdash; Jo&atilde;o Pedro is out and Danny Welbeck starts.</li>")

E("fx_0918_f4.html",
  "<li><strong>Chelsea sold their deadline-day midfielder without replacing him and their remaining holder is a doubt.</strong> Enzo Fern&aacute;ndez went to Manchester City with the intended replacement &mdash; reported as Monaco's Lamine Camara, who plays in tonight's third fixture &mdash; not signed, Andrey Santos went for &pound;50m, and Ca&iuml;cedo has a calf problem. That is the single position on this card with the least cover and the most recent change.</li>",
  "<li><strong>Chelsea sold their deadline-day midfielder without replacing him and their remaining holder is now confirmed out.</strong> Enzo Fern&aacute;ndez went to Manchester City with the intended replacement &mdash; reported as Monaco's Lamine Camara, who starts in tonight's third fixture &mdash; not signed, Andrey Santos went for &pound;50m, Ca&iuml;cedo is out and Lavia is a substitute. <strong>The central midfield that takes the field is a 36-year-old signed from tonight's opponents and a 21-year-old signed from Strasbourg</strong>, which is the least-covered and most recently changed unit on this card.</li>")

E("fx_0918_f4.html",
  "<li><strong>The single fact that would most change which family I choose is whether Moises Ca&iuml;cedo starts.</strong> With Enzo Fern&aacute;ndez sold on deadline day and unreplaced and Andrey Santos gone for &pound;50m, Ca&iuml;cedo is the last first-choice holder at the club, and Chelsea's 1.95 xG conceded per match was accumulated with him available. A confirmed team sheet naming him, or not, would settle whether the conceded side of the BTTS and totals rows is the one the four-match sample measured &mdash; and it bears directly on the discipline row too, against a Brentford side committing 15.5 fouls a match.</li>",
  "<li><strong>That question is now answered: Ca&iuml;cedo does not play, and Lavia does not start either.</strong> Chelsea's 1.95 xG conceded per match was accumulated with Ca&iuml;cedo available, so the conceded side of the BTTS and totals rows is no longer measuring the same team &mdash; which firms up BTTS and undercuts any read that needs Chelsea to concede at their existing rate rather than above it. <strong>The question that replaces it: whether a 36-year-old central midfielder and a 21-year-old, in a back-three system used for the first time, hold the ball against a press of 7.98 PPDA and 15.5 fouls a match under an official at 4.6 fouls per card.</strong> Nothing published settles that, and it is now the discipline row's largest single input.</li>")

# ---------------------------------------------------------------- f5
E("fx_0918_f5.html",
  "Espanyol foul more than anyone on the slate, Eder Sarabia is banned from the bench and the referee is making his seventh appearance in Primera</p>",
  "Espanyol foul more than anyone on the slate, Elche changed head coach in June, and the referee is making his fourth appearance in Primera</p>")

E("fx_0918_f5.html",
  "The structural headline is that this is <strong>the only fixture tonight in which both head coaches are the same men who finished last season &mdash; Manolo Gonz&aacute;lez at Espanyol and Eder Sarabia at Elche</strong> &mdash; and yet the squads underneath them turned over heavily, almost entirely through loans and purchase options rather than fees.",
  "The structural headline is a correction to what this card first carried. <strong>Elche have changed head coach: Eder Sarabia announced on 27 May 2026 that he was stepping down &mdash; his own decision, to rest, not a dismissal &mdash; and Mart&iacute;n Anselmi was appointed on 13 June 2026 on a one-year deal with an option for another.</strong> Anselmi is Argentine and arrives from Cruz Azul, Porto and Botafogo, with no previous season in Spain. Only Manolo Gonz&aacute;lez is the man who finished last season here, and the squads underneath both turned over heavily, almost entirely through loans and purchase options rather than fees. <strong>An earlier version of this card, built from a Spanish preview, named Sarabia as Elche's coach and reported him suspended from the bench. The confirmed team sheet names Anselmi and the club's own announcement dates the change to June: the preview was wrong and so was the card.</strong>")

E("fx_0918_f5.html",
  "<li><strong>Elche &mdash; turnover very high, funded by two large sales; Eder Sarabia continues but is suspended from the bench.</strong> <strong>No coaching change</strong>, though <strong>Sarabia cannot take his place on the touchline tonight through suspension</strong>.",
  "<li><strong>Elche &mdash; turnover very high, funded by two large sales; head coach changed 13 June 2026.</strong> <strong>Eder Sarabia stepped down of his own accord in late May and Mart&iacute;n Anselmi was announced on 13 June 2026</strong>, so the twelve arrivals below were assembled for a coach who had never worked in this division.")

E("fx_0918_f5.html",
  "<strong>Espanyol are without Jofre, Kike Garc&iacute;a and Javi Puado, all injured, with Gorosabel a doubt, and Omar El Hilali suspended for one match after being sent off against Rayo Vallecano</strong> &mdash; a red card taken three days ago, which is worth holding next to the card rates below. <strong>Elche's only confirmed injury absence is Yago Santiago</strong>, still recovering from a knee arthroscopy. <strong>Eder Sarabia is serving a touchline suspension and will not be on the bench.</strong> Probable elevens: <strong>Espanyol</strong> &mdash; Dmitrovi&#263;; Hartman, Riedel, Cabrera, Hinojo; Javi Hern&aacute;ndez, Exp&oacute;sito, Moscard&oacute;; Dolan, Zaragoza, Roberto Fern&aacute;ndez. <strong>Elche</strong> &mdash; Dituro; Sangar&eacute;, Chust, Redondo, Revivo; Valera, Aguado, Villar; Lemar, Buonanotte, Fer Ni&ntilde;o. Both probable back lines contain at least two players signed this summer.</li>",
  "<strong>Espanyol are without Javi Puado (knee), Kike Garc&iacute;a (hamstring) and Jofre Carreras (groin), and Omar El Hilali is suspended after his red card against Rayo Vallecano</strong> &mdash; a sending-off three days ago, which is worth holding next to the card rates below. <strong>Elche's only absence is Yago Santiago</strong>, still recovering from a knee arthroscopy: the shortest injury list on tonight's board. <strong>Confirmed elevens &mdash; Espanyol 4-2-3-1</strong>: Dmitrovi&#263;; Jes&uacute;s L&oacute;pez, Unai N&uacute;&ntilde;ez, Leandro Cabrera, Hinojo; Exp&oacute;sito, Javi Hern&aacute;ndez; Calatrava, Urko Gonz&aacute;lez, Zaragoza; Roberto Fern&aacute;ndez. <strong>Four of Espanyol's six summer loans are substitutes &mdash; Hartman, Moscard&oacute;, Drku&scaron;i&#263; and Dolan &mdash; so only Unai N&uacute;&ntilde;ez and Zaragoza start, and the &euro;5m Calatrava is the sole bought player in the eleven.</strong> <strong>Elche 4-3-3</strong>: Dituro; Buba Sangar&eacute;, Federico Redondo, V&iacute;ctor Chust, Revivo; Germ&aacute;n Valera, Morcillo, Gonzalo Villar; Cepeda, Lemar, Fer Ni&ntilde;o &mdash; with <strong>Buonanotte, Ponce and Aguado on the bench</strong>.</li>")

E("fx_0918_f5.html",
  "<strong>One source disagreement to flag:</strong> a Spanish preview reached in the same search places this fixture at Elche's Mart&iacute;nez Valero and describes both clubs as winless in 2026. The venue in the official fixture record is the <strong>RCDE Stadium in Barcelona with Espanyol at home</strong>, the referee designation is published as &ldquo;RCD Espanyol &ndash; Elche CF&rdquo;, and Espanyol have two wins this season. That article is not used.</li>",
  "<strong>Two source failures to flag, one of which reached the card.</strong> A Spanish preview placed this fixture at Elche's Mart&iacute;nez Valero and called both clubs winless in 2026; the confirmed team sheet gives the venue as the <strong>RCDE Stadium in Barcelona</strong>, matching the fixture record and the referee designation, so that flag was right and the article is not used. <strong>The second failure did reach the card: the same preview cluster named Eder Sarabia as Elche's head coach and reported him suspended from the bench. He left in May. That is corrected in the opening paragraph rather than quietly removed, and it is the one place on this board where a card stated something false.</strong></li>")

E("fx_0918_f5.html",
  "<li><strong>The one normal fixture is Espanyol&ndash;Elche.</strong>",
  "<li><strong>Espanyol&ndash;Elche has the deepest sample.</strong>")

for fn, pairs in EDITS.items():
    s = io.open(fn, encoding="utf-8").read()
    for old, new in pairs:
        if old not in s:
            sys.exit("MISS in %s: %s..." % (fn, old[:90]))
        s = s.replace(old, new, 1)
    io.open(fn, "w", encoding="utf-8").write(s)
    print("patched %s (%d edits)" % (fn, len(pairs)))
