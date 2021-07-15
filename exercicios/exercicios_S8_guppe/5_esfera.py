def volume_esfera(raio):
    volume = 4/3 * 3.14 * pow(raio, 3)
    return volume


def saida_dados():
    print(f'O volume da esfera é {volume_esfera(raio):.2f}')


raio = float(input(f'Digite o raio da esfera : '))
saida_dados()
volume_esfera(raio)


