import random

print("Insira o valor mínimo")
min = int(input())
print("Insira o valor máximo")
max = int(input())

sorteado = random.randint(min, max)
acertou = False
tentativas = 0
while not(acertou):
    sorteado_computador = random.randint(min, max)
    print(sorteado_computador)
    if sorteado_computador == sorteado:
        print("Acertou")
        acertou = True
    else:
        tentativas = tentativas + 1
    
print("###############")
print("Número de tentativas " + str(tentativas))
print(sorteado_computador)
