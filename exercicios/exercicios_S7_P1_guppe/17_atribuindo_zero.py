lista = list(range(10))
for indice, valor in enumerate(lista):
    lista[valor] = float(input(f'Digite um valor para o indice[{indice}]: '))
    if lista[valor] < 0:
       lista[valor] = 0

print(lista)



