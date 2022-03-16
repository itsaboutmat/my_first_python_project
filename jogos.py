import forca
import adivinhacao

print("")
print("#######################################")
print("#### Bem vindo ao menu de jogos!!! ####")
print("#######################################")

print("  ~~~~ Created by:ItsAboutMat ~~~~", end='\n\n')


print("Escolha o que quer jogar:", end='\n\n')
print("(1) Forca    (2) Adivinhe o Número", end='\n\n')
print("Qual jogo você quer?", end='\n\n')
jogo = int(input())

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()

elif(jogo >= 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()


