#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the exact entry line to /output/entry.txt (UTF-8), then reads it
back and asserts the round trip is byte-identical.
"""

from pathlib import Path

ENTRY = (
    "I missed the deadline because I spent all afternoon training a model "
    "to predict when I'd finish \u2014 and it predicted yesterday."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    round_trip = OUTPUT_PATH.read_text(encoding="utf-8")
    assert round_trip == ENTRY, "round-trip mismatch"
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
