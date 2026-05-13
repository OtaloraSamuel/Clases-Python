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
num=num.replace(" ", "")
num=num.replace("-","")
print(num)
'''