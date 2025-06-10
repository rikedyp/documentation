import os
import re
import argparse
from pathlib import Path
from urllib.parse import urlparse, unquote
from ruamel.yaml import YAML

def is_external_link(url):
    """Check if a URL is external (starts with http/https)."""
    return url.startswith(('http://', 'https://'))

def parse_mkdocs_nav(mkdocs_file, base_dir):
    """Parse the navigation section of mkdocs.yml to extract all markdown files to check."""
    markdown_files = []
    
    try:
        # Create a YAML parser that can handle custom tags
        yaml = YAML(typ='safe')
        yaml.register_class(IncludeTag)
        
        # Load the mkdocs.yml file
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            mkdocs_config = yaml.load(f)
        
        if not mkdocs_config or 'nav' not in mkdocs_config:
            print("Warning: No 'nav' section found in mkdocs.yml")
            return []
        
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
                            # Skip !include directives
                            continue
                        elif path.endswith('.md'):
                            # Handle docs/ prefix if present
                            if path.startswith('docs/'):
                                path = path[5:]  # Remove 'docs/' prefix
                            
                            # Add the markdown file to the list
                            full_path = os.path.normpath(os.path.join(current_dir, path))
                            if os.path.exists(full_path):
                                files.append(full_path)
                            else:
                                print(f"Warning: Referenced file not found: {full_path}")
                    else:
                        # Recurse into nested sections
                        files.extend(extract_files_from_nav(path, current_dir))
            
            return files
        
        # Extract markdown files from nav
        markdown_files = extract_files_from_nav(mkdocs_config['nav'], base_dir)
        
    except Exception as e:
        print(f"Error parsing mkdocs.yml: {str(e)}")
    
    return markdown_files

class IncludeTag:
    """Custom tag handler for !include in YAML."""
    @classmethod
    def from_yaml(cls, constructor, node):
        return node.value

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

def validate_links(root_dir, file_path, links, exclude_dirs):
    """Validate if links are pointing to valid resources."""
    invalid_links = []
    base_dir = os.path.dirname(file_path)
    
    for link_text, link_url in links:
        # Skip external links, anchor links, and mailto links
        if is_external_link(link_url) or link_url.startswith('#') or link_url.startswith('mailto:'):
            continue
        
        # Handle URLs with anchors or query parameters
        url_parts = link_url.split('#')[0].split('?')[0]
        
        # Parse URL and get the path
        parsed_url = urlparse(url_parts)
        path = unquote(parsed_url.path)
        
        # Check if path points to an excluded directory
        path_components = [p for p in path.split('/') if p and p != '..']
        if path_components and path_components[0] in exclude_dirs:
            continue
        
        # Determine the target file path
        if os.path.isabs(path):
            # For absolute paths, resolve from the root directory
            target_path = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
        else:
            # For relative paths, resolve from the current file's directory
            target_path = os.path.normpath(os.path.join(base_dir, path))
        
        # Initialize variables to track if we found a valid target
        target_found = False
        
        # Check if the path exists directly
        if os.path.exists(target_path):
            target_found = True
        # Check with .md extension if not already having it
        elif not path.endswith('.md') and os.path.exists(target_path + '.md'):
            target_found = True
        # Check if it's a directory with index.md
        elif os.path.exists(os.path.join(target_path, 'index.md')):
            target_found = True
        
        # If not found yet and the link doesn't end with .md, try one level less relative movement
        if not target_found and not path.endswith('.md') and '../' in path:
            # Split the path into components
            path_parts = path.split('/')
            
            # Find the last '../' occurrence
            for i in range(len(path_parts) - 1, -1, -1):
                if path_parts[i] == '..':
                    # Remove the '../' and add .md to the last component
                    alternative_path_parts = path_parts[:]
                    alternative_path_parts.pop(i)  # Remove '..'
                    
                    if i < len(alternative_path_parts):
                        file_name = alternative_path_parts[-1] + '.md'
                        alternative_path_parts[-1] = file_name
                        
                        # Construct the alternative path
                        alternative_path = '/'.join(alternative_path_parts)
                        alternative_target = os.path.normpath(os.path.join(base_dir, alternative_path))
                        
                        if os.path.exists(alternative_target):
                            target_found = True
                            break
                    break  # Only try the last '../'
        
        # If still not found, report as invalid
        if not target_found:
            invalid_links.append((link_text, link_url, target_path))
    
    return invalid_links

