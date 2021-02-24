"""
num = 123
#print([int(x) for x in str(num)])
convertido = list(map(int, str(num)))
print(convertido)
print(sum(convertido))

"""


def soma_lista():
    algarismo = int(input("Digite um numero inteiro com mais de uma dezena : "))
    convertido = list(map(int, str(algarismo)))
    soma = sum(convertido)
    return soma


print(soma_lista())

