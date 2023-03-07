import random

def mostra_uma_cabra(portas, pos):
    print("1 cabra")

def mostra_a_outra_cabra(portas, pos):
    for i in range(0, 3):
        if (portas[i] == 'g' and pos != i):
            return i

def mostra_portas(portas):
    print("|", end='')
    for i in portas:
        print(i, " | ", end='')
    print()

def mostra_portas_com_dica(portas, dica):
    print("|", end='')
    for i in portas:
        if i == dica:
            print(i, " | ", end='')
        else:
            print(" ", end='')
    print()


portas = ['c', 'g', 'g']
random.shuffle(portas)
mostra_portas(portas)

escolha_valida = False
print("Qual a porta escolhida (1 a 3): ", end='')
porta_escolhida = int(input())
while not escolha_valida:
    if (porta_escolhida < 1 or porta_escolhida > 3):
        print("Escolheu uma porta inválida")
        print("Qual a porta escolhida (1 a 3): ", end='')
        porta_escolhida = int(input())
    else:
        escolha_valida = True

if portas[porta_escolhida-1] == 'c':
    mostra_uma_cabra(portas, porta_escolhida - 1) 
else:
    pos_outra_cabra = mostra_a_outra_cabra(portas, porta_escolhida - 1)
    mostra_portas_com_dica(portas, pos_outra_cabra)
    print(pos_outra_cabra)

