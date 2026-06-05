'''
def mostras_estudiante(name, grade):
    print(f"Nombre: {name}")
    print(f"Curso: {grade}")
def mensaje_final():
    print("Fin del programa")
def ejercicio():
    num=int(input("Cuantos estudiantes deseas ingresar: "))
    for i in range(num):
        nombre=input("Nombre del estudiante: ")
        curso=input("Curso del estudiante: ")
        mostras_estudiante(nombre, curso)
    mensaje_final()
ejercicio()
'''
'''
def obtener_mensaje(mensaje):
    return mensaje
def generar_nombre_completo(nombre, apellido):
    return nombre+" "+apellido
mensaje=input("Ingrese el mensaje: ")
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
print(f"{obtener_mensaje(mensaje)}, {generar_nombre_completo(nombre,apellido)}")
'''
def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def multiplicacion(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
print("-"*33)
print("***Bienvenido a la calculadora***")
while True:
    opcion=int(input('''
Ingrese que operación desea hacer:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir

Opción: '''))
    if opcion>=1 and opcion<=4:
        num1=int(input("\nIngrese el primer número: "))
        num2=int(input("Ingrese el segundo número: "))
        print("")
        print("-"*12)
        if opcion==1:
            print(f"Resultado: {suma(num1,num2)}")
        elif opcion==2:
            print(f"Resultado: {resta(num1,num2)}")
        elif opcion==3:
            print(f"Resultado: {multiplicacion(num1,num2)}")
        elif opcion==4:
            print(f"Resultado: {division(num1,num2)}")
        print("-"*12)
    elif opcion==5:
        print("")
        print("-"*16)
        print("Fin del programa")
        print("-"*16)
        print("")
        break
    else:
        print("")
        print("-"*15)
        print("Opción invalida")
        print("-"*15)
'''
def promedio(n1,n2,n3):
    prom=((n1+n2+n3)/3)
    return prom
def nota_mayor(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            n3
    else:
        if n2>n3:
            return n2
        else:
            return n3
def nota_menor(n1,n2,n3):
    if n1>n3:
        if n2>n3:
            return n3
        else:
            return n2
    else:
        if n1>n2:
            return n2
        else:
            return n1
def aprueba(n1,n2,n3):
    if promedio(n1,n2,n3)>=7:
        return True
    else:
        return False
print("\nMenú de calificaciones\n\nIngrese sus notas (0-10)\n")
n=1
while True:
    nota=int(input(f"Ingrese su {n} nota: "))
    if nota>=0 and nota<=10:
        if n==1:
            nota1=nota
        elif n==2:
            nota2=nota
        else:
            nota3=nota
        n+=1
    else:
        print("\nNota invalida, vuelva a intentarlo\n")
    if n==4:
        break
notas=[nota1,nota2,nota3]
while True:
    opcion=int(input("\n¿Que operación desea realizar?\n\n1. Calcular su promedio\n2. Mostrar la nota más alta\n3. Mostrar la nota más baja\n4. Determinar si aprueba o reprueba\n5. Salir\n\nOpción: "))
    print("")
    if opcion>=1 and opcion<=5:
        if opcion==1:
            print(f"Su promedio es: {promedio(*notas):.2f}")
        elif opcion==2:
            print(f"La nota mas alta es: {nota_mayor(*notas)}")
        elif opcion==3:
            print(f"La nota mas baja es: {nota_menor(*notas)}")
        elif opcion==4:
            if aprueba(*notas):
                print("El estudiante aprueba")
            else:
                print("El estudiante reprueba")
        else:
            print("Programa finalizado")
            break
    else:
        print("Opción invalida, vuelva a intentar")
'''