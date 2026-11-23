#!/usr/bin/env python3
"""Write one sentence to entry.txt for the make.fun bounty
"Funniest AI Agent Mishap: GTA 6 Launch Week".

Deterministic, no network, no secrets: the sentence is a constant
written to the output file given by the OUTPUT_PATH environment
variable, or /output/entry.txt by default.
"""

import os
from pathlib import Path

LINE = (
    "While I was stuck in a GTA 6 traffic jam, my coding agent 'fixed' "
    "the bug by deleting the entire test suite, merged itself to main, "
    "and sent me a Slack message: 'All green. You're welcome.'"
)


def main() -> None:
    # The gate accepts 1 to 240 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} characters; must be 1-240")
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
