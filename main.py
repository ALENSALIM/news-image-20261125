"""Entry point: write the front page image to /output/entry.png.

Clears only the files inside the output folder (never the folder
itself), because the grader runs this as sandbox user 65534.
"""

import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import draw  # noqa: E402


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    out_path = os.path.join(out_dir, "entry.png")
    img = draw.build_image()
    assert img.size == (1024, 1024), img.size
    img.save(out_path, format="PNG")
    with open(out_path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    size = os.path.getsize(out_path)
    print("wrote %s (%d bytes, sha256 %s)" % (out_path, size, digest))
    assert size <= 1024 * 1024, size
    return 0


if __name__ == "__main__":
    sys.exit(main())
