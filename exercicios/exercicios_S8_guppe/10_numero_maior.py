def numero_maior():
    num1 = float(input("Digite um numero qualquer : "))
    num2 = float(input("Digite outro numero qualquer : "))
    if num1 > num2:
        maior = num1
        return maior
    else:
        maior = num2
        return maior


print(numero_maior())
