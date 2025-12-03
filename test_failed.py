#!/usr/bin/env python3
"""Test failed demo files."""

import sys
import os
sys.path.insert(0, '.')

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

# Test all demo files
pass_count = 0
fail_count = 0
failed_files = []

for demo in sorted(os.listdir('examples')):
    if not demo.endswith('.by'):
        continue
    demo_path = f'examples/{demo}'
    try:
        with open(demo_path, 'r') as f:
            code = f.read()
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        pass_count += 1
    except Exception as e:
        fail_count += 1
        failed_files.append((demo_path, str(e)))

print(f"PASS: {pass_count}")
print(f"FAIL: {fail_count}")
print()
if failed_files:
    print("Failed files:")
    for path, error in failed_files:
        print(f"  {path}: {error}")

