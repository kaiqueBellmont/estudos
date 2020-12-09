#conjuntos
conjunto_x = []
conjunto_y = []
for n in range(5):
    valor1 = int(input(f'Digite o valor "x" para o indice {n} : '))
    conjunto_x.append(valor1)
    valor2 = int(input(f'Digite o valor "y" para o indice {n} : '))
    conjunto_y.append(valor2)

produto_escalar = 0
for n in range(5):
    produto_escalar += (conjunto_x[n] * conjunto_y[n])

print(produto_escalar)
