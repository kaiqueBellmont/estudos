from collections import deque
lista = deque(range(20))
for indice, valor in enumerate(lista):
    print(f'Digite um valor para o indice {indice}: ')
    lista[valor] = input()


print(lista)
lista = set(lista)
print(sorted(lista))
print(lista)
