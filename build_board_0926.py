# -*- coding: utf-8 -*-
"""Phase 3 assembly for slate 0926. Copies BOARD_SHELL_2.html and fills its
placeholders. The shell's CSS and markup are not touched; the slate table
header cells already carry the seven v4 columns. Cards are concatenated
verbatim from fx_0926_f*.html; fixtures still TODO get a placeholder card.

BOARD_SHELL_2.html is not in this repository. When it is missing, the shell
is recovered from context-board_0925.html, the last board it produced: only
the filled regions are swapped back to their placeholders, so the CSS and
every other byte of the shell come through unchanged. Run board_grid.py on
the output afterwards."""
import html as _h
import io, os, re

SHELL = "BOARD_SHELL_2.html"
SHELL_FROM = "context-board_0925.html"


def shell_from_board(path):
    s = io.open(path, encoding="utf-8", newline="").read()

    def sub(pat, rep):
        nonlocal s
        s2, n = re.subn(pat, lambda m: m.expand(rep), s, count=1, flags=re.S)
        if n != 1:
            raise SystemExit("shell recovery: pattern not found: %s" % pat[:60])
        s = s2

    sub(r"(<title>Market Board ).*?(</title>)", r"\g<1>{{DATE}}\g<2>")
    sub(r'(<header class="top">.*?<h1>).*?(</h1>)', r"\g<1><!--HEADLINE-->\g<2>")
    sub(r'(<p class="standfirst">).*?(</p>)', r"\g<1><!--STANDFIRST-->\g<2>")
    sub(r'(<div class="metaline">\s*<span>).*?(</span>\s*<span>).*?(</span>)',
        r"\g<1><!--DATE-->\g<2><!--COMPETITIONS-->\g<3>")
    sub(r"<!--GRID:start-->.*?<!--GRID:end-->", "<!--GRID-->")
    sub(r'(<h2 class="sec">The one thing shaping every game on this card</h2>\r?\n  ).*?(\r?\n</section>)',
        r"\g<1><!--OVERVIEW-->\g<2>")
    sub(r'(<h2 class="sec">Today&rsquo;s slate.*?<tbody>\r?\n      ).*?(\r?\n    </tbody>)',
        r"\g<1><!--SLATE_ROWS-->\g<2>")
    sub(r'(\r?\n  )<div class="note"><strong>Evidence\.</strong>.*?</div>'
        r'(?:\r?\n  <div class="note"><strong>Completion\.</strong>.*?</div>)?(\r?\n</section>)',
        "\\g<1><!--PROVENANCE_NOTE-->\\g<1><!--COMPLETION_NOTE-->\\g<2>")
    sub(r'(<nav class="jump">\r?\n    ).*?(\r?\n  </nav>)', r"\g<1><!--NAV_LINKS-->\g<2>")
    sub(r'(</section>\r?\n\r?\n)<article class="fixture.*</article>'
        r'(\r?\n\r?\n<section>\r?\n  <h2 class="sec">Across the card</h2>)', r"\g<1><!--FIXTURES-->\g<2>")
    sub(r'(<h2 class="sec">Across the card</h2>\r?\n  )<ul>.*?</ul>(\r?\n</section>)', r"\g<1><!--CLOSING-->\g<2>")
    sub(r'(<p><strong>Sources\.</strong> ).*?(</p>\r?\n</footer>)', r"\g<1><!--SOURCES-->\g<2>")
    return s


if os.path.exists(SHELL):
    shell = io.open(SHELL, encoding="utf-8", newline="").read()
else:
    shell = shell_from_board(SHELL_FROM)
progress = io.open("progress_0926.md", encoding="utf-8").read()
done = {int(m.group(1)) for m in re.finditer(r"^f(\d+) \|.*\| DONE\s*$", progress, re.M)}
tiers = {int(m.group(1)): m.group(2) for m in re.finditer(r"^f(\d+) \|[^|]*\|[^|]*\| (T\d)", progress, re.M)}

