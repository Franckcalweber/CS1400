
# ============================================================
# TAREA: ENTRADA Y SALIDA DE ARCHIVOS
# PARTE 1: LISTA DE INTEGRANTES
# ============================================================

# PREGUNTA 1:
# ¿Cómo se llama el archivo .txt que se crea en este programa?
#
# RESPUESTA:
# El archivo se llama roster.txt.
# Se utiliza para guardar los nombres de los integrantes.


# PREGUNTA 2:
# ¿Qué objeto de Python se utiliza para leer el archivo?
#
# RESPUESTA:
# Se utiliza un objeto de archivo creado mediante la función
# open('roster.txt', 'r').
# La variable archivoRoster almacena ese objeto.


# PREGUNTA 3:
# ¿Cuál es el propósito del bucle while al leer el archivo?
#
# RESPUESTA:
# En realidad, el archivo se lee mediante un bucle for.
# El bucle while True se utiliza para mostrar el menú
# y permitir que el usuario agregue o elimine nombres
# hasta que decida salir.


# PREGUNTA 4:
# ¿Qué sucede con los datos a medida que se leen del archivo?
#
# RESPUESTA:
# Cada línea se lee, se eliminan los espacios y saltos
# de línea con .strip(), y luego el nombre se agrega
# a la lista roster mediante .append().


# PREGUNTA 5:
# ¿Qué representa la variable n?
#
# RESPUESTA:
# La variable n representa cada nombre almacenado en
# la lista roster durante el proceso de guardado.
# Se utiliza para escribir cada nombre en una línea.


# PREGUNTA 6:
# ¿Qué debe hacerse siempre con un archivo después
# de terminar de acceder a él?
#
# RESPUESTA:
# Se debe cerrar el archivo utilizando .close().
# Esto permite liberar recursos y asegurar que
# los datos se guarden correctamente.
# También se puede utilizar with open() para
# cerrarlo automáticamente.


# ============================================================
# CÓDIGO FUNCIONAL - PARTE 1
# ============================================================

roster = []

# Cargar la lista desde el archivo
try:
    archivoRoster = open('roster.txt', 'r', encoding='utf-8')

    for line in archivoRoster:
        roster.append(line.strip())

    archivoRoster.close()

except FileNotFoundError:
    print('Creando archivo para la lista.')

    archivoRoster = open('roster.txt', 'x', encoding='utf-8')
    archivoRoster.close()


# Menú principal
while True:

    print(f"\nLista: {roster}")
    print('1. Agregar Nombre\n2. Eliminar Nombre\n3. Salir')

    try:
        eleccion = int(input("Seleccion: "))

    except ValueError:
        print("Entrada no válida. Saliendo del programa.")
        break

    if eleccion == 1:
        toAdd = input('Nombre: ')
        roster.append(toAdd)

    elif eleccion == 2:
        toRemove = input('Eliminar: ')

        try:
            roster.remove(toRemove)

        except ValueError:
            print('Error al eliminar: el nombre no existe.')

    else:
        break


# Guardar la lista en el archivo
try:
    archivoRoster = open('roster.txt', 'w', encoding='utf-8')

    for n in roster:
        archivoRoster.write(n + '\n')

    archivoRoster.close()

    print("Lista guardada correctamente.")

except OSError:
    print('Error al escribir.')
