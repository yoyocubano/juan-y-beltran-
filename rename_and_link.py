import os
import re
import shutil

# Map of old to new filenames
renames = {
    "Juan_&_Beltrán_-_Tienda.html": "tienda.html",
    "Nuestra_Historia_-_Juan_&_Beltrán.html": "nosotros.html",
    "Contacto_-_Juan_&_Beltrán.html": "contacto.html",
    "Juan_&_Beltrán_-_Historias.html": "historias.html",
    "Blog_-_Juan_&_Beltrán.html": "blog.html",
    "Carrito_-_Juan_&_Beltrán.html": "carrito.html",
    "Juan_&_Beltrán_-_Detalle_de_Producto.html": "producto.html"
}

files_to_delete = [
    "Home_-_Juan_Beltrán.html",
    "Historias_-_Juan_Beltrán.html",
    "Juan_&_Beltrán_-_Home_Actualizada.html"
]

# Rename files safely using git mv
for old, new in renames.items():
    if os.path.exists(old):
        os.system(f'git mv "{old}" "{new}"')

for f in files_to_delete:
    if os.path.exists(f):
        os.system(f'git rm "{f}"')

# Now process all html files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old links with new links
    for old, new in renames.items():
        content = content.replace(old, new)
        # Also handle URL encoded versions if they exist
        content = content.replace(old.replace('&', '&amp;'), new)
    
    # Fix responsiveness of Hero Image on mobile
    # Find huge fixed heights
    content = re.sub(r'h-\[819px\]\s+md:h-\[921px\]', r'min-h-[60vh] h-auto pb-12', content)
    # The image inside the hero: replace object-cover with object-contain md:object-cover to prevent cutting off on mobile
    content = re.sub(r'object-cover opacity-80 object-center parallax-image', r'object-contain md:object-cover w-full h-auto max-h-[80vh] md:h-full opacity-80 object-center parallax-image', content)

    # Some images were squashed because they lacked full-width wrappers, 
    # Let's ensure containers don't overflow
    content = content.replace('w-[100vw]', 'w-full')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Renaming and UI fixes completed.")
