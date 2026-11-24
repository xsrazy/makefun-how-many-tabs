#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun bounty entry.

Writes one number, digits only, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): an honest count of open browser tabs.
"""

import os

TAB_COUNT = 184


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(str(TAB_COUNT).encode("ascii"))


if __name__ == "__main__":
    main()
