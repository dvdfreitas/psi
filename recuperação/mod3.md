# Plano de recuperação

## Módulo 3: Programação estruturada

Para cada um dos programas seguintes, deverá transcrever para o papel o código, comentando todas as linhas.

Deverá ainda fazer uma traçagem do código e explicar no geral o que faz o programa.

No final deverá combinar com o professor um exercício de validação dos conhecimentos.


### Código 1

```python
print("Introduza o primeiro número")
n1 = int(input())
print("Introduza o segundo número")
n2 = int(input())
print("Introduza o terceiro número")
n3 = int(input())

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

print(maior)
```

### Código 2

```python
import random

print("Número de sorteios")
n_sorteios = int(input())
print("Número mínimo:")
min = int(input())
print("Número máximo:")
max = int(input())
print("-------------")
soma_pares = 0
soma_impares = 0
for n in range(n_sorteios):
    n_sorteado = random.randint(min, max)
    print(n_sorteado)
    if n_sorteado % 2 == 0:
        soma_pares = soma_pares + n_sorteado
    else:
        soma_impares = soma_impares + n_sorteado
print("-------------")
print("Soma dos pares: " + str(soma_pares))
print("Soma dos ímpares: " + str(soma_impares))
```

### Código 3

```python3
print("Insira o número:")
numero = int(input())

primo = True
n_dividir = range(2, numero)
for n in n_dividir:
    if numero % n == 0:
        primo = False
        break

if primo:
    print("É primo")
else:
    print("Não é primo")
```

### Código 4

```python3
print("Introduza o número:")
numero = int(input())

mult = 1
for n in range(1, numero+1):
    mult = mult * n

print("O factor é: " + str(mult))
```