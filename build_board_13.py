# Assembles market-board_13.html from BOARD_SHELL_2.html + fx_13_f*.html + progress_13.md.
# Phase 3 helper. Narrative blocks at the top are rewritten by hand on each Phase 3 run;
# counts, slate rows, nav links and placeholder cards are generated.
import io, os, re

DATE = "Saturday 5 September 2026"

# id, kickoff, home, away, league (None until Phase 2 establishes it), venue, odds, t3_reason
F = [
 ("f1","15:00","Fiorentina","Torino","Serie A","Stadio Artemio Franchi, Florence",
  ("2.05","3.30","3.85","1.90","1.85","1.72","2.05","4.5","8.5"),None),
 ("f2","15:30","Bayer Leverkusen","Union Berlino","Bundesliga","BayArena, Leverkusen",
  ("1.37","5.25","7.50","1.35","2.95","1.50","2.40","3.5","10.5"),None),
 ("f3","15:30","Borussia M&ouml;nchengladbach","SV 07 Elversberg","Bundesliga","Borussia-Park, M&ouml;nchengladbach",
  ("1.90","3.80","3.75","1.43","2.60","1.50","2.40","3.5","9.5"),None),
 ("f4","15:30","Hoffenheim","Borussia Dortmund",None,None,
  ("2.60","3.80","2.45","1.42","2.65","1.37","2.85","3.5","9.5"),None),
 ("f5","15:30","SC Paderborn","Friburgo",None,None,
  ("3.75","3.65","1.95","1.60","2.20","1.53","2.35","3.5","9.5"),None),
 ("f6","15:30","Werder Brema","Lipsia",None,None,
  ("4.10","4.15","1.75","1.37","2.85","1.40","2.75","3.5","9.5"),None),
 ("f7","16:00","Brentford","Sunderland",None,None,
  ("1.73","3.80","4.75","1.80","1.95","1.72","2.05","3.5","9.5"),None),
 ("f8","16:00","Brighton","Leeds United",None,None,
  ("2.05","3.50","3.60","1.75","2.00","1.62","2.20","4.5","9.5"),None),
 ("f9","16:00","Fulham FC","Crystal Palace",None,None,
  ("2.15","3.25","3.60","1.90","1.85","1.68","2.10","3.5","9.5"),None),
 ("f10","16:00","Manchester City","Coventry City",None,None,
  ("1.18","7.50","13.00","1.35","3.00","2.00","1.75","2.5","10.5"),
  "five of ten captured markets are still two-sided, the shortest result price is 1.18, and the fixture carries the result-dead, derived-live 4/7 flag"),
 ("f11","16:00","Nottingham Forest","Tottenham",None,None,
  ("2.50","3.40","2.80","1.75","2.00","1.60","2.25","3.5","10.5"),None),
 ("f12","16:15","Athletic Bilbao","Atletico Madrid",None,None,
  ("3.00","3.30","2.40","1.85","1.85","1.62","2.15","4.5","9.5"),
  "it scored a total of 4 and lost the tie-break for the last reduced-depth slot; one club was carded in full within the last three slates"),
 ("f13","17:15","Lens","Lorient",None,None,
  ("1.55","4.35","5.50","1.60","2.20","1.68","2.05","3.5","9.5"),None),
 ("f14","18:00","Inter","Napoli",None,None,
  ("1.67","3.75","5.50","1.85","1.90","1.85","1.90","3.5","9.5"),
  "it scored a total of 3, separated cleanly by score with no tie-break; both clubs were carded in full within the last three slates"),
 ("f15","18:30","Hull City","Aston Villa",None,None,
  ("4.00","3.60","1.90","1.85","1.90","1.75","2.00","3.5","9.5"),None),
 ("f16","18:30","Rayo Vallecano","Racing Santander",None,None,
  ("2.00","3.50","3.75","1.65","2.10","1.55","2.30","5.5","10.5"),None),
 ("f17","18:30","Schalke 04","Bayern Monaco",None,None,
  ("14.00","8.50","1.15","1.20","4.20","1.65","2.10","3.5","9.5"),
  "four of eight captured markets are still two-sided, the lowest live-row count on the sheet, and the fixture carries the result-dead, derived-live 3/5 flag"),
 ("f18","20:45","Roma","Atalanta",None,None,
  ("1.70","3.80","4.90","1.65","2.15","1.62","2.20","3.5","9.5"),
  "it scored a total of 4 and lost the tie-break for the last reduced-depth slot; both clubs were carded in full within the last three slates"),
 ("f19","20:45","Le Havre AC","Brest",None,None,
  ("2.70","3.25","2.65","1.90","1.80","1.72","2.00","3.5","9.5"),None),
 ("f20","20:45","Nizza","Le Mans FC",None,None,
  ("1.75","3.75","4.50","1.75","1.97","1.65","2.10","4.5","9.5"),
  "it scored a total of 4; both clubs were carded in full within the last three slates and its distinctiveness score was still provisional at the triage cap"),
 ("f21","21:00","Villarreal","Deportivo La Coru&ntilde;a",None,None,
  ("1.48","4.60","6.25","1.65","2.15","1.72","2.00","4.5","10.5"),
  "it scored a total of 4 and lost the tie-break for the last reduced-depth slot"),
]

