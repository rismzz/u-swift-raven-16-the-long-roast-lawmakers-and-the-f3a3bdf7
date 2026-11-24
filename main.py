#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert —
writes the roast to /output/entry.txt.

The roast is embedded as a literal: deterministic, no randomness,
no network. It must be a single satirical sentence.

The roast: lawmakers who confidently regulate algorithms they have
never run, yet cannot convert a file to PDF — so the future of AI
suddenly depends on a staffer named Greg. The gap between the power
claimed and the competence shown is the whole joke.
"""

import os

LINE = (
    "They can regulate an algorithm they have never run, but ask "
    "them to convert a file to PDF and suddenly the future of AI "
    "rests on a staffer named Greg."
)


def main() -> None:
    # No trailing newline: a single satirical sentence.
    assert LINE.strip(), "roast must not be only whitespace"
    assert "\n" not in LINE, "roast must be a single sentence on one line"
    assert LINE.count(".") == 1, "roast must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