FIX = [
 # id, kickoff, competition (slate table), league line, home, away, venue, referee, flag
 (1, "15:00", "Nations League B &middot; B1 MD1", "UEFA &middot; Nations League B, Group B1 &middot; Matchday 1",
  "Slovenia", "Scotland", "Stadion Sto&zcaron;ice, Ljubljana", "Hora&#539;iu Fe&#537;nic", "both coaches new"),
 (2, "18:00", "Nations League C &middot; C1 MD1", "UEFA &middot; Nations League C, Group C1 &middot; Matchday 1",
  "San Marino", "Finland", "San Marino Stadium, Serravalle", "Nathan Verboomen", "promoted side"),
 (3, "18:00", "Nations League C &middot; C3 MD1", "UEFA &middot; Nations League C, Group C3 &middot; Matchday 1",
  "Faroe Islands", "Kazakhstan", "T&oacute;rsv&oslash;llur, T&oacute;rshavn", "Ishmael Barbara", "relegated side, new coach"),
 (4, "18:00", "Nations League C &middot; C4 MD1", "UEFA &middot; Nations League C, Group C4 &middot; Matchday 1",
  "Bulgaria", "Luxembourg", "Hristo Botev Stadium, Plovdiv", "Sander van der Eijk", "high squad turnover"),
 (5, "18:00", "Nations League C &middot; C4 MD1", "UEFA &middot; Nations League C, Group C4 &middot; Matchday 1",
  "Iceland", "Estonia", "Laugardalsv&ouml;llur, Reykjav&iacute;k", "Milo&scaron; Milanovi&cacute;", "relegated side"),
 (6, "20:45", "Nations League A &middot; A3 MD1", "UEFA &middot; Nations League A, Group A3 &middot; Matchday 1",
  "Czechia", "Croatia", "Fortuna Arena, Prague", "Simone Sozza", "promoted side, new coaches"),
 (7, "20:45", "Nations League A &middot; A3 MD1", "UEFA &middot; Nations League A, Group A3 &middot; Matchday 1",
  "England", "Spain", "Wembley Stadium, London", "Davide Massa", "promoted side"),
 (8, "20:45", "Nations League B &middot; B1 MD1", "UEFA &middot; Nations League B, Group B1 &middot; Matchday 1",
  "North Macedonia", "Switzerland", "To&scaron;e Proeski Arena, Skopje", "Daniel Schlager", "promoted and relegated sides"),
 (9, "20:45", "Nations League C &middot; C1 MD1", "UEFA &middot; Nations League C, Group C1 &middot; Matchday 1",
  "Albania", "Belarus", "Air Albania Stadium (Arena Komb&euml;tare), Tirana", "Sam Barrott", "both coaches new"),
 (10, "20:45", "Nations League C &middot; C3 MD1", "UEFA &middot; Nations League C, Group C3 &middot; Matchday 1",
  "Slovakia", "Moldova", "Futbal Tatran Arena, Pre&scaron;ov", "Juxhin Xhaja", "promoted side, new coach"),
]
N = len(FIX)
n_done = sum(1 for f in FIX if f[0] in done)
n_t1 = sum(1 for f in FIX if f[0] in done and tiers.get(f[0]) == "T1")
n_t2 = sum(1 for f in FIX if f[0] in done and tiers.get(f[0]) == "T2")
WORDS = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

DATE = "Saturday 26 September 2026"
HEADLINE = ("Eight coaches take their first competitive match of their current spell on today&rsquo;s card, "
            "and none of the twenty sides has played a competitive match this season")
STANDFIRST = ("Ten Nations League fixtures parsed from the typed sheet slate.10.xlsx &mdash; "
              "%d of %d cards built, %s at full T1 depth and %s at reduced T2 depth."
              % (n_done, N, WORDS[n_t1], WORDS[n_t2]))
COMPETITIONS = ("Nations League A matchday 1 &middot; Nations League B matchday 1 &middot; "
                "Nations League C matchday 1")

