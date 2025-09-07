# Tengo un diccionario con el stock de frutas
stock = {"manzanas": 10, "plátanos": 3, "naranjas": 25, "peras": 0}

# Filtro solo las frutas que tienen cantidad mayor a 0
disponibles = {fruta: cantidad for fruta, cantidad in stock.items() if cantidad > 0}

# Muestro solo las frutas disponibles en stock
print(disponibles)  # {'manzanas': 10, 'plátanos': 3, 'naranjas': 25}