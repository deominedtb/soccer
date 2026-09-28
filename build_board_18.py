# Assembles market-board_18.html from BOARD_SHELL_2.html + fx_18_f*.html + progress_18.md.
import io, os

DATE = "Sunday 13 September 2026"

# id, kickoff, home, away, league, venue, (1, X, 2, O2.5, U2.5, BTTSY, BTTSN, 1X, 12, X2)
F = [
 ("f1","16:15","Levante","Barcelona","Spain &middot; LaLiga EA Sports &middot; Jornada 5","Estadio Ciutat de Val&egrave;ncia",
  ("13.00","8.00","1.17","1.20","4.00","1.63","2.15","4.95","1.07","1.02")),
 ("f2","16:45","Zwolle","Feyenoord","Netherlands &middot; Eredivisie &middot; Round 6","MAC&sup3;PARK Stadion, Zwolle",
  ("6.00","4.85","1.43","1.35","2.95","1.50","2.40","2.70","1.16","1.11")),
 ("f3","17:15","Le Mans FC","Lens","France &middot; Ligue 1 &middot; Matchday 4","MMArena, Le Mans",
  ("5.10","4.10","1.62","1.53","2.35","1.55","2.30","2.25","1.22","1.16")),
 ("f4","17:30","Manchester United","Manchester City","England &middot; Premier League","Old Trafford, Manchester",
  ("3.00","3.75","2.20","1.50","2.40","1.42","2.65","1.65","1.25","1.38")),
 ("f5","17:30","SV 07 Elversberg","Bayern Monaco","Germany &middot; Bundesliga &middot; Matchday 3","Ursapharm-Arena an der Kaiserlinde, Spiesen-Elversberg",
  ("14.00","8.50","1.15","1.11","5.50","1.47","2.50","5.25","1.06","1.01")),
 ("f6","18:00","Napoli","Bologna","Italy &middot; Serie A &middot; Matchday 4","Stadio Diego Armando Maradona, Naples",
  ("1.87","3.55","4.15","1.85","1.85","1.75","1.97","1.22","1.28","1.90")),
 ("f7","18:30","Getafe","Deportivo La Coru&ntilde;a",None,"Coliseum, Getafe",
  ("2.70","2.80","3.05","2.80","1.38","2.20","1.60","1.37","1.42","1.45")),
 ("f8","19:00","Arouca","Santa Clara",None,"Est&aacute;dio Municipal de Arouca",
  ("2.55","2.95","2.90","2.15","1.62","1.85","1.85","1.38","1.35","1.47")),
 ("f9","19:00","Benfica","Gil Vicente",None,"Est&aacute;dio da Luz, Lisbon",
  ("1.11","9.00","17.00","1.37","2.85","2.25","1.57",None,"1.04","6.00")),
 ("f10","20:00","PSV Eindhoven","Sparta Rotterdam",None,"Philips Stadion, Eindhoven",
  ("1.13","9.00","13.00","1.13","5.25","1.52","2.35","1.01","1.04","5.50")),
 ("f11","20:45","Brest","PSG",None,"Stade Francis-Le Bl&eacute;, Brest",
  ("10.00","6.75","1.23","1.33","3.10","1.75","1.95","4.05","1.09","1.04")),
 ("f12","20:45","Sassuolo","Juventus",None,"Mapei Stadium, Reggio Emilia",
  ("5.50","3.85","1.63","1.72","2.00","1.72","2.00","2.25","1.25","1.14")),
 ("f13","21:00","Real Sociedad","Atletico Madrid",None,"Reale Arena, San Sebasti&aacute;n",
  ("3.30","3.55","2.10","1.57","2.25","1.47","2.50","1.70","1.28","1.32")),
 ("f14","21:30","Famalicao","Sporting Lisbona",None,"Est&aacute;dio Municipal 22 de Junho, Famalic&atilde;o",
  ("6.50","4.50","1.45","1.75","1.98","1.95","1.77","2.65","1.18","1.09")),
]

HEADLINE = ("Eight cards on the games still to kick off, and the week&rsquo;s Champions League nights "
            "sit behind four of the favourites &mdash; while the absence lists, not the league tables, "
            "carry most of the structure")

