# testando sapoha de listas

# esses *15 so deixa o codigo podre
print("Seja bem vindo!")

# carrinho = []
carrinho = list()
produto = ''
resposta = ''
while resposta != 'n':
    # Você pode colcoar uma string dentro do input
    # print()
    # aqui eu indiquei o tipo de dado do input
    # eu usei uma variavel difernte para ficar mais organizado
    # do que usar produto mesmo
    resposta = str(input("quer cadastrar um produto? \n(Digite 's' para sim "
                         "ou 'n' para sair) : ")).lower()  # isso aqui pega uma string e coloca minusculo
    if resposta == 'n' and len(carrinho) == 0:
        print("Você saiu sem cadastrar nenhum produto :( ")
        exit(0)

    while resposta != 'n':
        produto = str(input("Digite o nome do produto  ou sair para sair do programa: "))
        if produto == 'sair':
            resposta = 'n'
        else:
            carrinho.append(produto)

# isso aqui ta certissimo
for produto in carrinho:
    # esse print aqui já é valido, no inicio é feio
    print('_' * 10)
    print(produto)
# aqui printa o tamanho função len(variável)
print(f'Tamanho da lista = {len(carrinho)}')
# aqui printa a lista simples
print(f'Sua lista: {carrinho}')
# dessa forma printa o indice do vetor com o valor
# copia isso
for indice, valor in enumerate(carrinho):
    print(f'{indice +1} => {valor}')
exit(0)
