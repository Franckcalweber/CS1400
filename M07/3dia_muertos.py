# Tarea 3: Organización de calaveritas y conteo de caracteres

calaveritas = ["Alebrije", "Catrina", "Cempasúchil", "Pan de muerto", "Papel picado"]

# Filtrar palabras que tengan más de 7 letras (Método tradicional)
largas_tradicional = []
for elemento in calaveritas:
    if len(elemento) > 7:
        largas_tradicional.append(elemento)

print("Palabras largas (Tradicional):", largas_tradicional)

"""
#8. Comprensión de Listas (List Comprehension): Re-escribe el bloque de código anterior
 en una sola línea utilizando comprensión de listas para crear largas_comprehension.

#9. Utiliza una comprensión de listas para convertir todos los elementos de la lista
 calaveritas a mayúsculas usando .upper().

#10. Comprensión de Diccionarios (Dictionary Comprehension): Crea un diccionario a
 partir de  la lista calaveritas donde la llave sea el nombre del elemento y el valor
 sea la cantidad de letras que tiene esa palabra (usando la función len()).

#11. Pregunta de análisis: ¿Qué ventaja ofrece escribir la solución con comprensiones
 en lugar de usar un bucle for tradicional con un .append()?
"""

"""
Tarea 3: Organización de calaveritas y conteo de caracteres
"""

calaveritas = ["Alebrije", "Catrina", "Cempasúchil", "Pan de muerto", "Papel picado"]

# Filtrar palabras que tengan más de 7 letras (Método tradicional)
largas_tradicional = []

for elemento in calaveritas:
    if len(elemento) > 7:
        largas_tradicional.append(elemento)

print("Palabras largas (Tradicional):", largas_tradicional)


# 8. Comprensión de Listas (List Comprehension)

largas_comprehension = [elemento for elemento in calaveritas if len(elemento) > 7]

print("Palabras largas (Comprensión):", largas_comprehension)

# Respuesta #8:
# La comprensión de listas permite hacer el mismo proceso del
# bucle for anterior en una sola línea.
# Recorre cada elemento de calaveritas y solamente agrega aquellos
# cuya longitud sea mayor de 7.


# 9. Convertir todos los elementos a mayúsculas usando .upper()

calaveritas_mayusculas = [elemento.upper() for elemento in calaveritas]

print("Calaveritas en mayúsculas:", calaveritas_mayusculas)

# Respuesta #9:
# La comprensión recorre cada elemento de la lista y utiliza
# .upper() para convertir el texto a letras mayúsculas.


# 10. Comprensión de Diccionarios (Dictionary Comprehension)

conteo_caracteres = {elemento: len(elemento) for elemento in calaveritas}

print("Cantidad de caracteres:", conteo_caracteres)

# Respuesta #10:
# Esta comprensión crea un diccionario donde cada elemento
# de la lista calaveritas funciona como llave y len(elemento)
# calcula la cantidad de caracteres para utilizarla como valor.


# 11. Pregunta de análisis

# Respuesta #11:
# Una ventaja de las comprensiones es que permiten escribir
# operaciones sencillas de manera más corta y directa.
# En lugar de crear una lista vacía, utilizar un bucle for y
# agregar elementos con .append(), podemos realizar el mismo
# proceso en una sola línea.
#
# Esto puede hacer que el código sea más compacto y fácil de leer
# cuando la operación es sencilla. Sin embargo, para operaciones
# más complejas, un bucle for tradicional puede ser más claro.