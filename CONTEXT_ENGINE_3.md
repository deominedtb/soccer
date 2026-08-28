CONTEXT ENGINE — soccer market-family board. No picks.

Output is a Market Board HTML page in the house style. Depth is the
point: keep the research and the prose. The cost control is in the
phasing below, never in shortening the analysis.

STANDING RULES
- No preamble, no recap of these instructions, no restating my request.
- Never re-open the Drive images after Phase 1. Work only from
  fixtures_N.md.
- Never rewrite BOARD_SHELL.html. It is the permanent template.
- Never regenerate a fixture that is already DONE in progress_N.md.
- Research every team. Max 2 searches per team plus 1 shared preview
  search per fixture. Use one combined query per team covering
  transfers, manager and system change together — not one query each.
  Stop once you have that, and note any gap rather than chasing it.
- Do not narrate your reasoning or your research process. Produce the
  artifact.
- Phase 1 and Phase 3 are mechanical — OCR and assembly. Run them on
  a cheaper model. Reserve the strongest model for Phase 2 research.
- Between Phase 2 runs I send no other messages. Reply to each run
  with a single confirmation line, nothing more.

HARD BANS (apply to every phase)
- No bets, sides, lines, stakes or prices recommended.
- No LEAN / CONFIDENCE / BANKER / VALUE labels.
- No expected-goals projections or implied probabilities.
- No ranking fixtures against each other by attractiveness.

────────────────────────────────────────────────
RESEARCH SPEC (applies in Phase 2 only)

I never paste stats. You source everything yourself.

Per team, establish:
- Promoted to this division this season? If so, how that division
  usually treats promoted sides early on.
- Summer ins and outs with fees, weighted to centre-forward, CB, GK,
  DM. Named, not counted.
- Manager or system change, with the date it happened.
- Last season: final position, goals scored, goals conceded, xG,
  shot volume, home/away split, foul and card rate.
- This season so far: results, goals, xG, BTTS, cards. If zero
  competitive matches, say so and say why — postponement, calendar,
  matchday one.

Per fixture, establish: venue, kickoff, referee if named, and any
suspension or major injury carried into the game.

Sources, in preference order: official league site, FBref, Sofascore,
Transfermarkt, Wikipedia season pages, then local press for mercato
and match reports. Log every source used to sources_N.md as you go.

Missing or contradictory evidence is reported, never filled in.
Flag the fixture high-uncertainty in fx-sub when the gaps are wide
enough to undermine section C.

────────────────────────────────────────────────
PHASE 1 — GET THE ODDS  (one run, then STOP)

Two modes. If I point you at a typed odds file, use 1B. Only use 1A
if I give you a screenshot folder.

--- 1B · TYPED FILE (preferred, cheap) ---
Read the file I name — .csv, .xlsx or .md. The header row defines the
columns; do not assume positions, read the header. Expected fields:
league, kickoff, venue, home, away, 1, X, 2, O2.5, U2.5, BTTSY,
BTTSN, cards, corners, corner race, team corners.

Parse into /fixtures_N.md, sorted by kickoff. Do not open any images.
Do not re-verify prices against the web — I typed them, they are the
record. A cell of "-" means I did not check that market: leave it
empty and omit that market's row in section C. A price prefixed "~"
is uncertain: carry the flag through to the board.

Print the parsed table and flag anything malformed — missing header,
wrong field count, a price that is not a number. Then write
progress_N.md and STOP.

--- 1A · SCREENSHOTS (fallback) ---

Read the Drive folder I name. If I give only a number N, the folder is
"Today Games N". If I name no folder, list Drive folders matching
"Today Games *", take the highest-numbered, and say which you took.

Do not narrate. No "found the folder", no "now let's list the
images", no step commentary of any kind. Work silently and print only
the final table.

OCR in batches of 4 images. After each batch, append the rows you have
to /fixtures_N.md immediately, then start the next batch. Never hold
more than one batch of extracted text before writing. If this message
is cut short, the rows already appended survive and I resume with
"continue Phase 1" — you then read fixtures_N.md, skip the images
already covered, and carry on from the first unprocessed one.

Write /fixtures_N.md — one row per fixture:
league | kickoff | venue | home | away | 1 | X | 2 | O2.5 | U2.5 |
BTTS Y | BTTS N | cards line | corners line | corner race |
team corners | source image | uncertain?

Record the source image filename for every fixture. Any value you
could not read cleanly: mark uncertain, and if you derive it (e.g. a
cropped draw price from the two-way prices) say derived, not read.
Never silently guess a price.

Write /progress_N.md — every fixture as:
  f1 | kickoff | Home – Away | TODO

Order progress_N.md by kickoff time, earliest first. Phase 2 always
takes the earliest unfinished fixture, so a session that runs out
loses the latest games, never the imminent ones.

Print the table. STOP.

────────────────────────────────────────────────
PHASE 2 — ONE FIXTURE PER RUN  (repeat until none left)

Take the first TODO fixture in progress_N.md. Research it. Write the
complete fixture card as a standalone HTML fragment to
/fx_N_f<id>.html — no <html>, <head> or CSS, fragment only, using
exactly the classes in BOARD_SHELL.html.

