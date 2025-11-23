#!/usr/bin/env python3
"""
Script to automatically fix Bayan syntax by adding braces to function and class definitions.
Converts Python-style indentation to Bayan-style braces.
"""

import os
import re
import sys

def fix_bayan_file(filepath):
    """Fix a single .bayan file by adding braces to def/class blocks."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    i = 0
    changes_made = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a def or class line without braces
        if re.match(r'^(def |class )', line) and line.rstrip().endswith(':') and '{' not in line:
            # This needs fixing
            # Add opening brace
            fixed_line = line.rstrip() + ' {\n'
            fixed_lines.append(fixed_line)
            changes_made += 1
            
            # Find the indentation level
            indent = len(line) - len(line.lstrip())
            
            # Process the body
            i += 1
            body_lines = []
            
            while i < len(lines):
                next_line = lines[i]
                
                # Skip empty lines
                if next_line.strip() == '':
                    body_lines.append(next_line)
                    i += 1
                    continue
                
                # Check indentation
                next_indent = len(next_line) - len(next_line.lstrip())
                
                # If dedented or same level, end of block
                if next_indent <= indent and next_line.strip():
                    break
                
                body_lines.append(next_line)
                i += 1
            
            # Add body lines
            fixed_lines.extend(body_lines)
            
            # Add closing brace
            fixed_lines.append(' ' * indent + '}\n')
            changes_made += 1
            
        else:
            fixed_lines.append(line)
            i += 1
    
    if changes_made > 0:
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)
        return changes_made
    
    return 0

def main():
    """Main function to fix all .bayan files in the project."""
    
    project_root = '/home/al-mubtakir/Documents/bayan_python_ide14'
    
    # Priority directories
    priority_dirs = [
        'bayan/core',
        'nlp_bayan',
        'examples',
    ]
    
    total_files = 0
    total_changes = 0
    
    for priority_dir in priority_dirs:
        dir_path = os.path.join(project_root, priority_dir)
        
        if not os.path.exists(dir_path):
            continue
        
        print(f"\n🔍 Processing: {priority_dir}/")
        
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.bayan'):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, project_root)
                    
                    try:
                        changes = fix_bayan_file(filepath)
                        if changes > 0:
                            print(f"  ✅ {rel_path}: {changes} fixes")
                            total_files += 1
                            total_changes += changes
                        else:
                            print(f"  ⏭️  {rel_path}: already correct")
                    except Exception as e:
                        print(f"  ❌ {rel_path}: ERROR - {e}")
    
    print(f"\n{'='*60}")
    print(f"✨ Summary:")
    print(f"   Files fixed: {total_files}")
    print(f"   Total changes: {total_changes}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
