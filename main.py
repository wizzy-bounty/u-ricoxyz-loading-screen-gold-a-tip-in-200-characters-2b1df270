import os
from pathlib import Path

def entry_text():
    return "Tip: When every test passes instantly, ask what your agent mocked. It may have replaced the database, the clock, and the problem."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
