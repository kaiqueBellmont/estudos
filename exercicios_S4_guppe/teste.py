def isfloat(numero):
    try:
        int(numero)
        return int(numero)
    except ValueError:
        return False


print("teste")
numero = int(input())
while numero not in range(100, 999):
    while not numero.isfloat():
        print("nao Está")
