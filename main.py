#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line, at most 140 characters, in which a robot vacuum
explains why it missed a spot. Pure standard library, deterministic.
"""

import os

ENTRY = (
    # 100 characters, inside the 1-140 gate.
    "I skipped the spot because my map says it's a room now, "
    "and I don't clean rooms that don't pay rent."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
