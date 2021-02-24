def somar(a, b):
    return a + b


def calcular(a, b, funcao):
    return funcao(a, b)


print(calcular(10, 20, somar))


def saudacoes(nome):
    def cumprimento():
        return 'E ai ? tudo bem '
    return cumprimento() + nome + '?'


print(saudacoes('kaique'))
