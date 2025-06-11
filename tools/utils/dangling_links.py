import os
import re
import argparse
from pathlib import Path
from urllib.parse import urlparse, unquote
from ruamel.yaml import YAML

def is_external_link(url):
    """Check if a URL is external (starts with http/https)."""
    return url.startswith(('http://', 'https://'))

def parse_mkdocs_nav(mkdocs_file, base_dir, root_dir=None, subsites=None, target_subsite=None, debug=False, collect_subsites_only=False):
    """Parse the navigation section of mkdocs.yml to extract all markdown files to check."""
    markdown_files = []
    
    # If root_dir is not provided, use base_dir
    if root_dir is None:
        root_dir = base_dir
    
    # Track subsites
    if subsites is None:
        subsites = {}
    
    try:
        # Create a YAML parser that can handle custom tags
        yaml = YAML()
        yaml.preserve_quotes = True
        
        # Load the mkdocs.yml file
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            mkdocs_config = yaml.load(f)
        
        if not mkdocs_config or 'nav' not in mkdocs_config:
            if debug:
                print(f"Warning: No 'nav' section found in {mkdocs_file}")
            return markdown_files, subsites
        
        # Extract the markdown files from the nav section
        def extract_files_from_nav(nav_items, current_dir):
            files = []
            
            if isinstance(nav_items, list):
                for item in nav_items:
                    files.extend(extract_files_from_nav(item, current_dir))
            elif isinstance(nav_items, dict):
                for title, path in nav_items.items():
                    if isinstance(path, str):
                        if path.startswith('!include'):
                            # Handle !include directives
                            include_match = re.match(r'!include\s+(.+)', path)
                            if include_match:
                                include_path = include_match.group(1).strip('"\'')
                                # Resolve the include path relative to the current mkdocs.yml directory
                                mkdocs_dir = os.path.dirname(mkdocs_file)
                                included_mkdocs_path = os.path.normpath(os.path.join(mkdocs_dir, include_path))
                                
                                if os.path.exists(included_mkdocs_path):
                                    # Track this subsite
                                    subsite_dir = os.path.dirname(included_mkdocs_path)
                                    subsite_name = os.path.basename(subsite_dir)
                                    
                                    # Always track the subsite for cross-reference resolution
                                    subsite_rel_path = os.path.relpath(subsite_dir, root_dir)
                                    subsites[subsite_name] = subsite_rel_path
                                    
                                    # If we're only collecting subsites info, skip file collection
                                    if collect_subsites_only:
                                        continue
                                        
                                    # If target_subsite is specified, only collect files from that subsite
                                    if target_subsite and subsite_name != target_subsite:
                                        if debug:
                                            print(f"  Skipping !include: {os.path.relpath(included_mkdocs_path, root_dir)} (not target subsite)")
                                        continue
                                    
                                    if debug:
                                        print(f"  Following !include: {os.path.relpath(included_mkdocs_path, root_dir)}")
                                    
                                    # Get the base directory for the included mkdocs.yml
                                    included_base_dir = subsite_dir
                                    # Add 'docs' subdirectory if it exists
                                    docs_dir = os.path.join(included_base_dir, 'docs')
                                    if os.path.exists(docs_dir):
                                        included_base_dir = docs_dir
                                    # Recursively parse the included mkdocs.yml
                                    included_files, _ = parse_mkdocs_nav(included_mkdocs_path, included_base_dir, root_dir, subsites, target_subsite, debug, False)
                                    files.extend(included_files)
                                else:
                                    if debug:
                                        print(f"Warning: !include file not found: {included_mkdocs_path}")
                        elif path.endswith('.md'):
                            # Handle docs/ prefix if present
                            if path.startswith('docs/'):
                                path = path[5:]  # Remove 'docs/' prefix
                            
                            # Add the markdown file to the list
                            full_path = os.path.normpath(os.path.join(current_dir, path))
                            if os.path.exists(full_path):
                                files.append(full_path)
                            else:
                                # Try with 'docs' subdirectory
                                docs_path = os.path.normpath(os.path.join(os.path.dirname(current_dir), 'docs', path))
                                if os.path.exists(docs_path):
                                    files.append(docs_path)
                                else:
                                    if debug:
                                        print(f"Warning: Referenced file not found: {full_path}")
                    else:
                        # Recurse into nested sections
                        files.extend(extract_files_from_nav(path, current_dir))
            
            return files
        
        # Extract markdown files from nav
        if not collect_subsites_only:
            markdown_files = extract_files_from_nav(mkdocs_config['nav'], base_dir)
        
    except Exception as e:
        print(f"Error parsing {mkdocs_file}: {str(e)}")
    
    return markdown_files, subsites


