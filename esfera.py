import turtle

def desenhar():

    t = turtle.Turtle()
    s = turtle.Screen()

    s.bgcolor('black')
    t.pencolor('green')
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0,-100)
    t.pendown()

    a = 0
    b = 0
    while True:
        t.forward(a)
        t.left(b)
        a += 1
        b += 0.5

        if b == 180:
            break

    input()

if __name__ == "__main__":
    desenhar()