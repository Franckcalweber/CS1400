"""
====================================================================
Mi Primera Función en Turtle
====================================================================
NOMBRE: Franck Calderon
Objetivo:

Entender cómo encapsular código en una función para reutilizarlo y 
dibujar figuras personalizadas de manera sencilla.

Corre este programa y toma captura del resultado
====================================================================
"""

import turtle

# ==================================================================
# 1. Configuración de la Pantalla y Tortuga
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Funciones y Figuras")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)


# ==================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN
# ==================================================================

# Función para 
def dibujar_figura(lados, tamaño, color_borde, color_relleno):
    """
    Dibuja cualquier polígono regular basado en el número de lados.
    
    Parámetros:
    - lados: Número de lados que tendrá la figura (ej. 3 para triángulo, 5 para pentágono).
    - tamaño: Longitud de cada lado en píxeles.
    - color_borde: Color de las líneas.
    - color_relleno: Color del interior de la figura.
    """
    
    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
    angulo = 360 / lados

    # Configuración de colores
    t.color(color_borde, color_relleno)
    t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
    for _ in range(lados):
        t.forward(tamaño)
        t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==================================================================
# 3. DEMOSTRACIÓN / PRUEBAS (Demuestra el poder de la función)
# ==================================================================

# Dibujar una estrella/triángulo (3 lados)
mover(-150, 0)
dibujar_figura(lados=3, tamaño=80, color_borde="darkgreen", color_relleno="lightgreen")

# Dibujar un pentágono (5 lados)
mover(0, 0)
dibujar_figura(lados=5, tamaño=60, color_borde="purple", color_relleno="plum")

# Dibujar un hexágono (6 lados)
mover(150, 0)
dibujar_figura(lados=6, tamaño=50, color_borde="darkblue", color_relleno="skyblue")

mover(0, -150)
t.color("darkblue", "red")  # (Color del borde, Color de relleno - los puedes ajustar si deseas - TODO 5 los colores son parametros o argumentos?)
t.begin_fill()
for _ in range(4):
    t.forward(100)  # 
    t.left(90)      # 
t.end_fill()

# ==================================================================

# 4. PREGUNTAS
# ==================================================================
"""
1.  ¿Cuantas funciones hay en este programa? Que proposito tienen? En tus propias palabras agrega comentario completo.
Hay 2 funciones creadas en este programa.
La función dibujar_figura() sirve para dibujar diferentes polígonos
regulares. Podemos cambiar la cantidad de lados, el tamaño, el color
del borde y el color del relleno sin tener que repetir todo el código.

La función mover() sirve para cambiar la posición de la tortuga sin
dibujar líneas mientras se mueve. Levanta el lápiz, mueve la tortuga
a las coordenadas indicadas y después vuelve a bajar el lápiz.

2. ¿Qué parámetro de la función 'dibujar_figura' tendrías que cambiar para hacer un octágono (8 lados)?

Tendría que cambiar el parámetro "lados" y colocar lados=8.

3 ¿En que numero de linea termina la funcion mover?

En el código original, la función mover termina en la línea 64
con la instrucción t.pendown().

4. Bajo la seccion de pruebas, intenta hacer una nueva figura sin el uso de la funcion dibujar_figura.

Agregué un cuadrado utilizando un for loop directamente, sin llamar
a la función dibujar_figura().

5. Guarda una captura de pantalla con las 4 figuras en la carpeta M06.
      
"""


pantalla.exitonclick()