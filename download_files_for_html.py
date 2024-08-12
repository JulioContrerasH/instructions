import os
import requests
from bs4 import BeautifulSoup

# Ruta al archivo HTML
html_file_path = '/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/old_pages/code/soft_causality/ISP - Causality software.html'

# Ruta al directorio de destino para guardar los archivos descargados
download_directory = '/home/contrerasnetk/Documents/Repositories/Web_site_legacy/code/soft_causality'

# Extensiones de archivos a buscar
file_extensions = ['.zip', '.ZIP', '.tar', '.TAR', '.tar.gz', '.TAR.GZ', '.rar', '.RAR', '.mkv', '.MKV', '.pdf', '.PDF', '.mp4', '.MP4', '.m', '.M', '.ps', '.gz', '.PS', '.PS.gz', '.PS.GZ', '.ps.gz', '.txt', '.TXT', '.eps', '.EPS']

# Asegurar que el directorio de destino exista
os.makedirs(download_directory, exist_ok=True)

# Leer el contenido del archivo HTML
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analizar el contenido HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Función para descargar archivos, ignorando la verificación del certificado SSL
def download_file(url, download_path):
    try:
        response = requests.get(url, stream=True, verify=False)  # Ignorar la verificación del certificado SSL
        response.raise_for_status()
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Descargado: {url} a {download_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")

# Función para manejar la lógica de descarga
def handle_downloads(href):
    if any(href.lower().endswith(ext.lower()) for ext in file_extensions):  # Comparación sin distinción de mayúsculas y minúsculas
        file_name = os.path.basename(href)
        download_path = os.path.join(download_directory, file_name)
        if not os.path.exists(download_path):
            download_file(href, download_path)
        else:
            print(f"Archivo ya existe: {download_path}, saltando...")

# Encontrar todas las etiquetas <a> con los enlaces de archivos
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    handle_downloads(href)

# Encontrar todas las etiquetas <source> dentro de <video> con los enlaces de archivos
for source_tag in soup.find_all('source', src=True):
    src = source_tag['src']
    handle_downloads(src)

print("Descargas completas.")
