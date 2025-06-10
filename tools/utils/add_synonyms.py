#!/usr/bin/env python3
"""
Add APL symbol synonyms to markdown files.

This script processes all .md files in a directory (non-recursively) and:
1. Finds the first <h1> tag
2. Checks if it has a <span class="command"> child
3. Extracts any non-alphanumeric symbol from that span
4. Adds a hidden div with the symbol at the beginning of the file
"""

import os
import sys
import argparse
import re
from bs4 import BeautifulSoup


def extract_apl_symbol(html_content):
    """
    Extract APL symbol from the first h1 tag with a command span.
    
    Returns the symbol if found, None otherwise.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first h1 tag
    h1 = soup.find('h1')
    if not h1:
        return None
    
    # Check if h1 has a span with class "command"
    command_span = h1.find('span', class_='command')
    if not command_span:
        return None
    
    # Get the text content
    command_text = command_span.get_text()
    
    # Characters to ignore
    ignore_chars = set('{}()[]\'"\' ')
    
    # Extract non-alphanumeric symbols (excluding the ignore list)
    symbols = []
    for char in command_text:
        if not char.isalnum() and char not in ignore_chars:
            symbols.append(char)
    
    # Return the last symbol found (if any)
    if symbols:
        return symbols[-1]
    
    return None


def process_file(filepath, dry_run=False):
    """
    Process a single markdown file.
    
    Returns True if the file was modified (or would be modified in dry-run), False otherwise.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file already has the hidden div
    if content.startswith('<div style="display: none;">'):
        print(f"  Skipping {os.path.basename(filepath)} - already has hidden div")
        return False
    
    # Extract the APL symbol
    symbol = extract_apl_symbol(content)
    
    if symbol:
        if dry_run:
            print(f"  Would add symbol '{symbol}' to {os.path.basename(filepath)}")
        else:
            # Create the hidden div
            hidden_div = f'<div style="display: none;">\n  {symbol}\n</div>\n\n'
            
            # Add the div to the beginning of the file
            new_content = hidden_div + content
            
            # Write the modified content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  Added symbol '{symbol}' to {os.path.basename(filepath)}")
        return True
    else:
        print(f"  No APL symbol found in {os.path.basename(filepath)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Add APL symbol synonyms to markdown files'
    )
    parser.add_argument(
        'directory',
        help='Directory containing markdown files to process'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Only list files that would be modified without making changes'
    )
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory")
        sys.exit(1)
    
    # Get all .md files in the directory (non-recursive)
    md_files = [
        os.path.join(args.directory, f)
        for f in os.listdir(args.directory)
        if f.endswith('.md') and os.path.isfile(os.path.join(args.directory, f))
    ]
    
    if not md_files:
        print(f"No .md files found in {args.directory}")
        return
    
    if args.dry_run:
        print(f"DRY RUN: Checking {len(md_files)} markdown files in {args.directory}...")
    else:
        print(f"Processing {len(md_files)} markdown files in {args.directory}...")
    
    modified_count = 0
    for filepath in md_files:
        if process_file(filepath, dry_run=args.dry_run):
            modified_count += 1
    
    if args.dry_run:
        print(f"\nDRY RUN Complete! Would modify {modified_count} files.")
    else:
        print(f"\nComplete! Modified {modified_count} files.")


if __name__ == '__main__':
    main()