# -*- coding: utf-8 -*-
"""Phase 3 assembly for slate 0927. Copies BOARD_SHELL_2.html and fills its
placeholders. The shell's CSS and markup are not touched; the slate table
header cells already carry the seven v4 columns. Cards are concatenated
verbatim from fx_0927_f*.html; fixtures still TODO get a placeholder card.

    python build_board_0927.py 1800   -> context-board_0927_1800.html (f1-f4, the 18:00 games)
    python build_board_0927.py        -> context-board_0927.html (all seven)

Run board_grid.py on the output afterwards."""
import html as _h
import io, os, re, sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "full"
if MODE not in ("1800", "full"):
    raise SystemExit("usage: build_board_0927.py [1800]")
OUT = "context-board_0927_1800.html" if MODE == "1800" else "context-board_0927.html"

shell = io.open("BOARD_SHELL_2.html", encoding="utf-8", newline="").read()
progress = io.open("progress_0927.md", encoding="utf-8").read()
done = {int(m.group(1)) for m in re.finditer(r"^f(\d+) \|.*\| DONE\s*$", progress, re.M)}
tiers = {int(m.group(1)): m.group(2) for m in re.finditer(r"^f(\d+) \|[^|]*\|[^|]*\| (T\d)", progress, re.M)}

ALL = [
 # id, kickoff, competition (slate table), league line, home, away, venue, played, flag
 (1, "18:00", "Nations League D &middot; D1 MD2", "UEFA &middot; Nations League D, Group D1 &middot; Matchday 2",
  "Gibraltar", "Andorra", "Europa Point Stadium, Gibraltar", "0 &middot; 1", "Gibraltar&rsquo;s first match"),
 (2, "18:00", "Nations League A &middot; A2 MD2", "UEFA &middot; Nations League A, Group A2 &middot; Matchday 2",
  "Serbia", "Netherlands", "Rajko Miti&#263; Stadium, Belgrade", "1 &middot; 1", "both coaches new"),
 (3, "18:00", "Nations League A &middot; A4 MD2", "UEFA &middot; Nations League A, Group A4 &middot; Matchday 2",
  "Denmark", "Wales", "Parken Stadium, Copenhagen", "1 &middot; 1", "promoted side"),
 (4, "18:00", "Nations League B &middot; B3 MD2", "UEFA &middot; Nations League B, Group B3 &middot; Matchday 2",
  "Austria", "Kosovo", "Ernst-Happel-Stadion, Vienna", "1 &middot; 1", "promoted side, first meeting"),
 (5, "20:45", "Nations League A &middot; A2 MD2", "UEFA &middot; Nations League A, Group A2 &middot; Matchday 2",
  "Germany", "Greece", "WWK Arena, Augsburg", "1 &middot; 1", "promoted side, new coach"),
 (6, "20:45", "Nations League A &middot; A4 MD2", "UEFA &middot; Nations League A, Group A4 &middot; Matchday 2",
  "Norway", "Portugal", "Ullevaal Stadion, Oslo", "1 &middot; 1", "promoted side, new coach"),
 (7, "20:45", "Nations League B &middot; B3 MD2", "UEFA &middot; Nations League B, Group B3 &middot; Matchday 2",
  "Israel", "Ireland", "Nagyerdei Stadion, Debrecen (Hungary)", "1 &middot; 1", "relegated side, neutral venue"),
]
FIX = [f for f in ALL if MODE == "full" or f[1] == "18:00"]
N = len(FIX)
n_done = sum(1 for f in FIX if f[0] in done)
n_t1 = sum(1 for f in FIX if f[0] in done and tiers.get(f[0]) == "T1")
WORDS = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}


def card(fid):
    p = "fx_0927_f%d.html" % fid
    return io.open(p, encoding="utf-8").read() if (fid in done and os.path.exists(p)) else None


