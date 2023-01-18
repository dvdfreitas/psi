# lista_de_paises  = [
#     ('portugal', 'lisboa'),
#     ('frança', 'paris'),
#     ('itália', 'roma'),
#     ('espanha', 'madrid')
# ]

# for pais in lista_de_paises:
#     nome, capital = pais
#     print("A capital de", nome, "é", capital)

# Exemplo da máquina

def soma(moedas):
    total = 0
    for moeda in moedas:
        valor, quantidade = moeda
        total += valor * quantidade
    return total

def mostra_moedas_disponiveis(moedas):
    linha_separadora = "-" * 40
    print(linha_separadora)
    for moeda in moedas:
        valor, quantidade = moeda
        palavra = "moedas"
        total = quantidade * valor
        if (quantidade == 1):
            palavra = "moeda"

        print('{:3d} {:6s} de {:3.2f}€ = {:5.2f}€'.format(quantidade, palavra, valor, total))
    print(linha_separadora)
    print('{:27}€'.format(soma(moedas)))

moedas = [(2, 10), (1, 10), (0.5, 1), (0.2, 0), (0.1, 10), (0.05, 0), (0.02, 1), (0.01, 0)]

mostra_moedas_disponiveis(moedas)
