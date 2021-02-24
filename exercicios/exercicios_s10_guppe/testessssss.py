from random import choice


gen = (str(x) for x in range(1, 10000))
print(choice(tuple(gen)))

