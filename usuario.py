class usuario:
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.cedula=""
        
    def get_nombre(self):
        return self.nombre
    
    def set_capturar_nombre(self,nuevo_nombre):
        nuevo_nombre=input ("Ingrese su nombre: ")
        self.nombre=nuevo_nombre
        
    def get_apellido(self):
        return self.apellido
    def set_apellido(self,nuevo_apellido):
        nuevo_apellido=input ("Digite su apellido: ")
        self.apellido=nuevo_apellido
        
    def get_cedula(Self):
        return Self.cedula
    def set_cedula(self,nueva_cedula):
        nueva_cedula=int (input("Digite tu documento: "))
        self.cedula=nueva_cedula
        