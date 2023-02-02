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

## Grupos

- Grupo 1
    - Bernardo
    - Veiga
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
    - Davi
    - Daniel

## Trabalho

- capitalize()	Converte o primeiro caractere para maiúscula
- casefold()	Converte string em letras minúsculas
- center()	Retorna uma string centralizada
- count()	Retorna o número de vezes que um valor especificado ocorre em uma string
- encode()	Retorna uma versão codificada da string
- endswith()	Retorna true se a string terminar com o valor especificado
- expandtabs()	Define o tamanho da tabulação da string
- find()	Procura na string um valor especificado e retorna a posição de onde foi encontrado
- format()	Formata os valores especificados em uma string
- format_map()	Formata os valores especificados em uma string
- index()	Procura na string um valor especificado e retorna a posição de onde foi encontrado
- isalnum()	retorna True se todos os caracteres na string forem alfanuméricos
- isalpha()	Retorna True se todos os caracteres da string estiverem no alfabeto
- isascii()	Retorna True se todos os caracteres na string forem caracteres ASCII
- isdecimal()Retorna True se todos os caracteres na string forem decimais
- isdigit()	Retorna True se todos os caracteres na string forem dígitos
- isidentifier()	Retorna True se a string for um identificador
- islower()	Retorna True se todos os caracteres da string forem minúsculos
- isnumeric()Retorna True se todos os caracteres da string forem numéricos
- isprintable()	Retorna True se todos os caracteres na string forem imprimíveis
- isspace()	Retorna True se todos os caracteres na string forem espaços em branco
- istitle()	Retorna True se a string seguir as regras de um título
- isupper()	Retorna True se todos os caracteres da string forem maiúsculos
- join()	Converte os elementos de um iterável em uma string
- ljust()	Retorna uma versão justificada à esquerda da string
- lower()	Converte uma string em letras minúsculas
- lstrip()	Retorna uma versão de corte à esquerda da string
- maketrans()	Retorna uma tabela de tradução para ser usada nas traduções
- partition()	Retorna uma tupla onde a string é dividida em três partes
- replace()	Retorna uma string onde um valor especificado é substituído por um valor especificado
- rfind()	Procura na string um valor especificado e retorna a última posição de onde foi encontrado
- rindex()	Procura na string um valor especificado e retorna a última posição de onde foi encontrado
- rjust()	Retorna uma versão justificada à direita da string
- rpartition()	Retorna uma tupla onde a string é dividida em três partes
- rsplit()	Divide a string no separador especificado e retorna uma lista
- rstrip()	Retorna uma versão de corte à direita da string
- split()	Divide a string no separador especificado e retorna uma lista
- splitlines()	Divide a string nas quebras de linha e retorna uma lista
- startswith()	Retorna true se a string começar com o valor especificado
- strip()	Retorna uma versão aparada da string
- swapcase()	Troca as letras maiúsculas e minúsculas e vice-versa
- title()	Converte o primeiro caractere de cada palavra para maiúscula
- translate()	Retorna uma string traduzida
- upper()	Converte uma string em letras maiúsculas
- zfill()	Preenche a string com um número especificado de valores 0 no início


## Avançado 

### Carateres

Em 2021, a melhor definição de “caráter” que temos é um caractere Unicode. Da mesma forma, os itens que obtemos de um Python 3 str são caracteres Unicode, assim como os itens de um objeto unicode no Python 2 - e não os bytes brutos que obtivemos de um Python 2 str.

