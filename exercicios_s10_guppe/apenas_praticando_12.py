def potency(a, b):
    try:
        return a ** b
    except TypeError:
        try:
            return float(a) ** float(b)
        except ValueError:
            return f'ALgum desses caracteres não é válido : "{a}" e/ou "{b}"'


print(potency('%', 15))

from random import (
    random,
    randint,
    shuffle,
    choice
)

lista = [x for x in range(1, 11)]
lista2 = []
for x in range(1, 11):
    n = choice(lista)
    print(n)
    lista2.append(n)
    lista.remove(n)

print(lista)
print(lista2)


