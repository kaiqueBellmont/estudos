def isfloat(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return False

    while not isfloat(value):
        if not isfloat(value):
            print("Digite um número válido (Use '.' [ponto] caso necessário) :")
            value = input()


value = value(float)
string = 14.5

