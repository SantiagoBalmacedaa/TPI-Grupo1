import turtle
import time
import random
import sys

posponer = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Juego de la Serpiente")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Colores y formas
colores = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
formas = ["circle", "square", "triangle"]

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Bonus especial
bonus = turtle.Turtle()
bonus.speed(0)
bonus.shape("turtle")  
bonus.color("gold")
bonus.penup()
bonus.hideturtle() 

segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score: 0", align="center", font=("Courier", 24, "normal"))

pregunta_texto = turtle.Turtle()
pregunta_texto.speed(0)
pregunta_texto.color("white")
pregunta_texto.penup()
pregunta_texto.hideturtle()
pregunta_texto.goto(0, 50)

# Lista de preguntas
preguntas = [
    {"pregunta": "¿Cuántos lados tiene un triángulo?", "opciones": ["A) 2", "B) 3", "C) 4"], "respuesta": "B"},
    {"pregunta": "¿Qué forma tiene una pelota?", "opciones": ["A) Cuadrada", "B) Triangular", "C) Circular"], "respuesta": "C"},
    {"pregunta": "¿Qué figura parece un queso de pizza cortado?", "opciones": ["A) Círculo", "B) Cuadrado", "C) Triángulo"], "respuesta": "C"},
    {"pregunta": "¿Qué forma tiene una moneda?", "opciones": ["A) Triangular", "B) Circular", "C) Cuadrada"], "respuesta": "B"},
    {"pregunta": "¿Cuántas esquinas tiene un rectángulo?", "opciones": ["A) 4", "B) 2", "C) 3"], "respuesta": "A"},
    {"pregunta": "¿Todas las caras de un cubo son iguales?", "opciones": ["A) Sí", "B) No"], "respuesta": "A"},
]

movimiento_habilitado = True

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquiera():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Bonus multicolor
def cambiar_color_bonus():
    if bonus.isvisible():
        bonus.color(random.choice(colores))
        wn.ontimer(cambiar_color_bonus, 200) 

# Mostrar el bonus especial
def mostrar_bonus():
    if not bonus.isvisible():
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        bonus.goto(x, y)
        bonus.showturtle()
        cambiar_color_bonus() 
        wn.ontimer(bonus.hideturtle, 5000) 

# Función para mostrar pregunta
def mostrar_pregunta():
    global movimiento_habilitado
    movimiento_habilitado = False 

    pregunta = random.choice(preguntas)
    pregunta_texto.clear()
    opciones = "\n".join(pregunta["opciones"])
    pregunta_texto.write(f"{pregunta['pregunta']}\n{opciones}\nPresiona A, B o C para responder", 
                         align="center", font=("Courier", 16, "normal"))

    respuesta_correcta = pregunta["respuesta"]

    def verificar_respuesta(tecla):
        global movimiento_habilitado
        if tecla == respuesta_correcta:
            pregunta_texto.clear()
            pregunta_texto.write("¡Correcto!", align="center", font=("Courier", 16, "normal"))
            wn.update()
            time.sleep(1) 
            pregunta_texto.clear()
            movimiento_habilitado = True 
            texto.clear()
            texto.goto(0, 260) 
            texto.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        else:
            pregunta_texto.clear()
            pregunta_texto.write("Lo siento, es Incorrecto...\nCerrando el juego...", align="center", font=("Courier", 16, "normal"))
            wn.update()
            time.sleep(2)  
            wn.bye()  # Cierra la ventana automáticamente
            sys.exit()  # Termina el programa

    wn.onkeypress(lambda: verificar_respuesta("A"), "a")
    wn.onkeypress(lambda: verificar_respuesta("B"), "b")
    wn.onkeypress(lambda: verificar_respuesta("C"), "c")

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquiera, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for segmento in segmentos:
            segmento.goto(2000, 2000)

        segmentos.clear()

        score = 0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        mostrar_pregunta()  # Muestra pregunta cuando pierdes

    if cabeza.distance(comida) < 20:
        # Guardar el color y formas
        color_comida = comida.color()[0]
        forma_comida = comida.shape()

        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)

        # Cambiar a un nuevo color y forma
        comida.color(random.choice(colores))
        comida.shape(random.choice(formas))

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape(forma_comida)
        nuevo_segmento.color(color_comida)
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Colisión con el bonus
    if bonus.isvisible() and cabeza.distance(bonus) < 20:
        score += 50  # puntos
        bonus.hideturtle()

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(2000, 2000)

            segmentos.clear()

            score = 0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
            mostrar_pregunta()  # Muestra pregunta cuando colisionas con tu cuerpo

    # Mostrar el bonus con probabilidad baja
    if random.randint(1, 100) == 1: 
        mostrar_bonus()

    time.sleep(posponer)
