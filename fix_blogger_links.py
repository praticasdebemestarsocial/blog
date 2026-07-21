import os
import glob
import re
import json
import urllib.request
import urllib.parse
import base64
import time

IMGBB_API_KEY = "77d3db78594c03e413337c04f0b51e8c"
CACHE_FILE = "imgbb_cache.json"

url_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            url_cache = json.load(f)
    except:
        pass

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(url_cache, f, indent=4)

def upload_to_imgbb(image_url):
    """Baixa a imagem e faz o upload para o ImgBB, retornando a nova URL."""
    if image_url in url_cache:
        return url_cache[image_url]
        
    try:
        req_img = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img, timeout=15) as response:
            image_data = response.read()
            
        b64_image = base64.b64encode(image_data).decode('utf-8')
        
        data = urllib.parse.urlencode({
            'key': IMGBB_API_KEY,
            'image': b64_image
        }).encode('utf-8')
        
        req = urllib.request.Request('https://api.imgbb.com/1/upload', data=data)
        with urllib.request.urlopen(req, timeout=30) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get('success'):
                new_url = res_data['data']['url']
                url_cache[image_url] = new_url
                save_cache()
                return new_url
    except Exception as e:
        print(f"Erro ao fazer upload de {image_url}: {e}")
    
    return image_url

def fix_links():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    
    def replace_url(match):
        url = match.group(0)
        if 'blogger.googleusercontent.com' in url or 'bp.blogspot.com' in url:
            new_url = upload_to_imgbb(url)
            return new_url
        return url

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'blogger.googleusercontent.com' not in content and 'bp.blogspot.com' not in content:
            continue
            
        # We will find all URLs and replace them
        # Match http or https urls ending before ", ), space, or new line
        new_content = re.sub(r'https?://[^\s)"\'\]]+', replace_url, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
            print(f"Fixed {file_path}")

    print(f"Fixed {fixed_count} files.")

if __name__ == '__main__':
    fix_links()
