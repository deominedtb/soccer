# -*- coding: utf-8 -*-
"""Phase 3 assembly for slate 0925. Copies BOARD_SHELL_2.html and fills its
placeholders. The shell's CSS and markup are not touched; the slate table
header cells already carry the seven v4 columns. Cards are concatenated
verbatim from fx_0925_f*.html; fixtures still TODO get a placeholder card."""
import io, os, re

shell = io.open("BOARD_SHELL_2.html", encoding="utf-8").read()
progress = io.open("progress_0925.md", encoding="utf-8").read()
done = {int(m.group(1)) for m in re.finditer(r"^f(\d+) \|.*\| DONE\s*$", progress, re.M)}

FIX = [
 # id, kickoff, competition (slate table), league line, home, away, venue, referee, flag
 (1, "18:00", "Nations League B &middot; B2 MD1", "UEFA &middot; Nations League B, Group B2 &middot; Matchday 1",
  "Georgia", "Northern Ireland", "Boris Paichadze Dinamo Arena, Tbilisi", "Orel Grinfeld", "promoted side"),
 (2, "18:00", "Nations League C &middot; C2 MD1", "UEFA &middot; Nations League C, Group C2 &middot; Matchday 1",
  "Armenia", "Latvia", "Vazgen Sargsyan Republican Stadium, Yerevan", "Martin Mato&scaron;a", "high squad turnover"),
 (3, "20:45", "Nations League A &middot; A1 MD1", "UEFA &middot; Nations League A, Group A1 &middot; Matchday 1",
  "Italy", "Belgium", "Stadio Olimpico, Rome", "Daniel Siebert", "both coaches new"),
 (4, "20:45", "Nations League A &middot; A1 MD1", "UEFA &middot; Nations League A, Group A1 &middot; Matchday 1",
  "T&uuml;rkiye", "France", "Kocaeli Stadium, &#304;zmit", "Felix Zwayer", "promoted side, new coach"),
 (5, "20:45", "Nations League B &middot; B2 MD1", "UEFA &middot; Nations League B, Group B2 &middot; Matchday 1",
  "Hungary", "Ukraine", "Pusk&aacute;s Ar&eacute;na, Budapest", "Jarred Gillett", "relegated side, new coach"),
 (6, "20:45", "Nations League B &middot; B4 MD1", "UEFA &middot; Nations League B, Group B4 &middot; Matchday 1",
  "Poland", "Bosnia and Herzegovina", "PGE Narodowy, Warsaw", "Anastasios Papapetrou", "two relegated sides"),
 (7, "20:45", "Nations League B &middot; B4 MD1", "UEFA &middot; Nations League B, Group B4 &middot; Matchday 1",
  "Sweden", "Romania", "Strawberry Arena, Solna", "Ond&#345;ej Berka", "two promoted sides"),
 (8, "20:45", "Nations League C &middot; C2 MD1", "UEFA &middot; Nations League C, Group C2 &middot; Matchday 1",
  "Montenegro", "Cyprus", "Podgorica City Stadium, Podgorica", "Daniele Chiffi", "relegated side"),
]
N = len(FIX)
n_done = sum(1 for f in FIX if f[0] in done)

DATE = "Friday 25 September 2026"
HEADLINE = ("No side on tonight&rsquo;s card has played a competitive match this season, "
            "and Italy, Belgium, France, Ukraine and Romania all open under a coach appointed since their last one")
STANDFIRST = ("Eight Nations League fixtures parsed from the typed sheet slate.9.xlsx &mdash; "
              "%d of %d cards built at full T1 depth." % (n_done, N))
COMPETITIONS = ("Nations League A matchday 1 &middot; Nations League B matchday 1 &middot; "
                "Nations League C matchday 1")

OVERVIEW = """<p>The single structural fact across this card is that <strong>every number on it is last season&rsquo;s</strong>. This is matchday 1 of the 2026&ndash;27 Nations League and the first competitive fixture of the season for all sixteen sides on the card; ESPN&rsquo;s standings show 0 played everywhere. The gap to each side&rsquo;s last competitive match runs from 69 days (France, beaten in the World Cup third-place match) to 313 days (Armenia and Hungary, both last out in a November 2025 qualifier).</p>
<p>The second is who those numbers belong to. <strong>Italy open under Roberto Mancini (appointed 28 July, a second spell), Belgium under Mark van Bommel (from late July), France under Zinedine Zidane (28 July), Ukraine under Andrea Maldera (18 May) and Romania under Gheorghe Hagi (April, after Mircea Lucescu&rsquo;s death)</strong> &mdash; five sides across three fixtures playing their first competitive match under the man now in charge. Four sides carry a division change into tonight: Northern Ireland and T&uuml;rkiye promoted, into League B and League A respectively; Sweden and Romania promoted from League C; Poland, Bosnia-Herzegovina, Hungary and Montenegro relegated. <strong>Poland and Bosnia-Herzegovina meet as two sides relegated from League A into the same League B group, and Sweden and Romania meet as two sides promoted from League C into the same group</strong> &mdash; neither pairing occurred in either of the two prior League B editions. The absences land on the positions the spec weights: Belgium without Courtois, Doku and Trossard; France without Saliba, Konat&eacute;, Tchouam&eacute;ni and Za&iuml;re-Emery; T&uuml;rkiye without &Ccedil;alhano&#287;lu and Y&#305;ld&#305;z; Hungary without Varga and Sallai; Bosnia-Herzegovina without D&#382;eko (rested), Vasilj and Dedi&#263;; Sweden without Hien, Lagerbielke, Elanga and every goalkeeper who started for them in 2026.</p>
<div class="note"><strong>Structural consequence.</strong> Result families are the least readable on the card: the Asian handicap is Dangerous on seven of eight built cards, OK only at Montenegro&ndash;Cyprus, where two venue splits and the 2020&ndash;21 head-to-head agree; the 1X2 is Dangerous on five of eight (Italy&ndash;Belgium, T&uuml;rkiye&ndash;France, Hungary&ndash;Ukraine, Poland&ndash;Bosnia and Herzegovina, Sweden&ndash;Romania), OK at Georgia&ndash;Northern Ireland, Armenia&ndash;Latvia and Montenegro&ndash;Cyprus. Halves are Dangerous on seven of eight, split rather than dangerous only at Montenegro&ndash;Cyprus. Totals hold up everywhere &mdash; OK on all eight &mdash; and team goals are OK or split on all eight, because both rest on scoring rates that stayed close to the division line even where personnel changed. BTTS is Dangerous only at T&uuml;rkiye&ndash;France, where T&uuml;rkiye&rsquo;s scoring record against League A-tier opposition is thin and now without &Ccedil;alhano&#287;lu and Y&#305;ld&#305;z. Discipline is Dangerous only at Armenia&ndash;Latvia, where the referee has no senior international match in any record read. Corners carry the board&rsquo;s three Well-suited verdicts &mdash; Armenia&ndash;Latvia, Italy&ndash;Belgium and Montenegro&ndash;Cyprus &mdash; and are Dangerous only at Sweden&ndash;Romania, where Sweden&rsquo;s corner edge was built under a previous coach. Montenegro&ndash;Cyprus is the one card on the slate with no Dangerous verdict at all.</div>"""


