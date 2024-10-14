import os
import re
r"D:\GitHub\IPL-UV.github.io_copia\static\old_pages\data\after_effects\plone.css"
# Definir los patrones de búsqueda y reemplazo
buscar_patron = r"https://huggingface.co/datasets/isp-uv-es/Web_site_legacy/blob/main/"
reemplazar_patron = r"https://huggingface.co/datasets/isp-uv-es/Web_site_legacy/resolve/main/"

# Extensiones de archivos de texto
extensiones_texto = ['.html', '.md', '.txt', '.css', '.js', '.xml', '.json']

# Función para reemplazar en archivos
def reemplazar_en_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_nuevo = re.sub(buscar_patron, reemplazar_patron, contenido)

        if contenido != contenido_nuevo:  # Solo escribir si hay cambios
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido_nuevo)
            print(f"Reemplazos realizados en: {ruta_archivo}")
    except UnicodeDecodeError:
        print(f"Error de decodificación en {ruta_archivo}. Archivo omitido.")
    except Exception as e:
        print(f"Error al procesar {ruta_archivo}: {e}")

# Especifica el directorio raíz aquí
directorio_raiz = "D:/GitHub/IPL-UV.github.io"  # Cambia esta ruta según sea necesario

# Recorrer todos los archivos en el directorio especificado y sus subdirectorios
for directorio_actual, _, archivos in os.walk(directorio_raiz):
    for nombre_archivo in archivos:
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
        # Comprobar si el archivo tiene una extensión de texto
        if any(ruta_archivo.lower().endswith(ext) for ext in extensiones_texto):
            reemplazar_en_archivo(ruta_archivo)
