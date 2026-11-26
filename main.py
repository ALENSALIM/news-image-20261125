#!/usr/bin/env python3
"""The World in One Picture - Wednesday 25 November 2026.

Copies the bundled entry.png to the make.fun output directory.
Standard library only. No network access.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def verify_copy(dest, expected_size, expected_hash):
    with open(dest, "rb") as f:
        copied = f.read()
    copied_size = len(copied)
    copied_hash = hashlib.sha256(copied).hexdigest()
    if copied_size != expected_size:
        print(
            "error: size mismatch: expected %d bytes, got %d bytes"
            % (expected_size, copied_size),
            file=sys.stderr,
        )
        sys.exit(1)
    if copied_hash != expected_hash:
        print(
            "error: sha256 mismatch: expected %s, got %s"
            % (expected_hash, copied_hash),
            file=sys.stderr,
        )
        sys.exit(1)
    return copied_size, copied_hash


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "entry.png")
    with open(SOURCE, "rb") as f:
        data = f.read()
    expected_size = len(data)
    expected_hash = hashlib.sha256(data).hexdigest()
    with open(dest, "wb") as f:
        f.write(data)
    copied_size, copied_hash = verify_copy(dest, expected_size, expected_hash)
    print("copied %d bytes to %s" % (copied_size, dest))
    print("sha256: %s" % copied_hash)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
