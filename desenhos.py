import flor_de_lotus
import forma_infinita
import esfera

print("**************************")
print("***bem vindos a galeria***")
print("**************************")

print("(1) flor de lotus (2) quadrado infinito (3) triangulo infinito (4) esfera")
desenho = int(input("escolha o seu desenho : "))

if desenho == 1:
    print("flor de lotus")
    flor_de_lotus.desenhar()

elif desenho == 2:
    quadrado = int(input("escolha um angulo para fazer o desenho (fique entre 86 e 94): "))

    if quadrado > 85 and quadrado < 95:
        forma_infinita.desenhar(quadrado)
    else:
        print("numero invalido")
        input()

elif desenho == 3:
    triangulo = int(input("escolha um angulo para fazer o desenho (fique entre 116 e 124): "))

    if triangulo > 115 and triangulo < 124:
        forma_infinita.desenhar(triangulo)
    else:
        print("numero invalido")
        input()

elif desenho == 4:
    print("esfera")
    esfera.desenhar()