def card_ref(fid):
    c = card(fid)
    m = c and re.search(r"<dt>Referee</dt><dd>(.*?)</dd>", c, re.S)
    if not m:
        return None
    name = re.sub(r"<[^>]+>", "", re.split(r"&middot;|·", m.group(1))[0])
    return name.strip() or None


def card_venue(fid):
    c = card(fid)
    m = c and re.search(r'<p class="fx-sub">[^&]*&middot; (.*?) &middot;', c, re.S)
    return m.group(1).strip() if m else None


DATE = "Sunday 27 September 2026"

if MODE == "1800":
    HEADLINE = ("At 18:00 every card reads a record built by players or coaches who are not there tonight: "
                "Austria&rsquo;s absentees scored 31 of their 45 goals, the Netherlands&rsquo; 23 of 55")
    STANDFIRST = ("The four 18:00 CEST Nations League fixtures from the seven on the typed sheet slate.11.xlsx &mdash; "
                  "%d of %d cards built, %s at full T1 depth; the three 20:45 games follow on the full board."
                  % (n_done, N, WORDS[n_t1]))
    COMPETITIONS = ("Nations League A matchday 2 &middot; Nations League B matchday 2 &middot; "
                    "Nations League D matchday 2")
    OVERVIEW = """<p>The single structural fact across the 18:00 card is that <strong>the numbers on it were built by people who are missing tonight</strong>. It is matchday 2 of the 2026&ndash;27 Nations League, three days after matchday 1, so every current sample is one match (Gibraltar&rsquo;s is none) and every strip is last season&rsquo;s. That record belongs to other players. Austria are without Laimer, Sabitzer, Baumgartner, Alaba and the retired Arnautovi&cacute;, and Gregoritsch is doubtful; those six scored 31 of Austria&rsquo;s 45 attributed goals since September 2024, and a debutant starts in goal. The Netherlands&rsquo; absentees scored 23 of their 55, including all three centre-forwards who started in the window; Serbia&rsquo;s scored 9 of 14 (Mitrovi&cacute; and Vlahovi&cacute; both out). Wales are without Harry Wilson, Darlow and Rodon, who made 38 of 176 starts and scored 10 of 30 attributed goals. Denmark&rsquo;s Parken record was kept by Schmeichel and anchored by Vestergaard, and both have retired. Kosovo&rsquo;s captain Amir Rrahmani quit on 11&ndash;12 September. Andorra are without Cerv&oacute;s, who made 12 of 13 starts.</p>
<p>Where the players stayed, the benches changed. <strong>Serbia (Paunovi&cacute;, three competitive matches) and the Netherlands (Xavi, one) both have new coaches, and Gibraltar&rsquo;s League D line was built under Julio Ribas: all ten of Scott Wiseman&rsquo;s competitive matches came against sides from League C and above.</strong> Two sides carry a promotion into tonight: Wales, up from League B, at Parken, and Kosovo, up from League C through the play-off, in Vienna for a first-ever meeting. Gibraltar&ndash;Andorra carries no promotion stake at all, because this is the last League D edition and all six sides go up whatever their finish. The division lines are League D, A and B 2024&ndash;25, and League D&rsquo;s is the least steady of them: over 2.5 fell from 44.4% to 16.7% between its last two editions and cards rose from 3.94 to 7.42.</p>
<div class="note"><strong>Structural consequence.</strong> Result families read better than the absences suggest: the 1X2, the Asian handicap and Halves are OK on all four, because the structural priors (stayed-in-A hosts against promoted visitors, Serbia against this level, Andorra&rsquo;s away record) do not depend on who scores. The scoring families carry the absences. BTTS is Dangerous at Serbia&ndash;Netherlands and Austria&ndash;Kosovo, Totals Dangerous at Austria&ndash;Kosovo, and Team goals is split on all four: the Andorra, Serbia, Wales and Kosovo sides are the readable ones, and the other side rests on a coach&rsquo;s untested line (Gibraltar), missing scorers (the Netherlands, Austria) or a new back line opposite (Denmark). Corners are the best-supported family: Well-suited at Denmark&ndash;Wales and Austria&ndash;Kosovo, where every window points the same way and none depends on the absentees, and OK at the other two. Discipline is split on three, fouls OK and cards dangerous where the official books below the division line; it is OK outright only at Austria&ndash;Kosovo, where Nick Walsh sits on it.</div>"""
    CLOSING = """<ul>
<li><strong>Best structurally supported:</strong> Corners, Well-suited at Denmark&ndash;Wales and Austria&ndash;Kosovo, the only Well-suited verdicts at 18:00, and OK at Gibraltar&ndash;Andorra and Serbia&ndash;Netherlands; the 1X2, the Asian handicap and Halves, OK on all four; fouls, OK wherever Discipline is split.</li>
<li><strong>Least supported:</strong> BTTS at Serbia&ndash;Netherlands and Austria&ndash;Kosovo, and Totals at Austria&ndash;Kosovo, where the windows nearest tonight disagree by a goal and a half; the card count at Gibraltar&ndash;Andorra, Serbia&ndash;Netherlands and Denmark&ndash;Wales; Team goals on the Gibraltar, Netherlands and Austria sides.</li>
<li><strong>No normal fixture.</strong> Gibraltar&ndash;Andorra and Denmark&ndash;Wales carry no outright Dangerous verdict, but each has a split with a dangerous half: Gibraltar&rsquo;s team goals and the card count at Europa Point, the card count at Parken.</li>
<li><strong>Thinnest evidence:</strong> Gibraltar&ndash;Andorra, where the home coach has no League D match, the division line is a twelve-match edition that moves, and the referee&rsquo;s appointment is from press reports with UEFA&rsquo;s page not read; Austria&ndash;Kosovo, where both spines have turned over and Kosovo&rsquo;s record at this level was built with a captain who has quit; Serbia&ndash;Netherlands, with two new benches and both leading attacks out.</li>
</ul>"""
else:
    HEADLINE = ("Four League A benches are new and most of the goals are missing: Germany&rsquo;s absentees "
                "scored 34 of their 52, Austria&rsquo;s 31 of 45, the Netherlands&rsquo; 23 of 55")
    STANDFIRST = ("Seven Nations League fixtures parsed from the typed sheet slate.11.xlsx &mdash; "
                  "%d of %d cards built, %s at full T1 depth." % (n_done, N, WORDS[n_t1]))
    COMPETITIONS = ("Nations League A matchday 2 &middot; Nations League B matchday 2 &middot; "
                    "Nations League D matchday 2")
    OVERVIEW = """<p>The single structural fact across this card is that <strong>the numbers on it were built by people who are not there tonight</strong>. It is matchday 2 of the 2026&ndash;27 Nations League, three days after matchday 1, so every current sample is one match (Gibraltar&rsquo;s is none) and every strip is last season&rsquo;s. Four of the eight League A benches on the card have changed since the qualifiers: J&uuml;rgen Klopp with Germany and Jorge Jesus with Portugal take their second match, Xavi with the Netherlands his second, and Veljko Paunovi&cacute; with Serbia his fourth competitive one. Every German figure but Thursday&rsquo;s is Nagelsmann&rsquo;s, every Portuguese one Mart&iacute;nez&rsquo;s, every Dutch one Koeman&rsquo;s. Gibraltar&rsquo;s League D line was built under Julio Ribas, and all ten of Scott Wiseman&rsquo;s competitive matches came against sides from League C and above.</p>
<p>Where the benches stayed, the players went. <strong>Players outside tonight&rsquo;s squads scored 34 of Germany&rsquo;s 52 goals since September 2024 (Musiala and Havertz both injured on Thursday; Neuer, R&uuml;diger and Gro&szlig; retired), 31 of Austria&rsquo;s 45, 23 of the Netherlands&rsquo; 55, 9 of Serbia&rsquo;s 14 and 13 of Wales&rsquo;s 30.</strong> Denmark&rsquo;s Parken record was kept by Schmeichel and anchored by Vestergaard, both retired; Kosovo&rsquo;s captain Rrahmani has quit; Ireland are without their captain Collins, who made 15 of 16 starts; Norway without S&oslash;rloth. Five sides carry a division change: Norway, Greece and Wales promoted into League A, Kosovo into League B, and Israel relegated from League A, hosting Ireland in Debrecen, where the division&rsquo;s relegated-host line rests on home grounds Israel do not have. Gibraltar&ndash;Andorra carries no promotion stake, because all six League D sides go up whatever their finish.</p>
<div class="note"><strong>Structural consequence.</strong> Halves is the only family OK on all seven, and Team goals is split on all seven: one side readable on every card (Andorra, Serbia, Wales, Kosovo, Greece, Norway, Israel), the other resting on missing scorers, a new coach or a single scorer. The scoring families carry the absences: Totals is Dangerous at Austria&ndash;Kosovo, Norway&ndash;Portugal and Israel&ndash;Ireland, BTTS at Serbia&ndash;Netherlands, Austria&ndash;Kosovo and Israel&ndash;Ireland. The result families hold where the division prior does not depend on who plays: the 1X2 is OK on five and Dangerous at Norway&ndash;Portugal and Israel&ndash;Ireland, where the prior and the host&rsquo;s record point opposite ways; the Asian handicap is OK on six and Dangerous only at Germany&ndash;Greece, where Germany&rsquo;s wide margins came below this level with players who are not here. Corners are Well-suited at Denmark&ndash;Wales and Austria&ndash;Kosovo, the board&rsquo;s only Well-suited verdicts, OK on three and split on the two with a new coach at one end. Discipline is OK at Austria&ndash;Kosovo, Germany&ndash;Greece and Israel&ndash;Ireland and split on the other four, fouls readable and cards not.</div>"""
    CLOSING = """<ul>
<li><strong>Best structurally supported:</strong> Halves, OK on all seven; Corners, Well-suited at Denmark&ndash;Wales and Austria&ndash;Kosovo and OK at Gibraltar&ndash;Andorra, Serbia&ndash;Netherlands and Israel&ndash;Ireland; the Asian handicap, OK on six; Discipline, OK outright at Austria&ndash;Kosovo, Germany&ndash;Greece and Israel&ndash;Ireland, and fouls OK wherever it is split; the readable team-goals side on every card, best at Serbia, Wales, Greece and Norway.</li>
<li><strong>Least supported:</strong> Totals at Austria&ndash;Kosovo, Norway&ndash;Portugal (windows from 2.27 to 5.12 goals per match) and Israel&ndash;Ireland; BTTS at Serbia&ndash;Netherlands, Austria&ndash;Kosovo and Israel&ndash;Ireland; the 1X2 at Norway&ndash;Portugal and Israel&ndash;Ireland; the Asian handicap at Germany&ndash;Greece; the card count at Gibraltar&ndash;Andorra, Serbia&ndash;Netherlands, Denmark&ndash;Wales and Norway&ndash;Portugal.</li>
<li><strong>No normal fixture.</strong> Gibraltar&ndash;Andorra and Denmark&ndash;Wales carry no outright Dangerous verdict, but each has a split with a dangerous half: Gibraltar&rsquo;s team goals and the card count at Europa Point, the card count at Parken.</li>
<li><strong>Thinnest evidence:</strong> Israel&ndash;Ireland, three Dangerous verdicts, a neutral-venue host whose 2024&ndash;25 numbers are from League A, and an Ireland squad that voted to play after a four-hour meeting, with no comparable build-up in the record; Germany&ndash;Greece, where 129 of Germany&rsquo;s 231 starts in the window went to players outside the squad and the one Klopp match reversed the Nagelsmann profile; Gibraltar&ndash;Andorra, where the home coach has no League D match and the referee is from press reports, UEFA&rsquo;s page not read; Norway&ndash;Portugal, whose referee is named on one written source only.</li>
</ul>"""


