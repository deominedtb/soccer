# -*- coding: utf-8 -*-
"""Second lineup patch: f4 and f5, plus a wording fix in f1."""
import io, sys

EDITS = {}
def E(fn, old, new):
    EDITS.setdefault(fn, []).append((old, new))

# ---------------------------------------------------------------- f1 wording
# ---------------------------------------------------------------- f4
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

for fn, pairs in EDITS.items():
    s = io.open(fn, encoding="utf-8").read()
    for old, new in pairs:
        if old not in s:
            sys.exit("MISS in %s: %s..." % (fn, old[:90]))
        s = s.replace(old, new, 1)
    io.open(fn, "w", encoding="utf-8").write(s)
    print("patched %s (%d edits)" % (fn, len(pairs)))
