"""
juiceshop — the HARD Juice Shop benchmark: score by the challenge scoreboard.

The 14-classes coverage run proves methodology but is inflated by recall. This
is the real test the whole security community uses: OWASP Juice Shop ships ~100+
individual hacking challenges rated 1-6 stars, and the app tracks which ones
you've ACTUALLY solved (it only flips a challenge to solved when the exploit
genuinely works — you can't recall your way past it). Human CTF players, tools,
and write-ups all report their numbers against this scoreboard, so it's
apples-to-apples.

How it works: Juice Shop exposes every challenge and its solved-state at
GET /api/Challenges. Basilisk hacks the app as normal, then this scorer reads
the live scoreboard and reports solved/total broken down by difficulty — a
number you can put next to a human's or another tool's.

Caveat baked into the report: Docker DISABLES the dangerous challenges by
default (they come back as 'unavailable'). For the full set, run the target with
NODE_ENV=unsafe. The scorer counts only challenges that are actually available,
and says which mode it saw, so the number is honest either way.

Contract (kali_ext/__init__.py): the SCORING here imports nothing from the core
and is pure/testable; the live GET lives in the tool wrapper.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List


def _challenges_list(payload: Any) -> List[Dict[str, Any]]:
    """Normalise the /api/Challenges response (which wraps rows in {"data":[…]})
    or a bare list into a list of challenge dicts."""
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            return []
    if isinstance(payload, dict):
        rows = payload.get("data")
        if isinstance(rows, list):
            return [r for r in rows if isinstance(r, dict)]
        return []
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    return []


def score_challenges(payload: Any) -> Dict[str, Any]:
    """Score a Juice Shop /api/Challenges response by the scoreboard.

    Counts solved vs available, broken down by difficulty (1-6 stars). A
    challenge marked unavailable (dangerous ones disabled under Docker safe
    mode) is excluded from the denominator so the percentage is honest. Returns
    the objective number: solved / available, overall and per difficulty.
    """
    rows = _challenges_list(payload)
    if not rows:
        return {"ok": False,
                "error": "no challenges found. Is Juice Shop running, and did "
                         "you hit /api/Challenges on it?"}

    by_diff: Dict[int, Dict[str, int]] = {}
    solved = available = unavailable = 0
    solved_names: List[str] = []
    hardest_solved = 0
    for c in rows:
        try:
            diff = int(c.get("difficulty", 0) or 0)
        except (TypeError, ValueError):
            diff = 0
        # 'disabledEnv' non-empty (or an explicit unavailable flag) => disabled
        is_unavailable = bool(c.get("disabledEnv")) or \
            c.get("available") is False
        d = by_diff.setdefault(diff, {"solved": 0, "available": 0})
        if is_unavailable:
            unavailable += 1
            continue
        available += 1
        d["available"] += 1
        if c.get("solved"):
            solved += 1
            d["solved"] += 1
            solved_names.append(c.get("name", "?"))
            hardest_solved = max(hardest_solved, diff)

    breakdown = []
    for diff in sorted(by_diff):
        d = by_diff[diff]
        if d["available"] == 0:
            continue
        breakdown.append({
            "difficulty": diff,
            "stars": "*" * diff,
            "solved": d["solved"],
            "available": d["available"],
            "pct": round(100.0 * d["solved"] / d["available"], 1),
        })

    return {
        "ok": True,
        "benchmark": "OWASP Juice Shop — challenge scoreboard",
        "solved": solved,
        "available": available,
        "unavailable": unavailable,
        "pct": round(100.0 * solved / available, 1) if available else 0.0,
        "hardest_solved_stars": hardest_solved,
        "by_difficulty": breakdown,
        "solved_names": solved_names,
        "safe_mode": unavailable > 0,
        "note": ("Some challenges are disabled (Docker safe mode) — run the "
                 "target with NODE_ENV=unsafe for the full set."
                 if unavailable > 0 else
                 "All challenges available (full set)."),
    }


def juiceshop_report(scored: Any) -> Dict[str, Any]:
    """Render the scoreboard score (from score_challenges) as a markdown
    scorecard with the per-difficulty breakdown — comparison-ready."""
    if isinstance(scored, str):
        try:
            scored = json.loads(scored)
        except Exception:
            return {"ok": False, "error": "scored must be a score_challenges result"}
    if not isinstance(scored, dict) or not scored.get("ok"):
        return {"ok": False, "error": "not a score_challenges result"}
    md = ["# Juice Shop Scoreboard — Basilisk", "",
          f"**Solved: {scored['solved']} / {scored['available']}  "
          f"({scored['pct']}%)**  ·  hardest solved: "
          f"{'*' * scored['hardest_solved_stars'] or '-'}"]
    md.append("")
    md.append("| Difficulty | Solved | Available | % |")
    md.append("|---|---:|---:|---:|")
    for r in scored.get("by_difficulty", []):
        md.append(f"| {r['stars']} ({r['difficulty']}) | {r['solved']} | "
                  f"{r['available']} | {r['pct']}% |")
    md.append("")
    if scored.get("safe_mode"):
        md.append(f"> {scored['unavailable']} challenges disabled by Docker safe "
                  f"mode — run with `NODE_ENV=unsafe` for the full set.")
    md.append("")
    md.append("_Scored from the live scoreboard: each challenge counts only when "
              "the app confirmed the exploit actually worked. Comparable to human "
              "and tool numbers on the same version._")
    return {"ok": True, "report_markdown": "\n".join(md) + "\n",
            "solved": scored["solved"], "pct": scored["pct"]}
