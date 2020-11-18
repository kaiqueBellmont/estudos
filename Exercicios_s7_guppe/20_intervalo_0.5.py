"""
A = [1, -3, -2, 8, 4, -5, 6, -7]
B = []
C = []
for x in A:
    if x >= 0:
        B.append(x)
    else:
        C.append(x)

"""
vetor1 = list(range(4))
vetor2 = list
for indice, valor in enumerate(vetor1):
    vetor1[valor] = int(input(f'Digite o valor para o indice: [{indice}] do vetor1:'))

for num in enumerate(vetor1):
    if num < 0:
        vetor2.append(num)


print(vetor1)
print(vetor2)
