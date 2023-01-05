codigo = [1, 2, 3, 4, 5, 6]
nome = ["Bounty", "Mars", "Snickers", "Kit-kat", "Twix", "Lion"]
preco = [0.8, 1, 0.8, 0.9, 0.75, 0.8]

for i in range(len(codigo)):
    print("|{:3d} - {:12s} - {:6.2f}€ |".format(codigo[i], nome[i], preco[i]))    

linha_separadora = 31 * "-"

print(linha_separadora)
print("| {:20s} |".format("Máquina de venda automática"))
print(linha_separadora)
print("|{:3d} - {:12s} - {:6.2f}€ |".format(1, "Bounty", 0.8))
print("|{:3d} - {:12s} - {:6.2f}€ |".format(2, "Mars", 0.8))
print("|{:3d} - {:12s} - {:6.2f}€ |".format(3, "Snicker", 0.8))
print(linha_separadora)


