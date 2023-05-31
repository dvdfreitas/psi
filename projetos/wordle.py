import string
import random

lista_de_palavras = []

def ler_palavras(lingua):
    if lingua == "pt":
        print("Escolheu a Língua Portuguesa")
    lista_de_palavras = ['hotel', 'assim', 'salto']
    return lista_de_palavras

def imprime_letras(letras):
    print("\nLetras por utilizar: ", end='')
    separador = ""
    print(separador.join(letras))

def valida_palavra(palavra):
    valid = True

    # Testa o tamanho da palavra (deve ser 5)
    if len(palavra) != 5:
        valid = False

    print("Palavra:", palavra)
    print("Lista de palavras:", lista_de_palavras)
    if not palavra in lista_de_palavras:
        valid = False 

    return valid

def retira_letras_utilizadas(palavra):
    for letra in palavra:
        if letra in letras:
            letras.remove(letra)


letras = list(string.ascii_lowercase)
lista_de_palavras = ler_palavras("pt")
palavra_secreta = random.choice(lista_de_palavras)
print("** Palavra secreta:", palavra_secreta, "**")
      
tentativas = 5
acertou = False
while (tentativas > 0 and not acertou):
    print("\nTentativas:", tentativas)
    estaPalavraEValida = False # Péssimo nome de variável
    while not estaPalavraEValida:
        imprime_letras(letras)
        palavra = input("Insira a palavra (5 letras): ")
        estaPalavraEValida = valida_palavra(palavra)

    retira_letras_utilizadas(palavra)
    if palavra == palavra_secreta:
        acertou = True  
    tentativas -= 1


if acertou:
    print("\n\n *** Parabéns ***")
else:
    print("A palavra secreta era:", palavra_secreta)