def jogar():
    print("**************************************")
    print("***** bem vindo ao jogo da forca *****")
    print("**************************************")

    palavra = "machado".upper()
    letras = ['_','_','_','_','_','_','_',]

    print('palavra secreta - ' , letras)

    enforcou = False
    acertou = False
    tentativas  = 7

    while not enforcou and not acertou:

        chut = input("Que letra? ").strip().upper()

        if chut == palavra:
            acertou = True
            break
        

        if chut in palavra:
            index = 0
            for letra in palavra:
                if chut == letra:
                    letras[index] = letra.upper()
                index += 1
            print(letras)
        else:
            print('não existe')
            tentativas -= 1
            print('Você ainda tem ', tentativas, ' tentativas')

        enforcou = tentativas == 0
        acertou = "_" not in letras
        
    if acertou:
        print('VOCÊ GANHOU')
    else:
        print('VOCÊ PERDEU')

    print("FIM DE JOGO!!")

if(__name__ == "__main__"):
    jogar()
