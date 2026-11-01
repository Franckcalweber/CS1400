# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.


# TODO #3 Agregar comentarios a cada función explicando qué hace y cómo funciona.


def agregar_producto(inventario, nombre, precio):
    """
    Agrega un producto nuevo al inventario o actualiza su precio
    si el producto ya existe.

    Recibe el diccionario inventario, el nombre del producto y su precio.
    El precio se convierte a float para asegurar que sea un número.

    Si el precio es válido, el producto se guarda en el diccionario
    y la función devuelve True.

    Si el precio no puede convertirse a número, se genera un ValueError,
    el cual es capturado con try/except, y la función devuelve False.
    """

    try:
        # Convertimos el precio recibido a float para asegurar
        # que sea un valor numérico.
        precio_num = float(precio)

        # Agregamos el producto al diccionario.
        # Si ya existe, su precio será actualizado.
        inventario[nombre] = precio_num

        # True indica que el producto se guardó correctamente.
        return True

    except ValueError:
        # Si el precio contiene letras u otro valor que no puede
        # convertirse a float, capturamos el ValueError.
        return False


def buscar_precio(inventario, nombre):
    """
    Busca el precio de un producto dentro del inventario.

    Recibe el diccionario inventario y el nombre del producto.
    Utiliza el método .get() para buscar el producto sin provocar
    un error si la llave no existe.

    Si encuentra el producto, devuelve su precio.
    Si no existe, devuelve None.
    """

    # .get() devuelve el precio si encuentra el producto.
    # Si no existe, devuelve None.
    return inventario.get(nombre, None)


def listar_productos(inventario):
    """
    Muestra todos los productos almacenados en el inventario.

    Primero verifica si el diccionario está vacío.
    Si está vacío, muestra un mensaje informando al usuario.

    Si contiene productos, utiliza un ciclo for junto con .items()
    para recorrer los nombres y precios y mostrarlos en pantalla.
    """

    # Verificamos si el diccionario está vacío.
    if not inventario:
        print("\n> El inventario está vacío.")

    else:
        # Si existen productos, mostramos el encabezado.
        print("\n--- Inventario Actual ---")

        # .items() permite obtener el nombre y el precio
        # de cada producto almacenado en el diccionario.
        for producto, precio in inventario.items():

            # :.2f muestra el precio con exactamente dos decimales.
            print(f"• {producto}: ${precio:.2f}")