f = open("./ficheiros/exemplo.txt", "rt")
for linha in f:
    palavras = linha.split(',')
    print("Nome:",palavras[0])
    print("Telefone:",palavras[1])
    print("Morada:",palavras[2])