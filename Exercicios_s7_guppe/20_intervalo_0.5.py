lista = list(range(4))
for indice, valor in enumerate(lista):
    lista[valor] = int(input(f'Digite um numero entre 0 e 50: '))

lista_negativos = []
for num in lista:
    if num < 0:
        lista_negativos.append(num)
        lista.remove(num)
    elif num > 50:
        lista.remove(num)

print(f'Sua lista de negativos: {lista_negativos}')
print(f'Sua lista entre 1 e 50: {lista}')