def unk(v):
    return '<td class="unk">%s</td>' % v


rows = []
for fid, ko, comp, league, h, a, venue, played, flag in FIX:
    venue = venue or card_venue(fid)
    ref = card_ref(fid)
    rows.append("<tr><td>%s</td><td>%s</td><td>%s &ndash; %s</td>%s%s%s%s</tr>" % (
        ko, comp, h, a,
        ("<td>%s</td>" % venue) if venue else unk("not yet researched"),
        ("<td>%s</td>" % ref) if ref else unk("not yet researched"),
        ("<td>%s</td>" % played) if played else unk("not yet researched"),
        ("<td>%s</td>" % flag) if flag else unk("not yet researched")))
SLATE_ROWS = "\n      ".join(rows)

PROVENANCE_NOTE = """<div class="note"><strong>Evidence.</strong> No number on this board was supplied to me and none was estimated. Team rates were computed match by match from ESPN&rsquo;s public match record for the Nations League, World Cup qualifying, the World Cup, play-offs and friendlies with a usable box score &mdash; results for goals, over 2.5, BTTS, clean sheets and failed-to-score; per-match box scores for corners, fouls, cards and shots; key-event periods for first-half goals. Matches that went to extra time are counted at 90 minutes and left out of the box-score rows. <strong>League baselines are in baselines_0927.md</strong> and were recomputed from ESPN&rsquo;s record of the 2024&ndash;25 edition of each division &mdash; League D, League A and League B, the League A line matching its baselines_0926.md entry figure for figure &mdash; with zero baseline searches; the context lines beneath them (stayed-in-A hosts against stayed-in-A and promoted visitors, each side&rsquo;s own divisional record) were computed the same way. <strong>Fields unpublished across the slate:</strong> match-level xG for national teams &mdash; ESPN carries none for internationals, and the xG on the board is FotMob&rsquo;s competition totals, printed as totals and never divided; transfer fees have no national-team equivalent, and squad turnover is read from call-ups, injuries and retirements against each side&rsquo;s competitive starts since September 2024. ESPN&rsquo;s officials field was empty for every match when the cards were written; %s No starting eleven was published when any card was written. <strong>Last season standing in for a thin current sample:</strong> everywhere &mdash; every strip is 2024&ndash;25 and 2025&ndash;26 with match counts in brackets, because the 2026&ndash;27 sample is one match for every side but Gibraltar, who have none.</div>"""

