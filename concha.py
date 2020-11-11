import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(0)
t.hideturtle()


def hex(a):
    for i in ["orange","gold","red","gold","red","yellow"]:
        t.color(i)
        t.forward(a)
        t.right(60)

def rotacao():
    a = 20
    for i in range(80):
        hex(a)
        t.right(6)
        a += 2
        i

rotacao()

input()