import os
import re
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
import unicodedata
import concurrent.futures
import threading

# Configurações
SOURCE_DIR = r"c:\Users\Administrator\Documents\projetos\silviane\explodindo o blogspot\Takeout\Blogger\Blogs\Autoconhecimento na Era Digital_ Um olhar para dentro de você mesmo!\posts_md"
TARGET_DIR = r"c:\Users\Administrator\Documents\projetos\silviane\blog_praticas\_posts"
IMGBB_API_KEY = "77d3db78594c03e413337c04f0b51e8c"
CACHE_FILE = "imgbb_cache.json"

# Verifica se os diretorios existem
os.makedirs(TARGET_DIR, exist_ok=True)

cache_lock = threading.Lock()

# Carrega o cache de URLs
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        url_cache = json.load(f)
else:
    url_cache = {}

def save_cache():
    with cache_lock:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(url_cache, f, indent=4)

def upload_to_imgbb(image_url):
    """Baixa a imagem e faz o upload para o ImgBB, retornando a nova URL."""
    with cache_lock:
        if image_url in url_cache:
            return url_cache[image_url]
        
    try:
        req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
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
                with cache_lock:
                    url_cache[image_url] = new_url
                save_cache()
                return new_url
            else:
                return image_url
                
    except Exception as e:
        return image_url

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            return False

    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        return False
        
    fm_text = match.group(1)
    body = match.group(2)
    
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
            
    title = fm.get('title', 'Sem Título')
    date_str = fm.get('date', '')
    
    tags_str = fm.get('tags', '')
    tags = []
    if tags_str.startswith('[') and tags_str.endswith(']'):
        tags = [t.strip().strip("'").strip('"') for t in tags_str[1:-1].split(',')]
    tags = [t for t in tags if t]
    
    def replace_image(m):
        alt_text = m.group(1)
        full_url = m.group(2)
        url_match = re.match(r'^(\S+)(?:\s+.*)?$', full_url)
        url = url_match.group(1) if url_match else full_url
        rest = full_url[len(url):]
        if url.startswith('http'):
            new_url = upload_to_imgbb(url)
            return f"![{alt_text}]({new_url}{rest})"
        return m.group(0)

    body = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_image, body)
    # Remove wrappers around markdown images
    body = re.sub(r'\[(!\[.*?\]\(.*?\))\]\((?:https?:)?//(?:[a-zA-Z0-9-]+\.)?(?:blogspot\.com|blogger\.googleusercontent\.com).*?\)', r'\1', body)
    
    def replace_html_img(m):
        url = m.group(1)
        if url.startswith('http'):
            new_url = upload_to_imgbb(url)
            return m.group(0).replace(url, new_url)
        return m.group(0)
        
    body = re.sub(r'<img[^>]+src=["\'](.*?)["\']', replace_html_img, body)
    # Remove wrappers around html images
    body = re.sub(r'<a[^>]+href=["\'](?:https?:)?//(?:[a-zA-Z0-9-]+\.)?(?:blogspot\.com|blogger\.googleusercontent\.com).*?["\'][^>]*>\s*(<img[^>]+>)\s*</a>', r'\1', body)
    
    slug_date = "2024-01-01"
    formatted_date = date_str
    if date_str:
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', date_str)
        if date_match:
            slug_date = date_match.group(1)
            
    slug = slugify(title)
    if not slug:
        slug = "post-sem-nome"
        
    filename = f"{slug_date}-{slug}.md"
    target_path = os.path.join(TARGET_DIR, filename)
    
    categories = ['bem-estar']
    
    clean_body = re.sub(r'!\[.*?\]\(.*?\)', '', body)
    clean_body = re.sub(r'<img[^>]+>', '', clean_body)
    clean_body = re.sub(r'<.*?>', '', clean_body)
    clean_body = re.sub(r'[#\*_\[\]]', '', clean_body)
    desc_lines = [l.strip() for l in clean_body.split('\n') if l.strip()]
    description = ""
    if desc_lines:
        description = desc_lines[0][:150] + "..." if len(desc_lines[0]) > 150 else desc_lines[0]
        
    new_fm = f"""---
layout: post
title: "{title}"
date: {formatted_date}
tags: {json.dumps(tags, ensure_ascii=False)}
categories: {json.dumps(categories, ensure_ascii=False)}
description: "{description}"
---
"""
    final_content = new_fm + "\n" + body.strip() + "\n"
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    return True

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Erro: Diretório de origem não existe: {SOURCE_DIR}")
        return
        
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    print(f"Total de {len(files)} arquivos encontrados.")
    
    success = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(process_file, os.path.join(SOURCE_DIR, f)): f for f in files}
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                success += 1
            if (i + 1) % 50 == 0:
                print(f"Processado {i + 1}/{len(files)}...")
            
    print(f"Concluído! {success} arquivos processados e salvos em _posts.")

if __name__ == "__main__":
    main()
