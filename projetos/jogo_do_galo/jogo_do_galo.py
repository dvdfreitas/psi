import random

def print_tabuleiro():
    print('-------------')
    conta_para_enter = 0
    for valor in jogo:
        if valor == 0: 
            print('|   ', end='')
        elif valor == 1:
            print('| X ', end='')
        else:
            print('| O ', end='')
        conta_para_enter += 1
        if conta_para_enter == 3:
            print('|')
            print('-------------')
            conta_para_enter = 0

def cheio():
    # for i in range(9):
    #     if jogo[i] == 0:
    #         return False

    return not (0 in jogo)


jogo = [0] * 9

if len(jogo) != 9:
    print("Tamanho incorreto")
    exit()

print_tabuleiro()



jogador = 1
while (True):

    linha = -1
    while linha < 0 or linha > 2:
        print("Jogador", jogador, "insira a linha: ", end='')
        linha = int(input())

    coluna = -1
    while coluna < 0 or coluna > 2:
        print("Jogador", jogador, "insira a coluna: ", end='')
        coluna = int(input())    

    pos = linha * 3 + coluna

    if (jogo[pos] == 0):
        jogo[pos] = jogador
        print_tabuleiro()
        if jogador == 1:
            jogador = 2
        else:
            jogador = 1
    else:
        print("Posição já ocupada")

    if cheio():
        print("Terminou o jogo")
        break