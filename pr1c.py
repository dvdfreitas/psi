import random
import math
print("Insera o mínimo")
min = int(input())
print("Insera o máximo")
max = int(input())

acertou = False
sorteado = random.randint(min, max)
print("Sorteado: " + str(sorteado))
n_tentativas = 0

while not(acertou):
    tentativa = math.floor(min + (max - min) / 2)
    n_tentativas = n_tentativas + 1
    print("Tentativa entre " + str(min) + " e " + str(max) + " " + str(tentativa))
    if (tentativa == sorteado):
        print("Acertou")
        acertou = True
    elif (tentativa > sorteado):
        max = tentativa - 1
    else:
        min = tentativa + 1
print("Número de tentativas " + str(n_tentativas))