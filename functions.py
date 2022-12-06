num = None

def quadrado(n):
    return n ** 2

def dobro(n):
    return n * 2

def valida_se_existe_num():
    global num
    if num == None:
        print("O número ainda não foi definido")
        print("Insira o número ", end='')
        num = int(input())

def print_menu():
    print("------------------------")
    print("0 - Sair do menu")
    print("1 - Ler um número")
    print("2 - Calcular o quadrado")
    print("3 - Calcular o dobro")
    print("------------------------\n")
    print("Insira a sua opção:", end='')
print_menu()
opcao = int(input())

while opcao != 0:
    if opcao == 1:
        print("Insira o número", end='')
        num = int(input())
    elif opcao == 2:
        valida_se_existe_num()
        print("\nO quadrado do número é ", quadrado(num))
    elif opcao == 3:
        valida_se_existe_num()
        print("\nO dobro do número é ", dobro(num))
    print_menu()
    opcao = int(input())