import turtle

def desenhar(a):

    t = turtle.Turtle()

    t.speed(1000)
    t.color('red')

    n = 5
    while True:
        t.forward(n)
        t.left(a)
        n = n + 3

if(__name__ == "__main__"):
    quadrado = int(input("você pode fazer trangulo (120) ou quadrado (90): "))
    desenhar(quadrado)