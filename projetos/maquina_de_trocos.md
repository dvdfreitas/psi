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
    - Davi
- Grupo 2
    - Hugo
    - Alves
- Grupo 3
    - Sousa
    - Beatriz
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

# Como registar as moedas inseridas 

Uma possível solução para este problema era fazermos um conjunto de "prints":

```
print("Quantas moedas de 2€?, end=' ')
moedas_2 = int(input())
print("Quantas moedas de 1€?, end=' ')
moedas_1 = int(input())
print("Quantas moedas de 0.50€?, end=' ')
moedas_050 = int(input())
print("Quantas moedas de 0.20€?, end=' ')
moedas_020 = int(input())
print("Quantas moedas de 0.10€?, end=' ')
moedas_010 = int(input())
print("Quantas moedas de 0.05€?, end=' ')
moedas_005 = int(input())
print("Quantas moedas de 0.02€?, end=' ')
moedas_002 = int(input())
print("Quantas moedas de 0.01€?, end=' ')
moedas_001 = int(input())
```

Note-se que os nomes das variáveis ```moedas_1```, ```moedas_010``` e ```moedas_001``` foram utilizadas para se distinguirem. De forma semelhante para as restantes moedas.

Este é, no entanto, um processo pouco eficiente. Qualquer alteração ao texto de input e às moedas válidas, implica alterar todo o código anterior.

Uma solução mais inteligente é criar-se um vector com as possíveis moedas. A este vector vamos dar o nome de ```moedas_existentes```.

```
moedas_existentes = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
```

Poderemos usando um ciclo:

```
for pos in range(len(moedas_existentes)):
    print("Quantas moedas de {:4.2f}€? ".format(moedas_existentes[pos]))
```

O resultado da execução deste código será:

```
Quantas moedas de 2.00€? 
Quantas moedas de 1.00€? 
Quantas moedas de 0.50€? 
Quantas moedas de 0.20€? 
Quantas moedas de 0.10€? 
Quantas moedas de 0.05€? 
Quantas moedas de 0.02€? 
Quantas moedas de 0.01€?
```

Note-se que a o conteúdo da variável ```moedas_existentes[pos]``` para um número com 4 caracteres ```{:4.2f}``` (a contar com o ".") e duas casas decimais.

# Cálculo do total inserido

Vamos definir o número de moedas que a máquina tem disponíveis para trocos. No seguinte exemplo iremos definir que existem 10 moedas de cada tipo.

```
moedas_inseridas = [10, 10, 10, 10, 10, 10, 10, 10]
```

Lembre-se que o vector ```moedas_inseridas = [10, 10, 10, 10, 10, 10, 10, 10]``` está relacionada com vector ```moedas_existentes = [2, 1, 0.5, 0.2,0.1, 0.05, 0.02, 0.01]``` 

A separação da informação em vários vectores não faz sentido. Como já foi referido antes, no final, faremos uma versão com "tuplos".

Também a definição anterior poderia ser feita de forma mais dinâmica.

```
moedas_inseridas = [10] * len(moedas_existentes)
```

Não nos podemos esquecer de sempre que o utilizador inserir moedas, se actualize o vector ```moedas_inseridas = [10, 10, 10, 10, 10, 10, 10, 10]```.
 

# Cálculo de troco

## Com um número de moedas de troco infinitas

Numa primeira fase iremos calcular os trocos supondo que a máquina tem moedas infinitas de troco.

Para explicar o que queremos fazer, vamos imaginar que queremos dar o troco de 6.88€.

```
troco = 7.88 # Este valor é calculado fazendo a diferença entre o preço do produto e o valor inserido.
```

Faz sentido que sejam entregues as maiores moedas primeiro. Senão, uma solução seria entregar 688 moedas de um céntimo. Ninguém quer levar tantas moedas.

Intuitivamente, é fácil perceber que temos que entregar 3 moedas de 2€. Como se chega a este resultado?

