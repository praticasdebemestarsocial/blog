import glob
import re

def fix_markdown_links():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    
    # Regex to find: ![alt](url).ext)
    # We look for something that resembles a markdown image link followed immediately by .\w+)
    # Example: ![](url(1).gif).gif) -> the markdown parser during migration captured `(1)` as `(1).gif)` and left `.gif)` trailing.
    # Actually, let's just find any `.gif)`, `.png)`, `.jpg)`, `.jpeg)` at the end of a line that contains `![](`
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        changed = False
        
        for i, line in enumerate(lines):
            # If the line contains an image tag and ends with an extension followed by a parenthesis
            if re.search(r'!\[.*?\]\(.*?\)\.(?:jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\)$', line):
                # We just strip the trailing `.\w+)`
                new_line = re.sub(r'(\.(?:jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\))+$', '', line)
                if new_line != line:
                    lines[i] = new_line
                    changed = True
                    
        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            fixed_count += 1

    print(f"Fixed {fixed_count} files.")

if __name__ == '__main__':
    fix_markdown_links()
