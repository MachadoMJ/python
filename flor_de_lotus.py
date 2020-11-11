import turtle

def desenhar():

    t = turtle.Turtle()
    t.speed(0)

    linha = 15
    angulo_base = 45
    angulo = 0

    def flor(cor, anguloParam):
        t.left(anguloParam)
        t.color(cor)
        for i in range(220):
            t.forward(linha)
            t.left(i * 0.3)

        t.penup()
        t.home()
        t.pendown()
        
        anguloParam += angulo_base
        return anguloParam

    for i in range(2):
        angulo = flor('red', angulo)
        angulo = flor('blue', angulo)
        angulo = flor('green', angulo)
        angulo = flor('purple', angulo)
        i

    input()

if __name__ == "__main__":
    desenhar()