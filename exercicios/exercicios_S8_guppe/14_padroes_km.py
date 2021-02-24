def analise_carro(distancia_km, litros_consumidos):
    km_por_litro = distancia_km / litros_consumidos
    if km_por_litro > 8:
        return 'Venda o carro!'
    elif 8 >= km_por_litro <= 14:
        return 'Economico!'
    elif km_por_litro > 12:
        return 'Super economico!'
    return 'Dados inseridos incorretamente.'


distancia_km = float(input("Digite a distancia percorrida em KMs : "))
litros_consumidos = float(input("Digite a quantidade de litros consumidos no percurso : "))
print(analise_carro(distancia_km, litros_consumidos))



