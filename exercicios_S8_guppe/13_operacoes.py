def operacao(a, b, simbolo):
    if simbolo == '+':
        return a + b
    elif simbolo == '-':
        return a - b
    elif simbolo == '/':
        return a / b
    elif simbolo == '*':
        return a * b
    return "operação inválida"


def teste():
    global a
    global b
    global simbolo
    a = float(input("digite um numero real para 'a' : "))
    b = float(input("Digite um valor para b : "))
    simbolo = input("Digite um simbolo matematico : ")
    print(operacao(a, b, simbolo))


teste()
