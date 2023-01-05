# Introdução

# Casos paradigmáticos de utilização

Sabemos que a função ```range(10)``` cria uma sequência de número entre 0 e 9. 
Podemos transformar esta sequência numa lista usando a função ```list()```:
```
>>> lista = list(range(10))
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Como as listas são mutáveis, podemos realizar operações como a seguinte:

```
>>> lista[2:4] = [12, 13]
>>> lista
[0, 1, 12, 13, 4, 5, 6, 7, 8, 9]
```

Note que no exemplo anterior os índices são de 2 a 4 e não de 2 a 3.

# Slicing

Um problema importante de referir é o seguinte:
```
>>> lista[0:1] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
```

Este erro aconteceu porque quando se usa o slicing, o valor de atribuição tem de ser um iterable, mesmo que este só tenha um objeto.

# Ordenação (Sort)

The list.sort method sorts a list in place—that is, without making a copy. It returns None to remind us that it changes the receiver11 and does not create a new list. (Receiver is the target of a method call, the object bound to self in the method body.) This is an important Python API convention: functions or methods that change an object in place should return None to make it clear to the caller that the receiver was changed, and no new object was created. Similar behavior can be seen, for example, in the random.shuffle(s) function, which shuffles the mutable sequence s in place, and returns None.

In contrast, the built-in function sorted creates a new list and returns it. It accepts any iterable object as an argument, including immutable sequences and generators. Regardless of the type of iterable given to sorted, it always returns a newly created list.

Both list.sort and sorted take two optional, keyword-only arguments: 
- reverse: If True, the items are returned in descending order (i.e., by reversing the compar‐
ison of the items). The default is False.
- key: A one-argument function that will be applied to each item to produce its sorting key. For example, when sorting a list of strings, key=str.lower can be used to perform a case-insensitive sort, and key=len will sort the strings by character length. The default is the identity function (i.e., the items themselves are compared).

```
>>> fruits = ['grape', 'raspberry', 'apple', 'banana']
>>> sorted(fruits)
['apple', 'banana', 'grape', 'raspberry']
>>> fruits
['grape', 'raspberry', 'apple', 'banana']
>>> sorted(fruits, reverse=True)
['raspberry', 'grape', 'banana', 'apple']
>>> sorted(fruits, key=len)
['grape', 'apple', 'banana', 'raspberry']
>>> sorted(fruits, key=len, reverse=True)
['raspberry', 'banana', 'grape', 'apple']
>>> fruits
['grape', 'raspberry', 'apple', 'banana']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grape', 'raspberry']
```