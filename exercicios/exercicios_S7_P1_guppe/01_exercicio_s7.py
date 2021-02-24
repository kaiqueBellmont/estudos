#listaA: list = 1, 0, 5, -2, -5, 7
#(a)
listaA = [1, 0, 5, -2, -5, 7]
print(listaA)
#(b):
soma = listaA[0] + listaA[1] + listaA[5]
print(f' A soma dos vetores 0, 1 e 5 = {soma}')

'''
listaA.sort()
print(listaA)
'''
#(c):
listaA.insert(4, 100)
print(listaA)

for indice, valor in enumerate(listaA):
    print(f'índice[{indice}] = {valor}')




