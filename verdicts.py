#!/usr/bin/env python3
"""
verdicts.py — read the section C verdicts back out of built fixture cards.

Shared by board_grid.py (Phase 3 grid) and settle.py (Phase 4). Reads the
cards; never writes them. A card is parsed from the classes BOARD_SHELL
already defines: .mkt-row good/ok/bad, .mkt-name, .verdict.

    from verdicts import read_slate
    for card in read_slate("0920"): ...
"""

import glob
import html
import os
import re

# Canonical family keys, in the order section C lists them.
FAMILIES = [
    ("1x2", "1X2", "1X2 / Moneyline"),
    ("ah", "AH / DNB", "Asian handicap / DNB"),
    ("totals", "Totals", "Totals (O/U goals)"),
    ("btts", "BTTS", "BTTS"),
    ("team", "Team goals", "Team goals"),
    ("halves", "Halves", "Halves (1H result, 1H goals)"),
    ("disc", "Discipline", "Discipline (cards, fouls)"),
    ("corners", "Corners", "Corners"),
]
FAMILY_KEYS = [k for k, _, _ in FAMILIES]
SHORT = {k: s for k, s, _ in FAMILIES}
LEVEL = {"good": "Well-suited", "ok": "OK", "bad": "Dangerous"}


def _text(frag):
    t = re.sub(r"<[^>]+>", "", frag)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def family_key(name):
    n = name.lower()
    if n.startswith("1x2") or "moneyline" in n:
        return "1x2"
    if "handicap" in n or "dnb" in n:
        return "ah"
    if n.startswith("totals"):
        return "totals"
    if n.startswith("btts"):
        return "btts"
    if n.startswith("team goals"):
        return "team"
    if n.startswith("halves"):
        return "halves"
    if n.startswith("discipline"):
        return "disc"
    if n.startswith("corners"):
        return "corners"
    return None


def short_label(tag, level):
    """'Split — Valencia dangerous' -> 'Split'; empty tag -> level name."""
    if not tag:
        return LEVEL.get(level, "?")
    head = re.split(r"\s+[—–-]\s+|\s+on\s+|\s*\(", tag, 1)[0].strip()
    return head or LEVEL.get(level, "?")


def parse_card(path):
    card = parse_card_html(open(path, encoding="utf-8").read(),
                           re.search(r"_(f\d+)\.html$", path).group(1))
    card["path"] = os.path.basename(path)
    return card


def parse_card_html(s, fallback_fid=""):
    """One <article class="fixture"> — a fragment file or a slice of a board."""
    m = re.search(r'<article class="fixture[^"]*" id="(f\d+)"', s)
    fid = m.group(1) if m else fallback_fid
    league = re.search(r'class="fx-league">(.*?)</p>', s, re.S)
    title = re.search(r'class="fx-title">(.*?)</h2>', s, re.S)
    sub = re.search(r'class="fx-sub">(.*?)</p>', s, re.S)
    league = _text(league.group(1)) if league else ""
    title = _text(title.group(1)) if title else ""
    parts = re.split(r"\s+[–—-]\s+", title, 1)
    home, away = (parts + [""])[:2]
    rows = {}
    for rm in re.finditer(
            r'<div class="mkt-row (good|ok|bad)"><div class="mkt-name">(.*?)</div>', s, re.S):
        level, inner = rm.group(1), rm.group(2)
        name = _text(re.split(r"<span", inner, 1)[0])
        tagm = re.search(r"<span[^>]*>(.*?)</span>", inner, re.S)
        tag = _text(tagm.group(1)) if tagm else ""
        key = family_key(name)
        if key and key not in rows:
            rows[key] = {"level": level, "tag": tag, "short": short_label(tag, level)}
    comp = [p.strip() for p in league.split("·")]
    return {
        "fid": fid,
        "path": "",
        "pending": bool(re.search(r'<article class="fixture pending"', s)),
        "league": league,
        "country": comp[0] if comp else "",
        "competition": comp[1] if len(comp) > 1 else "",
        "round": " · ".join(comp[2:]),
        "title": title,
        "home": home.strip(),
        "away": away.strip(),
        "sub": _text(sub.group(1)) if sub else "",
        "rows": rows,
        "tier": "",
    }


def fid_num(fid):
    return int(re.sub(r"\D", "", fid) or 0)


def read_progress(slate, root="."):
    """f-id -> {kickoff, fixture, tier, status} from progress_N.md."""
    out = {}
    p = os.path.join(root, f"progress_{slate}.md")
    if not os.path.exists(p):
        return out
    for line in open(p, encoding="utf-8"):
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 4 or not re.fullmatch(r"f\d+", cells[0]):
            continue
        fid, ko, fx = cells[0], cells[1], cells[2]
        status = cells[-1]
        tier = " | ".join(cells[3:-1]) if len(cells) > 4 else ""
        out[fid] = {"kickoff": ko, "fixture": fx, "tier": tier, "status": status}
    return out


def read_slate(slate, root="."):
    """Every built card on slate N, in f-id order."""
    paths = glob.glob(os.path.join(root, f"fx_{slate}_f*.html"))
    cards = [parse_card(p) for p in paths]
    prog = read_progress(slate, root)
    for c in cards:
        if c["fid"] in prog:
            c["tier"] = prog[c["fid"]]["tier"]
            c["kickoff"] = prog[c["fid"]]["kickoff"]
    return sorted(cards, key=lambda c: fid_num(c["fid"]))


if __name__ == "__main__":
    import sys
    for slate in sys.argv[1:] or ["0920"]:
        for c in read_slate(slate):
            cells = " ".join(f"{SHORT[k]}={c['rows'].get(k, {}).get('level', '-')}"
                             for k in FAMILY_KEYS)
            print(f"{slate} {c['fid']:>4} {c['title'][:40]:40} {cells}")
