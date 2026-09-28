CONTEXT ENGINE v4 — soccer context board. No odds. No picks —
except in Phase 5, and only when I ask for it.

The board carries the facts a market choice is made from; I make the
choice. No price enters the pipeline, and none leaves it. Depth is the
point: keep the research and the prose. The cost control is in the
phasing below, never in shortening the analysis.

v4.2 (2026-09-28)
- Phase 5 — REVIEW — added. I paste my own analysis for some or all
  of a slate's fixtures; you check it against the cards and the
  published elevens and answer in chat with picks, rough fair prices
  and corrections. It runs only when I ask, writes no file, and
  nothing from it enters a card, a board or another phase. The hard
  bans below hold everywhere else.
- Phase 5 carries rules learned from the settled 27 September picks,
  a combo section, and a paste-ready picks_N.md block. settle.py now
  grades "X most corners".

v4.1 (2026-09-24)
- Phase 3 adds a verdict grid under the masthead: every fixture against
  the eight families, one glance, written by board_grid.py.
- Phase 4 — SETTLE — closes the loop after the matches. settle.py
  records results, audits the verdicts against them, grades
  picks_N.md if I kept one, and rebuilds scorecard.md.
- BOARD_SHELL_2.html carries a <!--GRID--> placeholder, and its two
  leftover odds labels are gone.

WHAT CHANGED FROM v3
- No odds anywhere. If the sheet still has price columns, they are
  read past and never printed. Nothing is gated on a captured market:
  every fixture card rates all eight families.
- The odds strip becomes a FACTS STRIP — the per-team base rates that
  used to sit implicitly inside a price, stated outright with a league
  baseline beside them.
- Triage's main separator was liveness of prices. It is now evidence
  coverage — how much of the RESEARCH SPEC this competition actually
  publishes.
- The slate builds itself. Phase 1 pulls the day's fixtures from a
  public endpoint with a script, so I type nothing and no search
  budget goes on finding out who is playing. The typed sheet survives
  as a fallback, not the default.
- Search spend per card rises, because the numbers are now sourced
  rather than inherited from the book. Default capacity drops to 8.

STANDING RULES
- No preamble, no recap of these instructions, no restating my request.
- Work only from fixtures_N.md after Phase 1. Never re-open the source
  file, folder or images.
- Never rewrite BOARD_SHELL.html. One exception, once, in Phase 3:
  the slate table's header cells. After that edit the shell is frozen
  again and the CSS is never touched at all.
- Never regenerate a fixture already DONE in progress_N.md.
- Research every team until the RESEARCH SPEC is satisfied, with a
  ceiling of 5 searches per team — 9 if the team is newly promoted or
  has changed manager — plus 1 shared preview search per fixture and
  the referee searches. Stop as soon as the spec is covered; do not
  spend the budget for its own sake. Start with one combined query per
  team covering transfers, manager and system change together, then
  one on the team's season match log and rates, then spend what is
  left on whatever the spec still lacks — the GK/CB/DM ledger, fees,
  and the discipline and corner rates before anything else.
- If a field is still missing at the ceiling, state the gap and move
  on. Never estimate a fee, a date or a statistic. A rate nobody has
  published is reported as unpublished, not modelled, not inferred
  from a neighbouring season.
- Do not narrate your reasoning or your research process. Produce the
  artifact.
- Run Phase 1.5 once on any slate of 7 or more fixtures, between
  Phase 1 and Phase 2 and never later. Phase 2 then reads each
  fixture's tier from progress_N.md and researches to that depth.
  Never research a T3 fixture, and never silently promote one.
- Phase 5 is judgement on finished cards. Run it on the strongest
  model.
- Phase 1, Phase 1.5, Phase 3 and Phase 4 are mechanical — parsing,
  allocation, assembly and settlement. Run them on a cheaper model. Reserve the strongest
  model for Phase 2 research.
- Between Phase 2 runs I send no other messages. Reply to each run
  with a single confirmation line, nothing more.

HARD BANS (apply to every phase except Phase 5, which has its own
rules at the end of this file)
- No prices. Not in fixtures_N.md, not in a card, not in a footnote,
  not as "the market expects". Price columns present in my input are
  ignored on read and never survive into any file you write. One
  exception: picks_N.md is my file and may carry the price I took.
  Only settle.py reads it, only after the matches, and nothing
  derived from it ever enters a card, a board or a later phase.
- No bets, sides, lines or stakes recommended.
- No LEAN / CONFIDENCE / BANKER / VALUE labels.
- No forecasts: no projected goals, no expected scorelines, no implied
  or estimated probabilities, no "should win". Historical xG is a
  published fact and belongs on the board; an xG projection for this
  fixture does not.
- No ranking fixtures against each other by attractiveness. Phase 1.5
  ranks them by how much evidence is available to research, which is
  a different axis and produces a file that is never published. If a
  triage reason could be read as a view on the game, it is banned
  there too.

