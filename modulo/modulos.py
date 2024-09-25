



import hashlib #importamos el diccionario 
from modulo.persistencia import guardarDat, cargarDat, CargarUser, guardarUser
from modulo.interfaz import menu, Entrada

#fucnion para encriptar la contraseña 
def passwDencrip(contra):
    #creamos el objeto usando SHA-256
    sha256 = hashlib.sha256()#crea un objeto hash para sha-256
    sha256.update(contra.encode('utf-8') )# codifica la contraseña  en bytes y actualiza el hash 
    return sha256.hexdigest() #Retorna el has en formato hexadecimal 

#Creacion del usuario para su primer ingreso 
def CrearUser(User):
    print("   Crear Usuario \n ")
    try:
    
        nombre = input("Escribe Tu Nombre de Registro\n ").strip().lower()
        if nombre in User:
            print("El usuario ya esta En Uso;\n Porfavor Escribe otro Usuario")
            return User
        
        passwEncrip = passwDencrip("SISGESA")
        User[nombre] ={"contraseña": passwEncrip,"cambiada":False} #contraseña predefinida
        guardarUser(User)
        print("Usuario Creado Correctamente con la Contraseña Predefinida:""   " "SISGESA\n")
        print("Porfavor Inicie Sesión y Cambia tu Contraseña en el Primer Acceso \n")
    except Exception as e:
        print (f"Ocurrio un error al Crear el Usuario: {e}")
        input("Presione cualquier tecla para continuar...")

    return User
    # inicia sesion por primera vez en el sofware 
       
#inica la funcion en el sofwar 
def inicSesion(User):
    try:
        print("      Registro de Usuario \n")
        # Cargar los datos de usuarios
        User = CargarUser()
        userName = input("Ingresa Tú Nombre de Usuario: ").strip().lower()
        
        # Verificar si el usuario existe en los datos
        if userName not in User:
            print("Usuario Incorrecto; intenta de Nuevo \n Crea una Cuenta")
            return False
        
        intentos = 3
        while intentos > 0:
            password = input("Ingresa Tu contraseña: ")
            passwEncrip = passwDencrip(password)

            # Verificar la contraseña
            if passwEncrip == User[userName]["contraseña"]:
                if not User[userName]["cambiada"]:  # Cambiar contraseña si es el primer inicio
                    print("Es tu Primer Inicio de sesión. \nDebes cambiar tu Contraseña\n")
                    newPass = input("Ingresa tu nueva contraseña: ")
                    newPassEncrip = passwDencrip(newPass)
                    User[userName]["contraseña"] = newPassEncrip
                    User[userName]["cambiada"] = True
                    guardarUser(User)
                    print("Contraseña Cambiada Correctamente.\n")
                 # Ingreso exitoso
                    print("Inicio de Sesión Exitoso.")
                return True
            else:
                intentos -= 1
                print(f"Contraseña Incorrecta. Intente Nuevamente. Quedan {intentos} intentos.")
        
        print("Se han agotado los intentos. Regresando al inicio...")
        return False

    except Exception as e:
        print(f"Se produjo un error: {e}")
        input("Oprima una Tecla Para volver al Inicio.")
    except KeyError:
        print("Error: El usuario no existe en los datos.")
    finally:
        print("Oprima Cualquier Tecla para Continuar...")

def gestionUser (User):
    while True:
        try:
            opc = Entrada() # llamamos funcion que nos da opc 1-2
            if opc == 1:
                CrearUser(User)#nuevo usuario
                input("Presione cualquier tecla para continuar...")
                continue
            elif opc == 2: # usuarios antiguo
                if  inicSesion(User):
                    break
                else:
                    continue
            
        except ValueError:
            print("Error: Entrada no válida. Por favor, eliga una opcion correcta ")
            input("Presione cualquier tecla para continuar...")
        except Exception as e:
            print(f"ocurrio un error: {e}")
            input("Presione cualquier tecla para continuar...")
    return User

def agregarEstud(datos):
    try:
            #Agrega un estudiante a la estructura de datos."""
            cod = input("Ingrese el Codigo del Estudiante:\n ")
            if not VerifiCod(cod, datos):
                print("Error: El código ya existe. Intente de nuevo.")
                return
            nombre = input("Ingrese el nombre del estudiante:\n ")
            edad = int(input("Ingrese la edad del estudiante:\n "))
            sexo = input("Ingrese sexo Masculino/ Femenino\n").strip().lower()
            if sexo not in ['masculino','femenino']:
                raise ValueError("Sexo debe ser 'Masculino' o 'femenino'. ")
            datos["estudiantes"][cod] = {"nombre": nombre,"edad": edad,"sexo": sexo,}
            guardarDat(datos)
            print("Se Guardo el Estudiante ", nombre)    
    except ValueError as e:
        print(f"Error.{e}. Intente de Nuevo. ")
    except Exception as e:
        print(f"Error Inesperado:{e}. Intente de Nuevo.")