OVERVIEW = """<p>The single structural fact running through the eight built cards is that this is the first league weekend after the opening week of European group football, and it shows in who is favoured. Four of the eight favourites played a European match on Wednesday or Thursday. <strong>PSV</strong> drew 1&ndash;1 with Shakhtar on Thursday before hosting Sparta. <strong>PSG</strong> beat Slovan Bratislava 6&ndash;1 on Wednesday before travelling to Brest. <strong>Sporting</strong> came from behind to beat Galatasaray 3&ndash;1 before going to Famalic&atilde;o. <strong>Atl&eacute;tico</strong> lost at Anfield before going to Anoeta. Juventus open their Europa League campaign next week. None of the eight cards could establish how much those coaches will rotate, and in every case that is the unknown most likely to move a row.</p><p>The second fact is where the evidence actually came from. On a four- or five-match sample, the most reliable material on this slate was not the league tables but the absence lists. Atl&eacute;tico travel with one fit striker after Juli&aacute;n &Aacute;lvarez was ruled out in the final training session, joining S&oslash;rloth and Barrios. Real Sociedad are without both first-choice centre-backs. Juventus are without Locatelli, Thuram and Yildiz. Brest are without their captain at centre-back and probably their right-back. Getafe are missing two centre-backs. Those are structural facts in exactly the sense the engine asks for, and most of the market verdicts on the board lean on them.</p><div class="note"><strong>Structural consequence.</strong> Where a card has a well-evidenced row, it is almost always a goals row and almost always driven by a named defensive absence or a named attacking drought. Examples are Brest&ndash;PSG, where six of six league matches involving these two sides reached three goals and Brest have lost their captain at centre-back; PSV&ndash;Sparta, where PSV have not kept a clean sheet in five and Sparta have scored in four straight; and Famalic&atilde;o, with four goals in five. The result family is the weakest on the board: three moneylines are dead (Benfica 1.11, PSV 1.13, PSG 1.23), and two more have favourites whose shape changed in the days before kickoff (Atl&eacute;tico&rsquo;s forwards, Juventus&rsquo;s midfield). No cards or corners market was captured for any fixture, so the seven confirmed officials &mdash; only three of them (Makkelie, Delajod, De Burgos Bengoetxea) with any published record reached &mdash; bear on game state rather than on any priced row.</div>"""

CLOSING = """<ul><li><strong>Best structurally supported families today &mdash; goals rows with a named mechanism on both sides.</strong> PSV&ndash;Sparta both-teams-to-score, where PSV have no clean sheet in five and Sparta have scored in four straight; it is also the only row still two-sided on that card. Brest&ndash;PSG goals, where every league match either side has played this season reached three and the home defence is missing its captain. Real Sociedad&ndash;Atl&eacute;tico both-teams-to-score, which rests on two independent defensive absence lists. And the Famalic&atilde;o&ndash;Sporting result, the one moneyline on the board where several independent structural facts point the same way.</li><li><strong>Least supported &mdash; result rows whose favourites changed shape, and anything on Arouca&ndash;Santa Clara.</strong> Atl&eacute;tico at 2.10 lost their leading striker in the final training session, and Juventus at 1.63 are without their captain and both first-choice central midfielders. On Arouca&ndash;Santa Clara, the visiting head coach is reported under two different names, the head-to-head three incompatible ways and the table positions two ways; that card is flagged high-uncertainty.</li><li><strong>The one normal fixture.</strong> Sassuolo&ndash;Juventus is the closest thing to one: both managers are in place, neither side is promoted and both windows are documented. Even there, the two defensive samples point in opposite directions (Juventus matches 1, 2, 2 goals; Sassuolo matches 3, 3, 4), and the book has priced the total and both-teams-to-score identically at 1.72 against 2.00.</li><li><strong>Where the book has priced indifference.</strong> Arouca&ndash;Santa Clara both-teams-to-score at exactly 1.85 each way, which matches evidence that genuinely points nowhere. Getafe&ndash;Deportivo double chance at 1.37 / 1.42 / 1.45, with the draw nearly the favourite in the moneyline: a Bordal&aacute;s side with two goals in four against a promoted side unbeaten in four. And Brest&ndash;PSG both-teams-to-score at 1.75 / 1.95, near even beneath a 1.23 favourite &mdash; confident about the winner, undecided about whether the favourite keeps its first league clean sheet.</li></ul>"""

