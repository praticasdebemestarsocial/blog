import glob
import re

def clean_stray_extensions():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern to match ).jpg), ).png), etc., even with quotes like ).jpg "irisdiagnose")
        # We want to remove the .jpg) or .png) completely.
        # So we look for \)\.(jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\b
        # Wait, the string is `.jpg)` or `.jpg "irisdiagnose")`
        # Let's just remove \.(jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\)
        # And also remove \.(jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\s*".*?"\)
        
        # This regex matches: .(jpg) or .(jpg "text")
        new_content = re.sub(r'\.(?:jpg|png|gif|jpeg|JPG|PNG|GIF|JPEG)\)(?:\s*"[^"]*"\))?', '', content)
        
        # In the frontmatter: description: ".jpg 'irisdiagnose').jpg)"
        # Let's just clean up descriptions that are completely garbage.
        new_content = re.sub(r'description:\s*".*?\.(?:jpg|png|gif|jpeg).*?"', 'description: ""', new_content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
            print(f"Cleaned {file_path}")

    print(f"Fixed {fixed_count} files with stray extensions.")

if __name__ == '__main__':
    clean_stray_extensions()
