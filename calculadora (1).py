class calculadora:
    from numeros import numeros
    from usuario import usuario
    
    def __init__(self,suma,resta,division,multiplicacion,registro):
        
        self.suma=suma
        self.resta=resta
        self.division=division
        self.multiplicacion=multiplicacion
        self.registro=registro
        
        def get_suma(self):
            return self.suma
        def set_suma(self,nueva_suma):
            nueva_suma=(self.numero_1+self.numero_2)
            self.suma=nueva_suma
            
            def get_resta(self):
                return self.resta
            def set_resta(self,nueva_resta):
                nueva_resta=(self.numero_1-self.numero_2)
                self.resta=nueva_resta
                
                def get_division(self):
                    return self.division
                def set_division(self,nueva_division):
                    nueva_division=(self.numero_1/self.numero_2)
                    self.division=nueva_division
                    
                    def get_multiplicacion(self):
                        return self.multiplicacion
                    def set_multiplicacion(self,nueva_multiplicacion):
                        nueva_multiplicacion=(self.numero_1/self.numero_2)
                        self.multiplicaion=nueva_multiplicacion
                        
                        def get_registro(self):
                            return self.registro
                        def set_registro(self):
                            print("Elije una opcion: 1. Sumar, 2.Restar, 3.Division, 4.Multiplicacion")
                            opcion=int(input("elige una opcion."))
                            if opcion==1:
                                print("resultado:",self.suma)
                            elif opcion==2:
                                print("resultado:",self.resta)
                            elif opcion==3:
                                print("resultado:",self.division)
                            elif opcion==4:
                                print("resultado:",self.multiplicacion)
                            else:
                                print("Error, tu opción no cumple con ninguna.")