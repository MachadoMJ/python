import turtle
import random

t = turtle.Turtle()

t.speed(0)
t.hideturtle()

def quadrado(size,c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
        i
    t.end_fill()

size = 280
while True:
    t.left(2)
    quadrado(size,(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    size -= 0.09