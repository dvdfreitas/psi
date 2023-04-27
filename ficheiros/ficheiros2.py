palavras = {}

ficheiro = open("ficheiros/exemplo.txt", "r")

for linha in ficheiro:
    for palavra in linha.split():
        if palavra in palavras.keys():
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

max_value = max(palavras, key=palavras.get)

print(max_value, ":", palavras[max_value])

for chave in palavras:
    print(chave, ":", palavras[chave])

print(palavras.keys())

print(palavras["Ana"])

print(palavras)