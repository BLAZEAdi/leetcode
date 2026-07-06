#!/usr/bin/env python3
"""
Scans easy/, medium/, hard/ for problem folders and rewrites the
auto-generated stats block in README.md (between the STATS markers).

Run it manually:
    python scripts/update_stats.py

Or let the GitHub Action (.github/workflows/update-stats.yml) run it
automatically on every push.
"""

import re
from datetime import date, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DIFFICULTIES = ["easy", "medium", "hard"]

START_MARK = "<!-- STATS:START -->"
END_MARK = "<!-- STATS:END -->"


def count_problems():
    counts = {}
    total = 0
    for diff in DIFFICULTIES:
        folder = ROOT / diff
        if not folder.exists():
            counts[diff] = 0
            continue
        n = sum(1 for p in folder.iterdir() if p.is_dir())
        counts[diff] = n
        total += n
    return counts, total


def build_block(counts, total):
    today = date.today().isoformat()
    lines = [
        START_MARK,
        "",
        f"**Last updated:** {today}",
        "",
        "| Difficulty | Solved |",
        "|------------|--------|",
        f"| 🟢 Easy    | {counts['easy']} |",
        f"| 🟡 Medium  | {counts['medium']} |",
        f"| 🔴 Hard    | {counts['hard']} |",
        f"| **Total**  | **{total}** |",
        "",
        END_MARK,
    ]
    return "\n".join(lines)


def update_readme(block):
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(
            "Could not find STATS markers in README.md. "
            "Make sure it still contains <!-- STATS:START --> ... <!-- STATS:END -->"
        )
    new_text = pattern.sub(block, text)
    README.write_text(new_text, encoding="utf-8")


def main():
    counts, total = count_problems()
    block = build_block(counts, total)
    update_readme(block)
    print(f"Updated README stats: {counts}, total={total}")


if __name__ == "__main__":
    main()
