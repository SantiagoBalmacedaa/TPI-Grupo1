#Inicializacion de variables
jugador1 = ""
jugador2 = ""
puntaje1 = 0
puntaje2 = 0


juego = True  #La condición del bucle es que ambos jugadores no ingresen -1

#Bucle principal del juego
while juego:
    #Solicitar la opcion elegida del jugador 1
    jugador1 = input("Jugador 1, elige piedra, papel o tijera (o ingresa -1 para finalizar): ").lower()
    if jugador1 == "-1":
        juego = False
        break  # Salir del bucle si el jugador 1 ingresa -1

    #Solicitar la opcion elegida del jugador 2
    jugador2 = input("Jugador 2, elige piedra, papel o tijera (o ingresa -1 para salir): ").lower()
    if jugador2 == "-1":
        juego = False
        break  #Salir del bucle si el jugador 2 ingresa -1

    #Determinar el ganador
    if jugador1 == jugador2:
        print("Es un empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra"):
        print("Jugador 1 gana")
        puntaje1 += 1
    elif (jugador2 == "piedra" and jugador1 == "tijera") or \
         (jugador2 == "tijera" and jugador1 == "papel") or \
         (jugador2 == "papel" and jugador1 == "piedra"):
        print("Jugador 2 gana")
        puntaje2 += 1
    else:
        print("Por favor, elige piedra, papel o tijera")

    #mostrar los puntos actuales
    print(f"Puntaje ACTUAL | Jugador 1: {puntaje1}, Jugador 2: {puntaje2}")

#Mostrar el resultado final
print("Juego terminado")
print(f"Puntaje FINAL | Jugador 1: {puntaje1}, Jugador 2: {puntaje2}")
