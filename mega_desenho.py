import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
t.hideturtle()
t.pensize(2)

s.bgcolor('black')
t.pencolor('purple')

def quadrado(size):
    for i in ['orange','yellow','orange','gold','blue','red']:
        t.color(i)
        t.forward(size)
        t.right(60)

def rotacao():
    size = 10
    for i in range(20):
        quadrado(size)
        t.forward(20)
        t.right(i * 0.5)
        size += 5

angulo = 60
for i in range(6):
    rotacao()

    t.penup()
    t.home()
    t.pendown()

    t.left(angulo)
    angulo += 60

input()