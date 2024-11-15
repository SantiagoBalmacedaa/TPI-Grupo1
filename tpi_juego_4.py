import pygame
import random

ANCHO, ALTO = 800, 600
FPS = 60
ancho_jugador, alto_jugador = 40, 40
pos_x_jugador, pos_y_jugador = ANCHO // 2, ALTO - alto_jugador - 20
color_jugador = (128, 0, 128)

radio_objeto = 15
velocidad_objeto = 5
objetos_cayendo = []

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("TPI Juego 4")
reloj = pygame.time.Clock()

fuente = pygame.font.SysFont("Courier New", 24)
fuente_grande = pygame.font.SysFont("Courier New", 36)

def dibujar_jugador(x, y):
    pygame.draw.rect(pantalla, color_jugador, (x, y, ancho_jugador, alto_jugador))

def generar_objeto_caido():
    x = random.randint(0, ANCHO - radio_objeto * 2)
    return {'x': x, 'y': 0}

def dibujar_puntaje(puntaje):
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto_puntaje, (10, 10))

def dibujar_fin_juego(puntaje):
    texto_fin_juego = fuente_grande.render("¡Has perdido!", True, ROJO)
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto_fin_juego, (ANCHO // 2 - texto_fin_juego.get_width() // 2, ALTO // 2 - 50))
    pantalla.blit(texto_puntaje, (ANCHO // 2 - texto_puntaje.get_width() // 2, ALTO // 2))

def juego_Esquivar():
    global pos_x_jugador, pos_y_jugador

    pos_x_jugador, pos_y_jugador = ANCHO // 2, ALTO - alto_jugador - 20
    objetos_cayendo.clear()  # Reiniciar los objetos cayendo para un nuevo juego

    corriendo = True
    puntaje = 0
    fin_juego = False

    while corriendo:
        pantalla.fill(NEGRO)

        dibujar_jugador(pos_x_jugador, pos_y_jugador)

        if not fin_juego:
            if random.randint(1, 6) == 1:
                objetos_cayendo.append(generar_objeto_caido())

            for objeto in objetos_cayendo:
                pygame.draw.circle(pantalla, ROJO, (objeto['x'] + radio_objeto, objeto['y'] + radio_objeto), radio_objeto)
                objeto['y'] += velocidad_objeto
                if objeto['y'] > ALTO:
                    objetos_cayendo.remove(objeto)
                    puntaje += 1

                if pos_x_jugador < objeto['x'] < pos_x_jugador + ancho_jugador or pos_x_jugador < objeto['x'] + radio_objeto * 2 < pos_x_jugador + ancho_jugador:
                    if pos_y_jugador < objeto['y'] < pos_y_jugador + alto_jugador:
                        fin_juego = True

            dibujar_puntaje(puntaje)

        else:
            dibujar_fin_juego(puntaje)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        if not fin_juego:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and pos_x_jugador > 0:
                pos_x_jugador -= 5
            if teclas[pygame.K_RIGHT] and pos_x_jugador < ANCHO - ancho_jugador:
                pos_x_jugador += 5

        pygame.display.flip()
        reloj.tick(FPS)

# Esta condición asegura que el juego no se ejecute automáticamente al ser importado.
if __name__ == "__main__":
    juego_Esquivar()
