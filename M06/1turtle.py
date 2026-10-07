""" TODO 1 agregar tu nombre fecha titulo de una manera bonita """
"Nombre: Franck Calderon"
"Fecha: 10/06/26"

# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen() # # Usamos sintaxis de punto . para acceder a la función Screen()
pantalla.bgcolor("lightblue")  # TODO 2 Cambia el color de fondo usando la función bgcolor()
pantalla.title("turtle_paint") #TODO 3 Asigna un título a la ventana usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# solo una t para hacer menos codigo despues. usaremos la t variable para usar otras funciones.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

# TODO 4 Utiliza """ """ para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6

# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("darkblue", "lightgreen")  # (Color del borde, Color de relleno - los puedes ajustar si deseas - TODO 5 los colores son parametros o argumentos?)
t.begin_fill()
# "darkblue" y "lightblue" son ARGUMENTOS.
# Son valores que estamos pasando a la función color().
# darkblue = color del borde
# lightblue = color del relleno

# TODO 6 Este for loop que hace?
# Este for loop se repite 4 veces.
# En cada repetición la tortuga avanza 100 píxeles
# y gira 90 grados hacia la izquierda.
# Al repetirlo 4 veces se forma un cuadrado.
for _ in range(4):
    t.forward(100)  # 
    t.left(90)      # 

# TODO 7 En que linea de codigo empezo el fill? o relleno?
# El relleno comienza en esta línea:
t.end_fill()

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()