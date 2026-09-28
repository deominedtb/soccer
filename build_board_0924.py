# -*- coding: utf-8 -*-
"""Phase 3 assembly for slate 0924. Copies BOARD_SHELL_2.html and fills its
placeholders. The shell's CSS and markup are not touched; the slate table
header cells already carry the seven v4 columns. Cards are concatenated
verbatim from fx_0924_f*.html; fixtures still TODO get a placeholder card."""
import io, os, re

shell = io.open("BOARD_SHELL_2.html", encoding="utf-8").read()
progress = io.open("progress_0924.md", encoding="utf-8").read()
done = {int(m.group(1)) for m in re.finditer(r"^f(\d+) \|.*\| DONE\s*$", progress, re.M)}

FIX = [
 # id, kickoff, competition (slate table), league line, home, away, venue, referee, flag
 (1, "18:00", "Nations League D &middot; D1 MD1", "UEFA &middot; Nations League D, Group D1 &middot; Matchday 1",
  "Andorra", "Malta", "Estadi de la FAF, Encamp", "Joey Kooij", "new Malta coach"),
 (2, "20:45", "Nations League A &middot; A2 MD1", "UEFA &middot; Nations League A, Group A2 &middot; Matchday 1",
  "Netherlands", "Germany", "Johan Cruijff Arena, Amsterdam", "Alejandro Hern&aacute;ndez Hern&aacute;ndez", "both coaches debut"),
 (3, "20:45", "Nations League A &middot; A2 MD1", "UEFA &middot; Nations League A, Group A2 &middot; Matchday 1",
  "Serbia", "Greece", "Rajko Miti&#263; Stadium, Belgrade", "Glenn Nyberg", "promoted side"),
 (4, "20:45", "Nations League A &middot; A4 MD1", "UEFA &middot; Nations League A, Group A4 &middot; Matchday 1",
  "Norway", "Denmark", "Ullevaal Stadion, Oslo", "Tobias Stieler", "promoted side"),
 (5, "20:45", "Nations League A &middot; A4 MD1", "UEFA &middot; Nations League A, Group A4 &middot; Matchday 1",
  "Portugal", "Wales", "Est&aacute;dio Jos&eacute; Alvalade, Lisbon", "Donatas Rum&scaron;as", "new coach, promoted side"),
 (6, "20:45", "Nations League B &middot; B3 MD1", "UEFA &middot; Nations League B, Group B3 &middot; Matchday 1",
  "Austria", "Israel", "Raiffeisen Arena, Linz", None, "relegated side"),
 (7, "20:45", "Nations League B &middot; B3 MD1", "UEFA &middot; Nations League B, Group B3 &middot; Matchday 1",
  "Kosovo", "Republic of Ireland", "Stadiumi Fadil Vokrri, Prishtina", None, "promoted side"),
 (8, "20:45", "Nations League D &middot; D2 MD1", "UEFA &middot; Nations League D, Group D2 &middot; Matchday 1",
  "Liechtenstein", "Lithuania", "Rheinpark Stadion, Vaduz", None, "relegated side"),
]
N = len(FIX)
n_done = sum(1 for f in FIX if f[0] in done)

DATE = "Thursday 24 September 2026"
HEADLINE = ("No side on tonight&rsquo;s card has played a competitive match this season, "
            "and the Netherlands, Germany and Portugal all open under a coach none of their numbers belong to")
STANDFIRST = ("Eight Nations League fixtures parsed from the typed sheet slate.8.xlsx &mdash; "
              "%d of %d cards built at full T1 depth so far, the rest still being researched." % (n_done, N))
COMPETITIONS = ("Nations League A matchday 1 &middot; Nations League B matchday 1 &middot; "
                "Nations League D matchday 1")

OVERVIEW = """<p>The single structural fact across this card is that <strong>every number on it is last season&rsquo;s</strong>. This is matchday 1 of the 2026&ndash;27 Nations League and the first competitive fixture of the season for all sixteen sides; ESPN&rsquo;s standings show 0 played everywhere. The strips therefore read the 2024&ndash;25 Nations League edition and 2025&ndash;26 World Cup qualifying and finals, and the gap to each side&rsquo;s last competitive match runs from 75 days (Norway, a World Cup quarter-final) to more than 300 (Serbia and Greece, November 2025).</p>
<p>The second is who those numbers belong to. <strong>The Netherlands open under Xavi (appointed 12 August) and Germany under J&uuml;rgen Klopp (contract from 15 August), Portugal under Jorge Jesus (appointed 10 July), and Malta under a coach who was in charge for none of their League D record.</strong> Serbia have been under Veljko Paunovi&#263; since 30 October 2025 and moved to a back four under him, after most of their strip was recorded. Three sides are new to League A: Greece through the March 2025 play-off, Norway and Wales as League B group winners. The absences land on the positions the spec weights: Germany without Wirtz, R&uuml;diger and Neuer; Serbia without Vlahovi&#263;, Mitrovi&#263;, Milenkovi&#263; and Rajkovi&#263;; Denmark with a new goalkeeper after Kasper Schmeichel&rsquo;s retirement; Wales without Darlow, Rodon, Lawlor and Harry Wilson; Norway without S&oslash;rloth; Austria without Laimer, Sabitzer, Baumgartner and Alaba, and without the retired Marko Arnautovi&#263;.</p>
<div class="note"><strong>Structural consequence.</strong> Result families are the least readable on the card: the Asian handicap is Dangerous on all seven built cards and the 1X2 on five of them, OK only at Portugal&ndash;Wales and Austria&ndash;Israel. Totals hold up best &mdash; OK on six of seven &mdash; because they rest on scoring rates that stayed near the division line through a change of coach or personnel; BTTS is OK on five. Corners carry the board&rsquo;s only Well-suited verdict, at Austria&ndash;Israel, where the split agrees in every window, and are OK on the four League A cards. Discipline is OK on five, and at Serbia&ndash;Greece it is the best-supported family on the card, because there the official is the stable half and the two sides&rsquo; records point opposite ways.</div>"""


