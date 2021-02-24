def printar_resultados():
    print(f'Conjunto dos positivos: {positivos}')
    print(f'Conjunto dos negativos: {negativos}')
    print(f'Quantidade denúmeros negativos: {qtd_negativos}')
    print(f'Soma dos números positivos: {soma_positivos}')


def separar_positivos_negativos(lista):
    positivos = []
    negativos = []
    for number in lista:
        if number >= 0:
             positivos.append(number)
        else:
             negativos.append(number)
    return positivos, negativos


lista = list(range(10))
soma_positivos = 0
qtd_negativos = 0
for indice, valor in enumerate(lista):
    print(f'Diite um número real qualquer para o indice {indice}:')
    lista[valor] = float(input())
    if lista[valor] > 0:
        soma_positivos += lista[valor]
    else:
        qtd_negativos += 1

positivos, negativos = separar_positivos_negativos(lista)
printar_resultados()
