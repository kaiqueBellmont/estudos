from collections import deque

lista = deque(range(5))
for indice, valor in enumerate(lista):
    lista[valor] = float(input(f'Digite um valor para o indice [{indice}]: '))


print(lista)
opcao = input(f'Digite "1" para imprimir a lista:\n' +
              'Digite "2" para imprimir a lista inversa:\n' +
              'Ou digite "0" para Sair : ')

if opcao == '1':
    print("sua lista:")
elif opcao == '2':
    print("Sua lista invertida:")
    lista = tuple(lista)
    print(lista[::-1])
elif opcao == '0':
    print("saindo do programa.....")
    exit(0)
else:
    print("Opção inválida")
    opcao = input("Digite a opção correta:")