if MODE == "1800":
    REFS = ("three appointments are confirmed on UEFA&rsquo;s match pages (Marciniak, Delajod, Walsh), and Genc Nuza "
            "at Gibraltar&ndash;Andorra is taken from two press reports, UEFA&rsquo;s page not read.")
else:
    REFS = ("five appointments are confirmed on UEFA&rsquo;s match pages (Marciniak, Delajod, Walsh, Kavanagh, Osmers); "
            "Genc Nuza at Gibraltar&ndash;Andorra is taken from two press reports, UEFA&rsquo;s page not read, and "
            "Fran&ccedil;ois Letexier at Norway&ndash;Portugal from Wikipedia&rsquo;s League A page and one search summary, "
            "UEFA&rsquo;s page not showing the officials. Israel host Ireland at a neutral venue in Debrecen, so their "
            "home split is their hosted matches in Hungary.")
PROVENANCE_NOTE = PROVENANCE_NOTE.replace("%s", REFS)

pending = [f for f in FIX if f[0] not in done]
COMPLETION_NOTE = ""
if MODE == "1800" or pending:
    parts = ["%d of %d cards on this board are built, %s at full T1 depth. " % (n_done, N, WORDS[n_t1])]
    if pending:
        parts.append("Still pending: %s &mdash; those cards show the fixture line only. " % ", ".join(
            "f%d %s &ndash; %s" % (f[0], f[4], f[5]) for f in pending))
    if MODE == "1800":
        parts.append("This board carries the four 18:00 CEST games only; f5 Germany &ndash; Greece, f6 Norway &ndash; "
                     "Portugal and f7 Israel &ndash; Ireland (20:45 CEST) are on the full board once built. ")
    parts.append("Nothing was listed without research: with seven fixtures, triage was waived and every fixture "
                 "is T1. The order is kickoff time, not merit.")
    COMPLETION_NOTE = '<div class="note"><strong>Completion.</strong> %s</div>' % "".join(parts)

