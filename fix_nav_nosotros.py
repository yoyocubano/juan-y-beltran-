import os
import glob
import re

html_files = glob.glob('*.html')

nav_html = """
<!-- Unified BottomNavBar (Mobile Only) -->
<nav class="fixed bottom-0 w-full z-50 flex justify-around items-center py-2 px-1 md:hidden bg-surface-container-low border-t border-outline-variant rounded-t-xl glass-header">
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-[20%] py-1 rounded-lg" href="#" onclick="window.location.href='index.html'">
        <span class="material-symbols-outlined text-[20px]">home</span>
        <span class="text-[10px] font-label-sm mt-1">Inicio</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-[20%] py-1 rounded-lg" href="#" onclick="window.location.href='tienda.html'">
        <span class="material-symbols-outlined text-[20px]">storefront</span>
        <span class="text-[10px] font-label-sm mt-1">Tienda</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-[20%] py-1 rounded-lg" href="#" onclick="window.location.href='nosotros.html'">
        <span class="material-symbols-outlined text-[20px]">groups</span>
        <span class="text-[10px] font-label-sm mt-1">Nosotros</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-[20%] py-1 rounded-lg" href="#" onclick="window.location.href='carrito.html'">
        <span class="relative">
            <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
            <div class="shopping-cart-badge absolute bg-primary text-on-primary w-4 h-4 rounded-full flex items-center justify-center text-[10px]" style="display:none; top:-5px; right:-10px;">0</div>
        </span>
        <span class="text-[10px] font-label-sm mt-1">Carrito</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-[20%] py-1 rounded-lg" href="#" onclick="window.location.href='contacto.html'">
        <span class="material-symbols-outlined text-[20px]">mail</span>
        <span class="text-[10px] font-label-sm mt-1">Contacto</span>
    </a>
</nav>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the existing nav with the new 5-item nav
    content = re.sub(r'<!-- Unified BottomNavBar \(Mobile Only\) -->.*?<\/nav>', nav_html, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Also create home.html as a direct clone of index.html to resolve the "home html" conflict request
import shutil
shutil.copy2('index.html', 'home.html')
# Now add home.html to the files we process
with open('home.html', 'r', encoding='utf-8') as f:
    home_content = f.read()
# Replace the title to denote it's home
home_content = re.sub(r'<title>.*?</title>', '<title>Juan &amp; Beltrán - Home Principal</title>', home_content)
with open('home.html', 'w', encoding='utf-8') as f:
    f.write(home_content)

print("Added Nosotros to mobile nav and created home.html")
