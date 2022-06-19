import random

print("###############################")
print("Bem vindo ao Jogo de Advinhação")
print("###############################")

numero_secreto = random.randrange(1, 101)
print(numero_secreto)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade? ")
print("(1) Fácial (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas +1):
    print("------------------------------")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 um 100: "))

    if (chute < 1 or chute > 100):
        print("Você deve digitar entre 1 e 100!")
        continue


    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou :)")
        print("Você fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu número foi maior que o número secreto!")
        elif (menor):
            print("Você errou! O seu número foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos 
    print("------------------------------")

print("Fim de jogo")