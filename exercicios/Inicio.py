import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100  milhões
gen_tempo = time.time() - gen_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')