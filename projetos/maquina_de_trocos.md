# Enunciado

Pretende-se que desenvolva um programa que calcule os trocos de uma máquina de trocos automáticos.

A máquina deverá ter:
- Número de moedas e notas introduzidas
- Quantidade de moedas e notas disponíveis na máquina
- Um conjunto de produtos e os seus respetivos preços.

## Dicas

Numa primeira fase pode ser útil dividir em diferentes objetivos:

1. Fazer a interação com o utilizador
    - Listar os produtos disponíveis
    - Inserir as moedas
2. Verificar a validade dos pedidos
3. Calcular os trocos

## Lógica

O desenvolvimento do projeto será feito em espiral. Algumas das decisões tomadas estarão longe de serem óptimas. A ideia é que se perceba mais à frente porque não são as melhores.

## Grupos

- Grupo 1
    - Bernardo
    - David
- Grupo 2
    - Hugo
    - Alves
- Grupo 3
    - Sousa
    - Beatruz
- Grupo 4
    - Afonso
    - Júnior
- Grupo 5
    - Cristiano
    - Filipe
- Grupo 6
    - Veiga
    - Daniel

# Fase 1: Desenvolvimento do menu

Nesta primeira iremos criar uma função que permita mostrar um menu. Uma possível solução seria fazer algo do género:

```
print("--------------------")
print("| Máquina de venda |")
print("--------------------")
print("| 1 - Bounty       |")
print("| 2 - Mars         |")
print("| 3 - Snickers     |")
print("| ...              |")
print("--------------------")
```

Um dos problemas desta solução é que se aparecer um texto maior numa das linhas, toda a formatação tem que ser refeita:

```
print("-------------------------------")
print("| Máquina de venda automática |")
print("-------------------------------")
print("| 1 - Bounty           | 0.8€ |")
print("| 2 - Mars             | 0.8€ |")
print("| 3 - Snickers         | 0.8€ |")
print("| ...                         ")
print("-------------------------------")
```

Este é um trabalho penoso e desnecessário. Para ultrapassar este problema podemos usar uma sintaxe de formatação de strings (Format String Syntax).

```
'{} {}'.format(a, b)
```

Esta é uma sintaxe com muitas opções, mas para iniciar iremos apenas ver algumas das suas aplicações.

Exemplos:
```
>>> print('|{:10s}|{:10d}|{:6.2f}|'.format('a', 10, 20.6))
|a         |        10| 20.60|
```

Na string anterior:
- 10s formata uma string para ocupar 10 espaços, justificado à esquerda por defeito;
- 10d formata um número para ocupar 10 espaços, justificado à direita por defeito;
- 6.2f formata um número de vírgula flutuante (float) para que ocupe 6 espaços (a contar com a "vírgula"), mas apenas 2 depois da vírgula.

Podemos usar esta técnica para melhorar o nosso menu:

```
print("-------------------------------")
print("| {:20s} |".format("Máquina de venda automática"))
print("-------------------------------")
print("|{:3d} - {:12s} - {:6.2f} €|".format(1, "Bounty", 0.8))
print("|{:3d} - {:12s} - {:6.2f} €|".format(2, "Mars", 0.8))
print("|{:3d} - {:12s} - {:6.2f} €|".format(3, "Snickers", 0.8))
print("-------------------------------")
```

Dá o seguinte resultado:

```
-------------------------------
| Máquina de venda automática |
-------------------------------
|  1 - Bounty       -   0.80€ |
|  2 - Mars         -   0.80€ |
|  3 - Snickers     -   0.80€ |
-------------------------------
```

Podemos também melhorar utilizando a multiplicação de strings:
```
>>> linha_separadora = 31 * "-"
>>> print(linha_separadora)
-------------------------------
```

Este é o primeiro passo para uma melhoria, mas podemos fazer muito melhor.
Um dos problemas do código anterior é termos que escrever todas as linhas.
Podemos usar listas para nos ajudar.
Nota: A vantagem de utilizar listas é muito mais do que simplificar o código. Permite automatizar muitos problemas. Mais à frente voltaremos a esta questão.

Uma possível solução poderia ser (iremos fazer bem melhor mais à frente):

codigo_do_produto = [1, 2, 3, 4, 5, 6]
nome_do_produto = ["Bounty", "Mars", "Snickers", "Kit-kat", "Twix", "Lion"]
preco_do_produto = [0.8, 1, 0.8, 0.9, 0.75, 0.8]

## Nome das variáveis

O nome das variáveis é muito importante. Neste caso, poderia omitir-se a parte final da variável (_do_produto) porque este programa não é muito grande e é fácil saber se estamos a falar do produto. No entanto, mais à frente, iremos ter uma variável com o valor total do produto e a nossa tendência pode ser também chamar a esta variável "preço". Se tivermos cuidado e dar um nome lógico, podemos omitir e passar a termos:

```
codigo = [1, 2, 3, 4, 5, 6]
nome = ["Bounty", "Mars", "Snickers", "Kit-kat", "Twix", "Lion"]
preco = [0.8, 1, 0.8, 0.9, 0.75, 0.8]
```

É necessário que, em caso de dúvida, mais vale ter nomes mais descritivos, mas sem exagerar.

Graças à utilização de listas, podemos escrever o seguinte código:

```
for i in range(len(codigo)):
    print("|{:3d} - {:12s} - {:6.2f}€ |".format(codigo[i], nome[i], preco[i]))
```

O resultado será o seguinte:

```
|  1 - Bounty       -   0.80€ |
|  2 - Mars         -   1.00€ |
|  3 - Snickers     -   0.80€ |
|  4 - Kit-kat      -   0.90€ |
|  5 - Twix         -   0.75€ |
|  6 - Lion         -   0.80€ |
```

Apesar de estar longe da perfeição (iremos utilizar "tuple" para uma solução ainda melhor), este exemplo, simplifica o nosso código e permite otimizar o nosso problema.

## Algumas notas

- O código que usamos é decimal, se fosse alfanumérico (A1, A2, B1, C1), teriamos que alterar a string de formatação;

- 