HEADLINE = ("Three promoted clubs, five new head coaches and a slate the triage "
            "cut in half &mdash; the first three cards are built and every one of them "
            "turns on a manager appointed since May")

OVERVIEW = """<p>The structural fact running through this card is that the odds sheet is 21 fixtures long and the evidence behind it is not. This is the largest slate parsed so far &mdash; three and a half times the size of the last one &mdash; and it arrives on the second or third matchday of five different competitions, which is precisely the point in a season when a club&rsquo;s last-season numbers describe a squad that no longer exists and its current numbers amount to 90 or 180 minutes. Every card on this board is written against that constraint rather than around it.</p><p>The second thread is managerial churn, and it is unusually concentrated. Of the six clubs carded so far, five are being coached by someone appointed since May 2026: Fabio Grosso arrived at Fiorentina from Sassuolo on a two-year deal reported at &euro;1.2m a year, Ignazio Abate took over at Torino, Carles Mart&iacute;nez replaced Ole Werner at Bayer Leverkusen, and Mauro Lustrinelli left a title-winning season at FC Thun on 21 May for his first Bundesliga job at Union Berlin. The exception proves the rule: Eugen Polanski keeps his job at M&ouml;nchengladbach precisely because he was the mid-season appointment who rescued the previous campaign, having taken over on 15 September 2025. The third thread is promotion. The Bundesliga came up three &mdash; Schalke 04, SV 07 Elversberg and SC Paderborn, replacing St. Pauli, Heidenheim and Wolfsburg &mdash; and one of them, Elversberg, won its first ever top-flight match 3&ndash;2 away at Leverkusen, which is the single loudest result on the sheet and also its least repeatable.</p><div class="note"><strong>Structural consequence.</strong> Discipline is again the family that carries the most evidence, and for the same reason as always: a referee&rsquo;s card rate does not move when clubs buy and sell. All three appointments on the built cards are named &mdash; Davide Massa at the Franchi, confirmed by the federation designation list with a full officiating team; Martin Petersen at Borussia-Park, confirmed; Benjamin Brand at the BayArena, reported in the match preview but not corroborated by a designation list, and flagged as such on that card. What none of the three has is a published fouls-per-card ratio, so on every card the mechanism behind the number is missing even where the number itself is solid. Two of the three sit above their posted line on the evidence available: Petersen&rsquo;s 4.07 yellows a game against a 3.5 line, Brand&rsquo;s 3.95 cards a game against the same. Massa is the odd case &mdash; the only figure published for him anywhere reached is a red-card rate of 0.41 per game, level-highest in Serie A and more than double the division average of 0.18, and it is set against the highest card line on the built cards at 4.5.</div>"""

