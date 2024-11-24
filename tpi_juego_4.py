#FALTA HACER: TRATAR DE QUE CUANDO PONGAS REINTENTAR SE PUEDAN RESPONDER LAS PREGUNTAS HECHAS EN EL DICCIONARIO, CARTELES YA HECHOS TRATAR DE MODIFICAR EL CARTEL DE REINTENTAR PARA QUE SE VEA MEJOR
import pygame
import random
import os

preguntas = {
    1: {
        "pregunta": "En Argentina se halla la montaña más alta del continente americano ¿cuál es esa montaña y dónde se localiza?",
    "opciones": {"a": " El volcán Llullaillaco, en la Provincia de Salta.", "b": "El nevado Tres Cruces, en la Provincia de Catamarca.", "c": "El cerro Aconcagua, en la Provincia de Mendoza.", "d": "El cerro Ramada, en la Provincia de San Juan."},
        "respuesta": "c"
    },
    2: {
        "pregunta": "¿Cuál es la capital de Argentina?",
        "opciones": {"a": "Córdoba", "b": "Buenos Aires", "c": "Rosario"},
        "respuesta": "b"
    },
    3: {
        "pregunta": "¿Qué animal es típico de la región de la Patagonia?",
        "opciones": {"a": "El pingüino", "b": "El yaguareté", "c": "El puma"},
        "respuesta": "a"
    },
    4: {
        "pregunta": "¿Qué fecha se celebra el Día de la Independencia en Argentina?",
        "opciones": {"a": "9 de julio", "b": "25 de mayo", "c": "20 de junio"},
        "respuesta":"a"    
    }, 
}


ANCHO, ALTO = 800, 600
FPS = 60
ancho_jugador, alto_jugador = 40, 40

color_jugador = (128, 0, 128)
radio_objeto = 15
velocidad_objeto = 5

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS_CLARO = (200, 200, 200)

def juego_Esquivar():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TPI Juego 4")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Courier New", 24)
    fuente_grande = pygame.font.SysFont("Courier New", 36)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.NOFRAME)

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
        pantalla.blit(texto_fin_juego, (ANCHO // 2 - texto_fin_juego.get_width() // 2, ALTO // 2 - 100))
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto_puntaje, (ANCHO // 2 - texto_puntaje.get_width() // 2, ALTO // 2 - 50))

        
        boton_reintentar = pygame.Rect(ANCHO // 2 - 150, ALTO // 2, 120, 50)
        boton_salir = pygame.Rect(ANCHO // 2 + 30, ALTO // 2, 120, 50)
        
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_reintentar)
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_salir)

        texto_reintentar = fuente.render("Reintentar", True, NEGRO)
        texto_salir = fuente.render("Salir", True, NEGRO)
        pantalla.blit(texto_reintentar, (boton_reintentar.x + 0, boton_reintentar.y + 8))
        pantalla.blit(texto_salir, (boton_salir.x + 30, boton_salir.y + 10))
        
        return boton_reintentar, boton_salir

    def reiniciar_juego():
        return ANCHO // 2, ALTO - alto_jugador - 20, [], 0, False

    corriendo = True
    while corriendo:
        pos_x_jugador, pos_y_jugador, objetos_cayendo, puntaje, fin_juego = reiniciar_juego()

        while corriendo and not fin_juego:
            pantalla.fill(NEGRO)
            dibujar_jugador(pos_x_jugador, pos_y_jugador)

            if random.randint(1, 7) == 1:
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
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and pos_x_jugador > 0:
                pos_x_jugador -= 5
            if teclas[pygame.K_RIGHT] and pos_x_jugador < ANCHO - ancho_jugador:
                pos_x_jugador += 5

            reloj.tick(FPS)

        if fin_juego:
            pantalla.fill(NEGRO)
            boton_reintentar, boton_salir = dibujar_fin_juego(puntaje)
            pygame.display.flip()
            
            esperando = True
            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        corriendo = False
                        esperando = False
                    elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        if boton_reintentar.collidepoint(evento.pos):
                            esperando = False 
                        elif boton_salir.collidepoint(evento.pos):
                            corriendo = False
                            esperando = False

    pygame.quit()

if __name__ == "__main__":
    juego_Esquivar()