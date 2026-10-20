# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida utilizando el nombre recibido."""
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")


# RESPUESTAS:
# 1. "nombre" es un parámetro de la función.
# 2. Para utilizar la función debemos llamarla y pasarle un argumento,
#    por ejemplo: mostrar_bienvenida("Ana")


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    """Calcula y retorna el precio final después de aplicar un descuento."""
    precio = float(precio)
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


def es_par(numero):
    """Determina si un número es par y retorna True o False."""
    return numero % 2 == 0


# RESPUESTAS:
# 3. La palabra clave utilizada para definir una función es: def
#
# 4. Las funciones son:
#    calcular_descuento()
#    es_par()
#
# 5. calcular_descuento(100) utiliza automáticamente el porcentaje
#    predeterminado de 10%. El resultado es 90.0.
#
# 6. calcular_descuento(200, 20) utiliza 200 como precio y 20 como
#    porcentaje. El resultado es 160.0.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")

compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# Prueba utilizando un precio decimal
compra_3 = calcular_descuento(99.99, 15)
print(f"Precio decimal con 15% de descuento: ${compra_3:.2f}")


# 7. PSEUDOCÓDIGO:
#
# calcular_descuento:
# INICIO
#     RECIBIR precio y porcentaje
#     CALCULAR descuento = precio * porcentaje / 100
#     CALCULAR precio_final = precio - descuento
#     RETORNAR precio_final
# FIN
#
# es_par:
# INICIO
#     RECIBIR numero
#     COMPROBAR si numero dividido entre 2 tiene residuo 0
#     RETORNAR True si es par o False si no es par
# FIN


# 8. PROPÓSITO:
# La función calcular_descuento recibe el precio de un producto y
# un porcentaje de descuento. Calcula el descuento y devuelve el
# precio final. Si no se especifica un porcentaje, utiliza 10%.


# 9. La función calcular_descuento acepta precios decimales
# utilizando float.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

resultado = mostrar_bienvenida("Julio")
print(resultado)


# RESPUESTAS:
#
# 10. resultado guarda None porque mostrar_bienvenida utiliza print()
#     pero no utiliza return.
#
# 11. return permite devolver el precio_final para poder almacenarlo
#     en variables como compra_1 y compra_2.
#
# 12. Al ejecutar print(descuento) fuera de la función aparece:
#     NameError: name 'descuento' is not defined
#
# 13. descuento es una variable local. Solo existe dentro de
#     calcular_descuento().
#
# 14. Si cambiamos return por print, la función muestra el resultado
#     pero devuelve None. Al intentar compra_1 + 5 aparecería un
#     TypeError porque no podemos sumar None y un número.
#
# 15. Podemos utilizar un keyword argument de esta manera:
#     calcular_descuento(200, porcentaje=20)
#
#     También podemos escribir:
#     calcular_descuento(precio=200, porcentaje=20)
#
# 16. Se agregaron docstrings dentro de las tres funciones.


# Prueba adicional de keyword argument
compra_4 = calcular_descuento(precio=150.50, porcentaje=25)
print(f"\nPrecio usando keyword arguments: ${compra_4:.2f}")


# Pruebas de es_par()
print("\n--- PRUEBA 3: Números pares ---")
print(f"¿10 es par?: {es_par(10)}")
print(f"¿7 es par?: {es_par(7)}")


# NOTA:
# Si quieres comprobar la pregunta 12, descomenta temporalmente:
# print(descuento)