vetor1 = []
vpares = []
vetor2 = []
vimpares = []

for n in range(10):
    valor1 = int(input(f'Informe o valor {n + 1}/10 do vetor1: '))
    vetor1.append(valor1)
    if valor1 % 2 == 0:
        vpares.append(valor1)
    valor2 = int(input(f'Informe o valor {n + 1}/10 do vetor2: '))
    vetor2.append(valor2)
    if valor2 % 2 == 1:
        vimpares.append(valor2)

print(f'Vetor 1: {vetor1}')
print(f'Pares do vetor 1: {vpares}')
print(f'Vetor 2: {vetor1}')
print(f'Ímpares do vetor 2: {vimpares}')