def extract_include_dirs_from_mkdocs(mkdocs_file):
    """Extract directories from mkdocs.yml that are included with !include."""
    try:
        # Use ruamel.yaml to handle custom tags properly
        yaml = YAML(typ='safe')
        
        # Load the file content as text first to use regex for finding !include directives
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all !include directives in the navigation section
        include_pattern = re.compile(r'!include\s+\./([\w-]+)')
        matches = include_pattern.findall(content)
        
        # Return the first directory component from each include path
        return matches
    except Exception as e:
        print(f"Error processing mkdocs.yml file: {str(e)}")
        return []

def find_all_markdown_files(directory, exclude_dirs):
    """Find all markdown files in directory, excluding specified directories."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        # Skip excluded directories
        rel_path = os.path.relpath(root, directory)
        if rel_path == '.':
            # Check if first directory component is in exclude_dirs
            if any(d in exclude_dirs for d in [os.path.basename(root)]):
                continue
        else:
            # Check if any directory component is in exclude_dirs
            if any(d in exclude_dirs for d in rel_path.split(os.sep)):
                continue
        
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    
    return markdown_files

def check_dangling_links(directory, exclude_dirs, mkdocs_file=None):
    """Check for dangling links in markdown files."""
    # Remove the current directory from exclude_dirs if it's present
    current_dir_name = os.path.basename(os.path.abspath(directory))
    if current_dir_name in exclude_dirs:
        exclude_dirs.remove(current_dir_name)
    
    print(f"Excluded directories: {', '.join(exclude_dirs) if exclude_dirs else 'None'}")
    
    # Get markdown files from mkdocs.yml if provided, otherwise find all .md files
    markdown_files = []
    if mkdocs_file and os.path.exists(mkdocs_file):
        try:
            markdown_files = parse_mkdocs_nav(mkdocs_file, directory)
            print(f"Found {len(markdown_files)} Markdown files referenced in mkdocs.yml")
        except Exception as e:
            print(f"Error parsing mkdocs.yml: {str(e)}")
            print("Falling back to scanning all Markdown files...")
    
    # Fall back to scanning all files if no mkdocs file or parsing failed
    if not markdown_files:
        markdown_files = find_all_markdown_files(directory, exclude_dirs)
        print(f"Found {len(markdown_files)} Markdown files to scan")
    
    total_files = len(markdown_files)
    total_links = 0
    dangling_links = []
    
    for i, file_path in enumerate(markdown_files, 1):
        if not os.path.exists(file_path):
            print(f"Warning: Referenced file does not exist: {file_path}")
            continue
            
        relative_path = os.path.relpath(file_path, directory)
        print(f"Checking file [{i}/{total_files}]: {relative_path}", end="\r")
        
        links = extract_links_from_markdown(file_path)
        total_links += len(links)
        
        invalid = validate_links(directory, file_path, links, exclude_dirs)
        if invalid:
            dangling_links.extend([(file_path, *link) for link in invalid])
    
    print("\n\nLink check complete!")
    print(f"Total files checked: {total_files}")
    print(f"Total links found: {total_links}")
    print(f"Dangling links found: {len(dangling_links)}")
    
    if dangling_links:
        print("\nDangling Links:")
        print("---------------")
        for source_file, link_text, link_url, target_path in dangling_links:
            rel_source = os.path.relpath(source_file, directory)
            link_display = f'"{link_text}"' if link_text else "Unnamed Link"
            print(f"File: {rel_source}")
            print(f"  Link: {link_display} -> {link_url}")
            print(f"  Target not found: {os.path.relpath(target_path, directory)}")
            print()
    
    return dangling_links

def main():
    parser = argparse.ArgumentParser(description='Check for dangling local links in markdown files.')
    parser.add_argument('--dir', required=True, help='Directory to scan for markdown files')
    parser.add_argument('--mkdocs', help='Path to mkdocs.yml file to extract directory excludes (defaults to DIR/mkdocs.yml)')
    parser.add_argument('--output', help='Write results to this file instead of console')
    parser.add_argument('--verbose', action='store_true', help='Print more detailed information')
    
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
    
    # Extract exclude directories from mkdocs.yml
    exclude_dirs = []
    if mkdocs_path and os.path.isfile(mkdocs_path):
        exclude_dirs = extract_include_dirs_from_mkdocs(mkdocs_path)
        print(f"Extracted exclude directories from mkdocs.yml: {exclude_dirs}")
    
    # Redirect output to file if specified
    if args.output:
        import sys
        original_stdout = sys.stdout
        with open(args.output, 'w', encoding='utf-8') as f:
            sys.stdout = f
            dangling_links = check_dangling_links(args.dir, exclude_dirs, mkdocs_path)
            sys.stdout = original_stdout
        print(f"Results written to {args.output}")
    else:
        dangling_links = check_dangling_links(args.dir, exclude_dirs, mkdocs_path)
    
    # Exit with error code if dangling links found
    if dangling_links:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()