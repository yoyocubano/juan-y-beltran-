import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the favicon to use the local thumbnail.jpg
    content = re.sub(r'<link rel="icon" type="image/jpeg" href="https://lh3\.googleusercontent\.com/aida-public/[^"]+">', 
                     '<link rel="icon" type="image/jpeg" href="https://juan-y-beltran-store.web.app/thumbnail.jpg">', content)
    
    # Replace og:image
    content = re.sub(r'<meta property="og:image" itemprop="image" content="https://lh3\.googleusercontent\.com/aida-public/[^"]+">',
                     '<meta property="og:image" itemprop="image" content="https://juan-y-beltran-store.web.app/thumbnail.jpg">', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated meta tags for WhatsApp preview in all HTML files.")
