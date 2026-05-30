import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Mapping names to URLs
nav_links = {
    'Inicio': 'index.html',
    'Tienda': 'Juan_&_Beltrán_-_Tienda.html',
    'Contacto': 'Contacto_-_Juan_&_Beltrán.html',
    'Blog': 'Blog_-_Juan_&_Beltrán.html',
    'Historias': 'Juan_&_Beltrán_-_Historias.html'
}

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject Apple UX assets
    if 'apple-ux.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="apple-ux.css">\n  <script src="apple-ux.js" defer></script>\n</head>')

    # 2. Add glass header to absolute or fixed top elements, or standard headers/navs
    content = re.sub(r'(<header[^>]*class=")([^"]*)(")', r'\1\2 glass-header sticky top-0 z-50\3', content)
    content = re.sub(r'(<nav[^>]*class=")([^"]*)(")', r'\1\2 glass-header sticky top-0 z-50\3', content)

    # 3. Add reveal-on-scroll to sections and main div blocks
    content = re.sub(r'(<section[^>]*class=")([^"]*)(")', r'\1\2 reveal-on-scroll\3', content)
    content = re.sub(r'(<article[^>]*class=")([^"]*)(")', r'\1\2 reveal-on-scroll\3', content)

    # 4. Global Responsiveness
    # Replace fixed large widths with responsive max widths and padding
    content = re.sub(r'w-\[1280px\]', 'w-full max-w-[1280px] px-4 md:px-8', content)
    content = re.sub(r'w-\[1440px\]', 'w-full max-w-[1440px] px-4 md:px-8', content)
    content = re.sub(r'h-\[1024px\]', 'min-h-[1024px] h-auto py-12', content)
    content = re.sub(r'h-\[800px\]', 'min-h-[800px] h-auto py-12', content)

    # Convert non-wrapping flex containers with children widths that might overflow
    # By changing flex-row to stack on mobile
    # We replace 'flex-row' with 'flex-col md:flex-row' where it makes sense, but global replace might break small icon rows.
    # Let's just add 'max-w-full overflow-hidden' to body to prevent x-scroll
    content = re.sub(r'<body([^>]*)>', r'<body\1 class="max-w-full overflow-x-hidden">', content)

    # Add parallax to hero images or large imgs
    content = re.sub(r'(<img[^>]*class=")([^"]*)(")', r'\1\2 parallax-image\3', content)

    # 5. Link Navigation
    # Replace >Inicio< inside links or divs with >Inicio< and wrap/add href
    for text, link in nav_links.items():
        # Find >Text< and if it's inside an <a> tag without href, add it, or add onclick
        content = re.sub(fr'>\s*{text}\s*<', f' onclick="window.location.href=\'{link}\'" style="cursor:pointer;">{text}<', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Responsive classes and Apple UI/UX applied to all HTML files.")