Fragment structure:

<article class="fixture" id="f1">
  <div class="fx-head">
    <p class="fx-league">Country &middot; League &middot; Matchday</p>
    <h2 class="fx-title">Home &ndash; Away</h2>
    <p class="fx-sub">kickoff &middot; venue &middot; one-line situation</p>
  </div>
  <div class="fx-body">
    <dl class="fx-odds">
      <div class="od"><dt>1 / X / 2</dt><dd>…</dd></div>
      … one .od per market present in fixtures_N.md …
    </dl>

    <h3 class="blk">A &middot; Squad, promotion &amp; transfer context</h3>
    <p>opening paragraph: promotion status, last-season finish with
       goals scored/conceded, the structural headline</p>
    <ul>
      <li><strong>Team — turnover low/medium/high, and where.</strong>
          Named ins and outs with fees, weighted to attacker, CB, GK,
          DM. Manager change with date.</li>
      <li>… same for the other team …</li>
      <li><strong>Suspensions / absences.</strong> …</li>
      <li><strong>Sample.</strong> What each side has actually played
          this season, and why if zero.</li>
    </ul>

    <h3 class="blk">B &middot; Style &amp; early-season reality</h3>
    Two paragraphs. Each side's shape — press vs deep block,
    possession vs counter, crossing and set-piece volume, foul rate.
    Then how the summer may have changed it, and say plainly when the
    evidence for that is a CV rather than a match.

    <h3 class="blk">C &middot; Market-type suitability</h3>
    <div class="mkt">
      <div class="mkt-row bad"><div class="mkt-name">1X2 / Moneyline<span class="verdict tag t-high">Dangerous</span></div><div class="mkt-why">2–3 sentences</div></div>
      … Asian handicap / DNB, Totals (O/U goals), BTTS, Team goals,
        Discipline (cards, fouls), Corners …
    </div>
    Row class + tag pairs: good/t-low = Well-suited,
    ok/t-mid = OK, bad/t-high = Dangerous. Compound verdicts are
    allowed and encouraged where true — "OK — best on the card",
    "Split — Valencia dangerous", "OK — asymmetric".
    Reasons must be structural: promotion, turnover, named transfers,
    style, venue, referee culture, sample size. Never form narrative.
    Include only the market rows that exist in fixtures_N.md, plus
    corners when a corner line was captured.

    <h3 class="blk">D &middot; Early-season risk notes</h3>
    <ul> 3–4 bullets: what makes last season's numbers misleading
    here, then a final bullet <strong>Most sensitive:</strong> … /
    <strong>Least sensitive:</strong> … </ul>

    <h3 class="blk">E &middot; Short market-type guide</h3>
    <ul> 3–5 bullets of the form "X is more robust than Y here
    because …", each tied to a specific named fact above. Where the
    book has priced a market at even money, say what that signals
    about its own confidence. </ul>
  </div>
</article>

Then mark that fixture DONE in progress_N.md immediately, append its
sources to /sources_N.md, and STOP. Print nothing but a one-line
confirmation of which fixture was written.

────────────────────────────────────────────────
PHASE 3 — ASSEMBLE  (run whenever I ask, finished or not)

Assemble every fixture marked DONE. For any still TODO, emit a
placeholder card — fx-head and the odds strip from fixtures_N.md,
then one line: "Context not yet built." State in the standfirst how
many of how many are complete. The board must always open.

Copy BOARD_SHELL.html and fill its placeholders. Do not touch the CSS.

- {{DATE}} and <!--DATE--> — the slate date
- <!--HEADLINE--> — a real headline about this card, not a label
- <!--STANDFIRST--> — one sentence: how many fixtures, which folder
  they came from, what was rebuilt
- <!--COMPETITIONS--> — e.g. "LaLiga jornada 2 · Ligue 1 matchday 1"
- <!--OVERVIEW--> — two or three <p> on the single structural fact
  shaping the whole card, closing with
  <div class="note"><strong>Structural consequence.</strong> …</div>
- <!--SLATE_ROWS--> — one <tr> per fixture straight from
  fixtures_N.md. Derived or unreadable values get class="unk" and a
  leading ~
- <!--PROVENANCE_NOTE--> — a <div class="note"> naming the exact
  image files with unreadable values and what was derived from what
- <!--COMPLETION_NOTE--> — omit entirely if every fixture is DONE.
  Otherwise a <div class="note"> saying how many of how many cards
  are built and which fixtures are still pending.
  Placeholder cards use <article class="fixture pending" id="fN">
  with the fx-head and fx-odds only, then
  <div class="pending-note">Context not yet built.</div>
- <!--NAV_LINKS--> — <a href="#f1">Home &ndash; Away<span>kickoff
  &middot; venue</span></a> per fixture
- <!--FIXTURES--> — concatenate fx_N_f1.html … fx_N_fX.html in order,
  verbatim. Do not regenerate or edit them.
- <!--CLOSING--> — a <ul> across the card: best structurally
  supported families today, least supported, the one normal fixture
  if there is one, and where the book has priced indifference
- <!--SOURCES--> — from sources_N.md

Write /market-board_N.html and present it.
