#!/usr/bin/env python3
"""news-image-20261119: emit the front page for 19 November 2026.

The image is baked into the repository as entry.png; this program only
places an exact copy at $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Two runs always produce identical bytes: the file is copied verbatim,
with no timestamps, randomness, or network access involved.
"""
from pathlib import Path
import os
import sys

IMAGE_NAME = "entry.png"


def run() -> int:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print(f"missing {IMAGE_NAME} beside {__file__}", file=sys.stderr)
        return 1
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME
    data = source.read_bytes()
    target.write_bytes(data)
    # Confirm the copy is complete: a short write must fail loudly
    # instead of handing the grader a truncated image.
    if target.stat().st_size != len(data):
        print(f"short write copying {IMAGE_NAME}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
