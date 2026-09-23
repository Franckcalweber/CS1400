
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
# Nombre: Franck Calderon
# M04 - Licencia de Conducir
# Este programa determina si una persona está en condiciones de conducir.

print("=== ¿ESTÁS LISTO PARA CONDUCIR? ===")

# Pedimos la información necesaria al usuario.
edad = int(input("¿Cuántos años tienes? "))

licencia = input("¿Tienes una licencia de conducir válida? (si/no): ").lower()

lentes = input("¿Tienes tus lentes contigo si los necesitas? (si/no): ").lower()

alcohol = input("¿Has tomado alcohol recientemente? (si/no): ").lower()


# La persona puede conducir si cumple con todas las condiciones de seguridad.
if edad >= 18 and licencia == "si" and lentes == "si" and not alcohol == "si":
    print("¡Todo está en orden! Puedes conducir. Maneja con cuidado 🚗")


# Si es mayor de edad pero tomó alcohol, debe entregar las llaves.
elif edad >= 18 and alcohol == "si":
    print("¡Entrega las llaves inmediatamente! 🔑")
    print("Es enserio?? Tomaste alcohol, así que hoy alguien más tendrá que conducir.")


# Si no tiene licencia O dejó los lentes, tampoco puede conducir.
elif edad >= 18 and (licencia == "no" or lentes == "no"):
    print("¡Alto ahí! Hoy no puedes conducir.")

    if lentes == "no":
        print("¡Parece que la abuela dejó los lentes en la cocina otra vez! 👓")

    if licencia == "no":
        print("Vas a manejar sin licencia? no creo. Entrega las llaves.")


# Si ninguna condición anterior se cumple, la persona es menor de edad.
else:
    print("Todavía no puedes conducir.")
    print("Eres menor de edad. Te toca ir de copiloto 😄")
# ==========================
# ANALYSIS - M04
# ==========================
#
# 1. ¿Cuántos commits hiciste?
# Hice 4 commits durante la tarea. Traté de guardar mis avances poco a poco
# en lugar de hacer un solo commit al final.
#
# 2. ¿Qué método te pareció más fácil de usar para guardar y subir tus cambios
# a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio
# Code? ¿Por qué?
# La interfaz visual de Visual Studio Code me pareció más fácil porque puedo
# ver los archivos que fueron modificados y hacer commit y push sin tener que
# recordar todos los comandos. Sin embargo, usar la terminal también me ayudó
# a entender mejor cómo funciona Git.
#
# 3. ¿Para qué sirve ejecutar el comando git status antes de empezar a trabajar
# y cómo te ayuda a saber qué archivos han sido modificados o están pendientes
# por guardar?
# El comando git status sirve para revisar el estado actual del repositorio.
# Me permite ver qué archivos fueron modificados, cuáles todavía no han sido
# agregados a un commit y si hay cambios pendientes. Es útil para saber
# exactamente qué está pasando con mis archivos.
#
# 4. ¿Por qué es fundamental descargar (git pull) los cambios más recientes
# del repositorio de la profesora antes de realizar y subir tus propias
# modificaciones al proyecto?
# Es importante hacer git pull para tener las últimas actualizaciones que la
# profesora haya agregado al repositorio, como nuevas tareas, correcciones o
# pruebas. Esto ayuda a trabajar con la versión más reciente y reduce la
# posibilidad de tener conflictos cuando suba mis propios cambios.
#
# 5. En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de
# un repositorio en GitHub y clonar (clone) un repositorio a tu computadora?
# Un fork crea una copia del repositorio original dentro de mi propia cuenta
# de GitHub. En cambio, clone descarga una copia del repositorio a mi
# computadora para que pueda trabajar con los archivos localmente.
# El fork está en GitHub y el clone está en mi computadora.
#
# 6. ¿Por qué es una buena práctica escribir mensajes claros y descriptivos
# en cada commit en lugar de usar palabras vagas como "cambios" o "listo"?
# Los mensajes descriptivos permiten saber qué se hizo en cada momento del
# proyecto. Si después aparece un error o necesito revisar una versión
# anterior, puedo identificar fácilmente qué cambios fueron realizados en
# cada commit.
#
# 7. ¿Qué tipos de mensajes agregaste?
# Agregué mensajes descriptivos relacionados con cada parte que iba
# completando, como "Agregando entradas de datos para M04",
# "Agregando condiciones para poder conducir",
# "Agregando situaciones que impiden conducir" y
# "Finalizando programa licencia de conducir M04".
#
# 8. ¿Cuál es tu sentencia preferida?
# Mi sentencia preferida fue elif porque me permite evaluar diferentes
# situaciones cuando la condición anterior no se cumple. En este programa
# la utilicé para comprobar situaciones específicas, como cuando una persona
# es mayor de edad pero ha tomado alcohol.
#
# 9. ¿Cuándo entra el programa a la segunda sentencia de tu tarea?
# El programa entra a la segunda sentencia cuando la primera condición if
# es falsa y la condición del primer elif es verdadera. En mi programa ocurre
# cuando la persona tiene 18 años o más y respondió que sí ha tomado alcohol.
# En ese caso, el programa indica que debe entregar las llaves inmediatamente.
#
# 10. ¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!
# Del README.md aprendí cómo utilizar GitHub durante el curso y cómo mantener
# organizado mi trabajo. Aprendí que primero debo hacer un fork del repositorio
# para tener mi propia copia en GitHub y después clonarlo a mi computadora.
# También aprendí la importancia de usar git status frecuentemente, hacer
# commits pequeños con mensajes descriptivos y subir mis avances con git push.
# Antes de comenzar un nuevo módulo debo obtener las actualizaciones de la
# profesora con git pull para trabajar con la versión más reciente y evitar
# conflictos. Finalmente, aprendí que debo entregar el enlace de mi propio
# fork en Canvas y no enviar un Pull Request al repositorio de la profesora.