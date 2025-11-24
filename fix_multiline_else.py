#!/usr/bin/env python3
"""Fix multi-line else: patterns"""
import re
from pathlib import Path

for bayan_file in Path('.').rglob('*.bayan'):
    with open(bayan_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix else:\n{ pattern (multiline)
    content = re.sub(r'\belse\s*:\s*\n(\s*)\{', r'else {\n\1', content, flags=re.MULTILINE)
    
    with open(bayan_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("✅ Fixed multi-line else: patterns")
