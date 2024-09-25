#crear entrada de bienvenida e inicio de sesion
def Entrada():  
    while True:
        print("\n                 Bienvenido                ")
        print("\nSistema de Gestion de Asistencia Academica ")
        print("\n")
        print("1. Crear Usuario \n 2. Iniciar Sesion ")
        try: # verificar que solo pueda una de las 2 opciones 
            opc = int(input("")) # Necesitamos saber si ya tiene una cuenta en el sistema 
            if opc < 1 or opc > 2:
                print("Error. Opción incorrecta.")
                input("Presione cualquier tecla para volver al menú ...")
                continue  # Volver al inicio del ciclo
            return opc  
        except ValueError:
            print("Error. Opcion Inválido.")
            input("Presione cualquier tecla para volver al menú ...")

            
            
def menu():
     while True:
         print("\n                 Bienvenido                ")
         print("** Menu Sistema Gestion Asistencia  **")
         print("1.Registro de Grupos ")
         print("2.Registro de Modulos ")
         print("3.Registro de Estudiantes")
         print("4.Registro de Docentes")
         print("5. Regustro de Asistencia")
         print("6.Consulta de Informacion  ")
         print("7.Generacion de Informes ")
         print("8. Cambio Contraseña  ")
         print("9. Salir del Sistema ")

         #print(">>> opcion?", end="")
         try:
             opcion = int(input(""))
             if opcion >= 1 and opcion <=9:
                return opcion
             else:
                print("Error. Opcion No Valida.")
                input("Presione cualquier tecla para continuar.")
                  
         except ValueError:
             print("Error. Opcion no valida.")
             input("presione cualquier tecla para volver al menu ...")
    