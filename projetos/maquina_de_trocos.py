moedas_existentes = [2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
moedas_inseridas = [1, 1, 0, 0, 0, 0, 50, 10000]
moedas_dar = [0] * len(moedas_existentes)

troco = 13.99

for pos in range(len(moedas_existentes)):
    moedas = round(troco // moedas_existentes[pos])
    moedas = min(moedas, moedas_inseridas[pos])
    troco = round(troco - moedas * moedas_existentes[pos], 2)
    moedas_dar[pos] += moedas

print(moedas_dar)




# moedas_troco = [10] * 8

# def print_menu():
#     linha_separadora = "-" * 38

#     codigo = [1, 2, 3, 4, 5, 6]
#     nome = ["Bounty", "Snickers", "Kitkat", "Garrafa de água", "Mars", "Sopa"]
#     preco = [0.8, 1, 0.8, 1, 2, 3]

#     print(linha_separadora)
#     print("| {:34s} |".format("Máquina automática de trocos"))
#     print(linha_separadora)
#     for i in range(len(codigo)):
#         print('|{:2d} | {:20s} | {:6.2f}€ |'.format(codigo[i], nome[i], preco[i]))
#     print(linha_separadora)

# print_menu()

# moedas_existentes = [2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
# moedas_inseridas = [0] * len(moedas_existentes)
# soma = 0
# for pos in range(len(moedas_existentes)):
#     print("Quantas moedas de {:4.2f}? ".format(moedas_existentes[pos]), end='')
#     moedas_inseridas = int(input())
#     valor = moedas_inseridas * moedas_existentes[pos]
#     moedas_troco[pos] = moedas_troco[pos] + moedas_inseridas[pos]
#     soma = valor + soma

# print("Total inserido: ", soma)
# print(moedas_troco)

# print_menu()

# for pos in range(len(moedas_existentes)):
#     print("Quantas moedas de {:4.2f}? ".format(moedas_existentes[pos]))