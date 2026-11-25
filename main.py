#!/usr/bin/env python3
"""Write the one-line entry to output/entry.txt.

The entry is a single joke about a meeting that should have been an email:
the meeting's only decision was to produce the very email it replaced.
"""

from pathlib import Path

LINE = "The meeting's only decision was to send an email summarising the meeting that should have been an email."


def main() -> None:
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {out}")


if __name__ == "__main__":
    main()