OVERVIEW = """<p>The single structural fact across this card is that <strong>every number on it is last season&rsquo;s, and much of it was set under coaches who have since gone</strong>. This is matchday 1 of the 2026&ndash;27 Nations League, and ESPN&rsquo;s standings show 0 played for all twenty sides. Ten of them last played a competitive match in November 2025, four in March 2026 and six at the World Cup; the gap runs from 69 days (Spain, the World Cup final) to 317 (Estonia, a qualifier in Oslo).</p>
<p>The second is who those numbers belong to. <strong>Eight coaches take their first competitive match of their current spell: Bo&scaron;tjan Cesar and S&eacute;bastien Pocognoli in Ljubljana, John van &rsquo;t Schip with Kazakhstan in T&oacute;rshavn, Santi Denia and Slaven Bili&cacute; (a second spell) in Prague, Rolando Maran and Viktor Goncharenko in Tirana, and Vladim&iacute;r Weiss (a second spell) with Slovakia in Pre&scaron;ov.</strong> Eleven sides carry a division change into tonight: San Marino and Moldova promoted from League D, North Macedonia from League C, Czechia and England from League B; Scotland and Switzerland relegated from League A, Finland, Albania, Kazakhstan and Iceland from League B. North Macedonia&ndash;Switzerland is a promoted side hosting a relegated one, in the first meeting of the two. This is also the first League C edition with no relegation. The absences land on the positions the spec weights: Slovenia without &Scaron;e&scaron;ko, Scotland without McTominay, Czechia without Schick (retired) and four injured defenders, England without Rice, Stones, Reece James and Spence, Switzerland without Xhaka, Embolo, Zakaria, Amenda and Vargas, and Iceland without their first-choice goalkeeper and Sverrir Ingi Ingason.</p>
<div class="note"><strong>Structural consequence.</strong> Result families are the least readable on the card: the 1X2 is Dangerous on seven of ten, OK only at San Marino&ndash;Finland, Iceland&ndash;Estonia and Slovakia&ndash;Moldova; the Asian handicap is Dangerous on five (Slovenia&ndash;Scotland, San Marino&ndash;Finland, Iceland&ndash;Estonia, North Macedonia&ndash;Switzerland, Slovakia&ndash;Moldova). Corners, the best-supported family on the 25 September board, are Dangerous on seven of ten here, because on most cards the corner split turns on the level of the opposition and tonight neither side meets its usual level; they are OK only at San Marino&ndash;Finland, Iceland&ndash;Estonia and England&ndash;Spain. Discipline and Team goals are the only families with no Dangerous verdict anywhere: Discipline is OK or split on all ten, each row carrying a published appointment, and Team goals are OK at Albania&ndash;Belarus and split on the other nine, with at least one side readable on each. Totals are OK or split on eight, Well-suited at Bulgaria&ndash;Luxembourg (the board&rsquo;s only Well-suited verdict) and Dangerous only at England&ndash;Spain. BTTS is Dangerous at Czechia&ndash;Croatia, England&ndash;Spain and Albania&ndash;Belarus; Halves only at Czechia&ndash;Croatia and England&ndash;Spain. Every card carries at least one Dangerous verdict.</div>"""


def unk(v):
    return '<td class="unk">%s</td>' % v


def card_ref(fid):
    try:
        c = io.open("fx_0926_f%d.html" % fid, encoding="utf-8").read()
    except IOError:
        return None
    m = re.search(r"<dt>Referee</dt><dd>(.*?)</dd>", c, re.S)
    if not m:
        return None
    name = re.split(r"&middot;|·", m.group(1))[0]
    name = re.sub(r"<[^>]+>", "", name)
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip() or None


rows = []
for fid, ko, comp, league, h, a, venue, ref, flag in FIX:
    built = fid in done
    ref = (card_ref(fid) or ref) if built else ref
    rows.append("<tr><td>%s</td><td>%s</td><td>%s &ndash; %s</td><td>%s</td>%s<td>0 &middot; 0</td><td>%s</td></tr>" % (
        ko, comp, h, a, venue,
        ("<td>%s</td>" % ref) if (built and ref) else unk("not yet researched"),
        flag))
SLATE_ROWS = "\n      ".join(rows)

