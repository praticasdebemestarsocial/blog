import os
import glob
import re
import json

CACHE_FILE = "imgbb_cache.json"

url_cache = {}
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        url_cache = json.load(f)

def fix_links():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    missing_urls = set()
    
    def replace_url(match):
        url = match.group(0)
        if 'blogger.googleusercontent.com' in url or 'bp.blogspot.com' in url:
            if url in url_cache:
                return url_cache[url]
            else:
                missing_urls.add(url)
        return url

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'blogger.googleusercontent.com' not in content and 'bp.blogspot.com' not in content:
            continue
            
        new_content = re.sub(r'https?://[^\s)"\'\]]+', replace_url, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1

    print(f"Fixed {fixed_count} files using cache.")
    print(f"Missing {len(missing_urls)} URLs from cache.")
    for u in list(missing_urls)[:10]:
        print("Missing:", u)

if __name__ == '__main__':
    fix_links()
