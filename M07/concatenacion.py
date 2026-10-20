"""
M7 Laboratorio presencial:
Elije una pareja para entrevistar.
La concatenación de cadenas para aprender a usar + y unir cadenas de texto.
Incluir espacios manualmente (" "), y combinar entrada del usuario con otros textos.
"""

# Tarea 1: Bienvenida

print("¡Bienvenido al programa de entrevista musical!")


# Tarea 2: Solicitar los datos
# IMPORTANTE: Aquí se definen las variables ANTES de utilizarlas.

nombre = input("Escribe tu primer nombre: ")

segundo_nombre = input(
    "Escribe tu segundo nombre (presiona Enter si no tienes): "
)

apellido = input("Escribe tu primer apellido: ")

segundo_apellido = input(
    "Escribe tu segundo apellido (presiona Enter si no tienes): "
)

cancion = input("Escribe tu canción favorita: ")


# Validar que los campos obligatorios no estén vacíos

if not nombre.strip():
    print("Por favor, escribe tu primer nombre.")
    exit()

if not apellido.strip():
    print("Por favor, escribe tu primer apellido.")
    exit()

if not cancion.strip():
    print("Por favor, escribe el nombre de una canción que te guste.")
    exit()


# Formatear los datos ingresados

nombre = nombre.strip().capitalize()
segundo_nombre = segundo_nombre.strip().capitalize()

apellido = apellido.strip().capitalize()
segundo_apellido = segundo_apellido.strip().capitalize()

cancion = cancion.strip().title()


# Tarea 3: Crear el nombre completo utilizando concatenación

nombre_completo = nombre

# Agregar segundo nombre solamente si existe
if segundo_nombre:
    nombre_completo = nombre_completo + " " + segundo_nombre

# Agregar primer apellido
nombre_completo = nombre_completo + " " + apellido

# Agregar segundo apellido solamente si existe
if segundo_apellido:
    nombre_completo = nombre_completo + " " + segundo_apellido


# Tarea 4: Mostrar el nombre completo

print("Tu nombre completo es " + nombre_completo + ".")


# Tarea 5: Crear un mensaje usando concatenación

mensaje_final = (
    "Hola "
    + nombre_completo
    + ", me encanta que tu canción favorita sea "
    + cancion
    + "!"
)

# Imprimir a la terminal

print(mensaje_final)