CLOSING = """<ul><li><strong>Best structurally supported family today &mdash; discipline, on the two fixtures with a confirmed appointment.</strong> M&ouml;nchengladbach&ndash;Elversberg and Fiorentina&ndash;Torino both carry a federation-confirmed official, and in Petersen&rsquo;s case a 288-match career record at 4.07 yellows a game against a 3.5 line. That is the only kind of evidence on this board built from more than two matchdays. Leverkusen&ndash;Union has the better-documented referee record of the three &mdash; 19 matches, 72 yellows, 3 reds, four penalties last season &mdash; but the appointment itself is reported rather than confirmed, which is why that row is rated one step below.</li><li><strong>Least supported family &mdash; goals totals, on all three built cards without exception.</strong> Two of the three are priced at 1.43 or shorter on the over: Leverkusen&ndash;Union at 1.35 off two matchday-one scorelines that produced six goals each, and M&ouml;nchengladbach&ndash;Elversberg at 1.43 off a promoted club&rsquo;s 64-goal second-tier season and a 3&ndash;0 defeat at Leipzig. The third, Fiorentina&ndash;Torino at 1.90/1.85, is the book declining to take a view on two attacks that have not scored, which is the honest position given the evidence.</li><li><strong>The one fixture where a season-long record still describes the team &mdash; none of the three, and that is the finding.</strong> Every built card has either a new head coach or a promotion inside it. The closest to a stable reading is M&ouml;nchengladbach, whose 42 goals scored and 53 conceded were produced under the coach still in the job, and even there the number covers a season he only joined in mid-September.</li><li><strong>Where the book has priced indifference.</strong> Twice on the built cards, and in both cases it is describing the evidence accurately. Fiorentina&ndash;Torino has cards at 1.80 both ways and a goals total at 1.90/1.85 &mdash; two winless teams under two new coaches, and a referee whose only published metric is his red-card rate. M&ouml;nchengladbach&ndash;Elversberg prices 1X and 12 identically at 1.25, an explicit statement that a home win and an away win are near-equivalent risks when the promoted side won at Leverkusen the week before.</li></ul>"""

SOURCES = ("""Sources are logged per fixture in <span class="mono">sources_13.md</span> as each card is built. """
           """For the cards on this board: Lega Serie A designation lists via calcionews24, toro.it, toronews.net, """
           """firenzeviola.it and CalVAR; bundesliga.com, DFB Datencenter, kicker.de and sportschau.de for German """
           """appointments and squads; Wikipedia season and transfer pages; football-italia.net, flashscore.com, """
           """violanation.com, bulinews.com, getfootballnewsgermany.com and Yahoo Sports for previews and mercato; """
           """statshub.com, whoscored.com, fussballdaten.de, oddalerts.com and sbonews.sbostats.com for referee """
           """records; ESPN, fotmob.com and Sky Sports for team news and head-to-head. Triage searches are logged """
           """separately under the Triage heading in the same file.""")

def kickoff_league(lg):
    return lg if lg else "competition not yet established"

