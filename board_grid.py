# -*- coding: utf-8 -*-
"""Verdict grid for a context board (CONTEXT_ENGINE_4 Phase 3).

    python board_grid.py context-board_N.html

Reads the fixture cards already on the board and writes the verdict grid
between <!--GRID:start--> and <!--GRID:end--> (or in place of a bare
<!--GRID--> placeholder): every fixture a row in board order, the eight
families as columns, each cell that card's section C verdict linking to
its card. Placeholder and T3 cards keep their row with the pending note.
Re-displays verdicts and nothing else; rerun on every refresh, replacing
its own previous grid. Output format matches the grid on
context-board_0925.html.
"""
import html, io, re, sys

FAMILIES = [
    # column header, data-row key (the .mkt-name prefix the jump script matches)
    ("1X2", "1X2"),
    ("AH / DNB", "Asian handicap"),
    ("Totals", "Totals"),
    ("BTTS", "BTTS"),
    ("Team goals", "Team goals"),
    ("Halves", "Halves"),
    ("Discipline", "Discipline"),
    ("Corners", "Corners"),
]

STYLE = """<style>
/* verdict grid - board_grid.py */
.vgrid-wrap{border:1px solid var(--line); background:var(--surface); overflow-x:auto}
table.vgrid{min-width:820px; font-size:13px; table-layout:fixed}
table.vgrid thead th{text-align:center; padding:9px 6px; font-size:10.5px; letter-spacing:.07em}
table.vgrid thead th:first-child{text-align:left; width:210px; position:sticky; left:0; z-index:1}
table.vgrid tbody td{padding:0; text-align:center; font-family:Archivo,sans-serif; white-space:nowrap}
table.vgrid tbody td:first-child{
  padding:8px 11px; text-align:left; position:sticky; left:0; z-index:1;
  background:var(--surface); border-right:1px solid var(--line);
  white-space:normal; overflow-wrap:anywhere; line-height:1.3;
}
table.vgrid tbody tr:nth-child(even) td:first-child{background:var(--surface-2)}
table.vgrid td:first-child a{color:var(--ink); text-decoration:none; font-weight:600; font-size:13.5px}
table.vgrid td:first-child a:hover{color:var(--accent)}
table.vgrid td:first-child .ko{font-size:11px}
table.vgrid td.v a{
  display:block; padding:9px 4px; text-decoration:none; font-weight:700;
  font-size:11px; letter-spacing:.05em; text-transform:uppercase;
  border-left:1px solid var(--surface);
}
table.vgrid td.good a{background:var(--good-soft); color:var(--good)}
table.vgrid td.ok a{background:var(--warn-soft); color:var(--warn)}
table.vgrid td.bad a{background:var(--bad-soft); color:var(--bad)}
table.vgrid td.v a:hover,table.vgrid td.v a:focus-visible{outline:2px solid currentColor; outline-offset:-2px}
table.vgrid td.none{
  padding:9px 12px; text-align:left; font-size:12px; font-weight:600;
  color:var(--muted); font-style:italic; letter-spacing:.02em;
}
table.vgrid tfoot th, table.vgrid tfoot td{
  padding:8px 6px; border-top:2px solid var(--ink); font-family:"IBM Plex Mono",monospace;
  font-size:12px; text-align:center; color:var(--ink-2); background:var(--surface-2);
}
table.vgrid tfoot th{
  text-align:left; font-family:Archivo,sans-serif; font-weight:700; font-size:10.5px;
  letter-spacing:.09em; text-transform:uppercase; position:sticky; left:0; padding-left:11px;
}
.vgrid-key{display:flex; flex-wrap:wrap; gap:6px 16px; margin:10px 0 0; font-size:13px; color:var(--muted)}
.vgrid-key span{display:inline-flex; align-items:center; gap:6px}
.vgrid-key i{display:inline-block; width:12px; height:12px}
.vgrid-key .k-good{background:var(--good-soft); border:1px solid var(--good)}
.vgrid-key .k-ok{background:var(--warn-soft); border:1px solid var(--warn)}
.vgrid-key .k-bad{background:var(--bad-soft); border:1px solid var(--bad)}
.mkt-row.vflash{animation:vflash 1.6s ease-out 1}
@keyframes vflash{0%,35%{background:var(--accent-soft); box-shadow:inset 3px 0 0 var(--accent)}100%{background:transparent}}
@media (prefers-reduced-motion:reduce){.mkt-row.vflash{animation:none; background:var(--accent-soft)}}
</style>"""

SCRIPT = """<script>
/* verdict grid - jump to the family's row on the card */
document.addEventListener("click", function (e) {
  var a = e.target.closest && e.target.closest("a[data-row]");
  if (!a) return;
  var card = document.getElementById(a.getAttribute("href").slice(1));
  if (!card) return;
  var want = a.getAttribute("data-row").toLowerCase(), hit = null;
  card.querySelectorAll(".mkt-row").forEach(function (r) {
    var n = r.querySelector(".mkt-name");
    if (!hit && n && n.textContent.trim().toLowerCase().indexOf(want) === 0) hit = r;
  });
  if (!hit) return;
  e.preventDefault();
  history.replaceState(null, "", "#" + card.id);
  hit.scrollIntoView({block: "center"});
  hit.classList.remove("vflash"); void hit.offsetWidth; hit.classList.add("vflash");
});
</script>"""


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def enc(s):
    return html.escape(s, quote=True).encode("ascii", "xmlcharrefreplace").decode("ascii")


