matriz = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z = 0
lista2 = list()
for x, y in enumerate(matriz):
    print(x)
    print(y[z])
    lista2.append(y[z])
    z += 1
