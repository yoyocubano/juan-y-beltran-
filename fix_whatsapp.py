import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

extra_meta = """
  <meta property="og:image:width" content="800">
  <meta property="og:image:height" content="800">
  <meta property="og:image:type" content="image/jpeg">
"""

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add the extra OG image tags right after og:image if they don't exist
    if "og:image:width" not in content:
        content = content.replace('itemprop="image" content="https://lh3.googleusercontent.com/aida-public/AB6AXuAxu5CMprBsza72a9eipJ64CIBAPooih9h_PtxV9SeBOtVKf6BJBuiGGM33Z2eozLnjnP0ztoJfYKpR24HNa7PjGg-YrQk9KV-sewQpi-UkH9lY9kSJC76ssNgioTIkgrFqx-YsM_pnlseQqNBmPUeawDwqQsJfkNLrJ6Ohk__M3Nw3pNypwAse9xY11wFkj_z_J0he4jQARrqD2Opnx28087zp6-CGz-_w_rsBlpbQY5AkjALary8Syoh_ij6klqwvAFtv0I_wNyQ">\n',
        'itemprop="image" content="https://lh3.googleusercontent.com/aida-public/AB6AXuAxu5CMprBsza72a9eipJ64CIBAPooih9h_PtxV9SeBOtVKf6BJBuiGGM33Z2eozLnjnP0ztoJfYKpR24HNa7PjGg-YrQk9KV-sewQpi-UkH9lY9kSJC76ssNgioTIkgrFqx-YsM_pnlseQqNBmPUeawDwqQsJfkNLrJ6Ohk__M3Nw3pNypwAse9xY11wFkj_z_J0he4jQARrqD2Opnx28087zp6-CGz-_w_rsBlpbQY5AkjALary8Syoh_ij6klqwvAFtv0I_wNyQ">\n' + extra_meta)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("WhatsApp precise OG tags added.")
