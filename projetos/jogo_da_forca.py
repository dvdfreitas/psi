import random

lista = {
    "países": ['frança', 'espanhã', 'portugal'],
    "animais": ['cão', 'gato', 'pássaro'],
    "fruta": ['limão', 'laranja'],
    "disciplinas": ['AC', 'RC']
}

i = 1
for categoria in lista.keys():
    print(i, "- A categoria", categoria, "tem", len(lista[categoria]), "palavras")
    i += 1

print("Insira a categoria escolhida", end=' ')
opcao = int(input())

i = 1
for categoria in lista.keys():
    if i == opcao:
        palavras = lista[categoria]
    i += 1

palavra_sorteada = random.choice(palavras)
print("A palavras secreta é",palavra_sorteada)

tamanho = len(palavra_sorteada)
print("Palavra secreta: ", (tamanho * "_"))