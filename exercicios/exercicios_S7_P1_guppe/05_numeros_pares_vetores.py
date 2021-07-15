lista = list(range(10))
valores_pares = 0
for indice, valor in enumerate(lista):
    print(f'Digite um valor para o indice [{indice}]:')
    lista[valor] = int(input())
    if lista[valor] % 2 == 0:
        valores_pares += 1


print(lista)
print(f'A lista tem {valores_pares} vetores com valor par.')
