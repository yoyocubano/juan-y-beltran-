import os
import glob
import re

html_files = glob.glob('*.html')

header_html = """
<!-- Unified TopAppBar -->
<header class="hidden md:flex justify-between items-center px-margin-desktop py-4 w-full bg-background/95 backdrop-blur-sm z-50 sticky top-0 border-b border-outline-variant glass-header">
    <div class="flex items-center gap-6">
        <a class="text-on-surface-variant hover:text-primary transition-colors text-label-md font-label-md uppercase" href="#" onclick="window.location.href='index.html'" style="cursor:pointer;">Inicio</a>
        <a class="text-on-surface-variant hover:text-primary transition-colors text-label-md font-label-md uppercase" href="#" onclick="window.location.href='tienda.html'" style="cursor:pointer;">Tienda</a>
        <a class="text-on-surface-variant hover:text-primary transition-colors text-label-md font-label-md uppercase" href="#" onclick="window.location.href='nosotros.html'" style="cursor:pointer;">Nosotros</a>
        <a class="text-on-surface-variant hover:text-primary transition-colors text-label-md font-label-md uppercase" href="#" onclick="window.location.href='contacto.html'" style="cursor:pointer;">Contacto</a>
    </div>
    <div class="text-center absolute left-1/2 -translate-x-1/2 cursor-pointer" onclick="window.location.href='index.html'">
        <div class="text-headline-lg font-headline-lg text-primary flex items-center justify-center gap-3">
            <img alt="Logo" class="w-10 h-10 object-cover rounded-full shadow-sm" src="https://juan-y-beltran-store.web.app/thumbnail.jpg"/>
            <span>Juan &amp; Beltrán</span>
        </div>
    </div>
    <div class="flex items-center gap-4 text-primary">
        <button aria-label="Carrito" class="relative hover:text-primary-container transition-all p-2 rounded-full hover:bg-surface-variant" onclick="window.location.href='carrito.html'">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">shopping_bag</span>
            <div class="shopping-cart-badge absolute bg-primary text-on-primary w-5 h-5 rounded-full flex items-center justify-center text-xs" style="display:none; top:-5px; right:-5px;">0</div>
        </button>
    </div>
</header>

<!-- Mobile Header Fallback -->
<header class="md:hidden flex justify-between items-center px-margin-mobile py-4 w-full bg-background/95 backdrop-blur-sm z-50 sticky top-0 border-b border-outline-variant glass-header">
    <div class="cursor-pointer text-headline-lg-mobile font-headline-lg-mobile text-primary flex items-center justify-center gap-2" onclick="window.location.href='index.html'">
        <img alt="Logo" class="w-8 h-8 object-cover rounded-full shadow-sm" src="https://juan-y-beltran-store.web.app/thumbnail.jpg"/>
        <span class="text-[20px]">Juan &amp; Beltrán</span>
    </div>
    <div class="flex items-center gap-2 text-primary">
        <button aria-label="Carrito" class="relative hover:text-primary-container transition-all p-2 rounded-full hover:bg-surface-variant" onclick="window.location.href='carrito.html'">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">shopping_bag</span>
            <div class="shopping-cart-badge absolute bg-primary text-on-primary w-4 h-4 rounded-full flex items-center justify-center text-[10px]" style="display:none; top:-2px; right:-2px;">0</div>
        </button>
    </div>
</header>
"""

nav_html = """
<!-- Unified BottomNavBar (Mobile Only) -->
<nav class="fixed bottom-0 w-full z-50 flex justify-around items-center py-2 px-4 md:hidden bg-surface-container-low border-t border-outline-variant rounded-t-xl glass-header">
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-16 py-1 rounded-lg" href="#" onclick="window.location.href='index.html'">
        <span class="material-symbols-outlined">home</span>
        <span class="text-label-sm font-label-sm mt-1">Inicio</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-16 py-1 rounded-lg" href="#" onclick="window.location.href='tienda.html'">
        <span class="material-symbols-outlined">search</span>
        <span class="text-label-sm font-label-sm mt-1">Tienda</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-16 py-1 rounded-lg" href="#" onclick="window.location.href='carrito.html'">
        <span class="relative">
            <span class="material-symbols-outlined">shopping_cart</span>
            <div class="shopping-cart-badge absolute bg-primary text-on-primary w-4 h-4 rounded-full flex items-center justify-center text-[10px]" style="display:none; top:-5px; right:-10px;">0</div>
        </span>
        <span class="text-label-sm font-label-sm mt-1">Carrito</span>
    </a>
    <a class="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary transition-colors w-16 py-1 rounded-lg" href="#" onclick="window.location.href='contacto.html'">
        <span class="material-symbols-outlined">mail</span>
        <span class="text-label-sm font-label-sm mt-1">Contacto</span>
    </a>
</nav>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace everything between <body ...> and <main with header_html
    content = re.sub(r'(<body[^>]*>).*?(<main)', r'\1\n' + header_html + r'\n\2', content, flags=re.DOTALL)

    # 2. Replace everything between </footer> and <script type="module" src="js/backend.js"> with nav_html
    # Some pages might not have a </nav>, so we just replace after footer.
    content = re.sub(r'(</footer>).*?(<script type="module" src="js/backend.js">)', r'\1\n' + nav_html + r'\n\2', content, flags=re.DOTALL)

    # 3. Add rel=icon correctly just in case
    # content = re.sub(r'<link rel="icon".*?>', '<link rel="icon" type="image/jpeg" href="https://juan-y-beltran-store.web.app/thumbnail.jpg">', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Standardized headers and navigation bars for {len(html_files)} HTML files.")