Se dividirmos 7.88€ por 2€, obtemos


```
>>> 7.88 / 2
3.94
```

Estamos interessados apenas na parte inteira do resultado. Para isso podemos usar o operador ```//``` que nos dá o resultado da divisão inteira.

```
>>> 7.88 // 2
3.94
```

O novo troco depois de se entregar 3 moedas de 2€ passa a ser ```7.88 - 3 * 2 = 1.88```. De forma mais "programada" podemos escrever:

```
moedas_2 = troco // 2
troco = moedas_2 * 2
```

De forma análoga, podemos acrescentar o cálculo para as restantes moedas:

```
moedas_1 = troco // 1
troco = moedas_1 * 2
moedas_050 = troco // 0.5
troco = moedas_05 * 0.5 
...
```

```
moedas_existentes = [2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
moedas_inseridas = [10] * len(moedas_existentes)
moedas_dar = [0] * len(moedas_existentes)

troco = 13.99

for pos in range(len(moedas_existentes)):
    moedas = round(troco // moedas_existentes[pos])
    troco = round(troco - moedas * moedas_existentes[pos], 2)
    moedas_dar[pos] += moedas
```

## Problemas 

Um dos problemas que certamente apareceram foram números com um valor semelhante a este ```1.000000001```.

A origem deste problema está na representação binária de número com vírgula flutuante. O ```0.1``` é um destes valores.

Um dos problemas que podes ter sentido é 

troco = round(7.68 - 3 * 2)



```
moedas_existentes = [2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
moedas_inseridas = [10] * len(moedas_existentes)

troco = 8.01

moedas_2 = round(troco // 2, 2) 
troco = round(troco - moedas_2 * 2, 2)
moedas_1 = round(troco // 1, 2)
troco = round(troco - moedas_1 * 1, 2)
moedas_05 = round(troco // 0.5, 2)
troco = round(troco - moedas_05 * 0.5, 2)
moedas_02 = round(troco // 0.2, 2)
troco = round(troco - moedas_02 * 0.2, 2)
moedas_01 = round(troco // 0.1, 2)
troco = round(troco - moedas_01 * 0.1, 2)
moedas_005 = round(troco // 0.05, 2)
troco = round(troco - moedas_005 * 0.05, 2)
moedas_002 = round(troco // 0.02, 2)
troco = round(troco - moedas_002 * 0.02, 2)
moedas_001 = round(troco // 0.01, 2)
troco = round(troco - moedas_001 * 0.01, 2)
```


## Com um número de moedas disponíveis limitado

Para adaptar o código anterior a um número de moedas limitadas, a solução é muito fácil. Para verificar se existem moedas suficientes. Por exemplo, o número de moedas de 2€ inseridas está na posição 0 do vector ```moedas_inseridas[0]```. Imaginemos que temos apenas 2 moedas de 2€ (```moedas_inseridas = [2, 10, 10, 10, 10, 10, 10, 10]```). Basta pensar que só podemos dar o valor mínimo entre o que desejamos e as que existem:

```
moedas_2 = troco // 2
moedas_2 = min(moedas_2, moedas_inseridas[0])
troco = moedas_2 * 2
```

De forma semelhante podemos calcular os trocos para as restantes moedas.

## Melhorias

O código poderá ser otimizado, recorrendo a vectores, como fizemos anteriormente na impressão do menu.

```
moedas_2 = troco // 2
troco = moedas_2 * 2
moedas_1 = troco // 1
troco = moedas_1 * 2
moedas_050 = troco // 0.5
troco = moedas_05 * 0.5 
...
```

```
for pos in range(len(moedas_existentes)):
    moedas = round(troco // moedas_existentes[pos])
    moedas = min(moedas, moedas_inseridas[pos])
    troco = round(troco - moedas * moedas_existentes[pos], 2)
    moedas_dar[pos] += moedas

print(moedas_dar)
```

# Como saber se é possível encontrar uma combinação de moedas?

