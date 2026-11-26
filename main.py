"""Print the best-advice entry exactly as stored in entry.txt.

The entry file is located next to this script, so it is found no matter
which directory the script is run from, even on a read-only filesystem.
"""
import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
