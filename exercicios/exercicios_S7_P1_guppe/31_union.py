tamanho = 10
conjunto1 = {input(f'Digite um valor numerico para o conjunto 1 (restante:({tamanho - valor}) : ')
             for valor in range(tamanho)}
conjunto2 = {input(f'Digite um valor numerico para o conjunto 2 (restante:({tamanho - valor}) : ')
             for valor in range(tamanho)}

union = conjunto1.union(conjunto2)
lista = list()
print(f'Conjunto 1 : {sorted(conjunto1)}')
print(f'Conjunto 2 : {sorted(conjunto2)}')
for indice, valor in enumerate(union):
    lista.append(valor)
print(f'união dos conjuntos : {sorted(lista)}')
