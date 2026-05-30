import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Link "Nosotros"
    content = re.sub(r'>\s*Nosotros\s*<', r' onclick="window.location.href=\'Nuestra_Historia_-_Juan_&_Beltrán.html\'" style="cursor:pointer;">Nosotros<', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
