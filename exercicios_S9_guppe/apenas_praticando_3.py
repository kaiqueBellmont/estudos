# lambdas
calculo = lambda x, y: x + y
print(calculo(10, 10))

pares = lambda x: x if x % 2 == 0 else print(f'{x} é impar')
print(pares(11))


lista0 = [x for x in range(10)]
print(lista0)

teste1 = lambda x: x ** 2 if x % 2 == 0 else x ** -1

for n in range(len(lista0)):
    print(teste1(n))


autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
