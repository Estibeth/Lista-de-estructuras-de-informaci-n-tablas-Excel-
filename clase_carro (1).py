class Parqueadero:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, registro):
        self.registros.append(registro)

    def registrar_salida(self, placa, hora_salida):
        for r in self.registros:
            if r.get_placa() == placa and r.get_estado() == "Entrada":
                r.set_hora_salida(hora_salida)
                return

    def mostrar_todo(self):
        print("\n" + "="*147)
        print(f"| {'CEDULA':10} | {'NOMBRE':16} | {'TIPO USUARIO':13} | {'PLACA':7} | {'TIPO CARRO':9} | {'COLOR':8} | {'PUESTO':6} | {'FECHA':10} | {'H. ENT':7} | {'H. SAL':7} | {'ESTADO':7} |")
        print("-" * 147)
        for r in self.registros:
            r.mostrar_detalle()
        print("="*147)