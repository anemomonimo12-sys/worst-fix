#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one commit-message line for a bug fix that made everything worse
to /output/entry.txt, and validates the gate: UTF-8 text, 1-100
characters, a single line, not only whitespace.
"""
import os

LINE = "fix: silence the warning - it was warning us about this fix"

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry is {len(line)} characters, must be 1-100")


def main() -> int:
    validate(LINE)
    # Confirm the line round-trips as UTF-8.
    LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