PROVENANCE_NOTE = """<div class="note"><strong>Evidence.</strong> No number on this board was supplied to me and none was estimated. Team rates were computed match by match from ESPN&rsquo;s public match record for the Nations League, World Cup qualifying, the World Cup, play-offs and friendlies with a usable box score &mdash; results for goals, over 2.5, BTTS, clean sheets and failed-to-score; per-match box scores for corners, fouls, cards and shots; key-event periods for first-half goals. <strong>League baselines are in baselines_0926.md</strong> and were recomputed from ESPN&rsquo;s record of the 2024&ndash;25 edition of each division &mdash; League A, League B and League C, each matching its baselines_0924.md or baselines_0925.md entry &mdash; with zero baseline searches, because 2026&ndash;27 has no completed match in any of today&rsquo;s groups; the context lines for promoted and relegated sides beneath them were computed the same way. <strong>Fields unpublished across the slate:</strong> match-level xG for national teams &mdash; ESPN carries none for internationals, and the xG on the board is FotMob&rsquo;s competition totals (qualifying, and the World Cup where played), printed as totals; transfer fees have no national-team equivalent, and squad turnover is read from call-ups, injuries and retirements against each side&rsquo;s competitive starts since September 2024. ESPN&rsquo;s officials field was still empty for all ten matches when the cards were written; every appointment on the board was taken from Wikipedia&rsquo;s division pages citing UEFA&rsquo;s match pages, most with a second source. Starting elevens were in ESPN&rsquo;s record before writing only for Slovenia&ndash;Scotland and Iceland&ndash;Estonia. For part of this session the environment&rsquo;s network policy blocked ESPN and Wikipedia: Iceland&ndash;Estonia was first built without them and then rebuilt in full, and Czechia&ndash;Croatia was re-read from ESPN before it was finished, so no card on this board rests on the blocked build. <strong>Last season standing in for a thin current sample:</strong> everywhere &mdash; every strip is 24/25 and 25/26 with match counts in brackets, because the 26/27 sample is zero for all twenty sides.</div>"""

pending = [f for f in FIX if f[0] not in done]
reduced = [f for f in FIX if f[0] in done and tiers.get(f[0]) == "T2"]
COMPLETION_NOTE = ""
if pending or reduced:
    parts = ["%d of %d cards are built, %s at full T1 depth" % (n_done, N, WORDS[n_t1])]
    if reduced:
        parts.append(" and %s at reduced T2 depth (%s: sections A, C and D only)" % (
            WORDS[len(reduced)], ", ".join("f%d %s &ndash; %s" % (f[0], f[4], f[5]) for f in reduced)))
    parts.append(". ")
    if pending:
        parts.append("Still pending: %s &mdash; those cards show the fixture line only. " % ", ".join(
            "f%d %s &ndash; %s" % (f[0], f[4], f[5]) for f in pending))
    parts.append("Nothing was listed without research. Triage set eight fixtures at T1 and two at T2 on capacity, "
                 "and f3 Faroe Islands &ndash; Kazakhstan was moved to T1 in Phase 2 when its first search found "
                 "Kazakhstan&rsquo;s coach change. The depth of each card follows the evidence available and the "
                 "capacity, not merit, and a reduced card is not a judgement on the game.")
    COMPLETION_NOTE = '<div class="note"><strong>Completion.</strong> %s</div>' % "".join(parts)

NAV_LINKS = "\n    ".join(
    '<a href="#f%d">%s &ndash; %s<span>%s &middot; %s</span></a>' % (fid, h, a, ko, venue.split(",")[0])
    for fid, ko, comp, league, h, a, venue, ref, flag in FIX)

cards = []
for fid, ko, comp, league, h, a, venue, ref, flag in FIX:
    path = "fx_0926_f%d.html" % fid
    if fid in done and os.path.exists(path):
        cards.append(io.open(path, encoding="utf-8").read().strip())
    else:
        md = league.split("&middot;")[-1].strip()
        cards.append("""<article class="fixture pending" id="f%d">
  <div class="fx-head">
    <p class="fx-league">%s</p>
    <h2 class="fx-title">%s &ndash; %s</h2>
    <p class="fx-sub">%s CEST &middot; %s</p>
  </div>
  <div class="fx-body">
    <dl class="fx-odds">
      <div class="od"><dt>Kickoff</dt><dd>%s CEST</dd></div>
      <div class="od"><dt>Venue</dt><dd>%s</dd></div>
      <div class="od"><dt>Matchday</dt><dd>%s</dd></div>
    </dl>
    <div class="pending-note">Context not yet built.</div>
  </div>
</article>""" % (fid, league, h, a, ko, venue, ko, venue, md))
FIXTURES = "\n\n".join(cards)

