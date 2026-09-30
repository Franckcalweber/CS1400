"""
M5 Laboratorio sobre Iteración

NOMBRE: Franck Calderon
ARCHIVO: bucles.py
"""


# ==========================================================
# SECCIÓN 1: ¿POR QUÉ USAR UN BUCLE?
# ==========================================================

# Código 1

print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")


# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta
# el enfoque mostrado en el Código 1?
#
# Tendríamos que escribir la misma línea 100 veces.
# Esto haría el código muy largo, repetitivo y difícil de mantener.


# 2. ¿Este enfoque manual permite adaptar el número de saludos
# dinámicamente si el usuario lo solicita?
#
# No. El número de saludos ya está escrito directamente en el código.
# Si el usuario quisiera una cantidad diferente, tendríamos que modificar
# manualmente el programa. Un bucle permite repetir según un valor variable.


# ==========================================================
# SECCIÓN 2: BUCLE while
# ==========================================================

# Código 2

respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")


# 3. Si escribimos "si" en la primera pregunta y "si" en la segunda,
# ¿pregunta una tercera vez?
#
# No. El programa finaliza después de la segunda respuesta.
# Esto sucede porque un if solo evalúa la condición una vez.
# No repite automáticamente el bloque aunque la nueva respuesta siga siendo "si".


# Modificación 1A usando while

respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")


# 4. ¿Cómo cambia el comportamiento respecto al if?
#
# El while repite el bloque mientras la condición siga siendo verdadera.
# Cada vez que el usuario escribe "si", vuelve a ejecutar el proceso y
# pregunta nuevamente.


# 5. ¿Es posible saber exactamente cuántas veces el usuario escribirá "si"?
#
# No. Depende de lo que el usuario decida ingresar durante la ejecución.
# Por eso se considera una iteración de cantidad indefinida.


# Modificación 1B: bucle infinito
#
# Si comentamos la línea que actualiza respuesta dentro del while,
# la variable nunca cambia.

# 6. ¿Qué sucede si no se actualiza la variable de control?
#
# El programa entra en un bucle infinito porque respuesta sigue siendo "si"
# y la condición nunca deja de ser verdadera.


# 7. ¿Qué combinación de teclas puede detener un bucle infinito?
#
# Ctrl + C


# ==========================================================
# SECCIÓN 3: BUCLE for Y range()
# ==========================================================

# Código 3

num = int(input("Introduce un número límite: "))

for i in range(10):
    print("Iteración:", i)


# 8. Si ingresamos 10, ¿cuántas veces se imprime "Iteración"?
#
# Se imprime 10 veces.
#
# ¿Influye el número ingresado?
# No. En este código la variable num no se usa dentro de range().
# El bucle siempre usa range(10).


# 9. Valores de i
#
# Valor inicial: 0
# Valor final: 9


# 10. ¿Se imprime el número 10?
#
# No. range(10) comienza en 0 y se detiene antes de llegar a 10.
# El límite superior de range() no se incluye.


# 11. ¿Hay diferencia entre range(10) y range(0, 10)?
#
# No. Ambos generan exactamente los mismos valores:
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# Modificación 2A

for i in range(1, num):
    print(i)


# 12. Si num = 20, ¿se detiene en 20 o en 19?
#
# Se detiene en 19 porque el límite superior no se incluye.


# 13. ¿Qué ajuste se necesita para incluir exactamente el número ingresado?
#
# Respuesta:
# range(1, num + 1)


# Modificación 2B

for i in range(2, 11, 2):
    print(i)


# 14. ¿Qué valores se imprimen?
#
# 2, 4, 6, 8, 10
#
# El tercer argumento es el paso.
# En este caso, el valor 2 hace que el bucle avance de 2 en 2.


# ==========================================================
# SECCIÓN 4: ITERACIÓN SOBRE SECUENCIAS
# ==========================================================

# Código 4

palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)


# 15. ¿Qué representa la variable letra?
#
# Representa un carácter individual de la cadena "Python"
# en cada repetición del bucle.
#
# Primero vale "P", luego "y", después "t", etc.


# 16. Comparación entre iteración directa y acceso por índices.
#
# La opción:
# for fruta in frutas:
#
# es más legible para un principiante porque accede directamente
# a cada elemento de la lista.
#
# Usar:
# for i in range(len(frutas)):
#
# requiere trabajar con índices y luego acceder usando frutas[i],
# por lo que es un poco más complejo.


# ==========================================================
# SECCIÓN 5: break Y continue
# ==========================================================

# Código 5

print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)


# 17. ¿Qué número falta en la demostración de continue?
#
# Falta el número 3.
#
# Cuando num vale 3, continue hace que Python salte el resto de esa
# iteración y continúe directamente con la siguiente.


# 18. ¿Qué números se imprimen en la demostración de break?
#
# Se imprimen:
# 1
# 2
#
# break termina completamente el bucle cuando num llega a 3.
# No continúa con 4 ni con 5.


# 19. En un while True para solicitar claves, ¿qué sentencia permite salir
# cuando la clave es correcta?
#
# break


# ==========================================================
# SECCIÓN 6: ACUMULACIÓN Y CONTEO
# ==========================================================

# Código 6

numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num

    if num > 5:
        mayores_a_cinco += 1

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)


# 20. ¿Con qué valor deben inicializarse las variables?
#
# suma_total = 0
# mayores_a_cinco = 0
#
# Deben inicializarse antes del bucle.
#
# Si se inicializan dentro del bucle, volverían a 0 en cada repetición,
# perdiendo los valores acumulados previamente.


# 21. Diferencia entre acumulador y contador.
#
# Un acumulador guarda una suma de diferentes valores.
#
# Ejemplo:
# suma_total += num
#
# Aquí se agrega el valor de num al total.
#
# Un contador aumenta normalmente de uno en uno para contar
# cuántas veces ocurre algo.
#
# Ejemplo:
# mayores_a_cinco += 1


# ==========================================================
# SECCIÓN 7: NORMALIZACIÓN CON .lower()
# ==========================================================

# Código 7

sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")


# 22. ¿Cuál es la diferencia visual entre sujeto1 y sujeto2?
#
# sujeto1 comienza con una P mayúscula.
# sujeto2 comienza con una p minúscula.
#
# El resultado inicial es:
# Diferentes
#
# Python distingue entre mayúsculas y minúsculas.


# Modificación

if sujeto1.lower() == sujeto2.lower():
    print("Iguales")
else:
    print("Diferentes")


# 23. ¿Qué resultado obtenemos?
#
# Iguales
#
# .lower() convierte todas las letras de una cadena a minúsculas.


# 24. ¿Por qué es útil .lower() en respuestas de usuario?
#
# Porque permite comparar diferentes formas de escribir la misma respuesta.
#
# Por ejemplo:
# "SI"
# "Si"
# "si"
#
# Después de usar .lower(), todas se convierten en:
# "si"
#
# Esto hace que la validación sea más flexible y evita errores por
# diferencias entre mayúsculas y minúsculas.