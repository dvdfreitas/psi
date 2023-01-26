# Variáveis

Python 3 allows non-ASCII identifiers in source code:

```
>>> ação = 'PBR' # ação = stock
>>> ε = 10**-6   # ε = epsilon
```

Some people dislike the idea. The most common argument to stick with ASCII iden‐
tifiers is to make it easy for everyone to read and edit code. That argument misses the point: you want your source code to be readable and editable by its intended audience, and that may not be “everyone.” If the code belongs to a multinational corporation or is open source and you want contributors from around the world, the identifiers should be in English, and then all you need is ASCII.

Now that Python can parse Unicode names and UTF-8 is the default source encod‐
ing, I see no point in coding identifiers in Portuguese without accents, as we used to do in Python 2 out of necessity—unless you need the code to run on Python 2 also. If the names are in Portuguese, leaving out the accents won’t make the code more read able to anyone.

## Variables Are Not Boxes

Alguns autores têm vindo a desconstruir a ideia que variáveis são caixas. Uma metáfora mais adequada é pensarmos em variáveis como etiquetas que colamos em objetos.

```
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> b
[1, 2, 3, 4]
```

A atribuição ```b = a``` não copia o conteúdo da "caixa" a para a "caixa" b. Cola apenas a etiqueta b ao objeto que já tem a etiqueta a.

Uma possível melhoria na linguagem é utilizar "ligar" em vez de "atribuir".

Python’s assignment statement x = … binds the x name to the object created
or referenced on the righthand side.

Because variables are mere labels, nothing prevents an object from having several labels assigned to it. When that happens, you have aliasing.

```
>>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
>>> lewis = charles
>>> lewis is charles
True
>>> id(charles), id(lewis)
(4300473992, 4300473992)
>>> lewis['balance'] = 950
>>> charles
{'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
>>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
>>> alex == charles
True
>>> alex is not charles
True
```

An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The is operator compares the identity of two objects; the id() function returns an integer representing its identity.

The == operator compares the values of objects (the data they hold), while is compares their identities.

While programming, we often care more about values than object identities, so ==
appears more frequently than is in Python code.

However, if you are comparing a variable to a singleton, then it makes sense to use is. By far, the most common case is checking whether a variable is bound to None.

This is the recommended way to do it: 

```
x is None
```

And the proper way to write its negation is:

```
x is not None
```

None is the most common singleton we test with is.

Usually we are more interested in object equality than identity. Checking for None is the only common use case for the is operator. Most other uses I see while reviewing code are wrong. If you are not sure, use ==. It’s usually what you want, and also works with None—albeit not as fast.

# Strings

