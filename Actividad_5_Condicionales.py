# Ejercicio 1
'''
print("---¿Tienes la edad suficiente para aprender a conducir?---")
edad=1
while edad!=894754388192412:
    edad=int(input("Ingresa tu edad: "))
    if edad!=894754388192412:
        if edad>=4 and edad<=79:
            if edad>=18:
                if edad==67:
                    print("Deberias estar avergonzado...")
                else:
                    print("Tienes la edad suficiente para aprender a conducir")
            else:
                if 18-edad==1:
                    print(f"Te falta 1 año para poder aprender a conducir")
                else:
                    print(f"Te faltan {18-edad} años para poder aprender a conducir")
        elif edad==0:
            print("¿Acabas de nacer y ya quieres conducir?")
        elif edad>0 and edad <4:
            print("Pero si eres un bebe, para que quieres saber")
        elif edad<0:
            print("Mmm esa edad no me suena")
        elif edad>79 and edad<100:
            print("Pues si que que tienes la edad para aprender a conducir, ¿pero no estas un poco viejo ya?")
        elif edad>=100 and edad<130:
            print("Para que quisieras aprender si basicamente estas a punto de ser un cadaver, tu familia esta esperando a reclamar tus bienes")
        elif edad>=130 and edad<300000:
            if edad==911:
                print("🏢 PUUUMMMMMM 🏢")
            else:
                print("Acaso eres un zombie o algo por el estilo?")
        elif edad>=300000 and edad<66000000:
            print("Vaya pero si eres un ser inmortal")
        elif edad>=66000000 and edad<4500000000:
            print("Estuviste desde los comienzos de la tierra, ¿como sobreviviste al meteorito de los dinosaurios?")
        elif edad>=4500000000 and edad<13800000000:
            print("La tierra ni existia pero tu si, ¿de donde vienes?")
        elif edad>=13800000000 and edad<1000000000000000:
            print("El UNIVERSO no existia, pero tu si, ¿acaso eres Dios?")
        else:
            print("No ingreses números randoms al azar, deja de llamar la atención")
'''
# Ejercicio 2
'''
edad=int(input("Ingresa tu edad: "))
mye=16
if edad>mye:
    if edad-mye==1:
        print("Eres 1 año mayor que yo")
    else:
        print(f"Eres {edad-mye} años mayor a mi")
elif edad<mye:
    if edad-mye==1:
        print("Eres 1 año menor a mi")
    else:
        print(f"Eres {-(edad-mye)} años menor a mi")
else:
    print("Wow tenemos la misma edad")
'''
# Ejercicio 3
'''
a=int(input("Ingresa el primer número: "))
b=int(input("Ingresa el segundo número: "))
if a>b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{b} es mayor que {a}")
'''
# Ejercicio 4
'''
nota=float(input("Ingrese su calificación: "))
if nota>=0 and nota<=59:
    print("Tu nota es F")
elif nota>=60 and nota<=69:
    print("Tu nota es D")
elif nota>=70 and nota<=79:
    print("Tu nota es C")
elif nota>=80 and nota<=89:
    print("Tu nota es B")
elif nota>=80 and nota<=100:
    print("Tu nota es A")
else:
    print("Calificiación invalida")
'''
# Ejercicio 5
'''
otonio=["Septiembre", "Octubre", "Noviembre"]
invierno=["Diciembre", "Enero", "Febrero"]
primavera=["Marzo", "Abril", "Mayo"]
verano=["Junio", "Julio", "Agosto"]
mes=input("Ingrese el mes (Siguiendo el siguiente formato: 'Enero', 'Febrero', etc..): ")
if mes in otonio:
    print("Estas en otoño")
elif mes in invierno:
    print("Estas en invierno")
elif mes in primavera:
    print("Estas en primavera")
elif mes in verano:
    print("Estas en verano")
else:
    print("Formato o mes invalido")
'''
#Ejercicio 6
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
print("--- Bienvenido a lista de frutas, para salir solo escribe 'Stop' ---")
while 1==1:
    fruta=input("Ingresa una fruta para añadir: ")
    if fruta in fruits:
        print("Esa fruta ya existe en la lista")
    elif fruta=="Stop":
        break
    else:
        fruits.append(fruta)
        print(fruits)
print("Saliendo del programa")
'''