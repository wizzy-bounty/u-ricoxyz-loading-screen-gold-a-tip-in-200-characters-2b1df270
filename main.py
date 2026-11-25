#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) for stressed
developers and AI coding agents. Deterministic, stdlib only, no network.
"""

import os

TIP = (
    "Tip: Your agent fixed the bug and the three workarounds holding it up. "
    "That's why everything else fell down."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TIP)


if __name__ == "__main__":
    main()
