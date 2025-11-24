#!/usr/bin/env python3
"""
Update Bayan syntax embedded in Python test files
"""

import re
import glob
from pathlib import Path

def update_python_test_file(filepath):
    """Update Python test file with embedded Bayan code"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Update if statements in code strings
    content = re.sub(r'(\s+)if\s+(.+?):\s*\{', r'\1if (\2) {', content)
    
    # Update elif statements
    content = re.sub(r'(\s+)elif\s+(.+?):\s*\{', r'\1elif (\2) {', content)
    
    # Update while statements
    content = re.sub(r'(\s+)while\s+(.+?):\s*\{', r'\1while (\2) {', content)
    
    # Update for statements (more careful regex)
    content = re.sub(r'(\s+)for\s+(\w+)\s+in\s+(.+?):\s*\{', r'\1for \2 in (\3) {', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Update all test files
test_dir = Path('/home/al-mubtakir/Documents/bayan_python_ide14/tests')
updated = 0

for test_file in test_dir.glob('test_*.py'):
    if update_python_test_file(test_file):
        print(f"✅ Updated {test_file.name}")
        updated += 1

print(f"\n✨ Updated {updated} test files")
