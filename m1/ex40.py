import random

print("Número de sorteios")
n_sorteios = int(input())
print("Número mínimo:")
min = int(input())
print("Número máximo:")
max = int(input())
print("-------------")
soma_pares = 0
soma_impares = 0
for n in range(n_sorteios):
    n_sorteado = random.randint(min, max)
    print(n_sorteado)
    if n_sorteado % 2 == 0:
        soma_pares = soma_pares + n_sorteado
    else:
        soma_impares = soma_impares + n_sorteado
print("-------------")
print("Soma dos pares: " + str(soma_pares))
print("Soma dos ímpares: " + str(soma_impares))