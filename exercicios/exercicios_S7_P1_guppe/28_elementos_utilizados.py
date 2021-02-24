lista = [float(input(f'Digite o valor para o indice {indice} : ')) for indice in range(10)]
lista_impares = list()
lista_pares = list()
for indice, valor in enumerate(lista):
    if valor < 0:
        lista_impares.append(valor)
    else:
        lista_pares.append(valor)

for indice, valor in enumerate(lista_pares):
    print(f'Ultilizados pares: indice :{indice} valor : {valor}')

for indice, valor in enumerate(lista_impares):
    print(f'Ultilizados impares: indice :{indice} valor: {valor}')
