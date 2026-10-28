# =============================================================
# MANEJO DE EXCEPCIONES Y CÓDIGO SEGURO EN PYTHON
# =============================================================


# =============================================================
# PARTE 1: CÓDIGO VULNERABLE A ERRORES
# =============================================================

# PREGUNTA 1:
# ¿Por qué la Operación 1 (10 / num) fallará si el usuario
# ingresa 0?
#
# RESPUESTA:
# La operación falla porque matemáticamente no es posible dividir
# un número entre cero. En Python, cuando intentamos ejecutar 10 / 0,
# se genera una excepción llamada ZeroDivisionError.
#
# ¿Por qué la Operación 2 (lst[num]) fallará si el usuario
# ingresa 100?
#
# RESPUESTA:
# La lista lst = [1, 3, 7, 3] solamente tiene cuatro elementos.
# Sus índices válidos son 0, 1, 2 y 3.
# Si intentamos acceder a lst[100], ese índice no existe y Python
# genera una excepción llamada IndexError.


# PREGUNTA 2:
# Ejecuta el programa con las entradas "dos", 0 y 100.
#
# RESPUESTAS:
#
# Entrada: "dos"
# ¿Llegó a imprimirse "El programa continuó..."? NO
# Excepción generada: ValueError
#
# Entrada: 0
# ¿Llegó a imprimirse "El programa continuó..."? NO
# Excepción generada: ZeroDivisionError
#
# Entrada: 100
# ¿Llegó a imprimirse "El programa continuó..."? NO
# Excepción generada: IndexError


# PREGUNTA 3:
# ¿Qué ocurre con las líneas de código siguientes cuando Python
# encuentra un error no capturado?
#
# RESPUESTA:
# Cuando Python encuentra una excepción que no ha sido capturada
# mediante try/except, detiene la ejecución normal del programa.
# Las instrucciones posteriores al error no se ejecutan.


# =============================================================
# PARTE 2: CONTROL DE FLUJO CON TRY / EXCEPT
# =============================================================

# PREGUNTA 4:
# Ejecuta el código e ingresa "dos".
# ¿Qué mensaje se imprime?
# ¿Se ejecuta la última línea?
#
# RESPUESTA:
# Se imprime:
# "Error: Debes ingresar un número entero válido (sin letras)."
#
# Sí, también se ejecuta:
# "El programa continúa su ejecución normal..."
#
# Esto ocurre porque el ValueError fue capturado mediante except,
# por lo que el programa puede continuar.


# PREGUNTA 5:
# Ejecuta el código e ingresa 0.
# ¿Por qué se activa "Ocurrió un error general" en lugar de
# ValueError?
#
# RESPUESTA:
# El número 0 puede convertirse correctamente a un entero,
# por lo tanto no se produce un ValueError.
#
# El problema aparece cuando Python intenta realizar 10 / 0.
# Esa operación genera un ZeroDivisionError.
#
# Como el código original no tiene un bloque específico para
# ZeroDivisionError, la excepción es capturada por el except general.


# PREGUNTA 6:
# Agrega un bloque except ZeroDivisionError.
#
# RESPUESTA:
# El bloque utilizado es:
#
# except ZeroDivisionError:
#     print("Error: No es posible dividir entre cero.")


# PREGUNTA 7:
# ¿Qué error ocurre al intentar acceder a un índice inexistente
# en una lista?
#
# RESPUESTA:
# El error se llama IndexError.
#
# El bloque para capturarlo es:
#
# except IndexError:
#     print("Error: El índice ingresado no existe en la lista.")


# PREGUNTA 8:
# Código corregido con las tres excepciones específicas.
#
# EJEMPLO:
#
# try:
#     lst = [1, 3, 7, 3]
#     num = int(input("Ingrese un número entero: "))
#
#     print(10 / num)
#     print(lst[num])
#
# except ValueError:
#     print("Error: Debes ingresar un número entero válido.")
#
# except ZeroDivisionError:
#     print("Error: No es posible dividir entre cero.")
#
# except IndexError:
#     print("Error: El índice ingresado no existe en la lista.")
#
# print("El programa continúa su ejecución normal...")


# =============================================================
# PARTE 3: TRACEBACK, RAISE Y FINALLY
# =============================================================