CLOSING = """<ul>
<li><strong>Best structurally supported:</strong> Discipline, OK or split on all ten fixtures, every row reading a published appointment against both team lines; Team goals, OK at Albania&ndash;Belarus and split on the other nine, with at least one side readable on each; Totals, Well-suited at Bulgaria&ndash;Luxembourg, OK or split on eight more, and best on the card at Albania&ndash;Belarus and Slovakia&ndash;Moldova; BTTS, OK on seven of ten.</li>
<li><strong>Least supported:</strong> the 1X2, Dangerous at Slovenia&ndash;Scotland, Faroe Islands&ndash;Kazakhstan, Bulgaria&ndash;Luxembourg, Czechia&ndash;Croatia, England&ndash;Spain, North Macedonia&ndash;Switzerland and Albania&ndash;Belarus; Corners, Dangerous at Slovenia&ndash;Scotland, Faroe Islands&ndash;Kazakhstan, Bulgaria&ndash;Luxembourg, Czechia&ndash;Croatia, North Macedonia&ndash;Switzerland, Albania&ndash;Belarus and Slovakia&ndash;Moldova; the Asian handicap, Dangerous on five of ten; BTTS at Czechia&ndash;Croatia, England&ndash;Spain and Albania&ndash;Belarus; Halves at Czechia&ndash;Croatia and England&ndash;Spain; Totals at England&ndash;Spain, where the windows run from 1.75 to 4.43 goals per match.</li>
<li><strong>No normal fixture.</strong> Every card carries at least one Dangerous verdict. San Marino&ndash;Finland and Iceland&ndash;Estonia come closest, with one each, on the Asian handicap.</li>
<li><strong>Thinnest evidence:</strong> Slovenia&ndash;Scotland, Albania&ndash;Belarus and Slovakia&ndash;Moldova, where the coaches changed after most figures in the strip were recorded and the cards are flagged high-uncertainty; North Macedonia&ndash;Switzerland, also flagged, where the home coach has one competitive match and players outside Switzerland&rsquo;s squad made 72 of their 198 competitive starts; Faroe Islands&ndash;Kazakhstan, where the referee&rsquo;s ESPN record is eleven matches, ten of them club matches and only four with a box score; Bulgaria&ndash;Luxembourg, built at reduced depth.</li>
</ul>"""

# Sources: the named source of every bullet under each fixture heading in sources_0926.md
src = io.open("sources_0926.md", encoding="utf-8").read()
items = []
for sec in re.split(r"^## ", src, flags=re.M)[1:]:
    head = sec.splitlines()[0]
    if not head.startswith("f"):
        continue
    for line in sec.splitlines()[1:]:
        if line.startswith("- "):
            t = re.split(r" — | -- ", line[2:])[0]
            t = re.sub(r"[`*]", "", t).strip()
            if t and t not in items:
                items.append(t)
SOURCES = " &middot; ".join(_h.escape(t) for t in items)

out = shell
out = out.replace("{{DATE}}", DATE)
out = out.replace("<!--DATE-->", DATE)
out = out.replace("<!--HEADLINE-->", HEADLINE)
out = out.replace("<!--STANDFIRST-->", STANDFIRST)
out = out.replace("<!--COMPETITIONS-->", COMPETITIONS)
out = out.replace("<!--OVERVIEW-->", OVERVIEW)
out = out.replace("<!--SLATE_ROWS-->", SLATE_ROWS)
out = out.replace("<!--PROVENANCE_NOTE-->", PROVENANCE_NOTE)
if COMPLETION_NOTE:
    out = out.replace("<!--COMPLETION_NOTE-->", COMPLETION_NOTE)
else:
    out = re.sub(r"\r?\n  <!--COMPLETION_NOTE-->", "", out).replace("<!--COMPLETION_NOTE-->", "")
out = out.replace("<!--NAV_LINKS-->", NAV_LINKS)
out = out.replace("<!--FIXTURES-->", FIXTURES)
out = out.replace("<!--CLOSING-->", CLOSING)
out = out.replace("<!--SOURCES-->", SOURCES)
io.open("context-board_0926.html", "w", encoding="utf-8", newline="").write(out)
print("context-board_0926.html: %d of %d cards built" % (n_done, N))
