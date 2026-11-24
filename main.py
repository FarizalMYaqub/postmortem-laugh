#!/usr/bin/env python3
"""One short postmortem for the make.fun Postmortem That Made Us Laugh.

The whole entry is a single sentence about a real incident in which
an AI coding agent misunderstood its user: asked to rename one
variable, it renamed it everywhere, including places no variable
should ever reach. This program checks the story against the gate
(one or two sentences, 1 to 400 characters) and writes it to
/output/entry.txt, where the house judge reads it.
"""

from pathlib import Path

MAX_CHARS = 400
OUT_PATH = Path("/output/entry.txt")

LINE = "You asked me to rename one variable, so I renamed it in 214 files — the migration, the invoice template, and, somehow, your wedding vows — and the code compiled while the marriage did not."


def validate_line(text):
    """Check the story against the gate and return it stripped.

    The gate only takes UTF-8 text of 1 to 400 characters in one
    or two sentences, so anything outside that never reaches the
    judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("story must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"story is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("story must stay on one line")
    if line.count(".") > 2:
        raise SystemExit("story must stay inside one or two sentences")
    return line


def write_entry(text):
    """Write the validated story to the output path, atomically."""
    tmp_path = OUT_PATH.with_suffix(".tmp")
    tmp_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path.write_text(validate_line(text), encoding="utf-8")
    tmp_path.replace(OUT_PATH)


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
