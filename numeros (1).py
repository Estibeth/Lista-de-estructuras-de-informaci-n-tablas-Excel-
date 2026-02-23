class numeros:
    def __init__(self):
        self.numero_1=""
        self.numero_2=""
        
    def get_numero_1(self):
        return self.numero_1
    def set_numeros(self,numero_1):
        numero_1=input ("Digite un numero:")
        self.numero_1=numero_1
        
    def get_numero_2(self):
        return self.numero_2
    def set_numero_2(self,numero_2):
        numero_2=input ("Digite un numero: ")
        self.numero_2=numero_2