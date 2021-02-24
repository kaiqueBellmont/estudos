print("Digite 5 valores para o programa.")
lista = list(range(5))
for indice, valor in enumerate(lista):
    print('Digite um numero:')
    lista[valor] = input()


maximo_valor = max(lista)
minimo_valor = min(lista)
print(f'Sua lista : {lista}')
print(f'O indice do  maximo é {lista.index(maximo_valor)} (Valor): {maximo_valor}')
print(f'O indice do minimo é {lista.index(minimo_valor)} (Valor): {minimo_valor}')

