palavras = {}

ficheiro = open("exemplo.txt", "r")

for linha in ficheiro:
    for palavra in linha.split():
        if palavra in palavras.keys():
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

max_value = max(palavras, key=palavras.get)

print(max_value, ":", palavras[max_value])