
"""
Actividad POO - La familia Madrigal de Encanto
Ejercicios 1 al 10

Conceptos:
Herencia, polimorfismo, encapsulamiento,
clases abstractas, composicion y duck typing.
"""

from abc import ABC, abstractmethod


# --------------------------------------------------
# CLASE BASE ABSTRACTA
# --------------------------------------------------
class Madrigal(ABC):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__energia = 100

    @property
    def energia(self):
        """Permite consultar la energia sin modificarla."""
        return self.__energia

    def gastar_energia(self, cantidad):
        """Reduce la energia sin permitir valores negativos."""
        self.__energia = max(0, self.__energia - cantidad)

    def descansar(self):
        """Recupera toda la energia."""
        self.__energia = 100
        print(f"😴 {self.nombre} descansa y recupera su energia.")

    # TODO 7: comprobar si el personaje esta cansado.
    def esta_cansado(self):
        """Devuelve True cuando la energia es menor a 30."""
        return self.__energia < 30

    @abstractmethod
    def usar_don(self):
        """Cada personaje debe implementar su propio don."""
        pass

    def __str__(self):
        return (
            f"{self.nombre} ({self.edad} años) - "
            f"Energia: {self.energia}%"
        )


# --------------------------------------------------
# CLASES HIJAS
# --------------------------------------------------

