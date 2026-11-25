#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
outside the grader). Standard library only, no network.
"""

import os

TEXT = (
    "Eleven stuffed animals arranged around my son \"so nobody's lonely,\" "
    "then he whispers, \"Dad, stay till the owl blinks.\" "
    "The owl is plastic. I stay till the owl blinks."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
