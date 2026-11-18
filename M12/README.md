
## Preguntas para familia_madrigal.py
#1. ¿Qué pasaría si quitas @abstractmethod y creas un Madrigal("Alguien", 30)? Pruébalo y explica qué error aparece y por qué es útil.
Cuando la clase `Madrigal` tiene el decorador `@abstractmethod` en el método `usar_don()`, Python no permite crear directamente un objeto de esa clase.

Si intento ejecutar:

```python
persona = Madrigal("Alguien", 30)
```

Obtengo un error `TypeError`, porque `Madrigal` es una clase abstracta con un método que debe implementarse en las clases hijas.

Si elimino `@abstractmethod`, puedo crear el objeto sin ese error. Sin embargo, `usar_don()` solamente contiene `pass`, por lo que no realiza ninguna acción.

**Conclusión:** El decorador `@abstractmethod` es útil porque obliga a las clases hijas a implementar métodos importantes y evita crear objetos incompletos.

---

#2. En Casita.dia_de_milagros() solo se escribe madrigal.usar_don(). ¿Por qué no necesitamos un if para cada personaje? (Pista: polimorfismo).

Esto ocurre gracias al **polimorfismo**.

Todos los personajes heredan de `Madrigal` y tienen un método llamado `usar_don()`, pero cada personaje lo implementa de manera diferente.

Por ejemplo:

- `Mirabel` demuestra su valentía.
- `Isabela` hace crecer flores.
- `Luisa` utiliza su fuerza.
- `Bruno` puede ver el futuro.

Cuando el programa ejecuta:

```python
madrigal.usar_don()
```

Python identifica automáticamente a qué clase pertenece el objeto y ejecuta el método correspondiente.

**Conclusión:** El polimorfismo permite utilizar el mismo método con diferentes objetos sin escribir condiciones `if` para cada personaje.

---

#3. ¿Por qué la energía es __energia y no simplemente energia? Intenta hacer familia[0].energia = 500 y luego familia[0].__energia = 500. ¿Qué diferencia notas?

El atributo `__energia` utiliza **encapsulamiento**, que ayuda a proteger los datos internos de un objeto.

En la clase `Madrigal`, la energía se consulta mediante una propiedad de solo lectura:

```python
@property
def energia(self):
    return self.__energia
```

Si intento ejecutar:

```python
familia[0].energia = 500
```

Python muestra un `AttributeError` porque la propiedad `energia` no tiene un método setter.

En cambio, si ejecuto:

```python
familia[0].__energia = 500
```

Python crea un atributo nuevo llamado `__energia`, pero no modifica el atributo privado original.

Esto sucede porque Python utiliza un mecanismo llamado **name mangling**, que internamente transforma el nombre original en `_Madrigal__energia`.

Por lo tanto, aunque el nuevo atributo tenga un valor de 500, la propiedad `energia` seguirá mostrando 100 si el personaje todavía no ha gastado energía.

**Conclusión:** El encapsulamiento permite controlar cómo se modifican los atributos y ayuda a evitar cambios incorrectos.

---

#4. Si quisieras que todos los Madrigal tuvieran una “casa” (habitación), ¿en qué clase lo agregarías y por qué?

Agregaría el atributo `habitacion` dentro de la clase base `Madrigal`, específicamente en su constructor `__init__()`.

Por ejemplo:

```python
class Madrigal(ABC):
    def __init__(self, nombre, edad, habitacion):
        self.nombre = nombre
        self.edad = edad
        self.habitacion = habitacion
        self.__energia = 100
```

Lo haría porque todos los personajes heredan de `Madrigal`, así que todos podrían tener una habitación sin repetir el mismo código en cada clase hija.

**Conclusión:** La herencia permite compartir atributos y métodos entre diferentes clases, facilitando la organización y el mantenimiento del programa.

---

## Tareas para programar
#5. Agrega un nuevo personaje, por ejemplo Abuela Alma, con un don propio (como “proteger a la familia”) y añádelo a la lista familia. Observa que no tienes que cambiar nada en Casita.

#6. Modifica Mirabel para que, además, tenga un atributo tiene_gafas = True usando super().__init__(), igual que lo hace Antonio.

#7. Agrega un método esta_cansado() en Madrigal que devuelva True si la energía es menor a 30. Luego haz que dia_de_milagros() salte a quien esté cansado y diga que necesita descansar.

#8. Crea una clase Villano o Visitante que no herede de Madrigal pero tenga también usar_don(). ¿Funciona con dia_de_milagros()? ¿Qué te dice eso sobre cómo funciona Python?

#9. Crea una subclase Antonio que, al cumplir la ceremonia, reciba un don y que el método cumplir_anios() aumente la edad en uno. Después haz que Pepa cambie su estado_de_animo según su energía (si baja de 50, se pone “triste”).

#10. Haz un pequeño menú con input() donde el usuario elija un personaje y use su don, mostrando cómo baja su energía.
Un truco para motivar

Si logras agregar un personaje nuevo sin tocar la clase Casita, ¡ya entendiste el poder del polimorfismo! Esa es justamente la ventaja de la POO: añadir cosas nuevas sin romper lo que ya funciona.