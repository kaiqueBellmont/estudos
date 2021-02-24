import math


def quadrado_perfeito(num):
    if num > 0 and int and math.sqrt(num) - math.floor(math.sqrt(num)) == 0:
        print(f'Seu numero {num} é um quadrado perfeito! ')
    else:
        print(f'Seu numero {num} não é um quadrado perfeito!')
    return num


num = int(input())
quadrado_perfeito(num)
