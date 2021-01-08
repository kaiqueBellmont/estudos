lista = list(range(8))
for indice, valor in enumerate(lista):
    print(f'Digite o valor para o vetor [{indice}]:')
    lista[valor] = int(input())

print(f'Digite o indice X :')
indice_x = int(input())
print(f'Digite o indice Y :')
indice_y = int(input())

print(f'a soma dos indices[{indice_x}] + [{indice_y}] = {lista[indice_x] + lista[indice_y]}')

