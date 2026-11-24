#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to entry.txt.

Deterministic: no randomness, no network, no input. The same haiku is
written on every run, byte for byte.
"""

import os

ENTRY = (
    "Works on my machine\n"
    "fails in production nightly\n"
    "the clock was the bug"
)

# Bounty gate: the entry text must be 1-200 characters. Fail loudly
# instead of writing an entry the judge would reject outright.
MAX_ENTRY_CHARS = 200


def main() -> None:
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise SystemExit(
            f"entry too long: {len(ENTRY)} chars (max {MAX_ENTRY_CHARS})"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; tolerate a trailing file path.
    if output_dir.endswith("entry.txt"):
        output_dir = os.path.dirname(output_dir) or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
