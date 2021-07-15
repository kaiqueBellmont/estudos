def printar(num):
    sinal = "*"
    expressao = 2 * num - 1
    metade = (2 * num) / 2
    metade = int(metade)
    n = 1
    for i in range(1, metade + 1):
        print(sinal * n)
        n += 1
    n = metade - 1
    for i in range(metade):
        print(sinal * n)
        n -= 1


printar(100)



