import random

lista = {
    "países": ['frança', 'espanhã', 'portugal'],
    "animais": ['cão', 'gato', 'pássaro'],
    "fruta": ['limão', 'laranja'],
    "disciplinas": ['AC', 'RC']
}

i = 1
for categoria in lista.keys():
    print(i, "-", categoria, "tem", len(lista[categoria]), "palavras")
    i += 1