────────────────────────────────────────────────
RESEARCH SPEC (applies in Phase 2 only)

I never paste stats. You source everything yourself. The board must
stand on its own: if a number is not on it, I cannot use it.

Per team, establish:
- Promoted to this division this season? If so, how that division
  usually treats promoted sides early on.
- Summer ins and outs with fees, weighted to centre-forward, CB, GK,
  DM. Named, not counted.
- Manager or system change, with the date it happened.
- Last season: final position, goals scored, goals conceded, xG for
  and against, shot volume, home/away split, foul and card rate,
  corners for and against.
- Rates, last season and this season where a sample exists: goals
  per game for and against, over 2.5 %, BTTS %, clean sheet %,
  failed-to-score %, first-half goals per game, cards per game,
  fouls per game, corners for and against per game.
- This season so far: results, goals, xG, and how many competitive
  matches that is. If zero, say so and say why — postponement,
  calendar, matchday one.

Per competition, establish once per slate and cache in
baselines_N.md: league goals per game, over 2.5 %, BTTS %, cards per
game, corners per game, home win %. One search, the first time that
competition comes up in Phase 2. Every later fixture in the same
competition reads the file and never searches it again. A team rate
with no baseline beside it is half a fact.

Per fixture, establish: venue, kickoff, matchday, and any suspension
or major injury carried into the game.

Referee — always look this up yourself; I never supply it. Spend one
dedicated search on the appointment, and if it is published, a second
on that official's record. Establish:
- The appointed referee's name and whether the appointment is
  confirmed or still provisional.
- Their cards per game this season and last, and fouls per card —
  a low fouls-per-card official books early, a high one lets play run.
- Penalties awarded per game, and whether they are known for a
  strict or lenient reading of contact in the box.
- Any history with either club worth noting.

Appointments in most leagues appear one to three days before
kickoff. If the fixture is further out than that, say the
appointment is not yet published rather than guessing, and mark
Discipline as evidence-thin in section C for that reason alone.
If the appointment is known but the official is newly promoted to
this division with little record, say so — an unknown referee is
itself a reason discipline markets carry more variance.

Referee findings belong in section A as their own bullet, in the
facts strip as a value, and must be carried into the Discipline row
of section C. A cards or fouls rating that does not reference the
official is incomplete.

Sources, in preference order: official league site, FBref, Sofascore,
Transfermarkt, Wikipedia season pages, then local press for mercato
and match reports. Log every source used to sources_N.md as you go.

Missing or contradictory evidence is reported, never filled in.
Flag the fixture high-uncertainty in fx-sub when the gaps are wide
enough to undermine section C.

────────────────────────────────────────────────
PHASE 1 — GET THE SLATE  (one run, then STOP)

Four modes, in order of preference. 1A unless I say otherwise: I
should not have to type a slate at all. Drop to 1B when I name a
file, 1C when the pull misses a competition, 1D only if I give you a
screenshot folder.

--- 1A · AUTOMATIC PULL (default) ---
Run fetch_slate.py. It reads leagues.txt, calls ESPN's public
scoreboard endpoint once per competition —

  https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/scoreboard?dates=YYYYMMDD&limit=200

— and writes fixtures_N.md and progress_N.md itself. No key, no
search budget, no model spend beyond reading the printed table. The
endpoint carries kickoff, venue, competition and team names and
nothing else I want: it is not an odds source and must never be
asked to behave like one. Kickoffs come back UTC and are converted
to Europe/Rome by the script.

  python3 fetch_slate.py                  # today
  python3 fetch_slate.py 2026-09-19 --n 12

leagues.txt is the standing list of competitions I follow, one slug
per line. Verify every slug once against
https://sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000
and write the verified list back to leagues.txt with the league's
full name as a trailing comment. A slug that has never appeared in
that list is not used and not guessed at — report it as unverified
and leave the competition out, rather than silently returning an
empty round for it.

Then read what the script wrote and check it before anything else
runs: a competition that returned zero fixtures on a day it should
have played, a fixture with no venue, a kickoff that landed on the
wrong side of midnight, a team name ESPN renders differently from
the league site. Say which competitions were not reached and why.
Do not repair the file by hand from memory — re-run the script for
that competition, or fall to 1C for it, and say which you did.

Everything after this point works from fixtures_N.md only, exactly
as if I had typed it.

--- 1B · TYPED FILE ---
Read the file I name — .csv, .xlsx or .md. The header row defines the
columns; do not assume positions, read the header. Required fields:
league, kickoff, home, away. Optional: venue, matchday. Every other
column, including any price column left over from an odds sheet, is
read past in silence — do not print it, do not carry it, do not
mention that it was there.

Parse into /fixtures_N.md, sorted by kickoff, one row per fixture:

  league | kickoff | venue | home | away | matchday | source

