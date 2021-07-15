tamanho = 10
lista = list()
for indice in range(tamanho):
    num = float(input(f'Digite um valor (sem repetir) ' +
                f'para o indice {indice} : (restante : {tamanho - indice}) : '))
    if num in lista:
        while num in lista:
            num = float(input(f'Digite um outro valor para o indice {indice} : '))
        lista.append(num)
    else:
        lista.append(num)

print(f'Sua lista:')
for indice, valor in enumerate(lista):
    print(f'Índice: {indice} -> {valor}')

