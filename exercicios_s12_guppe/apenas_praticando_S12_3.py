from random import choice


def escolhido(pessoa):
    def numero_escolhido():
        lista = (str(x) for x in range(10000))
        return choice(tuple(lista))
    return f'{pessoa} e {numero_escolhido()}'


print(escolhido('kaique'))


from random import randint


def sorteando(nome):
    def numero():
        numero_sorteado = randint(1, 1000)
        return numero_sorteado
    return f'Parabéns {nome} Seu número {numero()} foi sorteado e você é o vencedor ! '


print(sorteando('kaique'))


def falas_aleatorias(pessoa):
    def falas():
        falas = choice(('Hoje você vai morrer !', 'Amanhã é um novo dia!', 'Kaique para de estudar por hj ! '))
        return f'{pessoa}:  {falas}'
    return falas()


print(falas_aleatorias('João'))
