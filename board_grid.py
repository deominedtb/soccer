#!/usr/bin/env python3
"""
board_grid.py — Phase 3 add-on: the verdict grid at the top of a board.

    python board_grid.py context-board_0920.html
    python board_grid.py context-board_09*.html

Reads the fixture cards already inside the board (never the fx_ files, never
the web) and writes one grid: every fixture on the board, in the board's own
kickoff order, against the eight families, each cell the section C verdict of
that card. A cell links to its row on the card. Nothing is ranked, no side is
named, no price exists here — the grid only re-displays verdicts the cards
already carry.

Fills <!--GRID--> when the board has the placeholder; on a board built before
the shell had one, inserts the grid under the masthead. Re-running replaces
the grid in place. The CSS rides inside the grid block, so the shell's own
<style> is never edited by this script.
"""

import html
import re
import sys

from verdicts import FAMILIES, LEVEL, parse_card_html

START, END = "<!--GRID:start-->", "<!--GRID:end-->"
ROW_PREFIX = {"1x2": "1X2", "ah": "Asian handicap", "totals": "Totals", "btts": "BTTS",
              "team": "Team goals", "halves": "Halves", "disc": "Discipline", "corners": "Corners"}

CSS = """<style>
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

JS = """<script>
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


def esc(s):
    # Boards carry no charset declaration, so everything non-ASCII goes out as an
    # entity — the same way the cards write &ndash; and &aacute;.
    return html.escape(s or "", quote=True).encode("ascii", "xmlcharrefreplace").decode()


def articles(board):
    """Each <article class="fixture"> in board order, as HTML text."""
    starts = [m.start() for m in re.finditer(r'<article class="fixture', board)]
    out = []
    for i, st in enumerate(starts):
        end = board.find("</article>", st)
        out.append(board[st:end + len("</article>") if end != -1 else (starts[i + 1] if i + 1 < len(starts) else len(board))])
    return out


def kickoff(sub):
    m = re.search(r"\b(\d{1,2}:\d{2})\b", sub.split("·")[0]) or re.search(r"\b(\d{1,2}:\d{2})\b", sub)
    return m.group(1) if m else ""


def pending_text(art):
    m = re.search(r'<div class="pending-note">(.*?)</div>', art, re.S)
    t = re.sub(r"<[^>]+>", "", m.group(1)) if m else "Context not yet built."
    t = html.unescape(re.sub(r"\s+", " ", t)).strip()
    return t.split(" — ")[0].rstrip(".") + "."


def build(board):
    cards = [parse_card_html(a) for a in articles(board)]
    arts = articles(board)
    head = "".join(f"<th scope=\"col\">{esc(short)}</th>" for _, short, _ in FAMILIES)
    rows, counts = [], {k: {"good": 0, "ok": 0, "bad": 0} for k, _, _ in FAMILIES}
    built = 0
    for card, art in zip(cards, arts):
        fid = card["fid"]
        ko = kickoff(card["sub"])
        comp = card["competition"] or card["league"]
        name = (f'<a href="#{fid}">{esc(card["title"])}</a>'
                f'<span class="ko">{esc(ko)}{" &middot; " if ko and comp else ""}{esc(comp)}</span>')
        if card["pending"] or not card["rows"]:
            rows.append(f'<tr><td>{name}</td><td class="none" colspan="{len(FAMILIES)}">'
                        f'{esc(pending_text(art))}</td></tr>')
            continue
        built += 1
        cells = []
        for key, short, full in FAMILIES:
            r = card["rows"].get(key)
            if not r:
                cells.append('<td class="none">&ndash;</td>')
                continue
            counts[key][r["level"]] += 1
            tip = f'{full}: {r["tag"] or LEVEL[r["level"]]}'
            cells.append(f'<td class="v {r["level"]}"><a href="#{fid}" data-row="{esc(ROW_PREFIX[key])}" '
                         f'title="{esc(tip)}" aria-label="{esc(card["title"])}, {esc(tip)}">'
                         f'{esc(r["short"])}</a></td>')
        rows.append(f"<tr><td>{name}</td>{''.join(cells)}</tr>")

    foot = ""
    if built:
        def frow(level, label):
            return (f'<tr><th scope="row">{label}</th>'
                    + "".join(f"<td>{counts[k][level]}</td>" for k, _, _ in FAMILIES) + "</tr>")
        foot = f"<tfoot>{frow('good', 'Well-suited')}{frow('bad', 'Dangerous')}</tfoot>"

    return f"""{START}
{CSS}
<section class="vgrid-sec">
  <h2 class="sec">At a glance &mdash; every verdict on this board</h2>
  <div class="vgrid-wrap">
  <table class="vgrid">
    <thead><tr><th scope="col">Fixture</th>{head}</tr></thead>
    <tbody>
      {chr(10).join('      ' + r for r in rows).lstrip()}
    </tbody>
    {foot}
  </table>
  </div>
  <div class="vgrid-key">
    <span><i class="k-good"></i>Well-suited</span><span><i class="k-ok"></i>OK / Split</span>
    <span><i class="k-bad"></i>Dangerous</span>
    <span>Kickoff order. Click a cell for the reasoning on that card; hover for the full verdict.</span>
  </div>
</section>
{JS}
{END}"""


def inject(path):
    board = open(path, encoding="utf-8").read()
    grid = build(board)
    if START in board and END in board:
        a, b = board.index(START), board.index(END) + len(END)
        board = board[:a] + grid + board[b:]
    elif "<!--GRID-->" in board:
        board = board.replace("<!--GRID-->", grid, 1)
    elif "</header>" in board:
        i = board.index("</header>") + len("</header>")
        board = board[:i] + "\n\n" + grid + "\n" + board[i:]
    else:
        sys.exit(f"{path}: no <!--GRID--> placeholder and no </header> to anchor to")
    open(path, "w", encoding="utf-8").write(board)
    n = len(re.findall(r'<td class="v ', grid))
    print(f"{path}: grid written ({len(articles(board))} fixtures, {n} verdict cells)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        inject(p)
