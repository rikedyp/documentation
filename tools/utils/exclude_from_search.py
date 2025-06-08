import os
import re

def add_front_matter(file_path):
    """
    Adds MkDocs 'exclude from search' front matter to markdown file
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} does not exist. Skipping.")
        return
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the file already has front matter with search exclude
    front_matter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = front_matter_pattern.match(content)
    
    if match:
        # File has front matter, check if it has search exclude
        front_matter_content = match.group(1)
        if re.search(r'search:\s*\n\s*exclude:\s*true', front_matter_content):
            print(f"Search exclude front matter already exists in {file_path}. Skipping.")
            return
        else:
            print(f"File {file_path} has front matter but missing search exclude. Leaving unchanged as requested.")
            return
    
    # Front matter to add
    new_front_matter = """---
search:
  exclude: true
---

"""
    
    # Add front matter to the beginning
    new_content = new_front_matter + content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Added front matter to {file_path}")

def process_file_list(list_file):
    """
    Reads a text file containing paths and adds front matter to each markdown file
    """
    if not os.path.exists(list_file):
        print(f"Error: List file {list_file} does not exist.")
        return
    
    with open(list_file, 'r', encoding='utf-8') as file:
        for line in file:
            file_path = line.strip()
            if file_path:  # Skip empty lines
                add_front_matter(file_path)

def main():
    list_file = 'ghost.txt'  # Path to the list file
    process_file_list(list_file)
    print("Processing complete.")

if __name__ == "__main__":
    main()