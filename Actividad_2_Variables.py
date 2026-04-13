'''
Samuel
10/04/2026
Variables
'''
import math
nombre, apellido, nombreCompleto, pais, ciudad, edad, anio, estaCasado, esVerdadero, luzEncendidad=("Samuel", "Otálora", "Samuel Otálora", "Ecuador", "Quito", "16", "2026", True, True, False)
lista=["Samuel", "Otálora", "Samuel Otálora", "Ecuador", "Quito", "16", "2026", True, True, False]
for i in lista:
    print(type(i))
print(len(nombre))
print(f'La variable nombre tiene {len(nombre)} letras, y la variable apellido tiene {len(apellido)} letras')
numeroUno, numeroDos=(5, 4)
total, diferencia, producto, division, residuo, potencia, divisionEntera=(numeroDos+numeroUno, numeroUno-numeroDos, numeroUno*numeroDos, numeroUno/numeroDos, numeroDos%numeroUno, numeroUno**numeroDos, numeroUno//numeroDos)
areaCirculo=(math.pi*float(input("Ingresa el valor del radio del circulo  \n"))**2)
print(f'El area de tu circulo es de {areaCirculo}')
circunferenciaCirculo=(2*math.pi*float(input("Ingresa el valor del radio del circulo  \n")))
print(f'La circunferencia de tu circulo es de {circunferenciaCirculo}')
nombre_usuario, apellido_usuario, pais_usuario, edad_usuario=(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), input("Ingresa tu pais: "), input("Ingresa tu edad: "))