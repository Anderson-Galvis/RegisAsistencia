import json
from pathlib import Path 

def cargarDat(arch='datos.json'):
    #Carga los datos existentes desde el archivo JSON."""
    if Path(arch).is_file():
        try:
            with open(arch, 'r') as fd:
                datos = json.load(fd)
            if datos is None or not isinstance(datos, dict):
                raise ValueError("Archivo vacio o datos no validos ")
            return datos
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return {
                "estudiantes": {},
                "profesores": {},
                "modulo": {},
                "grupo": {}
            }

def guardarDat(datos, arch ='datos.json'):
    #Guarda los datos en el archivo JSON."""
    try:
     with open(arch, 'w') as fd:
           json.dump(datos, fd, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def CargarUser():
    try:   
        with open('User.json', 'r') as archivo:
            User =json.load(archivo)
            return User
    except(FileExistsError,Exception):
        return {}
               
def guardarUser(User):
    with open('User.json','w') as archivo:
        json.dump(User,archivo, indent=4)
        

            
    