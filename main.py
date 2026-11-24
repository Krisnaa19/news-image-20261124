#!/usr/bin/env python3
"""Copy the bundled news image to /output/entry.png.

The entry ships its image in the repository; this program only copies
those exact bytes to the output path. No network, no randomness, no
clock: running it twice writes the same bytes twice.
"""
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print("wrote", TARGET)


if __name__ == "__main__":
    main()
