lista = list(range(3))
lista_negativos = list
for indice, valor in enumerate(lista):
    print("Digite um numero negativo:")
    lista[valor] = float(input())
    if lista[valor] < 0:
        for indice, valor in enumerate(lista_negativos):
            lista_negativos = lista[valor]


print(lista)
print(lista_negativos)