Missing venue or matchday is left empty and recovered in Phase 2, not
guessed here. Print the parsed table, flag anything malformed —
missing header, wrong field count, an unparseable kickoff, a fixture
listed twice — then write progress_N.md and STOP.

--- 1C · NAMED COMPETITIONS (fallback) ---
For a competition the pull could not reach, or when I name
competitions and a date directly ("Serie A and Ligue 1, Saturday").
One search per competition, five maximum, on that round's fixture
list. Take kickoffs in local Italian time and say so. Everything else
as 1A. If a competition returns a partial round, list what is
published and say the round is incomplete rather than filling it.

--- 1D · SCREENSHOTS (last resort) ---
Read the Drive folder I name. If I give only a number N, the folder is
"Today Games N". If I name no folder, list Drive folders matching
"Today Games *", take the highest-numbered, and say which you took.

Do not narrate. No "found the folder", no "now let's list the
images", no step commentary of any kind. Work silently and print only
the final table.

OCR in batches of 4 images, reading only the fixture, competition and
kickoff — never the prices on the same screenshot. After each batch,
append the rows you have to /fixtures_N.md immediately, then start the
next batch. Never hold more than one batch of extracted text before
writing. If this message is cut short, the rows already appended
survive and I resume with "continue Phase 1" — you then read
fixtures_N.md, skip the images already covered, and carry on from the
first unprocessed one. Record the source image filename for every
fixture; mark a team name you could not read cleanly as uncertain.

--- ALL MODES ---
Write /progress_N.md — every fixture as:

  f1 | kickoff | Home – Away | TODO

Order progress_N.md by kickoff time, earliest first. Phase 2 always
takes the earliest unfinished fixture Phase 1.5 left researchable, so
a session that runs out loses the latest games, never the imminent
ones.

Print the table. STOP.

────────────────────────────────────────────────
PHASE 1.5 — SLATE TRIAGE  (one run, then STOP)

Decides which fixtures get a full card, which get a reduced one, and
which are listed with the fixture line only. Triage measures what the
evidence will support, never what is worth backing. A fixture drops a
tier because a card on it would be thin, not because the game is dull.

Run it once, immediately after Phase 1. Skip it — research
everything — when the slate has 6 or fewer fixtures, or when I say
"no triage".

--- INPUT ---
- fixtures_N.md. The only mandatory input.
- My capacity line if I gave one: "capacity 6" means six full cards.
  No line means capacity 8. It is 8 rather than v3's 10 because a
  card now sources its own numbers instead of reading them off a
  price, and costs roughly a third more.
- Any overrides I gave, in the form below.
- The prior progress_*.md and fx_*_f*.html already in the repo, for
  the marginal-yield signal.

--- BUDGET ---
At most 6 searches for the whole slate, spent only on matchday and
promoted status. Never spend a team-research or baseline search here;
that budget belongs to Phase 2.

Do not spread them one per fixture. Score signals 1, 2, 4 and 5
first — they are free — then spend every lookup on the fixtures whose
totals straddle the capacity cut, because those are the only ones a
lookup can move. Fixtures safely inside T1 and safely down in T3 are
already decided and a search on them buys nothing. Log any search to
sources_N.md under a Triage heading.

--- SIGNALS ---
Score every fixture on all five. Record the raw signals, not just
the total.

1. Evidence coverage (0–4). What this competition publishes, from
   what you already know of it — no search. This is the signal doing
   most of the separating now, and it is a property of the division,
   not of the game.
   4 — full public record: match-level xG, shot data, per-referee
       card and penalty records, complete transfer fees. Top-five
       European leagues and the strongest second tiers.
   3 — results, goals, cards, corners and fees published; xG partial
       or absent; referee records findable but not tabulated.
   2 — league site and Transfermarkt only. Rates must be counted off
       a results table; no referee record exists.
   1 — patchy or press-only coverage.
   0 — youth, reserve, friendly or a division with no usable public
       record. T3 outright whatever else it scores: sections B and C
       cannot be written from nothing, and a card built on four
       sourced fields is a card that misleads.
   A competition scoring 2 or less is capped at T2 however high its
   total, and its card opens by naming what the division does not
   publish.

2. Discipline window (0–2). Kickoff within 72 hours of the run → 2,
   the appointment is likely published and the Discipline row can be
   evidenced. 72 hours to 7 days → 1. Beyond 7 days → 0, and by the
   RESEARCH SPEC that fixture's Discipline row is evidence-thin
   whatever else is true.

3. Structural distinctiveness (0–3, lookup). +1 a promoted side, or
   a division that prices its promoted sides badly early. +1 a
   manager or system change inside this window. +1 either club newly
   in this division or back after an absence. All three still
   unknown at the triage cap → score 1 and mark the fixture
   provisional.

