lista = list(range(6))
for indice, valor in enumerate(lista):
    print(f'Digite o valor para o indice: [{indice}]')
    lista[valor] = float(input())


tupla = tuple(lista)
print(f'A lista {lista} invertida é :')
print(tupla[::-1])
