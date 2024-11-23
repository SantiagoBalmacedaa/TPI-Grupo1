import turtle
import time
import random

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

segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score: 0", align="center", font=("Courier", 24, "normal"))

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

    time.sleep(posponer)