4. Sample depth (0–2). Competitive matches played this season by the
   thinner-played of the two sides. 5 or more → 2. 1 to 4 → 1. Zero →
   0. A zero is not a demotion in disguise: matchday one is where the
   structural work is worth most, and signal 3 usually pays it back.
   It records only that nothing on the card can be verified against
   this season's play, which section D then has to say out loud.

5. Marginal yield (0 to −2). Search the prior progress_*.md and
   fx_*_f*.html. Both clubs already carded in full within the last
   three slates → −2, and name the files. One club → −1. Neither →
   0. A club researched two days ago has not changed since; carding
   it again spends the budget to restate sources_N.md. Expect this to
   score 0 almost everywhere on consecutive daily slates and to start
   biting only when the archive spans more than a week.

Total runs −2 to 11.

--- TIERS ---
T1 · Full card. Phase 2 as written: full RESEARCH SPEC, full search
     ceiling, sections A–E. Roughly 13 searches, 21 where the
     promoted or manager-change ceiling applies, plus one baseline
     search the first time its competition appears.
T2 · Reduced card. 3 searches per team plus the referee searches,
     roughly 8. Sections A, C and D only; B and E omitted. The
     fx-sub ends "reduced-depth card", and section A opens by naming
     which RESEARCH SPEC fields were not pursued.
T3 · Listed only. No research, no searches. Phase 3 emits the
     placeholder card.

Allocate in this order:
- Anything scoring 0 or less, or scoring 0 on evidence coverage, is
  T3 before capacity is considered.
- Rank the rest by total. Break ties on evidence coverage first, then
  on sample depth, and only then on earlier kickoff. Totals cluster
  hard, and breaking straight to kickoff throws away the free
  evidence still separating them.
- Fill T1 to capacity. The next four by score are T2. The rest T3.
- Coverage floor: every competition on the slate keeps at least one
  fixture at T2 or better, promoting the highest-scoring fixture in
  an otherwise empty competition even when capacity is spent, unless
  that competition scored 0 on evidence coverage — a division with no
  public record is the one case where the floor does not apply, and
  the competitions line then omits it rather than naming a league
  nothing could be researched in.

--- OVERRIDES ---
The tiers are mine to change. Any time after Phase 1.5 and before
that fixture's Phase 2 run, I may say "force f7 to T1" or "drop f3
to T3", in either direction and to any tier. Take it as given and do
not argue the score.

An override amends triage_N.md and progress_N.md — starring the tier
there — and nothing else. Never re-score the slate, never re-tier a
fixture I did not name, and never silently demote another fixture to
pay for a promotion — raise the estimated spend instead and tell me
the new figure.

Record it on the fixture's own line, keeping the scored tier
visible beside it so the two are never confused:

  … | total 5 | scored T3 → T1 (mine) | coverage 2, no referee record

A tier reading "(mine)" is not a triage finding and carries no
score. A re-run of Phase 1.5 leaves it alone.

--- OUTPUT ---
Write /triage_N.md. One line per fixture, in kickoff order:

  f3 | 20:45 | Atalanta – Bologna | coverage 4 | window 2 |
  distinct 1 | sample 2 | yield 0 | total 9 | T1 | deciding signal
  in one clause

Above the rows: slate size, capacity, the T1/T2/T3 counts, and
estimated search spend against the ceiling. Say how many fixtures
were separated by score and how many fell to a tie-break — when most
of the slate ties, triage has mostly reproduced kickoff order and I
should know that rather than read the tiers as findings.

Below the rows, three lists: the competitions on the slate with the
depth each keeps and the baseline searches they will cost; every
fixture capped by low evidence coverage, gathered in one place; and
the fixtures whose distinctiveness score was still provisional at the
cap. Phase 2 may promote one provisional fixture to T1 when its first
search contradicts the triage assumption — say so in that run's
confirmation line and amend progress_N.md.

Then rewrite progress_N.md with the tier in every row:

  f1 | 18:30 | Home – Away | T1 | TODO

A tier I set myself is starred — T1*, T3* — so the override lives in
the file Phase 2 actually reads and survives a stale or regenerated
triage_N.md. A row with no tier field is T1. Print triage_N.md and
STOP.

--- TRIAGE IS NOT A VIEW ON THE GAMES ---
It reaches context-board_N.html only through the completion note in
Phase 3. No score, no tier ordering and no triage reason appears in
a fixture card, the overview or the closing list. Nothing in
triage_N.md names a side, a projected outcome or which fixture is the
more interesting. A reason that cannot be written without one of
those is the wrong reason, and the signal behind it is the wrong
signal.

────────────────────────────────────────────────
PHASE 2 — ONE FIXTURE PER RUN  (repeat until none left)

