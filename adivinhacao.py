import random

def jogar():

    print("********************************")   #introdução
    print("bem vindo ao jogo da adivinhação")
    print("********************************")

    numero_secr = random.randrange(1,101)       #vai gerar um numero entre 1 e 100 para ser o numero secreto
    total_tent = 0
    pontos = 100

    print("E qual dificudade quer jogar? ")
    print("(1)facil  (2)MEDIO  (3)dificil")         # opções de difilcudade
    dificuldade = int(input("digite aqui: "))       # vai receber a difilculdade
    print("******************************")

    if(dificuldade == 1):       # vai identifivar a dificuldalde escolhida
        total_tent = 20
    elif(dificuldade == 2):
        total_tent = 10 
    else:
        total_tent  = 5

    for tentat in range (1,total_tent + 1):                      # vai repitir o jogo toda vez que eu errar

        print("tentativas {} de {} e um total de {} pontos".format(tentat, total_tent, pontos))         #vai me dizer quantas tentativas eu tenho
                                                                                                        #é melhor tirar o total de pontos em um programa oficial

        chut = int(input("digite um numero entre 1 e 100: "))    # vai me pergutar qual numero chutar
        print("**********************")
        print("seu numero foi: ", chut)     # vai me dizer qual numero eu coloquei

        
        if(chut < 1 or chut > 100):         # vai verificar se o numero que eu coloquei é valido
            print("SEU NUMERO DEVE SER ENTRE 1 A 100")
            continue


            #parametros de acerto e erro
        acertou = chut == numero_secr
        perdeu = tentat == total_tent
        maior = chut > numero_secr      
        menor = chut < numero_secr      


        if perdeu:          
            print("acabou a suas tentativas, você fez {} pontos, a resposta certa era {}".format(pontos, numero_secr)) 
            input()
            break       # se eu errar o break vai quebrar o laço do for in
        elif acertou: 
            print("você ganhou o jogo e fez {} pontos".format(pontos))
            input()
            break       # se eu acertar o break vai quebrar o laço do for in
        else:
            if maior:   # vai me informar se o numero foi grande
                print("seu numero tem que ser menor")
                print("**********************")
            elif menor: # vai me informar se o numero foi pequeno
                print("seu numero tem que ser maior")
                print("**********************")

            pontos_perdi = abs(numero_secr - chut) #calcula os pontos perdidos
            pontos = pontos - pontos_perdi

            if pontos < 0:
                print("você perdeu todos os pontos, a resposta certa era {}".format(numero_secr ))
                input()
                break

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()