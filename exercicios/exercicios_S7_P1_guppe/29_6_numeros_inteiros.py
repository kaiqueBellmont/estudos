numeros_pares = list()
numeros_impares = list()
lista = [int(input(f'Digite o valor para o indice {indice} : ')) for indice in range(6)]
for indice, valor in enumerate(lista):
    if valor < 0:
        numeros_impares.append(valor)
    else:
        numeros_pares.append(valor)

print(f'Numeros pares digitados: {numeros_pares}')
print(f'A soma dos numeros pares digitados: {sum(numeros_pares)}')
if len(numeros_impares) > 0:
    print(f'Numeros impares digitados: {numeros_impares}')
    print(f'Quantidade de numeros ímpares: {len(numeros_impares)}')

