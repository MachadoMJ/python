import turtle
import random
import colorsys

t = turtle.Turtle()

screen = turtle.Screen()
screen.tracer(1,1)

t.hideturtle()

n=200
chasers = []
for i in range(n):
    chasers.append(turtle.Turtle())

h = 0
for i in range(n):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    chasers[i].color(c)
    chasers[i].up()
    chasers[i].goto(random.uniform(-500,500), random.uniform(-500,500))
chasers[n-1].goto(0,-300)
chasers[n-1].shape('circle')
chasers[n-1].shapesize(1)

def chase():
    for i in range(n-1):
        angle = chasers[i].towards(chasers[i+1])
        chasers[i].seth(angle)
    chasers[n-1].left(2)
    chasers[n-1].fd(10)
    for i in range(n-1):
        chasers[i].fd(10)
    screen.update()
    screen.ontimer(chase,1000//20)
    
chase()