# Bayan Syntax Clarification & Converter Tool

## Summary

This document clarifies the correct Bayan syntax and provides a conversion tool for any legacy Python-style code.

## Correct Bayan Syntax

### Functions and Classes
```bayan
def function_name(params): {
    body
}

class ClassName: {
    body
}
```

**Important:** The colon `:` after function/class signatures is **REQUIRED** by Bayan!

### Control Structures
```bayan
if (condition) {
    body
}

while (condition) {
    body
}

for (var in iterable) {
    body
}
```

## Bayan is a Hybrid Language

Bayan combines the best of both worlds:
- **Colons** (like Python) after function/class signatures
- **Braces** (like C/Java) for code blocks
- **Parentheses** around conditions in control structures

This is **by design**, not a bug!

## Syntax Converter Tool

For any legacy files using pure Python syntax, use `convert_syntax.py`:

```bash
# Convert single file
python convert_syntax.py examples/myfile.by

# Convert all files
python convert_syntax.py --all
```

The tool:
- Converts Python-style indentation to braces
- Creates backups before conversion
- Skips files already using correct syntax

## Quick Reference

| Element | Correct Bayan Syntax | Wrong Python Syntax |
|---------|---------------------|---------------------|
| Function | `def f(x): { ... }` | `def f(x):\n    ...` |
| Class | `class C: { ... }` | `class C:\n    ...` |
| If | `if (x > 5) { ... }` | `if x > 5:\n    ...` |
| While | `while (i < 10) { ... }` | `while i < 10:\n    ...` |
| For | `for (i in range(5)) { ... }` | `for i in range(5):\n    ...` |

## See Also

- `convert_syntax.py` - Syntax conversion tool
- `SYNTAX_INCONSISTENCY_REPORT.md` - Detailed analysis
