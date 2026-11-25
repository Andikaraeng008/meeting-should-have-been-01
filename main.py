#!/usr/bin/env python3
"""Write the one-line entry to output/entry.txt.

The entry is a single joke about a meeting that should have been an email:
the meeting's only decision was to produce the very email it replaced.
"""

import os
from pathlib import Path

LINE = "The agenda had twelve items, the meeting lasted two hours, and the only thing we actually finished was the coffee — which, unlike the meeting, had a point."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {out}")


if __name__ == "__main__":
    main()
