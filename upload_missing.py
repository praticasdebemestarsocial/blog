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
    if image_url in url_cache:
        return url_cache[image_url]
    
    try:
        req_img = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img, timeout=10) as response:
            image_data = response.read()
            
        b64_image = base64.b64encode(image_data).decode('utf-8')
        
        data = urllib.parse.urlencode({
            'key': IMGBB_API_KEY,
            'image': b64_image
        }).encode('utf-8')
        
        req = urllib.request.Request('https://api.imgbb.com/1/upload', data=data)
        with urllib.request.urlopen(req, timeout=20) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get('success'):
                new_url = res_data['data']['url']
                url_cache[image_url] = new_url
                save_cache()
                print(f"Uploaded: {image_url}")
                time.sleep(1)  # Rate limiting
                return new_url
    except Exception as e:
        print(f"Error {e} on {image_url}")
    return image_url

def collect_urls():
    files = glob.glob('_posts/*.md')
    urls_to_upload = set()
    
    def extract_url(match):
        url = match.group(0)
        if ('blogger.googleusercontent.com' in url or 'bp.blogspot.com' in url) and url not in url_cache:
            urls_to_upload.add(url)
        return url

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            re.sub(r'https?://[^\s)"\'\]]+', extract_url, content)
            
    print(f"Found {len(urls_to_upload)} URLs to upload.")
    
    for i, url in enumerate(urls_to_upload):
        print(f"Uploading {i+1}/{len(urls_to_upload)}...")
        upload_to_imgbb(url)
        
    print("Finished uploading.")

if __name__ == '__main__':
    collect_urls()
