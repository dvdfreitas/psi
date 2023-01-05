print("Introduza a string", end=': ')
palavra = input()

lista = list(palavra)

for pos in range(len(lista)):
    if lista[pos] == 'a':
        lista[pos] = 'e'

palavra = ''.join(lista)

# Muito mais simples usar
# palavra.replace("a", "e")

print("Os a's foram substituídos por e's: ", palavra)