def build():
    shell = io.open("BOARD_SHELL_2.html", encoding="utf-8").read()
    prog = io.open("progress_13.md", encoding="utf-8").read().splitlines()
    status, tier = {}, {}
    for line in prog:
        if not line.strip():
            continue
        p = [c.strip() for c in line.split("|")]
        status[p[0]] = p[-1]
        tier[p[0]] = p[3].replace("*", "")

    rows, nav, cards = [], [], []
    built = pending_todo = listed = 0
    for fid, ko, home, away, lg, venue, o, t3 in F:
        title = "%s &ndash; %s" % (home, away)
        rows.append('      <tr><td>%s<span class="ko">%s &middot; %s</span></td>'
                    '<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'
                    '<td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                    % (title, ko, kickoff_league(lg), o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8]))
        nav.append('    <a href="#%s">%s<span>%s &middot; %s</span></a>'
                   % (fid, title, ko, venue if venue else "venue not yet established"))

        frag = "fx_13_%s.html" % fid
        if status.get(fid) == "DONE" and os.path.exists(frag):
            built += 1
            cards.append(io.open(frag, encoding="utf-8").read().rstrip())
            continue

        if tier.get(fid) == "T3":
            listed += 1
            note = ('<div class="pending-note">Not researched on this slate &mdash; %s. '
                    'That is a statement about the evidence available to research, not a judgement '
                    'on the game.</div>' % t3)
            sub = "%s CEST &middot; venue not established &mdash; listed with odds only" % ko
        else:
            pending_todo += 1
            note = '<div class="pending-note">Context not yet built.</div>'
            sub = "%s CEST &middot; venue not yet established &mdash; card pending at %s" % (ko, tier.get(fid, "T1"))

        odds_strip = (
            '    <dl class="fx-odds">\n'
            '      <div class="od"><dt>1 / X / 2</dt><dd>%s &middot; %s &middot; %s</dd></div>\n'
            '      <div class="od"><dt>O2.5 / U2.5</dt><dd>%s / %s</dd></div>\n'
            '      <div class="od"><dt>BTTS Y / N</dt><dd>%s / %s</dd></div>\n'
            '      <div class="od"><dt>Cards line</dt><dd>%s</dd></div>\n'
            '      <div class="od"><dt>Corners line</dt><dd>%s</dd></div>\n'
            '    </dl>\n' % (o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8]))

        cards.append(
            '<article class="fixture pending" id="%s">\n'
            '  <div class="fx-head">\n'
            '    <p class="fx-league">%s</p>\n'
            '    <h2 class="fx-title">%s</h2>\n'
            '    <p class="fx-sub">%s</p>\n'
            '  </div>\n'
            '  <div class="fx-body">\n%s    %s\n  </div>\n'
            '</article>' % (fid, kickoff_league(lg).capitalize() if lg else "Competition not yet established",
                            title, sub, odds_strip, note))

    total = len(F)
    researchable = 14
    standfirst = (
        "Twenty-one fixtures across five countries, parsed in typed-file mode from "
        "<span class=\"mono\">odds_13.xlsx</span> and triaged before research began &mdash; "
        "%d of the %d fixtures the triage left researchable are complete, %d at full depth "
        "and %d as reduced-depth cards, with the remaining %d listed on odds alone."
        % (built, researchable, sum(1 for f in F if status.get(f[0]) == "DONE" and tier.get(f[0]) == "T1"),
           sum(1 for f in F if status.get(f[0]) == "DONE" and tier.get(f[0]) == "T2"), total - built))

    completion = (
        '<div class="note"><strong>Completion.</strong> %d of the %d cards on this board are built: '
        '%d at full T1 depth and %d as reduced-depth T2 cards, which carry sections A, C and D only. '
        '%d fixtures the triage left researchable are still pending &mdash; %s &mdash; and appear here with '
        'their odds strip and no context. A further %d fixtures were listed without research at all: '
        '%s. That selection was made on the evidence available to research each fixture &mdash; how many '
        'of its captured markets are still two-sided, whether the referee appointment can exist yet, '
        'whether either club was already carded in full on a recent slate &mdash; and not on the merit of '
        'the games. A fixture listed with odds only is not a judgement on it, and every fixture on the '
        'sheet appears in the table and the index above regardless of tier.</div>'
        % (built, total, sum(1 for f in F if status.get(f[0]) == "DONE" and tier.get(f[0]) == "T1"),
           sum(1 for f in F if status.get(f[0]) == "DONE" and tier.get(f[0]) == "T2"),
           pending_todo,
           ", ".join(f[0] for f in F if status.get(f[0]) != "DONE" and tier.get(f[0]) != "T3"),
           listed,
           ", ".join(f[0] for f in F if tier.get(f[0]) == "T3")))

    provenance = (
        '<div class="note"><strong>Provenance.</strong> This slate was parsed in typed-file mode from '
        '<span class="mono">odds_13.xlsx</span>. No screenshots were involved, so there are no source image '
        'filenames and no OCR step: every price was read directly from a spreadsheet cell, none derived, none '
        'unreadable, and no value on this board carries an uncertainty marker. The workbook now holds seven tabs '
        '&mdash; an unused <span class="mono">odds_EXAMPLE</span> template, then <span class="mono">odds_7</span> '
        'through <span class="mono">odds_11</span> (28, 29, 30, 31 August and 4 September, all already consumed as '
        'fixtures_8 to fixtures_12), and a seventh tab whose title row reads &ldquo;MATCHES 05-09-2026 &mdash; odds '
        'read from screenshots&rdquo;, which is today&rsquo;s slate and the one read here, despite the tab itself '
        'still being internally named <span class="mono">odds_12</span>. That is the same one-file lag seen in the '
        'three previous workbooks and it was not used for numbering. The file is written in strict OOXML, which '
        'returns an empty sheet list to the usual reader; the worksheet XML was parsed directly from the zip and '
        'cross-checked against the shared-strings table. Kickoff times were normalised from Excel&rsquo;s '
        'floating-point time serialisation (<span class="mono">20:44:59.99999999997441975</span> &rarr; 20:45). Two '
        'fields are structurally absent rather than unread &mdash; there is no <span class="mono">league</span> '
        'column and no <span class="mono">venue</span> column anywhere in the sheet, so every competition, matchday '
        'and stadium named on this board was established by research, and the fixtures not yet researched carry no '
        'competition or venue at all rather than an inferred one. <span class="mono">Win/+2 Home/Away</span> is empty '
        'for all 21 rows. Home and away card splits are present for eight fixtures only &mdash; f1, f7, f8, f9, f10, '
        'f11, f15 and f18 &mdash; and are shown on those cards. Team names are recorded exactly as typed in the '
        'source; the Italian-style forms carried over from earlier slates (&ldquo;Union Berlino&rdquo;, '
        '&ldquo;Friburgo&rdquo;, &ldquo;Lipsia&rdquo;, &ldquo;Werder Brema&rdquo;, &ldquo;Bayern Monaco&rdquo;, '
        '&ldquo;Nizza&rdquo;) are kept in the table and index and rendered conventionally inside a card once that '
        'card is built.</div>')

    out = shell
    out = out.replace("{{DATE}}", DATE)
    out = out.replace("<!--DATE-->", DATE)
    out = out.replace("<!--HEADLINE-->", HEADLINE)
    out = out.replace("<!--STANDFIRST-->", standfirst)
    out = out.replace("<!--COMPETITIONS-->",
                      "Serie A matchday 3 &middot; Bundesliga matchday 2 &middot; Premier League "
                      "&middot; LaLiga &middot; Ligue 1 &middot; cup ties not yet established")
    out = out.replace("<!--OVERVIEW-->", OVERVIEW)
    out = out.replace("      <!--SLATE_ROWS-->", "\n".join(rows))
    out = out.replace("  <!--PROVENANCE_NOTE-->", "  " + provenance)
    out = out.replace("  <!--COMPLETION_NOTE-->", "  " + completion)
    out = out.replace("    <!--NAV_LINKS-->", "\n".join(nav))
    out = out.replace("<!--FIXTURES-->", "\n\n".join(cards))
    out = out.replace("  <!--CLOSING-->", "  " + CLOSING)
    out = out.replace("<!--SOURCES-->", SOURCES)

    io.open("market-board_13.html", "w", encoding="utf-8", newline="\n").write(out)
    print("built %d cards, %d pending, %d listed-only, %d fixtures total" % (built, pending_todo, listed, total))

if __name__ == "__main__":
    build()
