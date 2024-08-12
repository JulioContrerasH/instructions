from bs4 import BeautifulSoup
import os
import re
from PIL import Image
import shutil

# Ruta al archivo Markdown o HTML
file_path = '/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/old_pages/code/soft_causality/ISP - Causality software.html'

# Ruta al directorio de imágenes
images_base_path = '/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/images'
additional_images_path = os.path.join(images_base_path, 'adicionales')
old_images_path = '/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/old_pages/code/soft_causality/ISP - Causality software_files'
base_url_path = '/images'

# Asegurar que el directorio "adicionales" exista
os.makedirs(additional_images_path, exist_ok=True)

# Extensiones de imágenes a buscar
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']

# Leer el contenido del archivo
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    file_content = file.read()

# Diccionario para almacenar los archivos encontrados en el directorio de imágenes
image_files_dict = {}

# Recorrer el directorio de imágenes y llenar el diccionario
for root, dirs, files in os.walk(images_base_path):
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        file_path_rel = os.path.join(base_url_path, os.path.relpath(root, images_base_path), file).replace('\\', '/')
        image_files_dict[file_name.lower()] = (file_path_rel, file_ext.lower())

# Función para convertir imágenes a webp
def convert_to_webp(source_path, dest_path):
    with Image.open(source_path) as img:
        img.save(dest_path, 'webp')

# Función para actualizar la ruta de la imagen en HTML
def update_img_src(img, src):
    file_name, ext = os.path.splitext(os.path.basename(src))
    new_src, new_ext = image_files_dict.get(file_name.lower(), (None, None))
    
    if ext.lower() == '.gif':
        if new_src and new_ext == '.gif':
            img['src'] = new_src
        else:
            # Copiar el GIF a "adicionales" si no existe
            old_image_path = os.path.join(old_images_path, file_name + ext)
            if os.path.exists(old_image_path):
                new_image_path = os.path.join(additional_images_path, file_name + '.gif')
                shutil.copy2(old_image_path, new_image_path)
                new_src = os.path.join(base_url_path, 'adicionales', file_name + '.gif').replace('\\', '/')
                img['src'] = new_src
            else:
                print(f"No se encontró la imagen {old_image_path}")
    else:
        if new_src and new_ext in image_extensions:
            img['src'] = new_src
        else:
            # Convertir la imagen a webp y copiarla a "adicionales"
            old_image_path = os.path.join(old_images_path, file_name + ext)
            if os.path.exists(old_image_path):
                new_image_path = os.path.join(additional_images_path, file_name + '.webp')
                convert_to_webp(old_image_path, new_image_path)
                new_src = os.path.join(base_url_path, 'adicionales', file_name + '.webp').replace('\\', '/')
                img['src'] = new_src

# Función para actualizar la ruta de la imagen en Markdown
def update_img_src_md(src):
    file_name, ext = os.path.splitext(os.path.basename(src))
    new_src, new_ext = image_files_dict.get(file_name.lower(), (None, None))
    
    if ext.lower() == '.gif':
        if new_src and new_ext == '.gif':
            return f'![{file_name}]({new_src})'
        else:
            # Copiar el GIF a "adicionales" si no existe
            old_image_path = os.path.join(old_images_path, file_name + ext)
            if os.path.exists(old_image_path):
                new_image_path = os.path.join(additional_images_path, file_name + '.gif')
                shutil.copy2(old_image_path, new_image_path)
                new_src = os.path.join(base_url_path, 'adicionales', file_name + '.gif').replace('\\', '/')
                return f'![{file_name}]({new_src})'
            else:
                print(f"No se encontró la imagen {old_image_path}")
                return src
    else:
        if new_src and new_ext in image_extensions:
            return f'![{file_name}]({new_src})'
        else:
            # Convertir la imagen a webp y copiarla a "adicionales"
            old_image_path = os.path.join(old_images_path, file_name + ext)
            if os.path.exists(old_image_path):
                new_image_path = os.path.join(additional_images_path, file_name + '.webp')
                convert_to_webp(old_image_path, new_image_path)
                new_src = os.path.join(base_url_path, 'adicionales', file_name + '.webp').replace('\\', '/')
                return f'![{file_name}]({new_src})'
            else:
                print(f"No se encontró la imagen {old_image_path}")
                return src

# Función para mantener etiquetas específicas sin escape
def preserve_custom_tags(content):
    return re.sub(r'{{<.*?>}}', lambda m: m.group(0).replace('<', '&lt;').replace('>', '&gt;'), content)

def restore_custom_tags(content):
    return content.replace('&lt;', '<').replace('&gt;', '>')

# Verificar si el contenido es HTML o Markdown
if file_path.endswith('.html'):
    # Analizar el contenido HTML
    soup = BeautifulSoup(file_content, 'html.parser')

    # Encontrar y actualizar todas las etiquetas <img>
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            update_img_src(img, src)

    # Guardar el contenido modificado en el archivo HTML
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
else:
    # Procesar el contenido Markdown
    md_content = preserve_custom_tags(file_content)
    
    md_img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    md_content = md_img_pattern.sub(lambda match: update_img_src_md(match.group(1)), md_content)

    # Analizar el contenido Markdown con BeautifulSoup (por si hay HTML)
    soup = BeautifulSoup(md_content, 'html.parser')

    # Encontrar y actualizar todas las etiquetas <img> en HTML dentro del Markdown
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            update_img_src(img, src)

    # Restaurar las etiquetas específicas y guardar el contenido modificado en el archivo Markdown
    md_content = restore_custom_tags(str(soup))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(md_content)

print("Archivo actualizado con nuevas rutas de imágenes.")
