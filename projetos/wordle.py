import string

def ler_palavras(lingua):
    if lingua == "pt":
        print("Escolheu a Língua Portuguesa")

def valida_palavra(palavra):
    valid = True

    # Testa o tamanho da palavra (deve ser 5)
    if len(palavra) != 5:
        valid = False

    if not palavra in lista_de_palavras:
        valid = False 

    return valid

def retira_letras_utilizadas(palavra):
    for letra in palavra:
        if letra in letras:
            letras.remove(letra)


letras = list(string.ascii_lowercase)
lista_de_palavras = ler_palavras("pt")

while (True):
    estaPalavraEValida = False # Péssimo nome de variável
    while not estaPalavraEValida:
        print("Letras por utilizar")
        print(letras)
        palavra = input("Insira a palavra (5 letras): ")
        estaPalavraEValida = valida_palavra(palavra)

    retira_letras_utilizadas(palavra)

    print("Palavra:", palavra)