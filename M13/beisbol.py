class BeisbolJugador:
    def __init__(self, nombre="none", numero="none"):
        self.name = nombre
        self.number = numero
        self.batting_avg = 0.0

    def print_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número: {self.numero}")
        print(f"Promedio de bateo: {self.batting_avg}")

    def calcular_batting_promedio(self, hits, at_bats):
        if at_bats > 0:
            self.batting_promedio = hits / at_bats
        else:
            self.batting_promedio = 0.0
        return self.batting_promedio

# --- Implementación ---

# Instancia para Jugador 1
player1 = BeisbolJugador("Shohei Ohtani", "17")

# Añade otra instancia para un segundo jugador
player2 = BeisbolJugador("Aaron Judge", "99")

# Calcular e imprimir promedio del jugador 1
# Supongamos 150 hits en 500 turnos al bate
pro = player1.calcular_batting_promedio(150, 500)
print(f"El promedio de bateo de {player1.nombre} es: {pro}")

# Opcional: imprimir toda la info
player1.print_info()