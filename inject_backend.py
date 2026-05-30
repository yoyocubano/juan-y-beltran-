import os
import glob

html_files = glob.glob('*.html')
script_tag = '\n    <script type="module" src="js/backend.js"></script>\n'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Inject JS
    if 'src="js/backend.js"' not in content:
        content = content.replace('</body>', f'{script_tag}</body>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Inyectado backend.js en todos los archivos HTML")