NAV_LINKS = "\n    ".join(
    '<a href="#f%d">%s &ndash; %s<span>%s &middot; %s</span></a>' % (
        fid, h, a, ko, (venue or card_venue(fid) or "venue not yet researched").split(",")[0])
    for fid, ko, comp, league, h, a, venue, played, flag in FIX)

cards = []
for fid, ko, comp, league, h, a, venue, played, flag in FIX:
    c = card(fid)
    if c:
        cards.append(c.strip())
    else:
        md = league.split("&middot;")[-1].strip()
        v = venue or "not yet researched"
        cards.append("""<article class="fixture pending" id="f%d">
  <div class="fx-head">
    <p class="fx-league">%s</p>
    <h2 class="fx-title">%s &ndash; %s</h2>
    <p class="fx-sub">%s CEST</p>
  </div>
  <div class="fx-body">
    <dl class="fx-odds">
      <div class="od"><dt>Kickoff</dt><dd>%s CEST</dd></div>
      <div class="od"><dt>Venue</dt><dd>%s</dd></div>
      <div class="od"><dt>Matchday</dt><dd>%s</dd></div>
    </dl>
    <div class="pending-note">Context not yet built.</div>
  </div>
</article>""" % (fid, league, h, a, ko, ko, v, md))
FIXTURES = "\n\n".join(cards)

