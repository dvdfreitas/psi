import random

print("Quantos números quer na lista?")
numero = int(input())

lista = [None] * numero

for i in range(numero):
    lista[i] = random.randint(0,100)

print(lista)

minimo = lista[0]
maximo = lista[0]
pos_minimo = 0
pos_maximo = 0
for i in range(1, numero):
    if lista[i] > maximo:
        maximo = lista[i]
        pos_maximo = i + 1
    if lista[i] < minimo:
        minimo = lista[i]
        pos_minimo = i + 1

print("O máximo é", maximo, "e está na posição", pos_maximo)
print("O mínimo é", minimo, "e está na posição", pos_minimo)