#!/usr/bin/env python3
import sys
from pathlib import Path

# Allow common whitespace characters
_ALLOWED = {"\n", "\r", "\t"}

# Unicode categories for control/format are typically non-printable.
# We will treat characters with codepoint < 32 or in [127, 159] as non-printable,
# plus ZERO WIDTH chars and BOM explicitly.
_ZERO_WIDTH = {
    "\u200B",  # ZERO WIDTH SPACE
    "\u200C",  # ZERO WIDTH NON-JOINER
    "\u200D",  # ZERO WIDTH JOINER
    "\uFEFF",  # ZERO WIDTH NO-BREAK SPACE (BOM)
}


def has_non_printable(text: str) -> bool:
    for ch in text:
        o = ord(ch)
        if ch in _ALLOWED:
            continue
        if ch in _ZERO_WIDTH:
            return True
        if o < 32 or 127 <= o <= 159:
            return True
    return False


def main(paths):
    bad = []
    for p in paths:
        try:
            data = Path(p).read_text(encoding="utf-8")
        except Exception:
            # Binary or unreadable; skip (pre-commit 'types: [text]' should avoid these anyway)
            continue
        if has_non_printable(data):
            bad.append(p)
    if bad:
        sys.stderr.write("Found non-printable/control characters in:\n")
        for b in bad:
            sys.stderr.write(f" - {b}\n")
        sys.stderr.write("\nTip: remove zero-width/BOM and invisible controls. Re-save file as UTF-8 without BOM.\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