# PREGUNTA 9:
# En la línea:
#
# except ValueError as e:
#
# ¿Qué representa la variable e?
#
# RESPUESTA:
# La variable e representa el objeto de la excepción que fue
# capturada.
#
# Contiene información relacionada con el error ocurrido y nos
# permite obtener detalles técnicos sobre la excepción.


# PREGUNTA 10:
# ¿Qué ventaja ofrece traceback.format_tb() frente a mostrar
# solamente un mensaje amigable?
#
# RESPUESTA:
# traceback.format_tb() permite obtener información técnica sobre
# dónde ocurrió el error y la secuencia de ejecución que llevó
# hasta ese error.
#
# Esto es muy útil para los desarrolladores durante la depuración.
# Un mensaje amigable ayuda al usuario a entender el problema,
# mientras que el traceback ayuda al programador a encontrar la
# causa exacta del error.


# PREGUNTA 11:
# ¿En qué situaciones se ejecuta el bloque finally?
#
# RESPUESTA:
# El bloque finally se ejecuta al finalizar cada intento del bloque
# try, sin importar si ocurrió una excepción o si todo funcionó
# correctamente.
#
# Por ejemplo, se ejecutará:
# - Si el usuario escribe letras.
# - Si ingresa un número fuera del rango.
# - Si ingresa un número válido.


# PREGUNTA 12:
# ¿Qué función cumple la palabra clave raise?
#
# RESPUESTA:
# raise permite generar intencionalmente una excepción.
#
# En este ejercicio se utiliza cuando el número ingresado está
# fuera del rango permitido del 1 al 10.
#
# Por ejemplo:
#
# raise Exception("El número está fuera del rango permitido.")
#
# De esta manera podemos tratar una regla de validación como una
# excepción y manejarla mediante except.


# PREGUNTA 13:
# ¿Qué ocurre cuando el usuario ingresa un valor válido como 5?
#
# RESPUESTA:
# Como 5 se encuentra dentro del rango permitido de 1 a 10,
# no se ejecuta la instrucción raise.
#
# El bloque finally se ejecuta de todas maneras.
#
# Luego la condición del while deja de cumplirse, el bucle termina
# y se muestra:
#
# ¡Número válido ingresado con éxito! (5)


# =============================================================
# PARTE 4: APLICACIÓN PRÁCTICA - CALCULADORA ROBUSTA
# =============================================================


# PREGUNTA 14:
# ¿Cuál es el propósito de la instrucción break?
#
# RESPUESTA:
# break permite salir del bucle while True cuando el cálculo se
# realiza correctamente.
#
# Si ocurre algún error antes de llegar al break, el programa
# permanece dentro del bucle y permite que el usuario vuelva a
# intentarlo.


# PREGUNTA 15:
# Si el usuario ingresa n2 = 0 y selecciona la operación "/",
# ¿se ejecuta print(f"Resultado: {resultado}")?
#
# RESPUESTA:
# No.
#
# Primero Python intenta realizar la división.
#
# resultado = n1 / n2
#
# Si n2 es 0, se genera un ZeroDivisionError.
#
# En ese momento Python abandona el resto del bloque try y pasa
# directamente al bloque:
#
# except ZeroDivisionError
#
# Se muestra el mensaje de error y después se ejecuta finally.
#
# Como el programa nunca llegó al break, el bucle while True
# comienza nuevamente y permite realizar otro intento.


# PREGUNTA 16:
# ¿Qué sucedería si eliminamos el bucle while True?
#
# RESPUESTA:
# Sin el while True, el usuario solamente tendría un intento.
#
# Aunque el programa podría capturar el error y mostrar un mensaje,
# no volvería automáticamente a solicitar los números y la operación.
#
# El while True mejora la experiencia del usuario porque permite
# seguir intentando hasta completar correctamente un cálculo.


def calculadora_segura():
    print("\n--- Calculadora Robusta ---")

    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                raise ValueError("Operador no válido")

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"Resultado: {resultado}")
            break

        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

        except ValueError as e:
            if str(e) == "Operador no válido":
                print(f"Error de entrada: {e}")
            else:
                print("Error: Ingrese valores numéricos válidos.")

        except Exception as e:
            print(f"Error no esperado: {e}")

        finally:
            print("Intento de cálculo finalizado.")


calculadora_segura()




