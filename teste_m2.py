import random

print("Qual o tamanho da lista a criar: ", end='')
tamanho = int(input())
print("Qual o número mínimo que poderá ser gerado:", end='')
min = int(input())
print("Qual o número máximo que poderá ser gerado:", end='')
max = int(input())

if max < min:
    print("Introduziu um número máximo menor do que o mínimo.")
    exit()

lista = [None] * tamanho
for i in range(tamanho):
    lista[i] = random.randint(min, max)

print(lista)

for i in range(tamanho):
    if lista[i] % 2 == 0:
        print(lista[i], "é par:", lista[i]**2)
    else:
        print(lista[i], "é ímpar:", lista[i]*2)

soma = 0
for i in range(tamanho):
    soma = soma + lista[i]
print("A soma de todos os elementos gerados é", soma)