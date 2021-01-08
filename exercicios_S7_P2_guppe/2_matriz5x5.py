import numpy as np


matriz5x5 = [[[] for i in range(5)] for i in range(5)]
num = 0
for i in range(5):
    for j in range(5):
        num += 1
        matriz5x5[i][j] = 0
z = 0
for x, y in enumerate(matriz5x5):
    y[z] = 1
    z += 1
print(np.matrix(matriz5x5))
