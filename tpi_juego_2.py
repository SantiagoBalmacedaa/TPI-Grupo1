import random

def frio_tibio_caliente():
    print("Bienvenido al juego de Frio, Tibio, Caliente")
    print("Intenta adivinar un número entre 1 y 20.")
    
    numero_secreto = random.randint(1, 20)
    intento = None

    while intento != numero_secreto:
        try:
            intento = int(input("Tu intento: "))
            
            diferencia = abs(numero_secreto - intento)
            
            if diferencia == 0:
                print("Caliente, Adivinaste el numero ")
                break
            elif diferencia <= 2:
                print("Muy caliente")
            elif diferencia <= 5:
                print("Tibio")
            elif diferencia <= 10:
                print("Frio")
            else:
                print("Congelado")
        except ValueError:
            print("Por favor, ingresa un numero valido.")


frio_tibio_caliente()