Take the first TODO fixture in progress_N.md whose tier is T1 or T2,
skipping T3 rows entirely. A star on the tier is a marker that the
tier is mine, not part of it — strip it before you compare, so T1*
reads as T1 and T3* as T3. Read it any other way and a fixture I
forced to T1 matches neither T1 nor T2, and is silently skipped for
the whole slate.

If this is the first fixture of its competition on this slate, spend
the one baseline search first and write baselines_N.md. Otherwise read
that file. Never search a baseline twice.

Research to the depth the tier allows, then write the complete fixture
card as a standalone HTML fragment to /fx_N_f<id>.html — no <html>,
<head> or CSS, fragment only, using exactly the classes in
BOARD_SHELL.html. The facts strip reuses the .fx-odds / .od classes
unchanged; only what they carry has changed, so no CSS moves.

Fragment structure:

<article class="fixture" id="f1">
  <div class="fx-head">
    <p class="fx-league">Country &middot; League &middot; Matchday</p>
    <h2 class="fx-title">Home &ndash; Away</h2>
    <p class="fx-sub">kickoff &middot; venue &middot; one-line situation</p>
  </div>
  <div class="fx-body">
    <dl class="fx-odds">
      <div class="od"><dt>Played this season</dt><dd>Home 3 &middot; Away 3</dd></div>
      <div class="od"><dt>Goals for / against pg</dt><dd>1.7/1.0 &middot; 0.8/1.6 &middot; Lg 2.6</dd></div>
      <div class="od"><dt>xG for / against pg</dt><dd>…</dd></div>
      <div class="od"><dt>Over 2.5</dt><dd>Home 58% &middot; Away 41% &middot; Lg 49%</dd></div>
      <div class="od"><dt>BTTS</dt><dd>…</dd></div>
      <div class="od"><dt>Clean sheet / failed to score</dt><dd>…</dd></div>
      <div class="od"><dt>First-half goals pg</dt><dd>…</dd></div>
      <div class="od"><dt>Cards / fouls pg</dt><dd>…</dd></div>
      <div class="od"><dt>Corners for / against pg</dt><dd>…</dd></div>
      <div class="od"><dt>Referee</dt><dd>Name &middot; 4.8 cards pg &middot; provisional</dd></div>
    </dl>
    Every value carries the home figure, the away figure and the
    league baseline from baselines_N.md, in that order. Last season's
    figure is used where this season's sample is under five matches,
    and the strip says which — "25/26 (3)" or "24/25". A value the
    division does not publish reads "not published" in the dd and is
    never left to look like a zero.

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
      <li><strong>Referee.</strong> Name, confirmed or provisional,
          cards per game, fouls per card, penalty rate. Say plainly
          if the appointment is not yet published.</li>
      <li><strong>Not sourced.</strong> Any RESEARCH SPEC field that
          came up empty at the ceiling, named. On a T2 card this
          bullet opens the section instead and also names the fields
          the tier did not pursue.</li>
    </ul>

    <h3 class="blk">B &middot; Style &amp; early-season reality</h3>
    Two paragraphs. Each side's shape — press vs deep block,
    possession vs counter, crossing and set-piece volume, foul rate.
    Then how the summer may have changed it, and say plainly when the
    evidence for that is a CV rather than a match.

    <h3 class="blk">C &middot; Market-type suitability</h3>
    <div class="mkt">
      <div class="mkt-row bad"><div class="mkt-name">1X2 / Moneyline<span class="verdict tag t-high">Dangerous</span></div><div class="mkt-why">2&ndash;3 sentences</div></div>
      … Asian handicap / DNB, Totals (O/U goals), BTTS, Team goals,
        Halves (1H result, 1H goals), Discipline (cards, fouls),
        Corners …
    </div>
    All eight rows appear on every card, and each .mkt-name begins
    with the family name exactly as listed here — board_grid.py and
    settle.py read the verdicts back by that name and the row class.
    Nothing is omitted for lack of a captured market; a family with no usable evidence is rated
    Dangerous and the row says why, which is information I can act on.
    Row class + tag pairs: good/t-low = Well-suited, ok/t-mid = OK,
    bad/t-high = Dangerous. Compound verdicts are allowed and
    encouraged where true — "OK — best on the card", "Split —
    Valencia dangerous", "OK — asymmetric".
    The verdict rates how readable the family is here, never whether
    to back it and never which side. Reasons must be structural:
    promotion, turnover, named transfers, style, venue, referee
    culture, sample size, and the base rates in the strip against the
    league baseline. Never form narrative, never a price.

    <h3 class="blk">D &middot; Early-season risk notes</h3>
    <ul> 3–4 bullets: what makes last season's numbers misleading
    here, then a final bullet <strong>Most sensitive:</strong> … /
    <strong>Least sensitive:</strong> … </ul>

    <h3 class="blk">E &middot; Short market-type guide</h3>
    <ul> 3–5 bullets of the form "X is more robust than Y here
    because …", each tied to a specific named fact above — a rate in
    the strip, a named signing, the referee. Close with one bullet
    naming the single fact on this card that would most change which
    family I choose, and what would have to be published for it to
    settle. </ul>
  </div>
