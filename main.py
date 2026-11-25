#!/usr/bin/env python3
"""One-line laugh entry for make.fun.

Writes the single joke line to /output/entry.txt. Standard library
only, no network, no clock, no randomness: byte-identical output.
"""

import os

TEXT = "My savings account is just a checking account with commitment issues."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
