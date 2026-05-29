# Ejercicio lista
'''
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma=0
aprob=0
for num in notas:
    suma+=num
    if num>=7:
        aprob+=1
print(f"La suma total de las notas del curso es: {suma}")
print(f"El promedio del curso es: {suma/len(notas)}")
print(f"Aprobaron {aprob} estudiantes")
print(f"No aprobaron {len(notas)-aprob} estudiantes")
'''
# Ejercicio string
'''
contrasena = "Python2026"
letras=0
numeros=0
o=0
for i in contrasena:
    if i.isalpha():
        letras+=1
    else:
        numeros+=1
    if i=="O" or i=="o":
        o+=1
print(f"La contraseña tiene {letras} letras")
print(f"La contraseña tiene {numeros} números")
print(f"La letra 'o' aparece {o} vez")
'''
# Ejercicio con set
'''
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
n=0
l=0
for i in productos:
    m=0
    n+=1
    for a in i:
        m+=1
    if m>6:
        l+=1
print(f"Hay {n} productos únicos")
print(f"{l} productos tienen mas de 6 letras")
'''
# Ejercicio con break
'''
correo=input("Ingresa tu correo: ")
name=""
for i in correo:
    if i=="@":
        break
    name+=i
print(f"Tu nombre de usuario es {name}")
'''
# Ejercicio con continue
'''
num=input("Ingresa tu número de telefono: ")
nu=""
for i in num:
    if i==" " or i=="-":
        continue
    nu+=i
print(nu)
'''
#Ejercicios de for in range
'''
notas=[1,2,3,4,5,6,7,8,9,10]
n=-1
while n<=0 or n>=11:
    n=int(input("Ingresa el número de notas que quieres ver: "))
print(n)
for i in range(n):
    print(f"Notas registradas: {notas[i]}")
'''
#Ejercicio
'''
n=int(input("Ingrese un número: "))
for i in range(n,0,-1):
    text=""
    for a in range(1,i+1):
        text+=str(a)
    print(text)
'''
#Ejercicio
'''
num=int(input("Ingrese un número: "))
inicio=int(input("Ingrese el inicio de la tabla: "))
fin=int(input("Ingrese el fin de la tabla: "))
for i in range(inicio,fin+1):
    print(f'{num}x{i}={num*i}')
'''
#Ejercicio
'''
lst=[5,8,9,7,10]
suma=0
for i in range(1,4):
    suma+=lst[i]
print(f"Promedio: {suma/3}")
'''
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Mateo"]
for i in range(0,5,2):
    print(i)
    print(f"Pareja: {estudiantes[i]}, {estudiantes[i+1]}")