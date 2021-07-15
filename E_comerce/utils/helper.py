def formata_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


valor = 1500.00
print(formata_moeda(valor))
