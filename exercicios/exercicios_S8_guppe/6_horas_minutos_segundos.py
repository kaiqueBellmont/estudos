def conversao_segundos(horas, minutos, segundos):
    return (horas * 60 * 60) + (minutos * 60) + segundos


horas = 0
minutos = 0
segundos = 0


def teste():
    global horas
    global minutos
    global segundos
    horas = int(input("Digite a quantidade de horas : "))
    minutos = int(input("Digite a quantidade de minutos : "))
    segundos = int(input("Digite a quantidade de segundos : "))


teste()
print(f'O resultado de {horas} horas, {minutos} minutos e {segundos} segundos em segundos '
      f'é de {conversao_segundos(horas, minutos, segundos)} segundos')


