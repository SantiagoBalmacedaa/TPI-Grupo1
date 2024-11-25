import pygame
import random
import os

preguntas = {
    1: {
        "pregunta": "¿cuál es la montaña mas grande de argentina y donde esta?",
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
        "respuesta": "a"
    },
    5: {
        "pregunta": "¿Qué animal es conocido como el rey de la selva?",
        "opciones": {"a": "León ", "b": "Elefante", "c": "Tigre"},
        "respuesta": "a"
    },
    6: {
        "pregunta": "¿Cuál es el color del sol?",
        "opciones": {"a": "Azul", "b": "Rojo", "c": "Amarillo"},
        "respuesta": "c"
    },
    7: {
        "pregunta": "¿En qué estación del año cae la Navidad?",
        "opciones": {"a": "Invierno", "b": "Primavera", "c": "verano"},
        "respuesta": "c"
    },
    8: {
        "pregunta": "¿Cuál es el continente donde vive el Panda?",
        "opciones": {"a": "África", "b": "America", "c": "Asia"},
        "respuesta": "c"
    },
    9: {
        "pregunta": "¿Qué número sigue después del 5?",
        "opciones": {"a": "3", "b": "6", "c": "7"},
        "respuesta": "c"
    },
    10: {
       "pregunta": "¿Cuántos días tiene una semana?",
        "opciones": {"a": "5", "b": "6", "c": "7"},
        "respuesta": "c"
    },
    11: {
        "pregunta": "¿Qué insecto puede volar y tiene una picadura dolorosa?",
        "opciones": {"a": "Mosca", "b": "Mariposa", "c": "Mosquito"},
        "respuesta": "C"
    },
    12: {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": {"a": "Rio nilo", "b": "Amazonas", "c": "Rio parana"},
        "respuesta": "b"
    },
}

ANCHO, ALTO = 1000,600
FPS = 60
ancho_jugador, alto_jugador = 40, 40
color_jugador = (128, 0, 128)
radio_objeto = 15
velocidad_objeto = 5
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS_CLARO = (200, 200, 200)

def reiniciar_juego():
    pos_x_jugador = ANCHO // 2 - ancho_jugador // 2
    pos_y_jugador = ALTO - alto_jugador - 10
    objetos_cayendo = []
    puntaje = 0
    fin_juego = False
    return pos_x_jugador, pos_y_jugador, objetos_cayendo, puntaje, fin_juego

def juego_Esquivar():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TPI Juego 4")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Courier New", 18)
    fuente_grande = pygame.font.SysFont("Courier New", 20)

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

        pygame.draw.rect(pantalla, GRIS_CLARO, boton_reintentar, border_radius=10)
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_salir, border_radius=10)

        texto_reintentar = fuente.render("Reintentar", True, NEGRO)
        texto_salir = fuente.render("Salir", True, NEGRO)
        pantalla.blit(texto_reintentar, (boton_reintentar.x + 10, boton_reintentar.y + 10))
        pantalla.blit(texto_salir, (boton_salir.x + 30, boton_salir.y + 10))

        return boton_reintentar, boton_salir

    def mostrar_pregunta():
        indice = random.choice(list(preguntas.keys()))
        datos_pregunta = preguntas[indice]
        pantalla.fill(NEGRO)
        fuente_preguntas = pygame.font.SysFont("Courier New", 20)
        texto_pregunta = fuente_preguntas.render(datos_pregunta["pregunta"], True, BLANCO)
        pantalla.blit(texto_pregunta, (40, 40))
        y_opciones = 150
        for letra, texto in datos_pregunta["opciones"].items():
            texto_opcion = fuente.render(f"{letra}) {texto}", True, GRIS_CLARO)
            pantalla.blit(texto_opcion, (20, y_opciones))
            y_opciones += 40
        pygame.display.flip()
        esperando_respuesta = True
        while esperando_respuesta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                elif evento.type == pygame.KEYDOWN:
                    if evento.unicode.lower() == datos_pregunta["respuesta"]:
                        return True
                    else:
                        texto_error = fuente.render("¡Incorrecto! Intentá de nuevo.", True, ROJO)
                        pantalla.blit(texto_error, (50, y_opciones + 40))
                        pygame.display.flip()

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
                            if mostrar_pregunta():
                                esperando = False
                        elif boton_salir.collidepoint(evento.pos):
                            corriendo = False
                            esperando = False

    pygame.quit()

if __name__ == "__main__":
    juego_Esquivar()
