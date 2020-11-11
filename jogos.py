import adivinhacao
import forca

print("***************")
print("escolha um jogo")
print("***************")

print("(1) forca  (2)adivinhação")
jogo = int(input("qual jogo?  "))

if (jogo == 1):
    forca.jogar()
else:
    adivinhacao.jogar()
    