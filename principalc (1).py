from usuario import usuario
from calculadora import calculadora
from numeros import numeros 

usuario1 = usuario("Andrés", "1234")
numero1 = numeros(5)
numero2 = numeros(10)


calculadora1 = calculadora (numero1,numero2)


suma = calculadora1.resultado_suma
resta=calculadora1.resultado_resta
multiplicacion=calculadora1.resultado_multiplicacion
division=calculadora1.resultado_division

fecha_actual=calculadora1.get_fecha()
fecha_cambiada=calculadora1.set_fecha("2026-18-02")

#mostrar resultados
print(usuario1.mostrar_info())
print(calculadora1.mostrar_info())
print(numero1.mostrar_info())
print(numero2.mostrar_info())
print(f"suma:{suma}")
print(f"resta:{resta}")
print(f"multiplicacion:{multiplicacion}")
print(f"division:{division}")
print(f"fecha de la calculadora (antes):{fecha_actual}")
print(f"fecha de la calculadora (despues):{fecha_cambiada}")