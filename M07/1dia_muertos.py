"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

"""
Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar.
"""

"""
Tarea 1: Preparando la Oferta (Listas y Tuplas)
"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)
NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])


# 1. Modificación 1 (Listas)

ofrendas.append("Incienso copal")
ofrendas.sort()

print("Lista de ofrendas ordenada:", ofrendas)

# Respuesta #1:
# Al agregar "Incienso copal" y usar .sort(), la lista cambia.
# Los elementos quedan organizados alfabéticamente.
# También noto que el elemento que estaba en el índice 1 puede cambiar
# de posición después de ordenar la lista.
# Esto es posible porque las listas son mutables.


# 2. Modificación 2 (Tuplas)

# NIVELES_ALTAR[0] = "Gloria"

# Respuesta #2:
# Al intentar cambiar "Cielo" por "Gloria", Python genera un TypeError.
# Esto sucede porque una tupla es inmutable.
# Una vez creada, no podemos cambiar directamente sus elementos.
# La instrucción está comentada para que el resto del programa pueda ejecutarse.


# 3. Utilizar enumerate() dentro de un bucle for

print("Ofrendas y posiciones en el altar:")

for posicion, ofrenda in enumerate(ofrendas, start=1):
    print(posicion, ofrenda)

# Respuesta #3:
# enumerate() permite recorrer la lista y obtener la posición
# de cada elemento al mismo tiempo.
# start=1 hace que la numeración comience desde 1.