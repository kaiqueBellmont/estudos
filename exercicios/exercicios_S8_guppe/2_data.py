def data():
    dia = int(input(f'Digite o dia em numeros inteiros : '))
    mes = int(input(f'Digite o mes em numeros inteiros : '))
    ano = int(input(f'Digite o ano em numeros inteiros : '))
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 3:
        mes = 'março'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    elif mes == 12:
        mes = 'dezembro'
    else:
        print("data informada inváida")
    return print(f'Dia {dia} de {mes} de {ano}')


data()
