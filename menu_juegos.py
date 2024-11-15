import sys
from multiprocessing import Process
from tpi_juego_1 import piedra_papel_tijera
from tpi_juego_2 import frio_tibio_caliente

def juego_serpiente():
    # Ejecutar el juego de la serpiente desde el archivo original
    import tpi_juego_3
    tpi_juego_3.juego_serpiente()

def juego_Esquivar():
    # Ejecutar el juego 4 desde el archivo original
    import tpi_juego_4
    tpi_juego_4.juego_Esquivar()

def menu_principal():
    while True:
        print("\nMenú de Juegos:")
        print("1. Piedra, Papel o Tijera")
        print("2. Frío, Tibio, Caliente")
        print("3. Juego de la Serpiente")
        print("4. Juedo de Esquivar")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nIniciando Piedra, Papel o Tijera...")
            piedra_papel_tijera()
        elif opcion == "2":
            print("\nIniciando Frío, Tibio, Caliente...")
            frio_tibio_caliente()
        elif opcion == "3":
            print("\nIniciando Juego de la Serpiente...")
            # Ejecutar el juego 3 en un proceso separado
            proceso = Process(target=juego_serpiente)
            proceso.start()
            proceso.join()  # Esperar a que el juego termine antes de continuar
        elif opcion == "4":
            print("\nIniciando Juego 4...")
            juego_Esquivar()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
