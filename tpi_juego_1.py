
def piedra_papel_tijera():
    jugador1 = ""
    jugador2 = ""
    puntaje1 = 0
    puntaje2 = 0

    juego = True  

    while juego:
        jugador1 = input("Jugador 1, elige piedra, papel o tijera (o ingresa -1 para finalizar): ").lower()
        if jugador1 == "-1":
            juego = False
            break  

        jugador2 = input("Jugador 2, elige piedra, papel o tijera (o ingresa -1 para salir): ").lower()
        if jugador2 == "-1":
            juego = False
            break  

        if jugador1 == jugador2:
            print("Es un empate")
        elif (jugador1 == "piedra" and jugador2 == "tijera") or              (jugador1 == "tijera" and jugador2 == "papel") or              (jugador1 == "papel" and jugador2 == "piedra"):
            print("Jugador 1 gana")
            puntaje1 += 1
        elif (jugador2 == "piedra" and jugador1 == "tijera") or              (jugador2 == "tijera" and jugador1 == "papel") or              (jugador2 == "papel" and jugador1 == "piedra"):
            print("Jugador 2 gana")
            puntaje2 += 1
        else:
            print("Por favor, elige piedra, papel o tijera")

        print(f"Puntaje ACTUAL | Jugador 1: {puntaje1}, Jugador 2: {puntaje2}")

    print("Juego terminado")
    print(f"Puntaje FINAL | Jugador 1: {puntaje1}, Jugador 2: {puntaje2}")
    with open("persona.txt", "a", newline="") as file:
        file.write(f"Puntaje FINAL | Jugador 1: {puntaje1}, Jugador 2: {puntaje2}\n")