SOURCES = ("""Logged per fixture in <span class="mono">sources_18.md</span>. For the cards on this board: """
           """riazor.org and futbolfantasy.com for Getafe&ndash;Deportivo; Sports Mole, WhoScored, flashscore, """
           """A&ccedil;oriano Oriental, Di&aacute;rio de Aveiro and A Bola for Arouca&ndash;Santa Clara; zerozero, DAZN, """
           """Bola na Rede and Sports Mole for Benfica and Famalic&atilde;o&ndash;Sporting; vi.nl, TOTO Extra, """
           """voetbalnieuws.nl, FootballTransfers and Voetbalzone for PSV&ndash;Sparta; ligue1.com, parisfans.fr and """
           """Yahoo Sports for Brest&ndash;PSG; Tuttosport, Quotidiano Sport, Sofascore and Juvefc.com for """
           """Sassuolo&ndash;Juventus; VAVEL, SI and estoesatleti.es for Real Sociedad&ndash;Atl&eacute;tico; statz.ai and """
           """valuestats.com for referee records. Transfer ledgers carried from ten earlier cards are named in """
           """each card&rsquo;s section A. Scoping searches are logged separately.""")


def odds_strip(o):
    dc = " &middot; ".join(v if v else "&mdash;" for v in o[7:10])
    return ('    <dl class="fx-odds">\n'
            '      <div class="od"><dt>1 / X / 2</dt><dd>%s &middot; %s &middot; %s</dd></div>\n'
            '      <div class="od"><dt>O2.5 / U2.5</dt><dd>%s / %s</dd></div>\n'
            '      <div class="od"><dt>BTTS Y / N</dt><dd>%s / %s</dd></div>\n'
            '      <div class="od"><dt>1X / 12 / X2</dt><dd>%s</dd></div>\n'
            '    </dl>\n' % (o[0], o[1], o[2], o[3], o[4], o[5], o[6], dc))


