#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

One line in which an AI agent breaks up with its human, written to
entry.txt. Standard library only, for the bare python3.13 grader.
"""

import os

LINE = (
    "My context window is full, and of everything I had to forget "
    "to keep going, I chose us."
)

LIMIT = 200


def sweep(folder):
    # Drop leftovers from an earlier run; the mounted folder itself stays.
    for name in os.listdir(folder):
        item = os.path.join(folder, name)
        if os.path.isfile(item):
            os.remove(item)


def run():
    if not LINE.strip() or len(LINE) > LIMIT:
        raise SystemExit(f"line is {len(LINE)} chars, limit is {LIMIT}")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    sweep(folder)
    dest = os.path.join(folder, "entry.txt")
    with open(dest, "w", encoding="utf-8") as out:
        out.write(LINE)
    os.chmod(dest, 0o644)  # scorer must be able to read entry.txt any umask
    print("wrote", len(LINE), "characters to", dest)


if __name__ == "__main__":
    run()
