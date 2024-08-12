import os

def buscar_archivos(carpeta, nombre_parcial):
    archivos_encontrados = []
    for carpeta_raiz, subcarpetas, archivos in os.walk(carpeta):
        # Buscar coincidencias en el nombre de las carpetas
        for subcarpeta in subcarpetas:
            if nombre_parcial in subcarpeta:
                archivos_encontrados.append(os.path.join(carpeta_raiz, subcarpeta))
        # Buscar coincidencias en el nombre de los archivos
        for archivo in archivos:
            if nombre_parcial in archivo:
                archivos_encontrados.append(os.path.join(carpeta_raiz, archivo))
    return archivos_encontrados

# Ejemplo de uso
carpeta = "/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io"
nombre_parcial = "RBIG4IT"
resultados = buscar_archivos(carpeta, nombre_parcial)

for resultado in resultados:
    print(resultado)


#####################

import os

def buscar_patron_en_contenido(carpeta, patron):
    archivos_con_patron = []
    for carpeta_raiz, subcarpetas, archivos in os.walk(carpeta):
        for archivo in archivos:
            archivo_path = os.path.join(carpeta_raiz, archivo)
            try:
                with open(archivo_path, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    if patron in contenido:
                        archivos_con_patron.append(archivo_path)
            except Exception as e:
                # Opcional: Puedes descomentar la siguiente línea para ver los archivos que no se pudieron leer.
                # print(f"No se pudo leer el archivo {archivo_path}: {e}")
                pass
    return archivos_con_patron

# Ejemplo de uso
carpeta = "/home/contrerasnetk/Documents/Repositories/cloudsen12.github.io"
patron = "logo-huggingface-banner"

archivos_con_patron = buscar_patron_en_contenido(carpeta, patron)

if archivos_con_patron:
    for archivo in archivos_con_patron:
        print(archivo)
else:
    print("No se encontró el patrón en ningún archivo.")
