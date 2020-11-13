def ms_to_kmh(ms):
    kmh = ms * 3.6
    print(f'{ms}M/S = {kmh:.2f}KM/h\n')
    return kmh


def isfloat(ms):
    try:
        float(ms)
        return float(ms)
    except ValueError:
        return False


opcao_continuar = 'sim'
while  opcao_continuar == 'sim':
    print("Digite o valor em M/S: (Use o ponto caso necessário)")
    ms = input()
    while not isfloat(ms):
        if not isfloat(ms):
            print("Digite um número válido (Use '.' [ponto] caso necessário) :")
            ms = input()

    ms = float(ms)
    ms_to_kmh(ms)

    print("Você deseja fazer outra conversão? \n[digite 'sim' ou 'nao']")
    opcao_continuar = input().lower().replace(' ', '')

    while opcao_continuar != 'nao' and opcao_continuar != 'sim':
        print("Você deseja fazer outra conversão? \n[digite 'sim' ou 'nao']")
        opcao_continuar = input().lower().replace(' ', '')
        if opcao_continuar == 'sim':
            opcao_continuar = 'sim'
        elif opcao_continuar == 'nao':
            break
print("ENCERRANDO....")
exit(0)
opcao_continuar = 'sim'
while  opcao_continuar == 'sim':
    print("Digite o valor em M/S:(Use o ponto caso necessário)")
    ms = input()
    while not isfloat(ms):
        if not isfloat(ms):
            print("Digite um número válido (Use '.' [ponto] caso necessário) :")
            ms = input()

    ms = float(ms)
    ms_to_kmh(ms)

    print("Você deseja fazer outra conversão? \n[digite 'sim' ou 'nao']")
    opcao_continuar = input().lower().replace(' ', '')

    while opcao_continuar != 'nao' and opcao_continuar != 'sim':
        print("Você deseja fazer outra conversão? \n[digite 'sim' ou 'nao']")
        opcao_continuar = input().lower().replace(' ', '')
        if opcao_continuar == 'sim':
            opcao_continuar = 'sim'
        elif opcao_continuar == 'nao':
            break
print("ENCERRANDO....")
exit(0)