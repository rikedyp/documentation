"""
Convert the object-reference pages to inline the leading cross references.

By Stefan Kruger <stefan@dyalog.com>

python fix_objref.py --dir object-reference 

The results will end up as

    object-reference-transformed

which in turn should be pointed to by the config.json file used by

    mkdocs2pdf.py

"""

import re
import os
import argparse
import shutil
from pathlib import Path

def transform_markdown(file_path):
    """
    Transforms a specifically formatted markdown file according to the requirements.
    
    Args:
        file_path (str): Path to the markdown file to transform
        
    Returns:
        tuple: (bool, str) - Success status and either transformed content or error message
    """
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Check if the file has the expected format with regex
        h1_pattern = r'<h1 class="heading">.*?</h1>'
        links_pattern = r'\[(.*?)\]\((.*?)\)'
        purpose_pattern = r'\*\*Purpose:\*\*(.*?)(?=\*\*Description)'
        description_pattern = r'\*\*Description\*\*'
        
        if not (re.search(h1_pattern, original_content, re.DOTALL) and 
                re.search(links_pattern, original_content) and 
                re.search(purpose_pattern, original_content, re.DOTALL) and 
                re.search(description_pattern, original_content, re.DOTALL)):
            return False, "File does not match the expected format."
        
        # Extract the H1 heading
        h1_match = re.search(h1_pattern, original_content, re.DOTALL)
        h1_heading = h1_match.group(0) if h1_match else ""
        
        # Extract the Purpose section
        purpose_match = re.search(purpose_pattern, original_content, re.DOTALL)
        purpose_content = purpose_match.group(1).strip() if purpose_match else ""
        purpose_section = f"**Purpose:** {purpose_content}"
        
        # Extract the initial links section (all links between h1 and Purpose)
        links_section_pattern = re.compile(
            rf'{re.escape(h1_heading)}\s*(.*?)(?=\*\*Purpose:)',
            re.DOTALL
        )
        links_section_match = links_section_pattern.search(original_content)
        links_text = links_section_match.group(1).strip() if links_section_match else ""
        
        # Find all links in the links section
        transformed_links = []
        if links_text:
            links_matches = re.findall(links_pattern, links_text)
            
            for anchor_text, link_path in links_matches:
                # Get the absolute path to the linked file
                base_dir = os.path.dirname(file_path)
                linked_file_path = os.path.normpath(os.path.join(base_dir, link_path))
                
                # Read the linked file
                try:
                    with open(linked_file_path, 'r', encoding='utf-8') as linked_file:
                        linked_content = linked_file.read()
                    
                    # Extract all links from tables or lists in the linked content
                    link_extraction_pattern = r'\[(.*?)\]\((.*?)\)'
                    linked_items = re.findall(link_extraction_pattern, linked_content)
                    linked_items = [item[0] for item in linked_items]  # Extract only the anchor texts
                    
                    # Format the transformed link section
                    transformed_link = f"**{anchor_text}** {' '.join(linked_items)}"
                    transformed_links.append(transformed_link)
                    
                except Exception as e:
                    transformed_links.append(f"**{anchor_text}** [Error reading linked file: {str(e)}]")
        
        # Find the description section and everything after it
        description_and_after_pattern = re.compile(
            rf'\*\*Description\*\*(.*?)$',
            re.DOTALL
        )
        description_and_after_match = description_and_after_pattern.search(original_content)
        description_and_after = description_and_after_match.group(1) if description_and_after_match else ""
        
        # Build the transformed content
        transformed_content = f"{h1_heading}\n\n{purpose_section}\n\n"
        transformed_content += "\n\n".join(transformed_links)
        transformed_content += f"\n\n**Description**{description_and_after}"
        
        return True, transformed_content
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}"

def clone_directory(source_dir):
    """
    Creates a copy of the source directory with '-transformed' suffix.
    
    Args:
        source_dir (str): The directory to clone
        
    Returns:
        str: Path to the cloned directory, or None if failed
    """
    try:
        # Get the base name of the source directory
        source_path = Path(source_dir)
        parent_dir = source_path.parent
        dir_name = source_path.name
        
        # Create the target directory name
        target_dir = os.path.join(parent_dir, f"{dir_name}-transformed")
        
        # Check if target directory already exists
        if os.path.exists(target_dir):
            print(f"Target directory '{target_dir}' already exists.")
            user_input = input("Do you want to remove it and continue? (y/n): ").lower()
            if user_input == 'y':
                shutil.rmtree(target_dir)
            else:
                return None
        
        # Copy the entire directory tree
        shutil.copytree(source_dir, target_dir)
        print(f"Created clone of '{source_dir}' at '{target_dir}'")
        return target_dir
        
    except Exception as e:
        print(f"Error cloning directory: {str(e)}")
        return None

def process_directory(root_dir):
    """
    Recursively process markdown files in the given directory.
    
    Args:
        root_dir (str): The root directory to start processing from
    """
    total_files = 0
    transformed_files = 0
    errors = 0
    
    print(f"Starting to process files from {root_dir}")
    
    # Walk through all files and directories
    for root, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                total_files += 1
                
                # Try to transform the file
                success, result = transform_markdown(file_path)
                
                if success:
                    try:
                        # Write transformed content directly (no backup needed)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(result)
                            
                        transformed_files += 1
                        print(f"Transformed: {file_path}")
                        
                    except Exception as e:
                        errors += 1
                        print(f"Error saving transformation for {file_path}: {str(e)}")
    
    print(f"\nProcessing complete.")
    print(f"Total Markdown files found: {total_files}")
    print(f"Files transformed: {transformed_files}")
    print(f"Errors encountered: {errors}")

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description='Transform markdown files with a specific format in a directory and its subdirectories.'
    )
    
    parser.add_argument(
        '--dir',
        required=True,
        help='Root directory to process markdown files from'
    )
    
    args = parser.parse_args()
    
    # Validate the directory
    if not os.path.isdir(args.dir):
        print(f"Error: '{args.dir}' is not a valid directory.")
        return
    
    # Clone the directory first
    cloned_dir = clone_directory(args.dir)
    if not cloned_dir:
        print("Directory cloning failed or was cancelled. Exiting...")
        return
    
    # Process the cloned directory
    process_directory(cloned_dir)
    
    print(f"\nOriginal directory: {args.dir}")
    print(f"Transformed directory: {cloned_dir}")

if __name__ == "__main__":
    main()