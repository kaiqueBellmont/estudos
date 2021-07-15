import math


# este e o modo correto para pegar o valor do indice.
lista_simples = list(range(10))
lista_elevada = list(range(10))
for indice, valor in enumerate(lista_simples):
    print(f'Digite o valor para o indice [{indice}]:')
    lista_simples[valor] = int(input())
    lista_elevada[valor] = lista_simples[valor].__pow__(2)


print(lista_simples)
print(lista_elevada)
