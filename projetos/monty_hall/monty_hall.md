# O Problema de Monty Hall

## Introdução

O problema de Monty Hall surgiu baseado num programa de televisão chamado "Let’s Make a Deal". Neste programa eram mostradas 3 portas a um concorrente. Por trás de uma porta estava um carro e nas outras duas, um cabra. Caso o concorrente acertasse no carro, ganharia o prémio.

Depois do concorrente escolher uma das portas, o apresentador abria uma das portas não escolhidas onde estava uma cabra. Era dada a hipótese ao concorrente de mudar a sua escolha.

Contra a nossa intuição, estatisticamente, o concorrente deve alterar a sua opção.

## Objetivo

Neste projeto pretende-se desenvolver um programa que mostre que alterar a opção é a solução mais inteligente.

Este problema vai ser realizado em várias fases.

## Versão 1

Nesta versão pretende-se apenas fazer uma simulação da taxa de acerto se não houver hipótese de troca. 

Exemplo de programa:
```
Insira o número de repetições: 10
['g', 'c', 'g'] - Falhou
['g', 'g', 'c'] - Falhou
['g', 'g', 'c'] - Falhou
['c', 'g', 'g'] - Falhou
['g', 'c', 'g'] - Acertou
['g', 'g', 'c'] - Falhou
['c', 'g', 'g'] - Falhou
['g', 'c', 'g'] - Acertou
['g', 'g', 'c'] - Falhou
['g', 'g', 'c'] - Falho
```

### Representação da informação

Como podemos representar a informação?

Uma possível solução é termos uma lista a que daremos o nome de ```portas```em que:

- 'c' é o carro (car);
- 'g' é a cabra (goat);

Podiamos usar 'carro' e 'cabra', mas neste contexto, podemos usar uma representação mais compacta que não retirar legibilidade. Usou-se aqui o Inglês porque em Português carro e cabra, iniciam-se com a mesma letra.

É importante notar que na nossa lista só pode ter um 'c' e dois 'g's.

Exemplos válidos:

```
portas = ['c', 'g', 'g']
portas = ['g', 'c', 'g']
portas = ['g', 'g', 'c']
```

Pergunta: Existe mais alguma hipótese?

Exemplos inválidos:

```
portas = ['g', 'g', 'c']
portas = ['c', 'g', 'c']
portas = ['g', 'g', 'g']
```

### 

