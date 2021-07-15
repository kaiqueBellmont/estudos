import numpy as np


tamanho = 2
matriz5x5 = [[[] for i in range(tamanho)] for i in range(tamanho)]
for i in range(tamanho):
    for j in range(tamanho):
        matriz5x5[i][j] = int(input(f'Digite o valor para o indice [{i},{j}] : '))

x = int(input(f'Digite o valor de "x" : '))

for i in range(tamanho):
    for j in range(tamanho):
        if x == matriz5x5[i][j]:
            print(f'o valor {x} está no indice: {i},{j}')
            break

if x not in np.matrix(matriz5x5):
    print("valor não encontrado")