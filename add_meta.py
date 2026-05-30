import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

logo_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuAxu5CMprBsza72a9eipJ64CIBAPooih9h_PtxV9SeBOtVKf6BJBuiGGM33Z2eozLnjnP0ztoJfYKpR24HNa7PjGg-YrQk9KV-sewQpi-UkH9lY9kSJC76ssNgioTIkgrFqx-YsM_pnlseQqNBmPUeawDwqQsJfkNLrJ6Ohk__M3Nw3pNypwAse9xY11wFkj_z_J0he4jQARrqD2Opnx28087zp6-CGz-_w_rsBlpbQY5AkjALary8Syoh_ij6klqwvAFtv0I_wNyQ"

meta_tags = f"""
  <!-- Favicon & OpenGraph for WhatsApp Sharing -->
  <link rel="icon" type="image/jpeg" href="{logo_url}">
  <meta property="og:title" content="Juan & Beltrán">
  <meta property="og:description" content="Historias que se pueden abrazar. Catálogo premium y tienda con estética artesanal.">
  <meta property="og:image" itemprop="image" content="{logo_url}">
  <meta property="og:url" content="https://yoyocubano.github.io/juan-y-beltran-/">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Juan & Beltrán">
  <!-- End Meta -->
"""

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # If already added, skip to avoid duplicates
    if "og:title" not in content:
        content = content.replace('</head>', f'{meta_tags}</head>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Meta tags for Favicon and WhatsApp OpenGraph added to all HTML files.")
