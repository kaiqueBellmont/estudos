def notas(a, b, c, letra):
    if letra == 'A' or letra == 'a':
        return (a + b + c) / 3
    elif letra == 'p' or letra == 'P':
        media_ponderada = ((a * 5) + (b * 3) + (c * 2)) / 5 + 3 + 2
        return media_ponderada


def teste():
    global a
    global b
    global c
    a = float(input("Digite a nota 1 : "))
    b = float(input("Digite a nota 2 : "))
    c = float(input("Digite a nota 3 : "))
    letra = str(input("Digite A para media aritmetica ou P para ponderada : "))
    print(notas(a, b, c, letra))


teste()
