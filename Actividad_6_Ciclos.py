# Ejercicio 1
'''
n=1
num=1
suma=0
num=int(input("Ingrese un número entero positivo: "))
while num<1:
    print("Numero invalido")
    num=int(input("Ingrese un número entero positivo: "))
while n<=num:
    suma+=n
    n+=1
print(f"El total de la suma es: {suma}")
'''
# Ejercicio 2
'''
cant=0
suma=0
while True:
    precio=int(input("Ingrese el precio del producto: "))
    if precio<1:
        break
    else:
        cant+=1
        suma+=precio
print(f"Cantidad de productos: {cant} \nSuma total de las compras: {suma} \nRegistro de compras finalizado")
'''
# Ejercicio 3
'''
n=0
num=int(input("Ingrese un número entero positivo: "))
while num<1:
    print("Numero invalido")
    num=int(input("Ingrese un número entero positivo: "))
while n<=num:
    if n%5==0:
        n+=1
        continue
    else:
        print(n)
        n+=1
'''