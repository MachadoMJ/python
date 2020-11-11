import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

p = 300
def circle(turtle,a):
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.color('orange')
    turtle.up()
    turtle.goto(p,0)
    turtle.left(a)
    turtle.down()
    turtle.circle(424,90)
    
circle(t1,135)
p = t1.xcor()
circle(t2,-45)


t3.hideturtle()
t3.pensize(6)
t3.color('brown')

t3.begin_fill()
t3.up()
t3.goto(0,-124)
t3.down()
t3.circle(124)
t3.end_fill()


t4.hideturtle()
t4.dot(100)

input()