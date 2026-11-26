#!/usr/bin/env python3
"""Write a one-line museum placard for an office artifact to /output/entry.txt."""

import os

TITLE = "Potted ficus, c. 2019, ceramic."
BODY = (
    "The last survivor of the open-plan era, "
    "watered each Friday by a rotating order of interns."
)
CREDIT = "Gift of Facilities Management."

MAX_CHARS = 280


def build_line() -> str:
    return " ".join([TITLE, BODY, CREDIT])


def main() -> None:
    line = build_line()
    if len(line) > MAX_CHARS:
        raise ValueError(f"placard too long: {len(line)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
