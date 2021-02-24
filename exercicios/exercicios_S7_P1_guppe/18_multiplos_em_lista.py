from collections import Counter
lista = list(range(4))
multiplos = []
for indice, valor in enumerate(lista):
    lista[valor] = float(input("Digite um numero:"))


digito = int(input("Digite um numero para ver o mutiplo:"))
for num in lista:
    if num % digito == 0:
        multiplos.append(num)
print(multiplos)










'''
for indice, valor in enumerate(lista):
    lista[valor] = float(input(f'Digite um numero para o índice[{indice}]: '))

'''

