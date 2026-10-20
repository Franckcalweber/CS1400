"""
# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

#4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
 para imprimir una frase por cada ancestro.
(Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").

#5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.

#6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
#  convierte la lista flores_recibidas en un set usando la función set().

#7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron
 en el conjunto? ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?
"""
"""
Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)
"""

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = [
    "Cempasúchil",
    "Nube",
    "Cempasúchil",
    "Terciopelo",
    "Nube",
    "Cempasúchil"
]


# 4. Iteración en Diccionarios usando .items()

for ancestro, platillo in altares_familiares.items():
    print("Para", ancestro, "preparamos:", platillo)

# Respuesta #4:
# El método .items() permite recorrer las llaves y los valores
# del diccionario al mismo tiempo.
# En este caso, ancestro representa la llave y platillo representa
# el valor correspondiente.


# 5. Utilizar .keys() y .values()

print("\nNombres de los ancestros:")

for ancestro in altares_familiares.keys():
    print(ancestro)

print("\nPlatillos:")

for platillo in altares_familiares.values():
    print(platillo)

# Respuesta #5:
# .keys() permite obtener únicamente las llaves del diccionario,
# que en este caso son los nombres de los ancestros.
#
# .values() permite obtener únicamente los valores,
# que en este caso son los platillos favoritos.


# 6. Uso de Sets (Conjuntos)

flores_unicas = set(flores_recibidas)

print("\nLista original de flores:")
print(flores_recibidas)

print("\nFlores sin repetir:")
print(flores_unicas)

# Respuesta #6:
# set() convierte la lista en un conjunto.
# Los conjuntos no permiten elementos duplicados,
# por lo que cada tipo de flor aparece solamente una vez.


# 7. Reflexión

print("\nCantidad de flores en la lista original:", len(flores_recibidas))
print("Cantidad de flores diferentes:", len(flores_unicas))

# Respuesta #7:
# La lista original tenía 6 elementos.
# Después de convertirla en un set quedaron 3 elementos únicos:
# Cempasúchil, Nube y Terciopelo.
#
# Los sets son ideales para la limpieza de datos porque eliminan
# automáticamente los valores duplicados. Esto permite trabajar
# fácilmente con datos únicos sin tener que eliminar manualmente
# cada repetición.