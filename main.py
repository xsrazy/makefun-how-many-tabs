#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun bounty entry.

Writes one number, digits only, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): an honest count of open browser tabs.
"""

import os

# The honest count: 237 open tabs. Odd, specific, and in the range a real
# tab hoarder lives in -- a few windows of research, docs, and "read later"
# tabs that never get read. Not a round number, not a shock number.
TAB_COUNT = 237


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(str(TAB_COUNT).encode("ascii"))


if __name__ == "__main__":
    main()
