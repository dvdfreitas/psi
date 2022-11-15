import math

def imprime_menu():
    print("***********************************")
    print("1 - Ler os valores (a, b e c)")
    print("2 - Calcular o número de soluções")
    print("3 - Calcular a raiz")
    print("0 - Sair")
    print("***********************************")
    print("Introduza a sua opção:")

imprime_menu()
op = int(input())
while op != 0:
    if op == 1:
        print("Introduza o a")
        a = int(input())
        print("Introduza o b")
        b = int(input())
        print("Introduza o c")
        c = int(input())
    elif op == 2:
        dentro_raiz = b ** 2 - 4 * a *c
        if dentro_raiz == 0:
            print("Só tem uma solução")
        elif dentro_raiz < 0:
            print("Não tem soluções")
        else:
            print("Tem duas soluções")
    elif op == 3:
        dentro_raiz = b ** 2 - 4 * a *c
        if dentro_raiz == 0:
            x = - b / (2*a)
            print("Solução x = " + str(x))
        elif dentro_raiz < 0:
            print("Não tem soluções")
        else:
            x1 = (-b + math.sqrt(dentro_raiz)) / (2*a)
            x2 = (-b - math.sqrt(dentro_raiz)) / (2*a)
            print("X1: " + str(x1))
            print("X2: " + str(x2))
    imprime_menu()
    op = int(input())