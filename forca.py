import random

def jogar():

    mensagem_abertura()

    palavra = biblioteca_de_palavras()

    nivel = numero_tentativas()

    enforcou = False
    acertou = False
    erros = 0

    numero = random.randrange(0, len(palavra))

    palavra_secreta = palavra[numero].upper()
    palavra_secreta = palavra_secreta.strip()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print("Com {} letras, a palavra é: " .format(len(palavra_secreta)))
    print(letras_acertadas, end='\n\n')

    while (not acertou and not enforcou):
        print("*** Tentativa {} / {} ***".format(erros + 1, nivel))
        print("Escolha uma letra?")
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            print('\n'"Ops! Essa letra não tem! ", end='\n\n')
            print(letras_acertadas, end='\n\n')
            erros += 1
            desenha_forca(erros)



        enforcou = erros == nivel
        acertou ="_" not in letras_acertadas


    if(acertou):
        win_message()
    else:
        lose_message(palavra_secreta)


    jogar_novamente()






def mensagem_abertura():
    print("")
    print("#######################################")
    print("#### Bem vindo ao jogo da Forca!!! ####")
    print("#######################################")

    print("  ~~~~ Created by:ItsAboutMat ~~~~", end='\n\n')
    # Tela de abertura do game

def biblioteca_de_palavras():
    print("Escolha a dificuldade das palavras do jogo")
    print("(1) Fácil    (2) Difícil", end='\n\n')
    print("Em qual dificuldade você quer jogar?", end='\n\n')
    dificuldade = int(input())
    print()

    if (dificuldade == 1):
        print("Dificuldade escolhida: Fácil", end='\n\n')
        arquivo = open("easy_words.txt", "r")
        palavra = []

        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)

        arquivo.close()

    else:
        print("Dificuldade escolhida: Difícil", end='\n\n')
        arquivo = open("hard_words.txt", "r")
        palavra = []

        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)

        arquivo.close()
    return palavra
#Aqui o jogador escolhe de qual biblioteca de palavras ele quer jogar
#São 2 arquivos, um com palavras fáceis, outro com palavras difíceis


def numero_tentativas():
    print("Quer alterar sua quantidade de tentativas? "
          "Lembrando que por padrão você tem 6 tentativas"
          " para acertar a palavra", sep='\n')

    print("(1) Sim    (2) Não", end='\n\n')
    nivel = int(input())
    print()



    if (nivel == 1):
        print("Quantas tentativas você quer? ")
        nivel = int(input())
        print(end='\n\n')

    else:
        nivel = 6
    return nivel
#Aqui o jogador está escolhendo se quer alterar a quantidade de tentativas dele

def pede_chute():
    chute = input()
    print("")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1
    print(letras_acertadas, end='\n\n')

def jogar_novamente():
    print("Quer jogar novamente?")
    print("(1) SIM  (2) Não")

    play_again = int(input())

    if (play_again == 1):
        jogar()
    else:
        end_message()


def win_message():
    print("Você ganhou!!!" '\n\n')

def lose_message(palavra_secreta):
    print("Você perdeu!!!", end='\n\n')
    print("A PALAVRA ERA   >>> ", palavra_secreta, " <<<", end='\n\n')

#como o nome já diz, desenha a forca! hahaha
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)    ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print(" |             ")

    if(erros == 2):
        print(" |      (_)    ")
        print(" |       |     ")
        print(" |       |     ")
        print(" |             ")
        print(" |             ")

    if(erros == 3):
        print(" |      (_)    ")
        print(" |      /|     ")
        print(" |     / |     ")
        print(" |             ")
        print(" |             ")

    if(erros == 4):
        print(" |      (_)    ")
        print(" |      /|\    ")
        print(" |     / | \   ")
        print(" |             ")
        print(" |             ")

    if(erros == 5):
        print(" |      (_)    ")
        print(" |      /|\    ")
        print(" |     / | \   ")
        print(" |      /      ")
        print(" |     /       ")

    elif(erros >= 6):
        print(" |      (_)    ")
        print(" |      /|\    ")
        print(" |     / | \   ")
        print(" |      / \    ")
        print(" |     /   \   ")

    print(" |            ")
    print("_|___         ")
    print()

def end_message():
    print()
    print("#########################################")
    print("############## Fim do jogo ##############")
    print("#########################################", end='\n' * 3)

if(__name__ == "__main__"):
    jogar()
