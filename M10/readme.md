¿Qué hace el bloque try/except ValueError? Permite manejar errores cuando el usuario introduce un dato que no puede convertirse a número. Si escribe una edad incorrecta, el programa muestra un mensaje y asigna 0 como edad para poder continuar. 

¿Qué pasaría si el usuario escribe “veinte” y quitamos ese bloque?
Python produciría un ValueError porque int("veinte") no puede convertir esa palabra a un número entero. Sin el bloque que maneja el error, el programa se detendría.


Diccionarios y funciones (los refranes)
4. ¿Por qué guardamos los refranes en un diccionario y no en una lista? ¿Qué ventaja tiene que el refrán sea la clave y el significado el valor?
Porque un diccionario permite relacionar cada refrán con su significado mediante una clave y un valor. Esto facilita encontrar directamente el significado de un refrán sin tener que buscarlo en una lista.
5. ¿Para qué sirven las funciones decir_refran() y decir_refran_especifico()? ¿En qué se diferencian?
decir_refran() selecciona un refrán al azar y muestra su significado. En cambio, decir_refran_especifico() muestra un refrán determinado que recibe como argumento. La diferencia principal es que una función elige aleatoriamente y la otra permite seleccionar uno específico.
6. Si quisieras agregar un refrán de tu propia abuela, ¿qué línea tendrías que modificar? ¿Hay que cambiar algo más?
Tendría que agregar una nueva entrada al diccionario REFRANES, siguiendo el formato "refrán": "significado". No es necesario modificar las funciones porque trabajan automáticamente con los elementos del diccionario.

Decisiones (if / elif / else)
7. En el programa, ¿qué refrán recibe una persona de 18 años? ¿Y una de 17? Explica por qué.
Una persona de 18 años recibe “Uno pone y Dios dispone”, porque cumple la condición edad >= 18.

Una persona de 17 años recibe “Haz el bien y no mires a quien”, porque no cumple ninguna de las dos condiciones anteriores y entra en el bloque else.
8. ¿Qué pasaría si cambiáramos el orden y pusiéramos primero if edad >= 18 y después elif edad >= 60? ¿Alguien recibiría alguna vez el refrán de “Agua que no has de beber”?
Las personas de 60 años o más entrarían en la primera condición porque también tienen 18 años o más. Por eso, nunca se ejecutaría el bloque elif edad >= 60 y nadie recibiría el refrán “Agua que no has de beber, déjala correr” por esa condición de edad.

API y JSON (Parte 2)
9. ¿Qué convierte json.loads() y en qué se transforma? ¿Y json.dumps(), qué hace en dirección contraria?
json.loads() convierte un texto en formato JSON en objetos de Python, como diccionarios o listas. json.dumps() hace lo contrario: convierte un objeto de Python en una cadena de texto JSON.
10. Para obtener la ciudad del usuario, escribimos datos['address']['city']. ¿Por qué necesitamos dos pares de corchetes?
Porque estamos accediendo a un diccionario dentro de otro diccionario. El primer par de corchetes obtiene el diccionario address, y el segundo obtiene el valor asociado con la clave city.
11. Hay tres tipos de error en esa parte (HTTPError, URLError y JSONDecodeError). ¿Cuál ocurriría si no tienes internet? ¿Y si el servidor responde con una página rota?
Si no hay conexión a internet, normalmente se produce URLError. Si el servidor devuelve una respuesta con un código de error HTTP, como 404 o 500, se produce HTTPError. Si devuelve contenido que no es JSON válido, puede producirse JSONDecodeError.
12. ¿Por qué es buena idea usar timeout=10 al hacer la petición?
Porque establece un límite de 10 segundos para la operación de conexión. Así evitamos que el programa espere indefinidamente si el servidor tarda demasiado o existe un problema de red.

Juego y reflexión general (Parte 3)
13. En el juego “Completa el refrán”, ¿cómo divide el programa el refrán en dos mitades? ¿Qué hacen split(), join() y //?
Primero utiliza split() para separar el refrán en una lista de palabras. Después calcula la mitad con len(palabras) // 2, donde // realiza una división entera. Finalmente, join() une las palabras de cada mitad para formar dos cadenas de texto.
14. ¿Para qué sirve el bloque if __name__ == "__main__": al final del archivo?
Sirve para ejecutar la función main() únicamente cuando el archivo Python se ejecuta directamente. Si el archivo se importa desde otro programa, las funciones estarán disponibles sin ejecutar automáticamente el programa principal.
15. Pregunta abierta: si tuvieras que agregar una cuarta parte al programa, ¿qué agregarías y qué conceptos nuevos necesitarías usar?
Agregaría una opción para que el usuario pueda escribir sus propios refranes y significados, y guardarlos para utilizarlos después. Para hacerlo necesitaría utilizar input(), diccionarios, funciones y manejo de archivos con JSON para conservar la información incluso después de cerrar el programa.