def cards(board):
    for m in re.finditer(r'<article class="fixture( pending)?" id="(f\d+)">(.*?)</article>', board, re.S):
        yield m.group(2), bool(m.group(1)), m.group(3)


def row(fid, pending, body):
    title = text(re.search(r'<h2 class="fx-title">(.*?)</h2>', body, re.S).group(1))
    league = text(re.search(r'<p class="fx-league">(.*?)</p>', body, re.S).group(1))
    parts = [p.strip() for p in league.split("·")]
    comp = parts[1] if len(parts) > 2 else league
    sub = text(re.search(r'<p class="fx-sub">(.*?)</p>', body, re.S).group(1))
    ko = re.match(r"\s*(\d{1,2}:\d{2})", sub)
    ko = ko.group(1) if ko else ""
    head = '<td><a href="#%s">%s</a><span class="ko">%s &middot; %s</span></td>' % (
        fid, enc(title), ko, enc(comp))
    if pending:
        note = re.search(r'<div class="pending-note">(.*?)</div>', body, re.S)
        return '<tr>%s<td class="none" colspan="%d">%s</td></tr>' % (
            head, len(FAMILIES), enc(text(note.group(1)) if note else "Context not yet built.")), {}
    verdicts = {}
    for m in re.finditer(r'<div class="mkt-row (good|ok|bad)"><div class="mkt-name">(.*?)<span class="verdict[^"]*">(.*?)</span></div>', body, re.S):
        fam, verdict = text(m.group(2)), text(m.group(3))
        for _, key in FAMILIES:
            if fam.lower().startswith(key.lower()) and key not in verdicts:
                verdicts[key] = (m.group(1), fam, verdict)
    cells = []
    for _, key in FAMILIES:
        if key not in verdicts:
            cells.append('<td class="none">&mdash;</td>')
            continue
        cls, fam, verdict = verdicts[key]
        label = re.split(r"\s+—\s+", verdict)[0]
        full = "%s: %s" % (fam, verdict)
        cells.append('<td class="v %s"><a href="#%s" data-row="%s" title="%s" aria-label="%s, %s">%s</a></td>' % (
            cls, fid, key, enc(full), enc(title), enc(full), enc(label)))
    return "<tr>%s%s</tr>" % (head, "".join(cells)), verdicts


def grid(board):
    rows, good, bad = [], [0] * len(FAMILIES), [0] * len(FAMILIES)
    for fid, pending, body in cards(board):
        tr, verdicts = row(fid, pending, body)
        rows.append("      " + tr)
        for i, (_, key) in enumerate(FAMILIES):
            if key in verdicts:
                good[i] += verdicts[key][0] == "good"
                bad[i] += verdicts[key][0] == "bad"
    th = "".join('<th scope="col">%s</th>' % h for h, _ in FAMILIES)
    foot = ('<tr><th scope="row">Well-suited</th>%s</tr><tr><th scope="row">Dangerous</th>%s</tr>' % (
        "".join("<td>%d</td>" % n for n in good), "".join("<td>%d</td>" % n for n in bad)))
    return "\n".join([
        "<!--GRID:start-->",
        STYLE,
        '<section class="vgrid-sec">',
        '  <h2 class="sec">At a glance &mdash; every verdict on this board</h2>',
        '  <div class="vgrid-wrap">',
        '  <table class="vgrid">',
        '    <thead><tr><th scope="col">Fixture</th>%s</tr></thead>' % th,
        "    <tbody>",
        "\n".join(rows),
        "    </tbody>",
        "    <tfoot>%s</tfoot>" % foot,
        "  </table>",
        "  </div>",
        '  <div class="vgrid-key">',
        '    <span><i class="k-good"></i>Well-suited</span><span><i class="k-ok"></i>OK / Split</span>',
        '    <span><i class="k-bad"></i>Dangerous</span>',
        "    <span>Kickoff order. Click a cell for the reasoning on that card; hover for the full verdict.</span>",
        "  </div>",
        "</section>",
        SCRIPT,
        "<!--GRID:end-->",
    ])


def main(path):
    board = io.open(path, encoding="utf-8", newline="").read()
    g = grid(board)
    if "<!--GRID:start-->" in board:
        board = re.sub(r"<!--GRID:start-->.*?<!--GRID:end-->", lambda m: g, board, count=1, flags=re.S)
    elif "<!--GRID-->" in board:
        board = board.replace("<!--GRID-->", g, 1)
    else:
        sys.exit("no <!--GRID--> placeholder or previous grid in %s" % path)
    io.open(path, "w", encoding="utf-8", newline="").write(board)
    print("%s: verdict grid written, %d fixtures" % (path, g.count("<tr><td><a href=")))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else sys.exit("usage: python board_grid.py context-board_N.html"))