def extract_links_from_markdown(file_path):
    """Extract all markdown links from a file, excluding code blocks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # First, identify code blocks and create a mask to exclude them
        code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
        code_blocks = [(m.start(), m.end()) for m in code_block_pattern.finditer(content)]
        
        # Create a function to check if a position is inside a code block
        def is_in_code_block(pos):
            return any(start <= pos <= end for start, end in code_blocks)
        
        # Pattern to match markdown links [text](url) - more restrictive
        md_link_pattern = re.compile(r'(?<!!)\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)')
        
        # Pattern for HTML links
        html_link_pattern = re.compile(r'<a\s+href=["\'](.*?)["\'].*?>.*?</a>', re.IGNORECASE)
        
        # Find all markdown style links, excluding those in code blocks
        md_links = []
        for match in md_link_pattern.finditer(content):
            if not is_in_code_block(match.start()):
                md_links.append((match.group('text'), match.group('url')))
        
        # Find all HTML style links, excluding those in code blocks
        html_links = []
        for match in html_link_pattern.finditer(content):
            if not is_in_code_block(match.start()):
                html_links.append((None, match.group(1)))
        
        # Combine both types of links
        all_links = md_links + html_links
        
        return all_links
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return []


def validate_links(root_dir, file_path, links, subsites=None, verbose_debug=False):
    """Validate if links are pointing to valid resources."""
    invalid_links = []
    base_dir = os.path.dirname(file_path)
    
    # Determine which subsite the current file belongs to
    current_subsite = None
    rel_file_path = os.path.relpath(file_path, root_dir)
    if subsites:
        for subsite_name, subsite_path in subsites.items():
            if rel_file_path.startswith(subsite_path + os.sep):
                current_subsite = subsite_name
                break
    
    for link_text, link_url in links:
        # Skip external links, anchor links, and mailto links
        if is_external_link(link_url) or link_url.startswith('#') or link_url.startswith('mailto:'):
            continue
        
        # Handle URLs with anchors or query parameters
        url_parts = link_url.split('#')[0].split('?')[0]
        
        # Parse URL and get the path
        parsed_url = urlparse(url_parts)
        path = unquote(parsed_url.path)
        
        
        # Initialize variables to track if we found a valid target
        target_found = False
        checked_paths = []
        
        # Determine the target file path
        if os.path.isabs(path):
            # For absolute paths, resolve from the root directory
            target_path = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
        else:
            # For relative paths, resolve from the current file's directory
            target_path = os.path.normpath(os.path.join(base_dir, path))
        
        # List of possible target paths to check
        paths_to_check = []
        
        # 1. Check the exact path
        paths_to_check.append(target_path)
        
        # 2. If it doesn't end with .md, try adding it
        if not path.endswith('.md'):
            paths_to_check.append(target_path + '.md')
        
        # 3. Check if it's a directory with index.md
        paths_to_check.append(os.path.join(target_path, 'index.md'))
        
        # 4. For paths that look like they might be cross-subsite references,
        # try with 'docs' subdirectory
        if '/' in path and not path.startswith('/'):
            path_parts = target_path.split('/')
            if path_parts and path_parts[0] in subsites:
                subsite_root = os.path.join(root_dir, subsites[path_parts[0]])
                rest_of_path = '/'.join(path_parts[1:])
                docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                paths_to_check.append(docs_path)
                if not rest_of_path.endswith('.md'):
                    paths_to_check.append(docs_path + '.md')
                paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # 4. For MkDocs-style links without extensions
        # MkDocs resolves these differently than filesystem paths
        if not path.endswith('.md') and not path.endswith('/'):
            # For links that go up levels (../)
            if path.startswith('../'):
                # Try resolving as if we're already at the docs root
                # This handles cases where MkDocs flattens the URL structure
                path_parts = path.split('/')
                non_dot_parts = [p for p in path_parts if p != '..']
                if non_dot_parts:
                    # Try from the same directory as current file
                    same_level_path = os.path.join(base_dir, '/'.join(non_dot_parts))
                    paths_to_check.append(same_level_path)
                    paths_to_check.append(same_level_path + '.md')
                    paths_to_check.append(os.path.join(same_level_path, 'index.md'))
                    
                    # Also try from docs root for deeply nested references
                    from_root = os.path.join(root_dir, '/'.join(non_dot_parts))
                    paths_to_check.append(from_root)
                    paths_to_check.append(from_root + '.md')
                    paths_to_check.append(os.path.join(from_root, 'index.md'))
        
        # 5. For cross-subsite references, try different resolution strategies
        if path.startswith('../') and subsites:
            # Count how many levels up we go
            path_parts = path.split('/')
            up_levels = sum(1 for part in path_parts if part == '..')
            remaining_path = '/'.join(part for part in path_parts if part != '..')
            
            # Try resolving from the root of the current subsite
            if current_subsite:
                current_subsite_root = os.path.join(root_dir, subsites[current_subsite])
                subsite_relative_target = os.path.normpath(os.path.join(current_subsite_root, remaining_path))
                paths_to_check.append(subsite_relative_target)
                if not remaining_path.endswith('.md'):
                    paths_to_check.append(subsite_relative_target + '.md')
                paths_to_check.append(os.path.join(subsite_relative_target, 'index.md'))
            
            # Check if it's a cross-subsite reference
            # e.g., ../windows-ui-guide/session-window -> windows-ui-guide/docs/session-window.md
            if remaining_path and '/' in remaining_path:
                potential_subsite = remaining_path.split('/')[0]
                if potential_subsite in subsites:
                    subsite_root = os.path.join(root_dir, subsites[potential_subsite])
                    # Try with 'docs' subdirectory (common pattern)
                    rest_of_path = '/'.join(remaining_path.split('/')[1:])
                    docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                    paths_to_check.append(docs_path)
                    if not rest_of_path.endswith('.md'):
                        paths_to_check.append(docs_path + '.md')
                    paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # 5. Handle absolute paths that might be subsite references
        elif path.startswith('/') and subsites:
            path_parts = path.strip('/').split('/')
            if path_parts and path_parts[0] in subsites:
                potential_subsite = path_parts[0]
                subsite_root = os.path.join(root_dir, subsites[potential_subsite])
                # Try with 'docs' subdirectory
                if len(path_parts) > 1:
                    rest_of_path = '/'.join(path_parts[1:])
                    docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                    paths_to_check.append(docs_path)
                    if not rest_of_path.endswith('.md'):
                        paths_to_check.append(docs_path + '.md')
                    paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # Check all possible paths
        for check_path in paths_to_check:
            checked_paths.append(check_path)
            if os.path.exists(check_path):
                target_found = True
                break
        
        # If still not found, report as invalid
        if not target_found:
            invalid_links.append((link_text, link_url, checked_paths[0] if checked_paths else target_path))
    
    return invalid_links



def check_dangling_links(directory, mkdocs_file=None, target_subsite=None, stats_only=False, debug=False, verbose=False):
    """Check for dangling links in markdown files."""
    
    # Require mkdocs.yml file
    if not mkdocs_file:
        mkdocs_file = os.path.join(directory, 'mkdocs.yml')
    
    if not os.path.exists(mkdocs_file):
        print(f"Error: mkdocs.yml file not found at '{mkdocs_file}'")
        print("This tool only checks files referenced in mkdocs.yml navigation.")
        return []
    
    # Get markdown files from mkdocs.yml navigation only
    markdown_files = []
    subsites = {}
    
    try:
        # Determine base directory for the main mkdocs.yml
        base_dir = directory
        if os.path.exists(os.path.join(directory, 'docs')):
            base_dir = os.path.join(directory, 'docs')
        
        # First pass: collect all subsites information for cross-reference resolution
        _, all_subsites = parse_mkdocs_nav(mkdocs_file, base_dir, directory, 
                                          target_subsite=None, debug=False, 
                                          collect_subsites_only=True)
        
        if debug:
            if target_subsite:
                print(f"Parsing navigation from: {os.path.relpath(mkdocs_file, directory)} (filtering for subsite: {target_subsite})")
            else:
                print(f"Parsing navigation from: {os.path.relpath(mkdocs_file, directory)}")
        
        # Second pass: collect files from target subsite(s) only
        markdown_files, _ = parse_mkdocs_nav(mkdocs_file, base_dir, directory, 
                                           subsites=all_subsites,
                                           target_subsite=target_subsite, 
                                           debug=debug, 
                                           collect_subsites_only=False)
        
        # Use all_subsites for validation (not just the filtered ones)
        subsites = all_subsites
        
        if debug and subsites:
            print(f"All subsites available for cross-reference: {', '.join(sorted(subsites.keys()))}")
        
        if debug:
            print(f"\nFound {len(markdown_files)} Markdown files referenced in navigation")
    except Exception as e:
        print(f"Error parsing mkdocs.yml: {str(e)}")
        return []
    
    total_files = len(markdown_files)
    total_links = 0
    dangling_links = []
    subsite_stats = {} if stats_only else None
    
    for i, file_path in enumerate(markdown_files, 1):
        if not os.path.exists(file_path):
            print(f"Warning: Referenced file does not exist: {file_path}")
            continue
            
        relative_path = os.path.relpath(file_path, directory)
        if not stats_only:
            print(f"Checking file [{i}/{total_files}]: {relative_path}", end="\r")
        
        links = extract_links_from_markdown(file_path)
        total_links += len(links)
        
        invalid = validate_links(directory, file_path, links, subsites)
        if invalid:
            # Determine which subsite this file belongs to
            file_subsite = None
            for subsite_name, subsite_path in subsites.items():
                if relative_path.startswith(subsite_path + os.sep):
                    file_subsite = subsite_name
                    break
            if not file_subsite:
                file_subsite = "root"
            
            if stats_only:
                # Just count for stats
                if file_subsite not in subsite_stats:
                    subsite_stats[file_subsite] = 0
                subsite_stats[file_subsite] += len(invalid)
            else:
                # Full reporting
                dangling_links.extend([(file_path, *link) for link in invalid])
    
    if stats_only:
        print("\n\nSubsite Statistics:")
        print("-------------------")
        total_dangling = 0
        
        if target_subsite:
            # Only show stats for the target subsite
            count = subsite_stats.get(target_subsite, 0)
            total_dangling = count
            print(f"{target_subsite}: {count}")
        else:
            # Show stats for all subsites (only those with dangling links)
            for subsite in sorted(subsites.keys()):
                count = subsite_stats.get(subsite, 0)
                if count > 0:
                    total_dangling += count
                    print(f"{subsite}: {count}")
            
            # Check for root level dangling links
            if "root" in subsite_stats and subsite_stats["root"] > 0:
                print(f"root: {subsite_stats['root']}")
                total_dangling += subsite_stats['root']
        
        print(f"\nTotal dangling links: {total_dangling}")
        return []
    else:
        print("\n\nLink check complete!")
        print(f"Total files checked: {total_files}")
        print(f"Total links found: {total_links}")
        print(f"Dangling links found: {len(dangling_links)}")
        
        if dangling_links:
            print("\nDangling Links:")
            print("---------------")
            for source_file, link_text, link_url, target_path in dangling_links:
                rel_source = os.path.relpath(source_file, directory)
                link_display = f'[{link_text}]({link_url})' if link_text else f'({link_url})'
                print(f"File: {rel_source}")
                print(f"  Raw link: {link_display}")
                print(f"  Target not found: {os.path.relpath(target_path, directory)}")
                print()
        
        return dangling_links

def main():
    parser = argparse.ArgumentParser(description='Check for dangling local links in markdown files referenced in mkdocs.yml navigation.')
    parser.add_argument('--dir', default='.', help='Directory containing mkdocs.yml (defaults to current directory)')
    parser.add_argument('--mkdocs', help='Path to mkdocs.yml file (defaults to DIR/mkdocs.yml)')
    parser.add_argument('--subsite', help='Check only a specific subsite (e.g., windows-installation-and-configuration-guide)')
    parser.add_argument('--stats', action='store_true', help='Show only statistics per subsite')
    parser.add_argument('--output', help='Write results to this file instead of console')
    parser.add_argument('--verbose', action='store_true', help='Print more detailed information')
    parser.add_argument('--debug', action='store_true', help='Show debug information during processing')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"Error: '{args.dir}' is not a valid directory.")
        return
    
    
    # Determine the mkdocs file path
    mkdocs_path = args.mkdocs
    if not mkdocs_path:
        # Use the default mkdocs.yml in the document directory
        mkdocs_path = os.path.join(args.dir, 'mkdocs.yml')
        if not os.path.isfile(mkdocs_path):
            print(f"Warning: No mkdocs.yml found at '{mkdocs_path}'")
            mkdocs_path = None
    elif not os.path.isfile(mkdocs_path):
        print(f"Warning: Specified mkdocs.yml not found at '{mkdocs_path}'")
        mkdocs_path = None
    
    # Redirect output to file if specified
    if args.output:
        import sys
        original_stdout = sys.stdout
        with open(args.output, 'w', encoding='utf-8') as f:
            sys.stdout = f
            dangling_links = check_dangling_links(args.dir, mkdocs_path, args.subsite, args.stats, args.debug, args.verbose)
            sys.stdout = original_stdout
        print(f"Results written to {args.output}")
    else:
        dangling_links = check_dangling_links(args.dir, mkdocs_path, args.subsite, args.stats, args.debug, args.verbose)
    
    # Exit with error code if dangling links found
    if dangling_links:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()