import math


def catetos(a, b):
    hipotenusa = math.sqrt(pow(a, 2) + pow(b, 2))
    return hipotenusa


a = float(input("Digite o cateto a : "))
b = float(input("Digite o cateto b : "))
print(f'Hipotenusa = {catetos(a, b):.2f}')


