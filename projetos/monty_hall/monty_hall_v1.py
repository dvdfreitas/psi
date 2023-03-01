import random

print("Insira o número de repetições:", end=' ')
n_testes = int(input())

total_acertou = 0
for i in range(n_testes):
    portas = ['c', 'g', 'g']
    random.shuffle(portas)
    escolha = random.randint(0,2)
    if (portas[escolha] == 'c'):
        acertou = "Acertou"
        total_acertou += 1
    else:
        acertou = "Falhou"
    print(portas, "-", acertou)

print("Acertou um total de", total_acertou)