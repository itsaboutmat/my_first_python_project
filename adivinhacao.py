import random
def jogar():

    print("")
    print("###########################################")
    print("#### Bem vindo ao jogo de Adivinhação! ####")
    print("###########################################")

    print("     ~~~~ Created by:ItsAboutMat ~~~~", end='\n' * 3)

    numero_secreto = random.randrange(1,101)
    numero_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Em qual dificuldade você quer jogar?")
    print("(1) Fácil (2) Médio (3) Difícil", end='\n' * 2)
    nivel = int(input("Digite a dificuldade: "))
    print("")

    if(nivel == 1):
        numero_de_tentativas = 21
    elif(nivel == 2):
        numero_de_tentativas = 14
    else:
        numero_de_tentativas = 7

    for rodada in range(rodada, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str, end='\n' * 2)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Apenas números entre 1 e 100 são permitidos", end='\n')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns!!! Você acertou!!! Você fez um total de {} pontos" .format(pontos), end='\n' * 2)
            break
        else:
            if(maior):
                print("O seu chute foi MAIOR do que o número secreto!", end='\n' * 2)
                if(rodada == numero_de_tentativas):
                    print("O número secreto era {}, você fez um total de {} pontos" .format(numero_secreto, pontos))
            elif(menor):
                print("O seu chute foi MENOR do que o número secreto!", end='\n' * 2)
                if(rodada == numero_de_tentativas):
                    print("O número secreto era {}, você fez um total de {} pontos" .format(numero_secreto, (pontos)))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1


    jogar_novamente()


def jogar_novamente():
    print("Quer jogar novamente?")
    print("(1) SIM  (2) Não")

    play_again = int(input())

    if (play_again == 1):
        jogar()
    else:
        end_message()

def end_message():
    print()
    print("#########################################")
    print("############## Fim do jogo ##############")
    print("#########################################", end='\n' * 3)

if(__name__ == "__main__"):
    jogar()