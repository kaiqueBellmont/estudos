def triangulo(a, b, c):
    return a < b + c and b < a + c and c < b + a


def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return 'equilátero'
    elif a == b and a != c or a != b and b == c or a != b and a == c:
        return 'isosceles'
    elif a != b and b != c and c != a:
        return 'escaleno'
    return 'Valores inseridos incorretamente'


def programa():
    a = float(input("Digite o valor do lado 'a' "))
    if a <= 0:
        while a <= 0:
            a = float(input("Digite o valor do lado 'a' "))
    b = float(input("Digite o valor do lado 'b' "))
    if b <= 0:
        while b <= 0:
            b = float(input("Digite o valor do lado 'b' "))
    c = float(input("Digite o valor do lado 'c' "))
    if c <= 0:
        while c <= 0:
            c = float(input("Digite o valor do lado 'c' "))
    if not triangulo(a, b, c):
        print("Não é um triângulo.")
    else:
        print(tipo_triangulo(a, b, c))
        print(f'Medidas: a = {a}, b = {b}, c = {c}')


programa()

