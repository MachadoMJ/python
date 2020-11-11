import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
t.hideturtle()

def quadrado(a):
    for i in ["red", "black", "blue", "black"]:
        t.color(i)
        t.forward(a)
        t.left(90)
        

def rotacao():  
    a = 20
    for i in range(45): 
        quadrado(a)
        t.forward(i)
        t.right(15)
        a += 2 

rotacao()

input()