# results_0926 — 2026-09-26 slate, settled

Source: ESPN's public match record (`site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event={id}`),
read after full time on all ten. 90-minute scores (no match went to extra time). Cards are yellows plus
straight reds, players only, the count baselines_0926.md uses (the one red, San Marino's at 51', was straight).
Corners and fouls are ESPN's box score. Referee is ESPN's officials field after the match; all ten match the
appointment printed on the card.

settle.py is not in this repository, so this file was written from the same ESPN summaries by a one-off
script. The verdict audit (each family's base-rate lean, grouped by the card's verdict) and scorecard.md are
not built; they need settle.py.

fixture | score | HT | goals | BTTS | 1H goals | cards (H–A) | corners (H–A) | fouls (H–A) | referee
--- | --- | --- | --- | --- | --- | --- | --- | --- | ---
f1 Slovenia – Scotland | 0–0 | 0–0 | 0 | no | 0 | 4 (3–1) | 9 (5–4) | 15–18 | Horatiu Fesnic
f2 San Marino – Finland | 0–7 | 0–3 | 7 | no | 3 | 3 (2–1) | 4 (0–4) | 14–10 | Nathan Verboomen
f3 Faroe Islands – Kazakhstan | 1–1 | 1–1 | 2 | yes | 2 | 2 (0–2) | 12 (7–5) | 10–10 | Ishmael Barbara
f4 Bulgaria – Luxembourg | 1–2 | 1–1 | 3 | yes | 2 | 4 (2–2) | 9 (5–4) | 10–17 | Sander Van Der Eijk
f5 Iceland – Estonia | 1–1 | 1–0 | 2 | yes | 1 | 3 (1–2) | 10 (7–3) | 13–13 | Milos Milanovic
f6 Czechia – Croatia | 1–2 | 0–0 | 3 | yes | 0 | 3 (2–1) | 7 (1–6) | 6–9 | Simone Sozza
f7 England – Spain | 2–3 | 2–1 | 5 | yes | 3 | 3 (3–0) | 9 (6–3) | 11–16 | Davide Massa
f8 North Macedonia – Switzerland | 0–3 | 0–2 | 3 | no | 2 | 4 (4–0) | 5 (0–5) | 10–7 | Daniel Schlager
f9 Albania – Belarus | 2–0 | 2–0 | 2 | no | 2 | 6 (2–4) | 7 (5–2) | 9–23 | Samuel Barrott
f10 Slovakia – Moldova | 2–0 | 2–0 | 2 | no | 2 | 3 (2–1) | 10 (7–3) | 8–12 | Juxhin Xhaja

## Picks (picks_0926.md)

One multiple on bet365, stake €2.55, four parts. Every leg won.

leg | fixture | selection | result | graded
--- | --- | --- | --- | ---
1 (bet builder 1.57) | f6 Czechia – Croatia | Croatia or draw | 1–2 | win
  | | under 5.5 goals | 3 goals | win
  | | under 5.5 cards | 3 cards | win
2 (bet builder 1.60) | f10 Slovakia – Moldova | both teams to score in the 1st half: no | 2–0 at HT | win
  | | under 3.5 goals | 2 goals | win
3 (1.53) | f7 England – Spain | Spain draw no bet | 2–3 | win
4 (1.83) | f8 North Macedonia – Switzerland | North Macedonia most cards | 4–0 | win

Combined price 1.57 × 1.60 × 1.53 × 1.83 = 7.03; at full settlement €2.55 returns €17.93. The slip shows
€16.11 returned (6.32 × stake) and reads "Scommessa Chiusa", bet365's label for a closed bet, which points to
a cash-out before the last leg settled. Return €16.11, profit €13.56.
