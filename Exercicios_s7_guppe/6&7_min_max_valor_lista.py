lista = list(range(10))
for indice, valor in enumerate(lista):
    print(f'Digite o valor para o indice: [{indice}]')
    lista[valor] = float(input())


menor_valor = min(lista)
maior_valor = max(lista)
print(f'O menor valor da lista é o {menor_valor} indice: {lista.index(menor_valor)}')
print(f'O maior valor da lista é o {maior_valor} indice: {lista.index(maior_valor)}')


