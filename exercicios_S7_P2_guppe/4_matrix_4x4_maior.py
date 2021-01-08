import numpy as np


tamanho = 3
matriz4x4 = [[[] for i in range(tamanho)]for i in range(tamanho)]
linha = 0
coluna = 0
valormaximo = 0

for i in range(tamanho):
    for j in range(tamanho):
        matriz4x4[i][j] = int(input("digite : "))
        if matriz4x4[i][j] > valormaximo:
            valormaximo = matriz4x4[i][j]
            linha = i
            coluna = j

print(np.matrix(matriz4x4))
print(f'O valor maximo é : {valormaximo} indice: [{linha},{coluna}]')


