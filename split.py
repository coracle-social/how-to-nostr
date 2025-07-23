#!/usr/bin/env python3
"""
Script to split book.md into chapters based on single-# headings.
Each chapter will be written to a separate file in the content directory.
"""

import os
import re
import shutil

def empty_content_directory():
    """Empty the content directory, creating it if it doesn't exist."""
    content_dir = "content"
    
    if os.path.exists(content_dir):
        # Remove all files and subdirectories
        shutil.rmtree(content_dir)
    
    # Create the directory
    os.makedirs(content_dir)
    print(f"Emptied and recreated {content_dir} directory")

def sanitize_filename(title):
    """Convert a chapter title to a safe filename."""
    # Remove or replace problematic characters
    filename = re.sub(r'[^\w\s-]', '', title)
    filename = re.sub(r'[-\s]+', '-', filename)
    filename = filename.strip('-').lower()
    return filename

def split_book():
    """Split book.md into chapters based on single-# headings."""
    
    # Read the entire book
    with open('book.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by single-# headings (but not ##, ###, etc.)
    # This regex looks for lines that start with exactly one # followed by a space
    chapters = re.split(r'\n(?=^# [^#])', content, flags=re.MULTILINE)
    
    # Remove any empty chapters
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]
    
    chapter_count = 0
    
    for chapter in chapters:
        if not chapter:
            continue
            
        # Extract the title from the first line
        lines = chapter.split('\n')
        first_line = lines[0].strip()
        
        # Check if it's actually a single-# heading
        if not first_line.startswith('# '):
            continue
            
        # Extract title (remove the '# ' prefix)
        title = first_line[2:].strip()
        
        # Create filename
        chapter_count += 1
        safe_title = sanitize_filename(title)
        filename = f"{chapter_count:03d}-{safe_title}.md"
        filepath = os.path.join("content", filename)
        
        # Write the chapter to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chapter)
        
        print(f"Created: {filepath} - {title}")

def main():
    """Main function to orchestrate the splitting process."""
    print("Starting book splitting process...")
    
    # Check if book.md exists
    if not os.path.exists('book.md'):
        print("Error: book.md not found in current directory")
        return
    
    # Empty the content directory
    empty_content_directory()
    
    # Split the book into chapters
    split_book()
    
    print("Book splitting completed!")

if __name__ == "__main__":
    main()