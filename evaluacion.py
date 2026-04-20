# Evaluación
# ===== PARTE A =====
# 1. Análisis de datos y código
# a) Indica el tipo de dato de cada variable.
# Respuesta:
'''
nombre -> str
edad -> int
promedio -> float
cursos -> list
'''
# b) Escribe qué mostraría el programa en pantalla.
# Respuesta:
'''
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
5
'''
# c) Explica qué hace len(nombre).
# Respuesta:
'''
len(nombre) calcula la cantidad/número de caracteres dentro de la variable por lo que daria como 
resultado 5 ya que Lucía tiene 5 letras.
'''
# 2. Comprensión conceptual
# a) ¿Qué diferencia hay entre print() e input()?
# Respuesta:
'''
print() muestra lo que tu deseas, puede ser un número, el contenido de una variable, el resultado de una
operación, una cadena de texto, etc. En la pantalla del ordenador, en la parte de la terminal al 
ejecutar la función, mientras que input() pide al usuario ingresar un dato o valor, este tambien puede
mostrar texto en la terminal sin embargo la diferencia es que en el print() solo se muestra el texto y
continua el resto del programo, en cambio en input() muestra el texto (o puede no y solo espera la 
respuesta) y se pausa el programa hasta que el usuario ingrese lo pedido por el input().
'''
# b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
# Respuesta:
'''
Pueda dar un error si se usa directamente ya que por default el valor dentro del input(), o sea el que 
ingreso el usuario, es de tipo str o sea cadena de texto por lo que al usarlo en un cálculo que sería
un tipo int o sea número, no se puede calcular un str con int, por lo que no habria que usarlo dirctamente
si no especificar que la variable dentro de input() es un int para poder calcularlo.
'''
# c) Explica la diferencia entre /, // y %.
# Respuesta:
'''
El operador'/' hace una división normal, es decir te entrega el entero junto con sus decimales, mientras
que el operador '//' te entrega solamente el valor entero de la divisón, dejando aparte los decimales,
y finalmente el operador '%' te entrega el residuo que no se pudo calcular sin que salgan decimales es
decir 5/2 es 2 con decimales, antes de pasar a los decimales, 2x2=4 y 5-4=1 el residuo que quedo, que 
se necesitan decimales para calcular, es el 1, ese valor entruega el operador '%'.
'''
# d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
# Respuesta:
'''
En git bash, puedes colocar el comando 'python --version' y podras verificar la versión que estas
usando, tambien el la terminal de vs code puedes colocar la misma instrucción para verificarlo.
'''
# e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
# Respuesta:
'''
En la terminal de vs code puedes colocar la instrucción "help('keywords')", y esta te dara las
palabras reservadas de python.
'''
# ===== PARTE B =====
# 3. Corrección de código
'''
ancho = int(input("Ingrese el ancho del terreno: "))
largo = int(input("Ingrese el largo del terreno: "))
precio = int(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: ", area)
print("Costo estimado: ", costo)
'''
# a) ¿Cuáles eran los errores principales?
# Respuesta: 
'''
Los errores principales fueron que en los input() no se especifico que debian ser variables tipo int
por lo que saldria error al calcular por default los input() que son str con int, y otro error mayor
fue que en vez de una coma para separar en los print() pusieron signos + que estarian sumando str con
int lo que tambien causaria un error.
'''
# b) ¿Por qué tu corrección sí permite obtener resultados válidos?
# Respuesta:
'''
Por que especifica de manera adecuada el tipo de cada variable permitiendo hacer calculos y tambien
permite adjuntar a un str un valor int en el print() permitiendo mostrar los resultados.
'''
# 4. Construcción breve
# Respuesta:
'''
frase="Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
frase=frase.replace("Tecnología", "Programación")
frase=frase.split()
'''
# ===== PARTE C =====
# 5. Desarrolla un programa
nombre, apellido, pais, ancho_de_la_pared, alto_de_la_pared, precio_por_metro_cuadrado=input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su país: "), int(input("Ingrese el ancho de la pared: ")), int(input("Ingrese el alto de la pared: ")), int(input("Ingrese el precio por metro cuadrado"))
area_de_la_pared=ancho_de_la_pared*alto_de_la_pared
costo_total_estimado=area_de_la_pared*precio_por_metro_cuadrado
nombre_completo=nombre+" "+apellido
print(f'---Reporte Final---\nNombre completo: {nombre_completo}\nPaís: {pais}\nArea de la pared: {area_de_la_pared}\nCosto total estimado: {costo_total_estimado}')
print(f'---Adicional---\n{nombre_completo.upper()}\nLongitud de tu nombre completo: {len(nombre_completo)}\nLetra "a" en tu nombre completo: {"a" in nombre_completo}\nCosto total mayor a 100: {costo_total_estimado>100}')