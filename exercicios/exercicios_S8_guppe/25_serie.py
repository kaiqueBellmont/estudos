def somatorio(numero):
    serie = (2/4) + (5/5) + (10/6) + ((numero * numero) + 1) / (numero + 3)
    return serie


print(f'{somatorio(13):.5f}')

