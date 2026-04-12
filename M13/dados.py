import random

class Player:
    # Método init
    def __init__(self):
        self.score = 0
        self.totalRoll = 0

    # Método de instancia llamado roll
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.totalRoll = dice1 + dice2
        return self.totalRoll

    def __str__(self):
        return "Score: " + str(self.score)

    def addToScore(self):
        # Añade 1 a la variable de instancia score
        self.score += 1

# --- Lógica Principal (Main) ---
player1 = Player()
player2 = Player()

playing = True
while playing:
    action = input("Presiona 'r' para lanzar o 'q' para salir: ").lower()
    if action == 'q':
        playing = False
    elif action == 'r':
        p1_result = player1.roll()
        p2_result = player2.roll()
        
        print(f"Jugador 1 lanzó: {p1_result}")
        print(f"Jugador 2 lanzó: {p2_result}")

        if p1_result > p2_result:
            player1.addToScore()
            print("¡Punto para el Jugador 1!")
        elif p2_result > p1_result:
            player2.addToScore()
            print("¡Punto para el Jugador 2!")
        else:
            print("Empate en este lanzamiento.")
        
        print(f"Marcador actual -> P1: {player1.score} | P2: {player2.score}\n")

# Determinar quién gana al final
print("--- RESULTADO FINAL ---")
if player1.score > player2.score:
    print(f"¡EL GANADOR ES EL JUGADOR 1 con {player1.score} puntos!")
elif player2.score > player1.score:
    print(f"¡EL GANADOR ES EL JUGADOR 2 con {player2.score} puntos!")
else:
    print("El juego terminó en un empate total.")