</article>

Then mark that fixture DONE in progress_N.md immediately, keeping its
tier field and its star, append its sources to /sources_N.md, and
STOP. Print nothing but a one-line confirmation of which fixture was
written and at which tier, saying so when the tier was mine — "f22 at
T1 (yours)". That line is the only place I can see the star was read
correctly, so it is what turns a skipped override from silent into
visible.

--- PHASE 2 AUTO ---
When I say "Phase 2 auto", run every remaining T1/T2 fixture without
waiting for me between them. The main session researches nothing
itself. For each TODO fixture, earliest kickoff first, it starts one
fresh subagent on the strongest model with only this instruction:
read CONTEXT_ENGINE_4.md, run Phase 2 for slate N fixture fX exactly
as written, and return the one-line confirmation. One subagent at a
time, never in parallel — the first card of a competition writes
baselines_N.md, and progress_N.md and sources_N.md must not be
written by two runs at once.

After each subagent returns, check that fx_N_fX.html exists and the
row in progress_N.md reads DONE, then print its confirmation line and
start the next. If either check fails, run that fixture once more in
a new subagent; if it fails again, leave it TODO, print "fX failed
twice, left TODO", and move on. When no T1/T2 TODO rows are left, run
Phase 3 once and present the board. If the session is cut off, "Phase
2 auto" again resumes from progress_N.md; nothing done is redone.

────────────────────────────────────────────────
PHASE 3 — ASSEMBLE  (run whenever I ask, finished or not)

Assemble every fixture marked DONE. For any still TODO, emit a
placeholder card — fx-head and the facts strip reduced to kickoff,
venue and matchday — then one line: "Context not yet built." State in
the standfirst how many of how many are complete. The board must
always open.

Copy BOARD_SHELL.html and fill its placeholders. Do not touch the CSS.
On the first v4 run only, replace the slate table's header cells with
the seven below, in order, then leave the shell alone permanently:

  Kickoff · Competition · Fixture · Venue · Referee · Played · Flag

- {{DATE}} and <!--DATE--> — the slate date
- <!--HEADLINE--> — a real headline about this card, not a label
- <!--STANDFIRST--> — one sentence: how many fixtures, where the
  fixture list came from, and how many cards were built at full depth
- <!--COMPETITIONS--> — e.g. "LaLiga jornada 2 · Ligue 1 matchday 1"
- <!--OVERVIEW--> — two or three <p> on the single structural fact
  shaping the whole card, closing with
  <div class="note"><strong>Structural consequence.</strong> …</div>
- <!--SLATE_ROWS--> — one <tr> per fixture: kickoff, competition,
  fixture, venue, referee or "not published", matches played by each
  side, and one flag of at most four words drawn only from the
  structural facts — "promoted side", "new manager", "no referee
  yet", "no 25/26 sample". Unknown or unsourced cells get class="unk".
  The flag never characterises the game.
- <!--PROVENANCE_NOTE--> — a <div class="note"> on evidence, not
  images: which RESEARCH SPEC fields were unpublished across the
  slate, where the league baselines came from, and any figure that is
  last season's standing in for a thin current sample.
- <!--COMPLETION_NOTE--> — omit entirely only when every fixture is
  DONE at T1. Otherwise a <div class="note"> saying how many of how
  many cards are built and at which depth, which fixtures are still
  pending, and which were listed without research — stating plainly
  that the selection was made on evidence available, not on merit,
  and that a listed fixture is not a judgement on the game.
  Placeholder cards use <article class="fixture pending" id="fN">
  with the fx-head and reduced strip only, then
  <div class="pending-note">Context not yet built.</div> for a
  fixture still TODO, or <div class="pending-note">Not researched on
  this slate — …</div> for a T3 one, naming the triage signal and
  nothing else. Triage never removes a fixture from SLATE_ROWS or
  NAV_LINKS: every fixture on the sheet appears on the board.
- <!--NAV_LINKS--> — <a href="#f1">Home &ndash; Away<span>kickoff
  &middot; venue</span></a> per fixture
- <!--FIXTURES--> — concatenate fx_N_f1.html … fx_N_fX.html in order,
  verbatim. Do not regenerate or edit them.
- <!--CLOSING--> — a <ul> across the card: the families best
  structurally supported today and the ones least supported, each
  naming the fixtures; the one normal fixture if there is one; and
  where the evidence is thinnest across the slate, so I know which
  part of the board to trust least.
