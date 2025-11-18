#!/usr/bin/env python3
import sys
import tokenize
from io import BytesIO
from pathlib import Path
import re

ASCII_IDENT_RE = re.compile(rb"^[A-Za-z_][A-Za-z0-9_]*$")


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = path.read_bytes()
    except Exception:
        return errors

    try:
        for tok in tokenize.tokenize(BytesIO(data).readline):
            if tok.type == tokenize.NAME:
                text = tok.string.encode('utf-8')
                # Skip dunder and common builtins
                if text.startswith(b'__') and text.endswith(b'__'):
                    continue
                # Enforce purely ASCII identifier characters
                if not ASCII_IDENT_RE.match(text):
                    errors.append(f"{path}:{tok.start[0]} Non-English identifier: {tok.string}")
    except tokenize.TokenError:
        # Skip files that fail to tokenize
        return errors
    return errors


def main(paths):
    problems: list[str] = []
    for p in paths:
        path = Path(p)
        if not path.is_file():
            continue
        if path.suffix != '.py':
            continue
        # Scope limited to nlp_bayan only; pre-commit 'files:' should also filter
        if 'nlp_bayan' not in path.parts:
            continue
        problems.extend(check_file(path))

    if problems:
        sys.stderr.write("English-only identifier violations (nlp_bayan/*.py):\n")
        for line in problems:
            sys.stderr.write(line + "\n")
        sys.stderr.write("\nTip: Use English-only letters/digits/underscore for Python identifiers in nlp_bayan/.\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

