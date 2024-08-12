from bs4 import BeautifulSoup
import os

# Rutas y configuración
html_md_file_path = '/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/old_pages/code/soft_causality/ISP - Causality software.html'

search_directory = '/home/contrerasnetk/Documents/Repositories/Web_site_legacy/code/soft_causality'
base_url = '/home/contrerasnetk/Documents/Repositories/Web_site_legacy/code/soft_causality'

# Extensiones de archivos a buscar
file_extensions = ['.zip', '.ZIP', '.tar', '.TAR', '.tar.gz', '.TAR.GZ', '.rar', '.RAR', '.mkv', '.MKV', '.pdf', '.PDF', '.mp4', '.MP4', '.m', '.M', '.ps', '.gz', '.PS', '.PS.gz', '.PS.GZ', '.ps.gz' '.txt', '.TXT', '.eps', '.EPS']

# Leer el contenido del archivo HTML
with open(html_md_file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Diccionario para almacenar los archivos encontrados en el directorio de búsqueda
file_paths_dict = {}

# Recorrer el directorio de búsqueda y llenar el diccionario
for root, dirs, files in os.walk(search_directory):
    for file in files:
        # Verificar si la extensión completa del archivo está en las extensiones permitidas
        for ext in file_extensions:
            if file.endswith(ext):
                file_path = os.path.join(root, file)
                file_url = os.path.join(base_url, os.path.relpath(file_path, search_directory)).replace('\\', '/')
                file_paths_dict[file] = file_url
                break

print(file_paths_dict)

# Analizar el contenido HTML
soup = BeautifulSoup(file_content, 'html.parser')

# Actualizar rutas en los atributos href y src
for tag in soup.find_all(['a', 'img', 'link', 'script', 'source']):
    src_attr = 'href' if tag.name == 'a' else 'src'
    file_path = tag.get(src_attr)
    if file_path:
        # Normalizar la ruta del archivo para asegurar coincidencias exactas
        normalized_file_path = os.path.basename(file_path)
        if normalized_file_path in file_paths_dict:
            tag[src_attr] = file_paths_dict[normalized_file_path]

# Guardar el contenido modificado en el archivo HTML
with open(html_md_file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Archivo actualizado con nuevas rutas de archivos.")
