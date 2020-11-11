import turtle
import random

t = turtle.Turtle()
r = random.Random()
t.speed(0)

def quadrado(n,x,la,lb,a,color):
    t.up()
    t.goto(n,x)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(la)
        t.left(90)
        t.forward(lb)
        t.left(90)
        i
    t.end_fill()
    t.left(a)


for i in range(150):
    quadrado(r.randint(-700,600), r.randint(-300,300),#define a posição do quadrado
    r.randrange(5,101),r.randrange(5,101),#define o tamanho do quadrado
    r.randrange(0,361),#em que angulo o quadrado vai ficar
    (r.uniform(0,1),r.uniform(0,1),r.uniform(0,1)))#define a cor do quadrado
    

input()