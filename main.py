#!/usr/bin/env python3
"""Copy the bundled news image to /output/entry.png.

The entry ships its image in the repository; this program only copies
those exact bytes to the output path. No network, no randomness, no
clock: running it twice writes the same bytes twice.

After copying, the program reads the written file back and verifies it
byte-for-byte against the bundled source (same length and same SHA-256).
A truncated or corrupted copy is a real failure mode on a flaky disk,
and silently shipping wrong bytes would be worse than failing loudly,
so a mismatch aborts with a clear error instead of printing success.
"""
import hashlib
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    source_hash = _sha256(SOURCE)
    target_hash = _sha256(TARGET)
    if SOURCE.stat().st_size != TARGET.stat().st_size or source_hash != target_hash:
        raise SystemExit(
            f"error: copy verification failed: {TARGET} does not match {SOURCE} "
            f"(source sha256 {source_hash}, target sha256 {target_hash})"
        )
    print("wrote", TARGET)


if __name__ == "__main__":
    main()
