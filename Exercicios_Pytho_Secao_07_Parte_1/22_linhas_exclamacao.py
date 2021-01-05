def printar_pontos(num):
    ponto = "!"
    for i in range(1, num + 1):
        print(ponto * i)


num = int(input("Digite a quantidade de pontos/linhas "))
printar_pontos(num)
