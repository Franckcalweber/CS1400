
# ============================================================
# TAREA: ENTRADA Y SALIDA DE ARCHIVOS
# PARTE 2: SUMA DE NÚMEROS
# ============================================================

# PREGUNTA 7:
# ¿Cuál es el resultado de la suma de los números proporcionados?
#
# RESPUESTA:
# La suma total es 179.
#
# 0 + 1 + 12 + 35 + 8 + 13 + 21 + 34 + 55 = 179


# PREGUNTA 8:
# Si agregas la palabra "Python" al archivo de texto,
# ¿qué error muestra el programa?
#
# RESPUESTA:
# El programa genera un ValueError porque la palabra
# "Python" no puede convertirse a un número entero.
#
# El mensaje será:
# invalid literal for int() with base 10: 'Python'
#
# El bloque except captura el error y lo muestra
# en pantalla sin producir un cierre abrupto.


# PREGUNTA 9:
# ¿Por qué es necesario usar .strip() antes de
# convertir una línea a número?
#
# RESPUESTA:
# El método .strip() elimina espacios en blanco
# y saltos de línea al principio y al final del texto.
#
# Esto ayuda a limpiar los datos antes de convertirlos
# a números y evita problemas de formato.
#
# Aunque int() acepta ciertos espacios en blanco,
# usar .strip() es una buena práctica.


# PREGUNTA 10:
# Si el archivo tiene 9 números, ¿cuántas veces
# se ejecuta el bloque dentro del for?
#
# RESPUESTA:
# El bloque for se ejecuta 9 veces, una por cada
# línea del archivo que contiene un número.


# ============================================================
# CÓDIGO FUNCIONAL - PARTE 2
# ============================================================

try:
    suma = 0

    # Abrir archivo numeros.txt en modo lectura
    archivo = open('numeros.txt', 'r')

    # Recorrer cada línea del archivo
    for line in archivo:

        # Eliminar espacios y convertir a entero
        num = int(line.strip())

        # Mostrar el número
        print(num)

        # Agregar el número a la suma
        suma += num

    # Mostrar el total
    print(f"Total: {suma}")

    # Cerrar el archivo
    archivo.close()

except Exception as err:
    print(err)
