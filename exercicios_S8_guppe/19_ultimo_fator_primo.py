def primo(valor):
    ultimo_primo = 0
    for i in range(2, valor):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            ultimo_primo = i
        if valor <= 10:
            ultimo_primo = 7
        if 5 < valor < 7:
            ultimo_primo = 5
        if 2 <= valor <= 5:
            ultimo_primo = 3
        if valor <= 2:
            ultimo_primo = 2

    return ultimo_primo


valor = int(input())
print(primo(valor))

