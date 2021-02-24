"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        print(f'indice: ({i},{j}) = {matrix[i][j]}')
"""
import numpy as np


matriz4x4 = [[[] for i in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        matriz4x4[i][j] = i + j


print(matriz4x4)
print(np.matrix(matriz4x4))