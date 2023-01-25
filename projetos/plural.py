lista_de_palavras = [('computador', 'computadores'), ('caroça', 'caroças'), ('centímo', 'euros')]

print("Introduza a palavra:", end='')
palavra = input()

# if palavra[len(palavra)-1] == "l" and palavra[len(palavra)-2] == "a":
#     print("Termina em al")

for singular, plural in lista_de_palavras:
    if singular == palavra:
        final = plural

if palavra[-2:] == "al":
    print("Termina em al")
    final = palavra.replace('al', 'ais')
else:
    final = palavra + "s"

print("O plural de", palavra, " é ", final)