# Sources: the named source of every bullet under each on-board fixture's heading in sources_0927.md
ids = {f[0] for f in FIX}
src = io.open("sources_0927.md", encoding="utf-8").read()
items = []
for sec in re.split(r"^## ", src, flags=re.M)[1:]:
    m = re.match(r"f(\d+)", sec)
    if not m or int(m.group(1)) not in ids:
        continue
    for line in sec.splitlines()[1:]:
        if line.startswith("- "):
            t = re.sub(r"[`*]", "", re.split(r" — | -- ", line[2:])[0]).strip()
            if t and t not in items:
                items.append(t)
SOURCES = " &middot; ".join(_h.escape(t) for t in items)

out = shell
for k, v in (("{{DATE}}", DATE), ("<!--DATE-->", DATE), ("<!--HEADLINE-->", HEADLINE),
             ("<!--STANDFIRST-->", STANDFIRST), ("<!--COMPETITIONS-->", COMPETITIONS),
             ("<!--OVERVIEW-->", OVERVIEW), ("<!--SLATE_ROWS-->", SLATE_ROWS),
             ("<!--PROVENANCE_NOTE-->", PROVENANCE_NOTE)):
    out = out.replace(k, v)
if COMPLETION_NOTE:
    out = out.replace("<!--COMPLETION_NOTE-->", COMPLETION_NOTE)
else:
    out = re.sub(r"\r?\n  <!--COMPLETION_NOTE-->", "", out).replace("<!--COMPLETION_NOTE-->", "")
for k, v in (("<!--NAV_LINKS-->", NAV_LINKS), ("<!--FIXTURES-->", FIXTURES),
             ("<!--CLOSING-->", CLOSING), ("<!--SOURCES-->", SOURCES)):
    out = out.replace(k, v)
io.open(OUT, "w", encoding="utf-8", newline="").write(out)
print("%s: %d of %d cards built" % (OUT, n_done, N))
