"""
Guía de Trabajo 2: Métodos, Slicing y Matemáticas en Python

NOMBRE: Franck Calderon
MÓDULO 5
"""


# ==========================================================
# SECCIÓN 1: CONTEO INVERSO CON range()
# ==========================================================

# Código 1.1

num = int(input("Introduce el número inicial: "))

for i in range(num, 0, -1):
    print("Conteo:", i)


# ANÁLISIS

# 1. Ejecuta el programa e introduce 10.
# Inicio: 10 | Fin: 1


# 2. ¿Por qué es necesario que step sea negativo?
# Porque queremos que los números disminuyan en cada repetición.
# El -1 hace que Python vaya hacia atrás de uno en uno.


# 3. ¿Por qué el valor final se configuró en 0 si queremos terminar en 1?
# Porque range() no incluye el valor final.
# Al colocar 0 como límite, el último número que se imprime es 1.


# 4. Modifica el código para contar hacia atrás de 2 en 2
# y detenerse en 0.

# Respuesta:
# range(num, -1, -2)

# Ejemplo:
for i in range(num, -1, -2):
    print("Conteo de 2 en 2:", i)

# Nota: Esto llega exactamente a 0 cuando el número inicial es par.


# ==========================================================
# SECCIÓN 2: FUNCIONES MATEMÁTICAS DE PYTHON
# ==========================================================

import math

decNum = -34.5678
intNum = 9

print(round(decNum, 2))      # Línea A
print(round(decNum, 0))      # Línea B
print(int(decNum))           # Línea C
print(abs(decNum))           # Línea D

print(math.pow(intNum, 2))   # Línea E
print(math.sqrt(intNum))     # Línea F


# PREDICCIONES DE SALIDA

# 5. Resultado de round(decNum, 2):
# -34.57


# 6. Resultado de round(decNum, 0):
# -35.0


# 7. Resultado de int(decNum):
# -34
# int() no redondea. Elimina/trunca la parte decimal hacia cero.


# 8. Resultado de abs(decNum):
# 34.5678


# 9. Resultado de math.pow(intNum, 2):
# 81.0


# 10. Resultado de math.sqrt(intNum):
# 3.0


# ==========================================================
# SECCIÓN 3: COMPARACIÓN DE TEXTOS ASCII / UNICODE
# ==========================================================

miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)


# 11. Antes de ejecutar, ¿cuál creo que será el resultado?
# Predicción: manzana


# 12. ¿Cuál fue el resultado real?
# Resultado: manzana


# 13. ¿Por qué "manzana" fue seleccionada como la mayor?
# Python compara los caracteres de las palabras según sus valores
# Unicode. Las letras minúsculas tienen valores mayores que las
# mayúsculas en este caso. Como "m" es minúscula, tiene un valor
# mayor que "B" y "Z", por eso "manzana" es seleccionada.


# 14. Cambia max() por min(). ¿Qué valor obtienes y por qué?

miMin = min("Banano", "manzana", "Zanahoria")
print("El mínimo es:", miMin)

# Resultado: Banano
# "B" tiene un valor Unicode menor que "Z" y "m",
# por eso "Banano" es seleccionado por min().


# ==========================================================
# SECCIÓN 4: APLICACIÓN PRÁCTICA - FÍSICA Y MATEMÁTICAS
# ==========================================================

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")


# 15. Completa la asignación v =

# Respuesta:
# v = math.sqrt(20 * d)


# ==========================================================
# SECCIÓN 5: SEGMENTACIÓN DE CADENAS (SLICING)
# ==========================================================

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])


# 16. ¿Qué carácter imprime nombre[0]?
# B


# 17. ¿En qué índice se encuentra el espacio entre las palabras?
# Índice: 8


# Podemos visualizarlo así:
#
# Building Puentes
# 0123456789012345
#
# Building ocupa los índices 0 al 7.
# El espacio está en el índice 8.
# Puentes comienza en el índice 9.


# 18. Extraer exactamente la palabra "Puentes".

# Opción con 2 valores:
# nombre[9:16]

# Opción con límite implícito:
# nombre[9:]

print(nombre[9:16])
print(nombre[9:])


# ==========================================================
# SECCIÓN 6: FILTRADO E INSPECCIÓN DE CARACTERES
# ==========================================================

texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)


# 19. Si ingresamos "3 tigres en 2 árboles":
# contador_numeros = 2
#
# Los números encontrados son 3 y 2.


# 20. ¿Cómo determina Python si el carácter es un número?
# Python compara el carácter con los valores de los caracteres
# desde "0" hasta "9".
#
# caracter >= "0" comprueba que no sea menor que "0".
# caracter <= "9" comprueba que no sea mayor que "9".
#
# Si las dos condiciones son verdaderas, el carácter está
# dentro del rango de los dígitos del 0 al 9.


# ==========================================================
# SECCIÓN 7: MÉTODOS DE CADENAS (STRING METHODS)
# ==========================================================


# 21. Método .rfind('a'):
# Busca la última aparición de un carácter o texto dentro de
# una cadena y devuelve el índice donde comienza.
# Si no encuentra el texto, devuelve -1.


# 22. Método .isalpha():
# Comprueba si todos los caracteres de una cadena son letras.
# Devuelve True si todos son letras y existe al menos un carácter.
# De lo contrario, devuelve False.


# 23. Método .isdigit():
# Comprueba si todos los caracteres de una cadena son dígitos.
# Devuelve True si todos son dígitos y existe al menos un carácter.
# De lo contrario, devuelve False.