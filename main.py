#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short funny rant about a specific everyday annoyance
(the self-checkout machine) to /output/entry.txt. Deterministic:
same output on every run.
"""

import os

RANT = (
    'The self-checkout machine accused me of stealing my own groceries. '
    '"Unexpected item in the bagging area." '
    "It's a bag of rice. It weighs what rice weighs. "
    "Now a red light blinks at me while the teenager with the keycard "
    "strolls over at the speed of continental drift."
)


def main() -> None:
    # Gate: the scorer only accepts 1-400 characters of non-whitespace UTF-8.
    text = RANT
    if not (1 <= len(text) <= 400) or not text.strip():
        raise ValueError(f"rant is {len(text)} chars, must be 1-400 non-blank")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
