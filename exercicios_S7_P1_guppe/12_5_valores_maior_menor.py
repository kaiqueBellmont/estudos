print("Digite 5 valores para o programa.")
lista = list(range(5))
for indice, valor in enumerate(lista):
    print('Digite um numero:')
    lista[valor] = input()


maximo = max(lista)
minimo = min(lista)
media = (float(maximo) + float(minimo)) / 2
print(media)
