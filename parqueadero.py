class Parqueadero:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, registro):
        for r in self.registros:
            if r.get_puesto() == registro.get_puesto() and r.get_estado() == "Entrada":
                print(f"ALERTA: El puesto {registro.get_puesto()} ya está ocupado.")
                return
        self.registros.append(registro)

    def registrar_salida(self, placa, hora_salida):
        for r in self.registros:
            if r.get_placa() == placa and r.get_estado() == "Entrada":
                r.set_hora_salida(hora_salida)
                print(f" Salida procesada: {placa}")
                return
        print(f"Vehículo {placa} no encontrado o ya salió.")

    def mostrar_todo(self):
        ancho = 147
        print("\n" + "=" * ancho)
        print(f"| {'CEDULA':10} | {'NOMBRE':16} | {'TIPO USUARIO':13} | {'PLACA':7} | {'TIPO CARRO':9} | {'COLOR':8} | {'PUESTO':6} | {'FECHA':10} | {'H. ENT':7} | {'H. SAL':7} | {'ESTADO':7} |")
        print("-" * ancho)
        for r in self.registros:
            r.mostrar_detalle()
        print("=" * ancho)