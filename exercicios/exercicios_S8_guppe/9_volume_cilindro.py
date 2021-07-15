def volume():
    altura = float(input("Digite a altura do cilindro : "))
    raio = float(input("Digite o raio do cilindro : "))
    volume = 3.141592 * pow(raio, 2) * altura
    return volume


print(volume())
