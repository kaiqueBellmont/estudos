from collections import deque
from collections import Counter

lista = deque(range(10))
for indice, valor in enumerate(lista):
    print(f'Digite o valor para o indice {indice} :')
    lista[valor] = input()


repetidos = Counter(lista)
print(repetidos)
print(lista)
