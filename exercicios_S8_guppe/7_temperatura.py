def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9.0/5.0) + 32.0
    return fahrenheit


celsius = float(input("Digite a temperatura em celsius para ser convertida : "))
print(celsius_to_fahrenheit(celsius))
