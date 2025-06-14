#!/usr/bin/env python3
#chmod +x Juegopingpong.py
#./Juegopingpong.py
# python3 "/home/takamura/Documents/Desarrollo web/Python/Proyectos portfolio/Juegopingpong.py"

# Sin Reinicio y sin randomizar comienzo pelota (Hace cosas raras)

import turtle
import math

# Configuración ventana
ventana = turtle.Screen()
ventana.title("Pong en Python")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Paletas
def crear_paleta(x):
    paleta = turtle.Turtle()
    paleta.speed(0)
    paleta.shape("square")
    paleta.color("white")
    paleta.shapesize(stretch_wid=6, stretch_len=1)
    paleta.penup()
    paleta.goto(x, 0)
    return paleta

paleta_izq = crear_paleta(-350)
paleta_der = crear_paleta(350)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
velocidad = 4
pelota.dx = velocidad
pelota.dy = velocidad

# Puntos
puntos_izq = 0
puntos_der = 0

# Texto marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Marcador: 0 - 0", align="center", font=("Courier", 20, "normal"))

def actualizar_marcador():
    marcador.clear()
    marcador.write(f"Marcador: {puntos_izq} - {puntos_der}", align="center", font=("Courier", 20, "normal"))

# Mensaje de inicio
juego_empezado = False
mensaje_inicio = turtle.Turtle()
mensaje_inicio.speed(0)
mensaje_inicio.color("white")
mensaje_inicio.penup()
mensaje_inicio.hideturtle()
mensaje_inicio.goto(0, 0)
mensaje_inicio.write("Pulsa ENTER para comenzar", align="center", font=("Courier", 20, "bold"))

def comenzar_juego():
    global juego_empezado
    if not juego_empezado:
        juego_empezado = True
        mensaje_inicio.clear()
        mover_pelota()

# Movimiento paletas
def mover_paleta(paleta, direccion):
    nueva_y = paleta.ycor() + (20 if direccion == "arriba" else -20)
    if -240 < nueva_y < 250:
        paleta.sety(nueva_y)

ventana.listen()
ventana.onkeypress(comenzar_juego, "Return")
ventana.onkeypress(lambda: mover_paleta(paleta_izq, "arriba"), "w")
ventana.onkeypress(lambda: mover_paleta(paleta_izq, "abajo"), "s")
ventana.onkeypress(lambda: mover_paleta(paleta_der, "arriba"), "Up")
ventana.onkeypress(lambda: mover_paleta(paleta_der, "abajo"), "Down")

# Lógica de rebote y colisiones
cooldown = False

def reset_cooldown():
    global cooldown
    cooldown = False

def rebote_horizontal():
    pelota.dy *= -1
    pelota.sety(max(min(pelota.ycor(), 290), -290))

def detectar_colision(paleta, x_ref, invertir_dx):
    if x_ref < pelota.xcor() < x_ref + 10 and paleta.ycor() - 50 < pelota.ycor() < paleta.ycor() + 50:
        pelota.setx(x_ref)
        pelota.dx = -velocidad if invertir_dx else velocidad
        return True
    return False

def reiniciar_pelota(direccion):
    global puntos_izq, puntos_der
    if direccion == "derecha":
        puntos_der += 1
        pelota.dx = velocidad
    else:
        puntos_izq += 1
        pelota.dx = -velocidad
    actualizar_marcador()
    pelota.goto(0, 0)
    pelota.dy = math.copysign(velocidad, pelota.dy)

def mover_pelota():
    global cooldown

    if not juego_empezado:
        ventana.ontimer(mover_pelota, 16)
        return

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if not cooldown:
        if abs(pelota.ycor()) > 290:
            rebote_horizontal()
            cooldown = True
            ventana.ontimer(reset_cooldown, 50)

        if detectar_colision(paleta_der, 340, True) or detectar_colision(paleta_izq, -350, False):
            cooldown = True
            ventana.ontimer(reset_cooldown, 50)

    if pelota.xcor() < -390:
        reiniciar_pelota("derecha")

    if pelota.xcor() > 390:
        reiniciar_pelota("izquierda")

    pelota.dx = math.copysign(velocidad, pelota.dx)
    pelota.dy = math.copysign(velocidad, pelota.dy)

    ventana.update()
    ventana.ontimer(mover_pelota, 16)

ventana.mainloop()