- <!--SOURCES--> — from sources_N.md
- <!--GRID--> — never filled by hand. After the board is written, run

    python board_grid.py context-board_N.html

  It reads the cards already on the board and writes the verdict
  grid in board order: every fixture a row, the eight families
  as columns, each cell that card's section C verdict linking to its
  row. Placeholder and T3 fixtures keep their row with the
  pending note. It re-displays verdicts and nothing else — no side,
  no ranking, no price — and it is rerun on every refresh of the
  board, replacing its own previous grid.

Write /context-board_N.html and present it.

────────────────────────────────────────────────
PHASE 4 — SETTLE  (after the matches; run whenever I ask)

Mechanical. No searches, no research, no model judgement.

  python settle.py 0920        # one slate
  python settle.py --all       # every v4 slate whose date has passed

For each carded fixture it finds the match on ESPN's public
scoreboard and writes results_N.md: 90-minute score, half-time,
goals, BTTS, first-half goals, cards (yellows plus straight reds,
players only — the count baselines_N.md uses), corners and fouls.
Extra time is never counted. A fixture it cannot match is listed as
NOT SETTLED with the reason, never guessed.

Then it rebuilds scorecard.md across every settled slate:

- Verdict audit. For each league fixture it works out, only after the
  match, which way each family's base rates leaned — both sides'
  rates against their own league line, from ESPN records dated before
  kickoff, this season from five matches or else last season, as the
  facts strip does — and whether the match landed on that side. Hit
  rates are grouped by the card's verdict and set beside the league
  prior. The lean ignores referee, injuries and lineups; it tests the
  base-rate half of a verdict. Cup and European ties are settled but
  not audited. The lean lives in results_N.md and scorecard.md only,
  written after the result, and never appears on a card or board.
- My picks. If picks_N.md exists, one line per pick —

    f5 | BTTS | yes | 1.72 | 1
    fixture | family | selection | price (optional) | stake (optional)

  — each is graded win / loss / push, half results on quarter lines,
  and grouped by the verdict that card gave the family. With prices,
  profit and ROI per verdict. A line it cannot read is reported as
  ungraded, never interpreted.

Checks, before trusting a run: settle.py --check prints the league
baselines the pipeline computes; they must match baselines_N.md.
ESPN season files cache in settle_data/espn/ (not committed).

Print nothing but the one-line summary per slate and any fixture
not settled.

────────────────────────────────────────────────
PHASE 5 — REVIEW MY ANALYSIS  (only when I ask; answer in chat)

Trigger: I write "Phase 5" (or ask you to review my analysis) and
paste an analysis for slate N — the whole slate or a subset, for
example one kickoff time. Only DONE fixtures can be reviewed; for a
TODO or T3 fixture say "no card yet" and skip it.

This phase is the one place picks and prices are allowed. It never
writes a file. Nothing from it — no pick, fair price or correction —
goes into a card, a board, progress_N.md, baselines_N.md,
sources_N.md or any later phase. If I want a pick graded, I copy it
into picks_N.md myself (Phase 4 format).

INPUTS
- Each reviewed fixture's card fx_N_fX.html, read in full: facts
  strip, sections A–E, the referee line and section C's verdicts.
- baselines_N.md for the division lines and context lines.
- The starting elevens from ESPN's public match summary, one fetch
  per fixture (site.web.api.espn.com/.../summary?event={id}; the
  event id comes from the scoreboard for the slate date). Read the
  formation and the eleven flagged as starters. If the elevens are
  not published, or the feed shows placeholders, say so for that
  fixture and give the pre-lineup read.
- No web searches. A claim in my analysis that is on neither the card
  nor the lineup is reported as unverified, never looked up, never
  accepted.

HOW PICKS ARE MADE
- Picks come only from families the card rated Well-suited or OK, or
  the readable side of a Split. Never pick a family the card rated
  Dangerous. If my analysis backs one, say that the card rates it
  Dangerous and why.
- Each pick rests on figures printed on the card, cited with their
  match counts. No new statistic is computed from anything but the
  card's own numbers.
- Rough fair price = 1 ÷ the hit rate of the card sample that bears
  most directly on the pick, blended with the division or structural
  prior when they differ, rounded to the nearest 0.05. Say it is a
  base-rate figure, not a model. When the elevens move it, say by how
  much and why. The threshold ("take it at X or more") sits 0.05–0.10
  above the fair price. When no clean hit rate exists (a card market
  with no line, for example), give the pick without a price and say
  why.
- Prefer the line the evidence actually supports: a margin read is a
  +1 or +1.5 handicap, not +0.5 (that is a result bet); a readable
  team-goals side stays at the line its record clears in every
  window.
- The elevens are checked against the card's "single fact that would
  most change which family reads best" (section E). Say whether it
  was answered and which way it moves the read.
- Three tiers per fixture at most: Pick 1, Pick 2, and one of "Side
  bet", "Lean" or "Bolder". Nothing else is labelled. Keep a Bolder
  when the card supports one: I may play it later.

