import random

def jogar():

    print("")
    print("#######################################")
    print("#### Bem vindo ao jogo da Forca!!! ####")
    print("#######################################")

    print("  ~~~~ Created by:ItsAboutMat ~~~~", end='\n\n')


    #Aqui o jogador escolhe de qual biblioteca de palavras ele quer jogar
    #São 2 arquivos, um com palavras fáceis, outro com palavras difíceis

    print("Escolha a dificuldade das palavras do jogo")
    print("(1) Fácil    (2) Difícil", end='\n\n')
    print("Em qual dificuldade você quer jogar?", end='\n\n')
    dificuldade = int(input())
    print()

    if (dificuldade == 1):
        print("Dificuldade escolhida: Fácil", end='\n\n')
        arquivo = open("easy_words.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    else:
        print("Dificuldade escolhida: Difícil", end='\n\n')
        arquivo = open("hard_words.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()


        #Aqui o jogador está escolhendo se quer alterar a quantidade de tentativas dele

    print("Quer alterar sua quantidade de tentativas? " 
          "Lembrando que por padrão você tem 6 tentativas"
          " para acertar a palavra", sep='\n')

    print("(1) Sim    (2) Não", end='\n\n')
    nivel = int(input())
    print()

    enforcou = False
    acertou = False
    erros = 0

    if (nivel == 1):
        print("Quantas tentativas você quer? ")
        nivel = int(input())
        print(end='\n\n')

    else:
        nivel = 6


    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    palavra_secreta = palavra_secreta.strip()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print("Com {} letras, a palavra é: " .format(len(palavra_secreta)))
    print(letras_acertadas, end='\n\n')

    while (not acertou and not enforcou):
        print("*** Tentativa {} / {} ***".format(erros + 1, nivel))
        print("Escolha uma letra?")
        chute = input()
        print("")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index +=  1
            print(letras_acertadas, end='\n\n')

        else:
            print('\n'"Ops! Essa letra não tem! ", end='\n\n')
            print("Letras que você já chutou: ")
            print(letras_acertadas, end='\n\n')
        erros += 1


        enforcou = erros == nivel
        acertou ="_" not in letras_acertadas


    if(acertou):
        print("Você ganhou!!!" '\n\n')
    else:
        print("Você perdeu!!!", end='\n\n')
        print("A PALAVRA ERA   >>> ", palavra_secreta, " <<<", end='\n\n')

    print("#####################")
    print("#### Fim do jogo ####")
    print("#####################", end='\n' * 3)


if(__name__ == "__main__"):
    jogar()