def agregarProfe(datos):
    try:
        """Agrega un profesor a la estructura de datos."""
        cod = input("Ingrese el Codigo del Profesor.")
        if not VerifiCod(cod, datos):
            print("Error: El Codigo ya existe en el sistema.\n Intente Otro.\n")
            return        
        nombre = input("Ingrese el nombre del profesor: ")
        cedula = int(input("Ingrese el número de cédula del profesor: "))
        datos["profesores"][cod] = {"nombre":nombre,"cedula": cedula}
        guardarDat(datos)
        print("Agregado Correctamente.")    
    except ValueError as e:
        print("Error: Debe ingresar un numero valido para la cedula.\n")
    except Exception as e:
        print(f"Error Inesperado: {e}. Intente de nuevo.")

def agregarMod(datos):
    """Agrega un módulo a la estructura de datos."""
    try:
        cod = input("Ingrese el Codigo del Modulo: ")
        if not VerifiCod(cod, datos):
            print("Error. El Codigo ya existe. Intente con Otro\n")
            return   
        nombre = input("Ingrese Nombre del módulo: ")
        duraSem = input("Ingrese la Duracion en Semanas: ")
        datos["modulo"][cod] = {"nombre": nombre, "DuracSemana": duraSem}
        guardarDat(datos)
        print("Modulo guardado correctamente.")
    except Exception as e:
        print(f"Error Inesperado: {e}. Intente de Nuevo.")
#se piden los datos para los grupos        
def agregarGrupo(datos):
    """Agrega un grupo a la estructura de datos."""
    
    try:
        cod = input("Ingrese El Codigo del Grupo: ")
        if not VerifiCod(cod, datos):
            print("Error. El Codigo ya existe en el sistema. intente otro.\n")
            return
        nomGrup = input("Ingrese Nombre del Grupo: ")
        sigla = input("Ingrese las siglas del Grupo")
        datos["grupo"][cod] = {"nombre": nomGrup,"sigla": sigla}
        guardarDat(datos)
        print("Grupo Agregado Correctamente.")
    except Exception as e:
        print(f"Error Inesperado: {e}. Intente de nuevo.\n")       
        
def VerifiCod(cod, datos):
    try:
        if (cod in datos["estudiantes"]or
            cod in datos["profesores"]or
            cod in datos["modulo"]or
            cod in datos["grupo"]):
            return False #el codigo ya exite 
        return True #el codigo no existe    
    except Exception as e:
        print(f"Error Inesperado. Intente de Nuevo.{e}\n")         

def limpiarPanta():
    print("\n" * 50)

def cambiarPsw(User):
    #Permite al usuario cambiar su contraseña si es necesario."""
    try:
        userName = input("Ingresa tu Nombre de Usuario: ").strip().lower()  # Solicitar el nombre de usuario
        if userName not in User:
            print("Usuario no encontrado.")
            return
        
        # Pregunta por la contraseña actual
        password = input("Ingresa tu contraseña actual: ")
        passwEncrip = passwDencrip(password)  # Encriptar la contraseña ingresada

        # Verificar la contraseña
        if passwEncrip == User[userName]["contraseña"]:
            # Solicitar nueva contraseña
            newPass = input("Ingresa tu nueva contraseña: ")
            newPassEncrip = passwDencrip(newPass)  # Encriptar la nueva contraseña
            User[userName]["contraseña"] = newPassEncrip  # Actualizar la contraseña
            User[userName]["cambiada"] = True  # Marcar como contraseña cambiada
            guardarUser(User)  # Guardar los cambios
            print("Contraseña Cambiada Correctamente.\n")
        else:
            print("Contraseña Incorrecta. Intente Nuevamente.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
        input("Oprima una tecla para continuar...")



def menuPrin(datos):
    while True:
        
        opcion = menu()

        try:
            if opcion == 1:
                agregarGrupo(datos)  # Llama a la función para registrar usuario
                guardarDat(datos)
            elif opcion == 2:
                agregarMod(datos)  # Llama a la función para iniciar sesión
                guardarDat(datos)
            elif opcion == 3:
                agregarEstud(datos)  # Llama a la función para agregar estudiante
                guardarDat(datos)
            elif opcion == 4:
                agregarProfe(datos)  # Llama a la función para agregar profesor
                guardarDat(datos)
            elif opcion == 5:
                agregarAsist(datos)  # Llama a la función para agregar módulo
                guardarDat(datos)
            elif opcion == 6:
                ConsutarInf(datos)  # Llama a la función para agregar grupo
            elif opcion == 7:
                generaInfor(datos)
            elif opcion == 8:
                cambiarPsw(datos)
            elif opcion == 9:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error Inesperado {e}")        
                     

