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