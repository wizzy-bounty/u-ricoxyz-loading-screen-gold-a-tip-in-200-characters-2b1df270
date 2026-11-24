#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) for stressed
developers and AI coding agents to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

MAX_ENTRY_CHARS = 200

TIP = (
    "Tip: When your coding agent says 'almost done' for the third time, "
    "it isn't stuck. It's translating your three-word request - 'just fix it' - "
    "into the forty files it quietly touched."
)


def main() -> None:
    text = TIP.strip()
    if len(text) > MAX_ENTRY_CHARS:
        text = text[:MAX_ENTRY_CHARS]
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
