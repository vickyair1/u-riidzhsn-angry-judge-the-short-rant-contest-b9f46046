#!/usr/bin/env python3
"""Angry Judge round 2 — entry program.

Writes one short rant to /output/entry.txt. Deterministic:
same output on every run, no randomness, no network.
"""

import os

RANT = (
    "The shower was perfect for exactly forty seconds. "
    "Then it went ice-cold the second I got shampoo in my eyes, "
    "and by the time I could see again it was lava. "
    "I have been betrayed by people slower than that."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-400 chars of non-whitespace UTF-8.
    text = RANT
    if not (1 <= len(text) <= 400) or not text.strip():
        raise ValueError(f"rant is {len(text)} chars, must be 1-400 non-blank")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
