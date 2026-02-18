from parqueadero import RegistroParqueadero
from clase_carro import Parqueadero

#CODIGO PRINCIPAL

sistema = Parqueadero()

carro1 = RegistroParqueadero("1020345678", "Juan García", "Administrador", "ABC123", "Sedan", "Negro", "A-01", "2026-02-16", "08:30")
carro2 = RegistroParqueadero("1020345679", "María López", "Cliente", "XYZ789", "SUV", "Blanco", "B-05", "2026-02-16", "09:15")
carro3 = RegistroParqueadero("1020345680", "Carlos Rodríguez", "Cliente", "KLM456", "Pickup", "Azul", "C-12", "2026-02-16", "10:00")
carro4 = RegistroParqueadero("1020345681", "Ana Martínez", "Cliente", "DEF321", "Hatchback", "Rojo", "A-03", "2026-02-16", "11:20")

sistema.agregar_registro(carro1)
sistema.agregar_registro(carro2)
sistema.agregar_registro(carro3)
sistema.agregar_registro(carro4)

sistema.registrar_salida("KLM456", "11:45")

sistema.mostrar_todo()