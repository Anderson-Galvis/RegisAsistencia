from modulo import modulos
from modulo.persistencia import cargarDat, guardarDat, CargarUser

#1cargar los datos 
User = CargarUser()
modulos.limpiarPanta
#2gestionar ingreso a la plataforma
modulos.gestionUser(User)

# Despues 
datos = cargarDat()
guar = guardarDat
modulos.menuPrin(datos)