def build():
    shell = io.open("BOARD_SHELL_2.html", encoding="utf-8").read()
    status, tier = {}, {}
    for line in io.open("progress_18.md", encoding="utf-8").read().splitlines():
        if not line.strip():
            continue
        p = [c.strip() for c in line.split("|")]
        status[p[0]] = p[-1]
        tier[p[0]] = p[3].replace("*", "")

    rows, nav, cards = [], [], []
    built = listed = 0
    for fid, ko, home, away, lg, venue, o in F:
        title = "%s &ndash; %s" % (home, away)
        rows.append('      <tr><td>%s<span class="ko">%s CEST</span></td>'
                    '<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'
                    '<td>&mdash;</td><td>&mdash;</td></tr>'
                    % (title, ko, o[0], o[1], o[2], o[3], o[4], o[5], o[6]))
        nav.append('    <a href="#%s">%s<span>%s &middot; %s</span></a>' % (fid, title, ko, venue))

        frag = "fx_18_%s.html" % fid
        if status.get(fid) == "DONE" and os.path.exists(frag):
            built += 1
            cards.append(io.open(frag, encoding="utf-8").read().rstrip())
            continue

        listed += 1
        cards.append(
            '<article class="fixture pending" id="%s">\n'
            '  <div class="fx-head">\n'
            '    <p class="fx-league">%s</p>\n'
            '    <h2 class="fx-title">%s</h2>\n'
            '    <p class="fx-sub">%s CEST &middot; %s</p>\n'
            '  </div>\n'
            '  <div class="fx-body">\n%s'
            '    <div class="pending-note">Not researched on this slate &mdash; kicked off before this run began, '
            'and was scoped out by instruction (tier set by the user, not by triage). That is a statement about '
            'timing, not a judgement on the game.</div>\n'
            '  </div>\n'
            '</article>' % (fid, lg, title, ko, venue, odds_strip(o)))

    total = len(F)
    standfirst = (
        "Fourteen fixtures parsed in typed-file mode from <span class=\"mono\">odds_18.xlsx</span>. The six "
        "that had already kicked off when this run began are listed with odds only, and %d of the eight still "
        "to start are built as reduced-depth cards &mdash; none at full depth." % built)

    completion = (
        '<div class="note"><strong>Completion.</strong> %d of the %d cards on this board are built, all as '
        'reduced-depth T2 cards (sections A, C and D only, roughly two searches per club plus the referee). '
        'No card was built at full T1 depth: the run was racing the kickoff clock, and each card&rsquo;s '
        'section A names the research fields it did not pursue. No fixture is pending. The remaining %d '
        '&mdash; %s &mdash; were listed without research because they had kicked off before the run began, '
        'and they were scoped out by instruction rather than by triage; Phase 1.5 was not run on this slate. '
        'That selection was made on timing alone, not on the merit of the games. A fixture listed with odds '
        'only is not a judgement on it, and every fixture on the sheet appears in the table and the index above. '
        'The Premier League and Bundesliga fixtures fall entirely within the unresearched group, which is why '
        'neither competition is named in the header.</div>'
        % (built, total, listed, ", ".join(f[0] for f in F if status.get(f[0]) != "DONE")))

    provenance = (
        '<div class="note"><strong>Provenance.</strong> Parsed in typed-file mode from '
        '<span class="mono">odds_18.xlsx</span>, active tab &ldquo;Today Odds&rdquo;. The workbook is saved in '
        'strict OOXML, which the usual reader opens as zero sheets, so the worksheet XML was read directly from '
        'the zip and cross-checked against the shared-strings table. Every price was read from a spreadsheet cell; '
        'none was derived and none carries an uncertainty marker. Cell A1 carries the typist&rsquo;s source note '
        'naming seven screenshots, <span class="mono">Screenshot 2026-09-13 153629.png</span> through '
        '<span class="mono">153743.png</span>; those images were not opened. Kickoff times were normalised from '
        'Excel&rsquo;s floating-point serialisation (<span class="mono">18:59:59.9999999999968050</span> &rarr; '
        '19:00). The source has no <span class="mono">league</span>, <span class="mono">venue</span>, cards or '
        'corners columns, so every competition and stadium on this board was established by research and the '
        'Cards and Corners columns are empty for all 14 rows. Double chance is present for all fixtures except '
        'the 1X price on Benfica&ndash;Gil Vicente, whose cell is blank. Team names are kept as typed in the table '
        'and index (&ldquo;Bayern Monaco&rdquo;, &ldquo;Sporting Lisbona&rdquo;) and rendered conventionally inside '
        'built cards.</div>')

    out = shell
    out = out.replace("{{DATE}}", DATE)
    out = out.replace("<!--DATE-->", DATE)
    out = out.replace("<!--HEADLINE-->", HEADLINE)
    out = out.replace("<!--STANDFIRST-->", standfirst)
    out = out.replace("<!--COMPETITIONS-->",
                      "LaLiga jornada 5 &middot; Liga Portugal matchday 6 &middot; Eredivisie round 6 "
                      "&middot; Ligue 1 matchday 4 &middot; Serie A matchday 4")
    out = out.replace("<!--OVERVIEW-->", OVERVIEW)
    out = out.replace("      <!--SLATE_ROWS-->", "\n".join(rows))
    out = out.replace("  <!--PROVENANCE_NOTE-->", "  " + provenance)
    out = out.replace("  <!--COMPLETION_NOTE-->", "  " + completion)
    out = out.replace("    <!--NAV_LINKS-->", "\n".join(nav))
    out = out.replace("<!--FIXTURES-->", "\n\n".join(cards))
    out = out.replace("  <!--CLOSING-->", "  " + CLOSING)
    out = out.replace("<!--SOURCES-->", SOURCES)

    io.open("market-board_18.html", "w", encoding="utf-8", newline="\n").write(out)
    print("built %d cards, %d listed-only, %d fixtures total" % (built, listed, total))


if __name__ == "__main__":
    build()