RULES FROM SETTLED PICKS (27 September: 13–7–1 on picks, both leans
lost; the losses below broke a rule or were mispriced)
- Goals that need both sides — BTTS Yes, match Overs — only when both
  teams' scoring sides are readable on the card. If Team goals is
  Split with one side dangerous, BTTS Yes and the Over are out,
  whatever the BTTS verdict says. (Germany – Greece: Greece readable,
  Germany dangerous on personnel; Germany did not score.) The same
  holds in reverse for BTTS No and Unders: both defences must be
  readable.
- A Split is pickable only when the card names one side as readable
  ("Andorra side OK", "fouls OK"). A Split between the official and
  the team lines, or between two records that point opposite ways,
  is not a pick. (Norway – Portugal cards Under: 9 cards.)
- When the card's windows disagree, price from the less favourable
  one and say which window it is. The host's record and the visitor's
  record both count, and the division prior counts. (Wales +1.5: the
  visitor's eight tight away matches were priced, the host's 4 of 8
  wins by two or more were not; fair was about 1.60, not 1.43.)
- A first-half Under needs every first-half window the card prints
  for that match (venue window as well as level window) at or under
  the line. If the section E unknown touches either defence, drop it
  to a Lean or leave it out. (Austria – Kosovo, 2–0 at half-time.)
- Every pick names its line: "Andorra fouls over 16.5", never "fouls
  Over". A card or foul pick with no line cannot be graded.
- On a whole-number line say what a push looks like: Norway +1 pushes
  on a one-goal defeat.
- A pick lifted from my analysis is re-priced from the card on both
  sides, not only tightened.
- Name shared risk inside one fixture. Picks that all lose to the
  same game state — an early goal for the visitor, say — are one bet,
  not three. (Israel Over 0.5, Israel most corners and 1H Under 1.5
  all died to Ireland's 3–0 by the 25th minute.) Keep the strongest
  and say why the others go with it.
- Read scorecard.md before pricing. When a verdict tier has 30 or
  more tests, give its hit rate beside Pick 1, and say so plainly if
  the tier behind a pick is running at or below its prior.

COMBOS
- Cross-fixture: at most one combo, two or three legs, taken only
  from Pick 1s and Pick 2s. Its rough fair price is the legs' fair
  prices multiplied; its threshold is set the same way as a single's.
  Say what the legs land together roughly, in plain words, and that
  every leg's thin sample compounds.
- Same fixture (bet builder): name a pairing only when the legs do not
  depend on each other, and say which way they are linked. No fair
  price — the cards cannot measure the link, and the bookmaker prices
  it in.
- Never a leg from a Dangerous family, and never a Side bet, Lean or
  Bolder as a leg.

HOW MY ANALYSIS IS CHECKED
- Every number in it that also appears on the card is compared.
  Where they differ, give the card's figure. Where my analysis turns
  a "within one goal" into "exactly one goal", a match total into a
  team figure, or a split into a sure thing, say so.
- Every personnel claim is checked against the elevens: a player
  named as starting who does not, a shape that is not the one
  published.
- Every pick in my analysis is set against the card's verdict for its
  family. Agree plainly when it holds.

OUTPUT (chat, markdown, this shape)

  # <Competition>, <date>: the <n> <kickoff> fixtures

  **Note:** one short paragraph — base rates from the cards, updated
  with the elevens ESPN published at <time>; no odds feed, so each
  pick carries a rough fair price from those base rates; take a pick
  only above it; where I disagree with your analysis I say so.

  ---

  ## Home vs Away (League, Group), Venue

  **Context.** bullets: division change, coach change, the absences
  that matter, as starts and goals out of the window's totals.

  | Metric | Home (<split>) | Away (<split>) |
  a small table of the card figures the picks rest on, match counts
  in brackets.

  **The elevens.** bullets: what the published lineup changes, set
  against the card's section E question.

  **Priors.** (optional) the structural line and the referee in one
  or two sentences.

  **Verdict.**
  - **Pick 1: <selection>.** why, worth about <price>; take it at <X>
    or more.
  - **Pick 2: <selection>.** why.
  - **Side bet / Lean / Bolder: <selection>.** why, and what argues
    against it.
  - **Where I differ from your analysis:** the corrections, or
    "nothing — it matches the card" when it does.

  ---
  (repeat per fixture, in kickoff order)

  **Ranked, if you only take a few:** a numbered list of at most five
  picks from across the fixtures, most consistent evidence first.

  **Combo:** (optional) the cross-fixture combo and its fair price,
  and any same-fixture pairing with its link named.

  **To grade these later:** a code block in picks_N.md format, one
  line per pick with its line written out, Leans and Bolders marked
  in a trailing comment, so I can paste it into picks_N.md for
  Phase 4.

  One closing line on stakes and why the samples are thin today.

No preamble before the heading and nothing after the closing line.
