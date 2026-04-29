name=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad:"))
puntaje=float(input("Ingrese su puntaje: "))
asist=float(input("Asistencia: "))
code=input("Ingrese su codigo de invitación: ")
name.upper()
print(f"Participante: {name}")
name.split()
"".join(name)
print(f"Caracteres del nombre: {len(name)-1}")
promedio=(puntaje+asist)/2
print(f"Promedio general: {promedio}")
if edad>=14:
    if promedio>=80:
        if code=="PYTHON2026":
            print("Acceso VIP")
        else:
            print("Acceso general")
    elif promedio>=60 and promedio<=79:
        print("Acceso con observación")
    else:
        print("No puede ingresar por bajo rendimiento")
else:
    if code=="PYTHON2026":
        print("Acceso VIP")
    else:
        print("No cumple la edad mínima")
if puntaje>=90 and asist>=90:
    print("Candidato destacado")
elif puntaje<50 or asist <50:
    print("Requiere refuerzo previo")