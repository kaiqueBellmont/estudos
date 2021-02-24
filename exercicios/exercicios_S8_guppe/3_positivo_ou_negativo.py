def positivo_ou_negativo(num):
    if num > 0:
        num = 1
    elif num < 0:
        num = -1
    elif num == 0:
        num = 0
    return num


num = float(input("Digite um número real : "))
print(positivo_ou_negativo(num))
