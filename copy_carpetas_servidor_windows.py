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

def host_terminal(command):
    command = f'ssh -p 30 -i C:/Users/contr/Documents/.ssh/id_rsa_new julio@deep.uv.es {command}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return set(result.stdout.split())

def scp_copy(remote_host, remote_path, local_path, ssh_port, ssh_key):
    scp_command = [
        "scp", "-r", "-P", str(ssh_port), "-i", ssh_key,
        f"{remote_host}:{remote_path}",
        local_path.replace('\\', '/')
    ]
    subprocess.run(scp_command, check=True)


ruta_local = r'D:/borrar'
ruta_origen = "/media/disk/users/julio/resol/write_fusion.py"
scp_copy(f"{username}@{hostname}", ruta_origen, ruta_local, port, key_path)