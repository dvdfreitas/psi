lista1 = [
    ('mão', 'mãos'), 
    ('sopa', 'sopas'),
]

lista2 = [
    ('mão', 'mãos'), 
    ('aula', 'aulas'),
]

def calcula_plural(palavra):

    plural = palavra + "s"

    return plural

lista1 = [
    ('mão', 'mãos'), 
    ('aula', 'aulas'),
    ('sopa', 'sopas'),
]


def junta_listas(lista1, lista2):

    resultado = []

    for element in lista1:
        if element not in lista2: 
            resultado += element
    resultado += lista2

    return resultado

print(junta_listas(lista1, lista2))


# lista_de_palavras = [('computador', 'computadores'), ('caroça', 'caroças'), ('centímo', 'euros')]

# print("Introduza a palavra:", end='')
# palavra = input()

# # if palavra[len(palavra)-1] == "l" and palavra[len(palavra)-2] == "a":
# #     print("Termina em al")

# for singular, plural in lista_de_palavras:
#     if singular == palavra:
#         final = plural

# if palavra[-2:] == "al":
#     print("Termina em al")
#     final = palavra.replace('al', 'ais')
# else:
#     final = palavra + "s"

# print("O plural de", palavra, " é ", final)
