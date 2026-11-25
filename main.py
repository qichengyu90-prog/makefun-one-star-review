#!/usr/bin/env python3
"""Entry for make.fun's "One-Star Review of Something Essential" bounty.

Writes one single-line one-star review (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Gravity: one star. Keeps dropping my phone face-down and has never once apologised."


def main():
    # Fail fast if the entry ever stops being one line of at most 160 chars.
    if len(LINE) > 160 or "\n" in LINE:
        raise SystemExit("LINE must be one line of at most 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
