lista = list(range(50))
for i, valor in enumerate(lista):
    lista[valor] = (i + 5 * i) % (i + 1)

print(f'{lista}')

