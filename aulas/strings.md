# Introdução

O conceito de "string" é bastante simples. Uma string é uma sequência de carateres. 

Em Python as strings são imutáveis. 

Exercício: O que é um objeto imutável?


# Slice

Podemos cortar uma "fatia" de uma string utilizando a notação [a:b:c]. 

- a: posição de início da "fatia";
- b: posição final da "fatia";
- c: passo entre o início e o final.

O passo (stride) pode ser negativo, retornando os itens em "reverse".

```
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1]
'elcycib'
>>> s[::-2]
'eccb'
```

## replace

O método ```replace()``` substitui uma frase por outra frase.

```
string.replace(valor_antigo, novo_valor, conta)
```

- valor_antigo - Obrigatório. A string a ser procurada.
- novo_valor - Obrigatório. A string que irá substituir
- count - O número de vezes a substituir a string. Se não for especificado, todas as ocorrências irão ser substituídas.


## Avançado 

### Carateres

In 2021, the best definition of “character” we have is a Unicode character. Accordingly, the items we get out of a Python 3 str are Unicode characters, just like the items of a unicode object in Python 2—and not the raw bytes we got from a Python 2 str.

