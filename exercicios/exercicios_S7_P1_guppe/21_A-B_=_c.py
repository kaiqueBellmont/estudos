'''
listaA = list(range(2))
listaB = list(range(2))
listaC = []
for indice, valor in enumerate(listaA):
    listaA[valor] = int(input(f'Digite um valor para o indice [{indice}] da lista A : '))

for indice, valor in enumerate(listaB):
    listaA[valor] = int(input(f'Digite um valor para o indice [{indice}] da lista B : '))

zip_object = zip(listaA, listaB)
for listaA_valor, listaB_valor in zip_object:
    listaC.append(listaA_valor - listaB_valor)
print(listaC)
'''

a = {100, 20}
b = {13, 18}
c = set.difference(a - b)
print(c)



