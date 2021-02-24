tamanho = 15
lista = [float(input(f'Digite um valor para a posição {indice} : (restante: {tamanho - indice}) : '))
         for indice in range(tamanho)]

for indice, valor in enumerate(lista):
    if valor == 0:
        lista.remove(valor)

for indice, valor in enumerate(lista):
    print(f'{indice} = {valor}')

print(f'Tamanho da lista sem os "0":  {len(lista)}')

