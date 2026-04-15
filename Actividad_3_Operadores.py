'''
Samuel
12/4/2026
Operadores
'''
import math
edad=16
est=float(1.72)
area_triangulo=(0.5*float(input("Ingrese la base del triangulo: "))*float(input("Ingrese la altura del triangulo: ")))
perimetro_triangulo=(float(input("Ingrese el lado a del triangulo: "))+float(input("Ingrese el lado b del triangulo: "))+float(input("Ingrese el lado c del triangulo: ")))
longitud, ancho=(float(input("Ingrese la longitud del rectangulo: "))), (float(input("Ingrese el ancho del rectangulo: ")))
area_rectangulo=longitud*ancho
perimetro_rectangulo=2*(longitud+ancho)
radio=float(input("Ingrese el radio del circulo: "))
area_circulo=math.pi*(radio**2)
circunferencia_circulo=2*math.pi*radio
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente=(y2-y1)/(x2-x1)
distancia_euclidiana=math.sqrt((x2-x1)**2+(y2-y1)**2)
x=float(input("Ingrese un valor para x: "))
y_resultado=(x**2)+(6*x)+9
python=len("python")
dragon=len("dragón")
comparacion_longitud=python == dragon
on_en_ambos="on" in "python" and "on" in "dragón"
jerga_en_oracion="jerga" in "Espero que este curso no esté lleno de jerga."
longitud_float=float(python)
longitud_string=str(longitud_float)
verificacion_division=int(7 // 3) == int(2.7)
comparacion_tipos=type("10") == type(10)
pago_total=float(input("Ingrese las horas trabajadas:"))*float(input("Ingrese la tarifa por hora: "))
segundos_vividos=float(input("Ingrese el número de años que ha vivido: "))*365*24*60*60
for i in range(1,6):
    print(i, i**0, i**1, i**2, i**3)