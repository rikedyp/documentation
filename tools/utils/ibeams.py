"""
Recursively searches through markdown files in the given directory
to find those containing headings with the specified i-beam pattern.
Then inserts a hidden search keyword section at the top of each matching file
if it doesn't already exist.

<!-- Hidden search keywords -->
<div style="display: none;">
  {number}⌶
</div>

"""

import os
import re

def find_and_update_markdown_files(root_directory):
    """
    The pattern looks for: 
    <h1 class="heading"><span class="name">Any text</span> <span class="command">...NUMBER⌶...</span></h1>
    
    Args:
        root_directory (str): The root directory to start the search from
        
    Returns:
        list: A list of tuples containing (filename, extracted_number)
    """
    results = []

    heading_pattern = r'<h1 class="heading"><span class="name">.*?</span> <span class="command">.*?(\d+)⌶.*?</span></h1>'
    # Pattern to check if the hidden div with the i-beam already exists
    hidden_div_pattern = r'<div style="display: none;">\s*\d+⌶\s*</div>'
    
    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check if either the comment or the div element already exists
                    if "<!-- Hidden search keywords -->" in content or re.search(hidden_div_pattern, content):
                        continue
                        
                    matches = re.search(heading_pattern, content)
                    
                    if matches:
                        number = matches.group(1)                        
                        section_to_insert = f"""
<!-- Hidden search keywords -->
<div style="display: none;">
  {number}⌶
</div>

"""
                        
                        updated_content = section_to_insert + content
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        
                        results.append((file_path, number))
                
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
    
    return results

def main():
    root_dir = "language-reference-guide"
    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' directory does not exist.")
        return
    results = find_and_update_markdown_files(root_dir)
    
    if not results:
        print("\nNo files were updated.")
    else:
        print(f"\nUpdated {len(results)} file(s):")
        for file_path, number in results:
            print(f"File: {file_path}, added keyword section for i-beam: {number}")
            
if __name__ == "__main__":
    main()