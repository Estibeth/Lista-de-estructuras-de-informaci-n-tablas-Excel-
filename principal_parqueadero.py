from user_parqueadero import RegistroParqueadero
from parqueadero import Parqueadero
import clase_carro

def iniciar_programa():
    clase_carro.imprimir_bienvenida()

    sistema = Parqueadero()

    cliente1 = RegistroParqueadero("1020345678", "Juan García", "Administrador", "ABC123", "Sedan", "Negro", "A-01", "2026-02-16", "08:30")
    cliente2 = RegistroParqueadero("1020345679", "María López", "Cliente", "XYZ789", "SUV", "Blanco", "B-05", "2026-02-16", "09:15")
    cliente3 = RegistroParqueadero("1020345680", "Carlos Rodríguez", "Cliente", "KLM456", "Pickup", "Azul", "C-12", "2026-02-16", "10:00")
    cliente4 = RegistroParqueadero("1020345681", "Ana Martínez", "Cliente", "DEF321", "Hatchback", "Rojo", "A-03", "2026-02-16", "11:20")

    sistema.agregar_registro(cliente1)
    sistema.agregar_registro(cliente2)
    sistema.agregar_registro(cliente3)
    sistema.agregar_registro(cliente4)

    sistema.registrar_salida("KLM456", "11:45")

    sistema.mostrar_todo()

if __name__ == "__main__":
    iniciar_programa()