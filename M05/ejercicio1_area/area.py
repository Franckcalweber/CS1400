"""
## 📗 Calcular el Área de un Círculo

### Instrucciones:
1. Importa el módulo math.
2. Declara una variable radio_circulo = 5.
3. Crea una variable booleana llamada radio_valido usando un operador de comparación para verificar que el radio sea mayor que 0.
4. Utiliza una estructura if/else para calcular el área con la fórmula (math.pi * (radio_circulo ** 2)) únicamente si el radio es válido.
5. Reto: Modifica el código para que el radio sea ingresado por el usuario mediante input() (convertido con float()) asegurando que pase las pruebas automáticas (pytest).Importa el módulo `math`.

NOMBRE: [Tu Nombre]
MODULO 5 - TAREA 1
AREA DE UN CÍRCULO
Uso de variables, importación de módulos, operadores booleanos y sentencias if/else.
"""

# Hay varias bibliotecas de Python que contienen funciones y variables predefinidas. 
# Una de ellas es 'math', que contiene el valor de pi (math.pi) y muchas otras funciones matemáticas.
import math

# TODO Tarea 1: Declarar la variable 'radio_circulo' y asignarle el valor 5
# 

# TODO Tarea 2: Crea una variable booleana llamada 'radio_valido' usando un operador de comparación.
# El radio debe ser mayor que 0 para ser válido.
radio_valido = False  # Reemplaza con tu código (ej: radio_circulo > 0)


# TODO Tarea 3: Descomenta y completa la estructura if/else para calcular y mostrar el área solo si el radio es válido.
# Si no es válido, imprime un mensaje de error. 
# if ____________:
#     area = math.pi * (radio_circulo ** 2)
#     print(f"El área del círculo es: {area}")
# else:
#     print("Error: El radio debe ser mayor que cero.")


# Salida esperada (con radio = 5):
# El área del círculo es: 78.53981633974483


# TODO Reto: Modifica la variable 'radio_circulo' para que sea el número ingresado por el usuario. 
# (Usa la función input() y recuerda convertirlo con float() para aceptar decimales). Y asegúrate de que tu estructura final cumpla con 
# todos los requisitos para que el script pase la prueba automática (pytest).