def unk(v):
    return '<td class="unk">%s</td>' % v


def card_ref(fid):
    try:
        c = io.open("fx_0924_f%d.html" % fid, encoding="utf-8").read()
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

PROVENANCE_NOTE = """<div class="note"><strong>Evidence.</strong> No number on this board was supplied to me and none was estimated. Team rates were computed match by match from ESPN&rsquo;s public match record for the Nations League, World Cup qualifying and the World Cup &mdash; results for goals, over 2.5, BTTS, clean sheets and failed-to-score; per-match box scores for corners, fouls, cards and shots; key-event periods for first-half goals. <strong>League baselines are in baselines_0924.md</strong> and were built the same way from the 2024&ndash;25 edition of each division, because 2026&ndash;27 has no completed match: League A over 48 group matches, League D over 12, with 2022&ndash;23 as a cross-check. League D&rsquo;s twelve-match line is the thinnest baseline on the board. <strong>Fields unpublished across the slate:</strong> match-level xG for national teams &mdash; ESPN carries none for the Nations League or qualifying and Understat does not cover internationals; the only xG on the board is partial World Cup and qualifying figures for Germany and Portugal from FootyStats and Opta Analyst, and every other xG cell reads not published. Transfer fees have no national-team equivalent; squad turnover is read from call-ups, injuries and retirements. <strong>Last season standing in for a thin current sample:</strong> everywhere &mdash; every strip is 24/25 and 25/26 with match counts in brackets, because the 26/27 sample is zero for every side.</div>"""

pending = [f for f in FIX if f[0] not in done]
COMPLETION_NOTE = ""
if pending:
    names = ", ".join("f%d %s &ndash; %s" % (f[0], f[4], f[5]) for f in pending)
    COMPLETION_NOTE = ("""<div class="note"><strong>Completion.</strong> %d of %d cards are built, all at full T1 depth. Still pending: %s &mdash; research is in progress and those cards show the fixture line only. Triage put all eight fixtures at T1 because capacity covered the whole slate; nothing was listed without research, and a pending card is not a judgement on the game.</div>"""
                       % (n_done, N, names))

NAV_LINKS = "\n    ".join(
    '<a href="#f%d">%s &ndash; %s<span>%s &middot; %s</span></a>' % (fid, h, a, ko, venue.split(",")[0])
    for fid, ko, comp, league, h, a, venue, ref, flag in FIX)

cards = []
for fid, ko, comp, league, h, a, venue, ref, flag in FIX:
    path = "fx_0924_f%d.html" % fid
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
<li><strong>Best structurally supported:</strong> Corners at Austria&ndash;Israel, the one Well-suited verdict on the board; Totals, OK at Andorra&ndash;Malta, Netherlands&ndash;Germany, Norway&ndash;Denmark, Portugal&ndash;Wales, Austria&ndash;Israel and Liechtenstein&ndash;Lithuania; BTTS, OK at Andorra&ndash;Malta, Netherlands&ndash;Germany, Norway&ndash;Denmark, Portugal&ndash;Wales and Austria&ndash;Israel; match corners, OK on all four League A cards; Discipline, OK at Serbia&ndash;Greece (the best family on that card), Norway&ndash;Denmark, Portugal&ndash;Wales, Austria&ndash;Israel and Liechtenstein&ndash;Lithuania.</li>
<li><strong>Least supported:</strong> the Asian handicap, Dangerous on every built card; the 1X2, Dangerous everywhere except Portugal&ndash;Wales and Austria&ndash;Israel; first-half result, Dangerous inside every Halves row; corners in both League D ties; BTTS at Serbia&ndash;Greece and Liechtenstein&ndash;Lithuania, where the two sides&rsquo; steadiest series pull opposite ways; Discipline at Andorra&ndash;Malta and Netherlands&ndash;Germany, where the official&rsquo;s records point opposite ways.</li>
<li><strong>No normal fixture.</strong> Every built card carries a coach debut, a promoted side, or a long list of absences at the weighted positions, and every strip is last season&rsquo;s.</li>
<li><strong>Thinnest evidence:</strong> Netherlands&ndash;Germany and Serbia&ndash;Greece, both flagged high-uncertainty because their rates belong to previous coaches or shapes; Andorra&ndash;Malta and Liechtenstein&ndash;Lithuania, on four- and six-match Nations League samples against a twelve-match division line. The pending cards are not yet on the board at all.</li>
</ul>"""

# Sources: the named source of every bullet under each fixture heading in sources_0924.md
src = io.open("sources_0924.md", encoding="utf-8").read()
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
import html as _h
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
    out = out.replace("  <!--COMPLETION_NOTE-->\n", "").replace("<!--COMPLETION_NOTE-->", "")
out = out.replace("<!--NAV_LINKS-->", NAV_LINKS)
out = out.replace("<!--FIXTURES-->", FIXTURES)
out = out.replace("<!--CLOSING-->", CLOSING)
out = out.replace("<!--SOURCES-->", SOURCES)
io.open("context-board_0924.html", "w", encoding="utf-8").write(out)
print("context-board_0924.html: %d of %d cards built" % (n_done, N))
