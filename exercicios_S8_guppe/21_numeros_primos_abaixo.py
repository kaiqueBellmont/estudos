def quantidade_primos(num):
    global lista1
    for i in range(2, num):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            lista1.append(i)
        if i == 2 or i == 3 or i == 5 or i == 7:
            lista1.append(i)
    return len(lista1)


lista1 = list()
print(f'{quantidade_primos(100)} : {lista1[::-1]}')


