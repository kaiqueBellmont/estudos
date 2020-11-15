lista = list(range(6))
for indice, valor in enumerate(lista):
    print(f'Digite um número PAR para o indice {indice}:')
    lista[valor] = float(input())
    while not lista[valor] % 2 == 0:
        print(f'Digite apenas numeros PARRES indice: {indice}:')
        lista[valor] = float(input())

print(f'Sua lista {lista}')
print(f'Sua lista invertida:{lista[::-1]}')