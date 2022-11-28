import random

lista = [None] * 10

for pos in range(10):
    lista[pos] = random.randint(0,10)
    if lista[pos] % 2 == 0:
        print(lista[pos], "é par")
    else:
        print(lista[pos], "é ímpar")

print(lista)