# TODO 6: agregar gafas usando super().
class Mirabel(Madrigal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.tiene_gafas = True

    def usar_don(self):
        print(f"🔍 {self.nombre} demuestra su valentia.")
        self.gastar_energia(5)


class Isabela(Madrigal):

    def usar_don(self):
        print(f"🌸 {self.nombre} hace crecer flores y cactus.")
        self.gastar_energia(15)


class Luisa(Madrigal):

    def usar_don(self):
        print(f"💪 {self.nombre} levanta objetos muy pesados.")
        self.gastar_energia(25)


class Julieta(Madrigal):

    def usar_don(self):
        print(f"🍲 {self.nombre} cocina arepas que sanan heridas.")
        self.gastar_energia(10)


# TODO 9: el animo de Pepa depende de su energia.
class Pepa(Madrigal):

    def __init__(self, nombre, edad, estado_de_animo="feliz"):
        super().__init__(nombre, edad)
        self.estado_de_animo = estado_de_animo

    def gastar_energia(self, cantidad):
        super().gastar_energia(cantidad)

        if self.energia < 50:
            self.estado_de_animo = "triste"

    def usar_don(self):
        clima = {
            "feliz": "☀️ sale el sol",
            "triste": "🌧️ empieza a llover",
            "enojada": "⛈️ cae una tormenta con rayos"
        }

        print(
            f"{clima.get(self.estado_de_animo, '☁️ hay nubes')} "
            f"porque {self.nombre} esta {self.estado_de_animo}."
        )

        self.gastar_energia(15)

    def descansar(self):
        super().descansar()
        self.estado_de_animo = "feliz"


class Dolores(Madrigal):

    def usar_don(self):
        print(f"👂 {self.nombre} escucha sonidos lejanos.")
        self.gastar_energia(10)


class Camilo(Madrigal):

    def usar_don(self):
        print(f"🎭 {self.nombre} se transforma en otra persona.")
        self.gastar_energia(20)


class Antonio(Madrigal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.animales = ["jaguar", "tucan", "capibara", "coati"]

    def usar_don(self):
        print(
            f"🐆 {self.nombre} habla con los animales: "
            f"{', '.join(self.animales)}."
        )
        self.gastar_energia(10)


# TODO 9: subclase de Antonio con ceremonia y cumpleaños.
class AntonioCeremonia(Antonio):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.don_recibido = False

    def cumplir_anios(self):
        """Aumenta la edad y activa el don al cumplir 5."""
        self.edad += 1
        print(f"🎂 {self.nombre} ahora tiene {self.edad} años.")

        if self.edad >= 5 and not self.don_recibido:
            self.cumplir_ceremonia()

    def cumplir_ceremonia(self):
        """Entrega a Antonio su don de hablar con animales."""
        if self.edad >= 5:
            self.don_recibido = True
            print(f"✨ {self.nombre} recibe su don en la ceremonia.")
        else:
            print("Antonio aun no tiene edad para la ceremonia.")

    def usar_don(self):
        if self.don_recibido:
            super().usar_don()
        else:
            print(f"🔒 {self.nombre} todavia no tiene su don.")


class Bruno(Madrigal):

    def usar_don(self):
        print(f"🔮 {self.nombre} puede ver el futuro.")
        self.gastar_energia(30)


# TODO 5: nuevo personaje Abuela Alma.
class AbuelaAlma(Madrigal):

    def usar_don(self):
        print(f"🕯️ {self.nombre} protege a toda la familia.")
        self.gastar_energia(20)


# TODO 8: visitante que NO hereda de Madrigal.
class Visitante:

    def __init__(self, nombre):
        self.nombre = nombre

    def usar_don(self):
        print(f"🎩 {self.nombre} realiza un truco especial.")

    def __str__(self):
        return f"{self.nombre} - Visitante"


# --------------------------------------------------
# CLASE CASITA
# --------------------------------------------------
class Casita:

    def __init__(self):
        self.habitantes = []

    def dar_bienvenida(self, personaje):
        """Agrega un personaje a la casa."""
        self.habitantes.append(personaje)
        print(f"🏠 Bienvenido a la Casita, {personaje.nombre}.")

    def mostrar_familia(self):
        print("\n=== FAMILIA MADRIGAL ===")

        for personaje in self.habitantes:
            print(" •", personaje)

    def dia_de_milagros(self):
        """Utiliza polimorfismo y evita usar dones sin energia."""
        print("\n✨ DIA DE LOS MILAGROS ✨")

        for personaje in self.habitantes:

            # TODO 7: comprobar si esta cansado.
            # getattr permite incluir al Visitante.
            comprobar = getattr(
                personaje, "esta_cansado", None
            )

            if callable(comprobar) and comprobar():
                print(
                    f"😴 {personaje.nombre} esta cansado "
                    "y necesita descansar."
                )
                continue

            # TODO 8: duck typing.
            personaje.usar_don()


# --------------------------------------------------
# TODO 10: MENU INTERACTIVO
# --------------------------------------------------
def menu(casita):
    """Permite elegir personajes y utilizar sus dones."""

    while True:
        print("\n========== MENU ==========")
        print("1. Mostrar personajes")
        print("2. Usar don de un personaje")
        print("3. Descansar")
        print("4. Dia de los milagros")
        print("5. Cumpleaños de Antonio")
        print("6. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            casita.mostrar_familia()

        elif opcion in ("2", "3"):
            print("\nSelecciona un personaje:")

            for i, personaje in enumerate(
                casita.habitantes, start=1
            ):
                print(f"{i}. {personaje.nombre}")

            seleccion = input("Numero: ").strip()

            if not seleccion.isdigit():
                print("Debes escribir un numero.")
                continue

            indice = int(seleccion) - 1

            if indice < 0 or indice >= len(casita.habitantes):
                print("Personaje no valido.")
                continue

            personaje = casita.habitantes[indice]

            if opcion == "2":
                # El visitante no necesita energia.
                comprobar = getattr(
                    personaje, "esta_cansado", None
                )

                if callable(comprobar) and comprobar():
                    print(
                        f"{personaje.nombre} necesita descansar."
                    )
                else:
                    personaje.usar_don()
                    print(personaje)

            elif opcion == "3":
                if hasattr(personaje, "descansar"):
                    personaje.descansar()
                    print(personaje)
                else:
                    print("Este visitante no utiliza energia.")

        elif opcion == "4":
            casita.dia_de_milagros()
            casita.mostrar_familia()

        elif opcion == "5":
            for personaje in casita.habitantes:
                if isinstance(personaje, AntonioCeremonia):
                    personaje.cumplir_anios()
                    break

        elif opcion == "6":
            print("¡Gracias por visitar la Casita!")
            break

        else:
            print("Opcion invalida.")


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------
def main():

    casita = Casita()

    familia = [
        Mirabel("Mirabel", 15),
        Isabela("Isabela", 21),
        Luisa("Luisa", 19),
        Julieta("Julieta", 50),
        Pepa("Pepa", 48, estado_de_animo="enojada"),
        Dolores("Dolores", 22),
        Camilo("Camilo", 17),
        AntonioCeremonia("Antonio", 4),
        Bruno("Bruno", 52),
        AbuelaAlma("Abuela Alma", 75),
        Visitante("Visitante Magico")
    ]

    for persona in familia:
        casita.dar_bienvenida(persona)

    casita.mostrar_familia()

    # Inicia el menu interactivo.
    menu(casita)


if __name__ == "__main__":
    main()

