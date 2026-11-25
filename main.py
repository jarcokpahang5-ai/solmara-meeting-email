#!/usr/bin/env python3
"""One-line joke entry for make.fun bounty
'The Meeting That Should Have Been an Email'.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the chosen line to /output/entry.txt and prints it to stdout.
"""

import os

LINE = (
    "This meeting could've been an email \u2014 instead, twelve people "
    "spent 45 minutes watching one guy read it out loud."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
