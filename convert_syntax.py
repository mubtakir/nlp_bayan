#!/usr/bin/env python3
"""
Python to Bayan Syntax Converter
=================================

Converts Python-style syntax (colons + indentation) to Bayan syntax (braces).

Usage:
    python convert_syntax.py <file.by>
    python convert_syntax.py --all  # Convert all .by and .bayan files
"""

import re
import sys
import os
from pathlib import Path


def convert_line(line, indent_level):
    """Convert a single line from Python to Bayan syntax"""
    stripped = line.lstrip()
    current_indent = len(line) - len(stripped)
    
    # Check if line ends with colon (control structure)
    if stripped and stripped.rstrip().endswith(':'):
        # Remove colon and add opening brace
        converted = line.rstrip()[:-1].rstrip() + ' {\n'
        return converted, current_indent // 4, True  # Assuming 4-space indent
    
    return line, indent_level, False


def convert_file_content(content):
    """Convert entire file content from Python to Bayan syntax"""
    lines = content.split('\n')
    result = []
    indent_stack = [0]  # Stack to track indentation levels
    brace_lines = []  # Lines that opened braces
    
    for i, line in enumerate(lines):
        # Skip empty lines and comments
        if not line.strip() or line.strip().startswith('#'):
            result.append(line)
            continue
        
        stripped = line.lstrip()
        current_indent = len(line) - len(stripped)
        
        # Check if we need to close braces (dedent)
        while len(indent_stack) > 1 and current_indent < indent_stack[-1]:
            indent_stack.pop()
            brace_lines.pop()
            # Add closing brace with proper indentation
            result.append(' ' * indent_stack[-1] + '}')
        
        # Check if line ends with colon
        if stripped.rstrip().endswith(':'):
            # Remove colon and add opening brace
            converted = line.rstrip()[:-1].rstrip() + ' {'
            result.append(converted)
            # Push new indent level
            indent_stack.append(current_indent + 4)
            brace_lines.append(i)
        else:
            result.append(line)
    
    # Close any remaining open braces
    while len(indent_stack) > 1:
        indent_stack.pop()
        result.append(' ' * indent_stack[-1] + '}')
    
    return '\n'.join(result)


def convert_file(filepath):
    """Convert a single file"""
    print(f"Converting: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already uses braces
        if '{' in content and '}' in content:
            print(f"  ⚠️  File already uses braces, skipping...")
            return False
        
        converted = convert_file_content(content)
        
        # Backup original file
        backup_path = str(filepath) + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Write converted content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f"  ✅ Converted successfully (backup: {backup_path})")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def convert_all_files(directory='examples'):
    """Convert all .by and .bayan files in directory"""
    converted_count = 0
    skipped_count = 0
    error_count = 0
    
    for ext in ['*.by', '*.bayan']:
        for filepath in Path(directory).rglob(ext):
            result = convert_file(filepath)
            if result is True:
                converted_count += 1
            elif result is False:
                skipped_count += 1
            else:
                error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion Summary:")
    print(f"  ✅ Converted: {converted_count}")
    print(f"  ⚠️  Skipped: {skipped_count}")
    print(f"  ❌ Errors: {error_count}")
    print(f"{'='*60}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python convert_syntax.py <file.by>")
        print("  python convert_syntax.py --all")
        sys.exit(1)
    
    if sys.argv[1] == '--all':
        convert_all_files()
    else:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        convert_file(filepath)


if __name__ == '__main__':
    main()
