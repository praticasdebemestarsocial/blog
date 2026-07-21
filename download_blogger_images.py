import os
import glob
import re
import urllib.request

ASSETS_DIR = 'assets/img/posts'
os.makedirs(ASSETS_DIR, exist_ok=True)

def download_image(url, filename):
    filepath = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(filepath):
        return f"/assets/img/posts/{filename}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded: {filename}")
        return f"/assets/img/posts/{filename}"
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url

def fix_links_local():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    
    def replace_url(match):
        url = match.group(0)
        if 'blogger.googleusercontent.com' in url or 'bp.blogspot.com' in url:
            # Extract filename from URL or generate one
            filename = url.split('/')[-1]
            if not filename or '.' not in filename:
                filename = f"image_{hash(url)}.jpg"
            else:
                # Remove query params
                filename = filename.split('?')[0]
                
            new_url = download_image(url, filename)
            return new_url
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

    print(f"Fixed {fixed_count} files by downloading images locally.")

if __name__ == '__main__':
    fix_links_local()
