# Este é um programa que verifica casos primos em um vetor.
import math
lista = [int(input(f'Digite o valor para o vetor [{i}] :')) for i in range(10)]
for indice, valor in enumerate(lista):
    for i in range(2, valor):
        if valor < 9 and valor != 7:
            if valor % i == 0:
                break
            else:
                print(f'{valor} é primo no indice {indice}')

        if valor % i == 0:
            break
        elif valor % 3 == 0:
            break
        elif valor % 5 == 0:
            break
        else:
            print(f'{valor} é primo no indice {indice}')
            break

#essa desgraça deu trabalho demais pqp

