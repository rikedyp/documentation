import os
import re
import argparse

def find_links(filepath, target_substring):
    """
    Search a markdown file for links whose URL contains a specified substring.
    
    Args:
        filepath (str): Path to the markdown file to search
        target_substring (str): Substring to search for in the URLs
        
    Returns:
        list: List of URLs that contain the target substring
    """
    # Regular expression to match markdown links: [text](url)
    pattern = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
    results = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return results
    
    for match in pattern.finditer(content):
        url = match.group(1)
        if target_substring in url:
            results.append(url)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Find links in markdown files containing a specified substring.')
    parser.add_argument('--target', default="json", help='Substring to search for in URLs (default: "json")')
    
    args = parser.parse_args()
    target_substring = args.target
    
    # Walk the current directory recursively
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.lower().endswith('.md'):
                full_path = os.path.join(root, filename)
                links = find_links(full_path, target_substring)
                for url in links:
                    print(f"{full_path} : {url}")

if __name__ == '__main__':
    main()