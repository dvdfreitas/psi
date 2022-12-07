import math
import random

print("Insira o mínimo: ", end='')
min = int(input())
print("Insira o máximo: ", end='')
max = int(input())

sorteado = random.randint(min, max)
print("O número sorteado foi:", sorteado)


acertou = False
n_tentativas = 0

while not acertou:
    tentativa = round(float((max + min) / 2))
    n_tentativas = n_tentativas + 1
    print(tentativa)
    if tentativa > sorteado:
        max = tentativa
    elif tentativa < sorteado:
        min = tentativa
    else:
        acertou = True 

print("Acertou no número em", n_tentativas, "tentativas")