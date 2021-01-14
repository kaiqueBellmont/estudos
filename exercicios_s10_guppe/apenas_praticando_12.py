def potency(a, b):
    try:
        return a ** b
    except TypeError:
        try:
            return float(a) ** float(b)
        except ValueError:
            return f'ALgum desses caracteres não é válido : "{a}" e/ou "{b}"'


print(potency('%', 15))
