import random

def mostra_uma_cabra(portas):
    lista = []
    pos = 0
    for i in portas:
        if i=='g':
            lista += [pos]
        pos += 1
    cabra = random.randint(0, len(lista)-1)
    return lista[cabra]

# Programa que deve ser otimizado
def mostra_a_outra_cabra(portas, escolha):
    pos = 0
    for i in portas:
        if i == 'g' and pos != escolha:
            return pos
        pos += 1

# Deve ser otimizado
def muda_porta(escolha_porta, escolha_apresentador):
    lista = [0, 1, 2]
    for i in lista:
        if i != escolha_porta and i != escolha_apresentador:
            return i

def print_portas(portas):
    print('|', end='')
    for i in portas:
        print(i, end='|')
    print()
       
       

acertou_mudando = 0
acertou_mantendo = 0

for teste in range(10):
    # Valores da lista
    # g = goat
    # c = car
    portas = ['g', 'g', 'g']
    pos_carro = random.randint(0,2)
    portas[pos_carro] = 'c'
   
    print("\n###########")
    print("# Teste", teste, end=' #')
    print("\n###########")
    print_portas(portas)
   
    escolha_porta_1 = random.randint(0,2)
    print("Escolheu a porta", escolha_porta_1)
   
    if portas[escolha_porta_1] == 'c':
        porta_apresentador = mostra_uma_cabra(portas)
    else:
        porta_apresentador = mostra_a_outra_cabra(portas, escolha_porta_1)
    print("Apresentador mostra a porta", porta_apresentador)
       
    escolha_porta_2 = muda_porta(escolha_porta_1, porta_apresentador)
   
    if (portas[escolha_porta_2] == 'c'):
        #print("Acertou")
        acertou_mudando += 1
    if portas[escolha_porta_1] == 'c':
        #print("Falhou")
        acertou_mantendo += 1
       
print("Acertou mudando: ", acertou_mudando)
print("Acertou mantendo: ", acertou_mantendo)
