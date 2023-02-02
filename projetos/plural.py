lista = [
    ('mão', 'mãos'), 
    ('sopa', 'sopas'),
    ('lápis', 'lápis')
]


def calcula_plural(palavra):


    if palavra[-1] == "r" or palavra[-1] == "s" or palavra[-1] == "z":
        resultado = palavra + "es"    
    elif palavra[-2:] == "ão":
        resultado = palavra.replace('ão', 'ões')
    else:
            resultado = palavra + "s"

    for singular, plural in lista:
        if singular == palavra:
            resultado = plural
        
    return resultado


def junta_listas(lista1, lista2):

    resultado = []

    for element in lista1:
        if element not in lista2: 
            resultado += element
    resultado += lista2

    return resultado

print(calcula_plural("lápis"))
print(calcula_plural("sopa"))
print(calcula_plural("caneta"))
print(calcula_plural("raiz"))
print(calcula_plural("rapaz"))
print(calcula_plural("bar"))
print(calcula_plural("revés"))
print(calcula_plural("opinião"))
print(calcula_plural("ãoão"))


#print(junta_listas(lista1, lista2))

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
