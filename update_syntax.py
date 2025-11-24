#!/usr/bin/env python3
"""
Script to update Bayan syntax from old style to new style:
  Old: if condition: { }
  New: if (condition) { }
  
Also handles: while, for, elif
Does NOT change: def, class, try, except, else, finally, with
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple

def update_bayan_syntax(content: str) -> Tuple[str, int]:
    """
    Update Bayan code syntax from old to new style.
    Returns: (updated_content, number_of_changes)
    """
    original = content
    changes = 0
    
    # Pattern 1: if/elif with condition followed by colon and brace
    # Match: if <condition>: {
    # Replace: if (<condition>) {
    # Use lookahead to ensure we have :\s*\{
    pattern_if = r'\b(if|elif)\s+(.+?):\s*\{'
    
    def replace_if(match):
        nonlocal changes
        keyword = match.group(1)  # 'if' or 'elif'
        condition = match.group(2).strip()
        changes += 1
        return f'{keyword} ({condition}) {{'
    
    content = re.sub(pattern_if, replace_if, content)
    
    # Pattern 2: while with condition followed by colon and brace
    # Match: while <condition>: {
    # Replace: while (<condition>) {
    pattern_while = r'\bwhile\s+(.+?):\s*\{'
    
    def replace_while(match):
        nonlocal changes
        condition = match.group(1).strip()
        changes += 1
        return f'while ({condition}) {{'
    
    content = re.sub(pattern_while, replace_while, content)
    
    # Pattern 3: for loop
    # Match: for <var> in <iterable>: {
    # Replace: for <var> in (<iterable>) {
    pattern_for = r'\bfor\s+(\w+)\s+in\s+(.+?):\s*\{'
    
    def replace_for(match):
        nonlocal changes
        var = match.group(1)
        iterable = match.group(2).strip()
        changes += 1
        return f'for {var} in ({iterable}) {{'
    
    content = re.sub(pattern_for, replace_for, content)
    
    return content, changes


def update_file(filepath: Path, dry_run: bool = False) -> Tuple[bool, int]:
    """
    Update a single file.
    Returns: (was_modified, number_of_changes)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        updated_content, changes = update_bayan_syntax(original_content)
        
        if changes > 0:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ Updated {filepath} ({changes} changes)")
            else:
                print(f"🔍 Would update {filepath} ({changes} changes)")
            return True, changes
        else:
            if dry_run:
                print(f"⏭️  No changes needed for {filepath}")
            return False, 0
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False, 0


def find_bayan_files(root_dir: Path) -> List[Path]:
    """Find all .bayan files in the directory tree."""
    return list(root_dir.rglob('*.bayan'))


def find_markdown_files(root_dir: Path) -> List[Path]:
    """Find all .md files in the directory tree."""
    # Focus on documentation directories
    doc_dirs = [
        root_dir / 'docs',
        root_dir / 'docs' / 'تعليمية',
    ]
    
    md_files = []
    for doc_dir in doc_dirs:
        if doc_dir.exists():
            md_files.extend(doc_dir.rglob('*.md'))
    
    # Also check root README files
    for readme in ['README.md', 'README_AR.md', 'QUICKSTART.md']:
        readme_path = root_dir / readme
        if readme_path.exists():
            md_files.append(readme_path)
    
    return md_files


def update_markdown_syntax(content: str) -> Tuple[str, int]:
    """
    Update Bayan code blocks inside markdown files.
    Only updates code inside ```bayan ... ``` blocks.
    """
    changes = 0
    
    # Find all bayan code blocks
    pattern = r'(```bayan\s*\n)(.*?)(```)'
    
    def replace_code_block(match):
        nonlocal changes
        prefix = match.group(1)
        code = match.group(2)
        suffix = match.group(3)
        
        updated_code, block_changes = update_bayan_syntax(code)
        changes += block_changes
        
        return prefix + updated_code + suffix
    
    content = re.sub(pattern, replace_code_block, content, flags=re.DOTALL)
    
    return content, changes


def update_markdown_file(filepath: Path, dry_run: bool = False) -> Tuple[bool, int]:
    """Update a markdown file with Bayan code blocks."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        updated_content, changes = update_markdown_syntax(original_content)
        
        if changes > 0:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ Updated {filepath} ({changes} changes)")
            else:
                print(f"🔍 Would update {filepath} ({changes} changes)")
            return True, changes
        else:
            if dry_run:
                print(f"⏭️  No changes needed for {filepath}")
            return False, 0
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False, 0


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Update Bayan syntax from old to new style'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without making changes'
    )
    parser.add_argument(
        '--bayan-only',
        action='store_true',
        help='Only update .bayan files, skip markdown'
    )
    parser.add_argument(
        '--docs-only',
        action='store_true',
        help='Only update documentation files'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Root directory to search (default: current directory)'
    )
    
    args = parser.parse_args()
    
    root_dir = Path(args.directory).resolve()
    
    if not root_dir.exists():
        print(f"❌ Directory not found: {root_dir}")
        sys.exit(1)
    
    print(f"🔍 Searching for files in: {root_dir}\n")
    
    if args.dry_run:
        print("🌵 DRY RUN MODE - No files will be modified\n")
    
    total_files = 0
    total_changes = 0
    
    # Update .bayan files
    if not args.docs_only:
        bayan_files = find_bayan_files(root_dir)
        print(f"📝 Found {len(bayan_files)} .bayan files\n")
        
        for filepath in sorted(bayan_files):
            modified, changes = update_file(filepath, args.dry_run)
            if modified:
                total_files += 1
                total_changes += changes
    
    # Update markdown files
    if not args.bayan_only:
        print("\n" + "="*60)
        md_files = find_markdown_files(root_dir)
        print(f"📚 Found {len(md_files)} documentation files\n")
        
        for filepath in sorted(md_files):
            modified, changes = update_markdown_file(filepath, args.dry_run)
            if modified:
                total_files += 1
                total_changes += changes
    
    # Summary
    print("\n" + "="*60)
    print(f"\n✨ Summary:")
    print(f"   Files modified: {total_files}")
    print(f"   Total changes: {total_changes}")
    
    if args.dry_run:
        print(f"\n💡 Run without --dry-run to apply changes")
    else:
        print(f"\n✅ All updates completed successfully!")


if __name__ == '__main__':
    main()
