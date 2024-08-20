import random
import subprocess

# Configuración SSH
hostname = "deep.uv.es"
username = "julio"
port = 30
key_path = r"C:\Users\contr\Documents\.ssh\id_rsa_new"

# Rutas en el servidor
ruta_servidor_tm = '/media/disk/databases/LuisGomez/MSS/MSS_TM'
ruta_servidor_tm_corrected = '/media/disk/databases/LuisGomez/MSS/MSS_TM_CORRECTED'

# Ruta en tu máquina local
ruta_local = r'D:/MSS_TM'

# Obtener listas de carpetas en ambas rutas usando SSH y 'ls'
def obtener_carpetas_remotas(ruta):
    command = f'ssh -p {port} -i {key_path} {username}@{hostname} "ls -1 {ruta}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return set(result.stdout.split())

carpetas_tm = obtener_carpetas_remotas(ruta_servidor_tm)
carpetas_tm_corrected = obtener_carpetas_remotas(ruta_servidor_tm_corrected)

# Filtrar 15 carpetas que están en ambas (seleccionadas de forma aleatoria)
carpetas_comunes = random.sample(list(carpetas_tm.intersection(carpetas_tm_corrected)), 15)

# Filtrar 15 carpetas adicionales que están solo en MSS_TM (seleccionadas de forma aleatoria)
carpetas_exclusivas_tm = random.sample(list(carpetas_tm.difference(carpetas_tm_corrected)), 15)

# Combinar las carpetas seleccionadas
carpetas_seleccionadas = carpetas_comunes + carpetas_exclusivas_tm

# Función para ejecutar scp usando subprocess
def scp_copy(remote_host, remote_path, local_path, ssh_port, ssh_key):
    scp_command = [
        "scp", "-r", "-P", str(ssh_port), "-i", ssh_key,
        f"{remote_host}:{remote_path}",
        local_path.replace('\\', '/')
    ]
    subprocess.run(scp_command, check=True)

# Copiar cada carpeta seleccionada
for carpeta in carpetas_seleccionadas:
    ruta_origen = f"{ruta_servidor_tm}/{carpeta}/"
    ruta_destino = f"{ruta_local}/{carpeta}"
    scp_copy(f"{username}@{hostname}", ruta_origen, ruta_destino, port, key_path)

print("Copiado completado.")
