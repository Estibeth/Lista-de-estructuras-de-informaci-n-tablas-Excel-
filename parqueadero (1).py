class RegistroParqueadero:
    def __init__(self, cedula, nombre, tipo_usuario, placa, tipo_carro, color, puesto, fecha, hora_entrada):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__tipo_usuario = tipo_usuario
        self.__placa = placa
        self.__tipo_carro = tipo_carro
        self.__color = color
        self.__puesto = puesto
        self.__fecha = fecha
        self.__hora_entrada = hora_entrada
        self.__hora_salida = ""  
        self.__estado = "Entrada"

    def get_placa(self): return self.__placa
    def get_estado(self): return self.__estado
    def get_puesto(self): return self.__puesto
    def set_hora_salida(self, hora):
        self.__hora_salida = hora
        self.__estado = "Salida"

    def mostrar_detalle(self):
        h_salida = self.__hora_salida if self.__hora_salida != "" else "  --  "
        print(f"| {self.__cedula:10} | {self.__nombre:16} | {self.__tipo_usuario:13} | {self.__placa:7} | {self.__tipo_carro:9} | {self.__color:8} | {self.__puesto:6} | {self.__fecha:10} | {self.__hora_entrada:7} | {h_salida:7} | {self.__estado:7} |")