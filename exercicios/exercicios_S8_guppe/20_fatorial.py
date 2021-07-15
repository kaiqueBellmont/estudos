def fatorial(numero):
    """
    função simples que retorna o fatorial de um numero
    :param numero:
    :return:
    """
    resultado = 1
    for n in range(1, numero):
        resultado *= numero
        numero -= 1
    return resultado


print(fatorial(7))

