
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
  #Acabo de agregar los codigos de mi programa para esta tarea