def unk(v):
    return '<td class="unk">%s</td>' % v


def card_ref(fid):
    try:
        c = io.open("fx_0925_f%d.html" % fid, encoding="utf-8").read()
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

PROVENANCE_NOTE = """<div class="note"><strong>Evidence.</strong> No number on this board was supplied to me and none was estimated. Team rates were computed match by match from ESPN&rsquo;s public match record for the Nations League, World Cup qualifying, the World Cup, play-offs and friendlies with a usable box score &mdash; results for goals, over 2.5, BTTS, clean sheets and failed-to-score; per-match box scores for corners, fouls, cards and shots; key-event periods for first-half goals. <strong>League baselines are in baselines_0925.md</strong> and were rebuilt the same way from the 2024&ndash;25 edition of each division &mdash; League A and League B recomputed to match their baselines_0924.md entries, League C new to the archive &mdash; because 2026&ndash;27 has no completed match in any of today&rsquo;s groups. <strong>Fields unpublished across the slate:</strong> match-level xG for national teams &mdash; ESPN carries none for the Nations League, qualifying or the World Cup, and Understat does not cover internationals; the xG that does appear on the board is a handful of season-total qualifying figures (Georgia, Northern Ireland, T&uuml;rkiye, France, Montenegro, Cyprus) printed as totals because no source states a match count, and every other xG cell reads not published. Transfer fees have no national-team equivalent; squad turnover is read from call-ups, injuries and retirements against each side&rsquo;s starting elevens since September 2024. Two referees carry thin records: Martin Mato&scaron;a (f2) has no senior international match in any source read, and Ond&#345;ej Berka (f7) is named on Wikipedia only, with UEFA&rsquo;s own page and ESPN listing no official yet, so his card marks the appointment provisional. <strong>Last season standing in for a thin current sample:</strong> everywhere &mdash; every strip is 24/25 and 25/26 with match counts in brackets, because the 26/27 sample is zero for all sixteen sides.</div>"""

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
    path = "fx_0925_f%d.html" % fid
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
<li><strong>Best structurally supported:</strong> Corners, Well-suited at Armenia&ndash;Latvia, Italy&ndash;Belgium and Montenegro&ndash;Cyprus and OK on four of the remaining five; Totals, OK on all eight fixtures; BTTS, OK on seven of eight; Team goals, OK or split (asymmetric between the two sides) on all eight.</li>
<li><strong>Least supported:</strong> the Asian handicap, Dangerous on seven of eight, OK only at Montenegro&ndash;Cyprus; Halves, Dangerous on seven of eight, split only at Montenegro&ndash;Cyprus; the 1X2, Dangerous at Italy&ndash;Belgium, T&uuml;rkiye&ndash;France, Hungary&ndash;Ukraine, Poland&ndash;Bosnia and Herzegovina and Sweden&ndash;Romania; Discipline at Armenia&ndash;Latvia, the only card where the official has no senior international record at all; Corners at Sweden&ndash;Romania, where Sweden&rsquo;s edge belongs to a previous coach.</li>
<li><strong>The one normal fixture.</strong> Montenegro&ndash;Cyprus is the only card on the slate with no Dangerous verdict in any row.</li>
<li><strong>Thinnest evidence:</strong> Armenia&ndash;Latvia, where players outside tonight&rsquo;s squad made half of Armenia&rsquo;s competitive starts in the window and the referee has no senior international match in any source read; Italy&ndash;Belgium and T&uuml;rkiye&ndash;France, where a new-coach side fields a back line with almost no competitive starts together; Sweden&ndash;Romania, where Romania&rsquo;s coach has no competitive match on record at all.</li>
</ul>"""

# Sources: the named source of every bullet under each fixture heading in sources_0925.md
src = io.open("sources_0925.md", encoding="utf-8").read()
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
io.open("context-board_0925.html", "w", encoding="utf-8").write(out)
print("context-board_0925.html: %d of %d cards built" % (n_done, N))
