# Tengo una lista de palabras
palabras = ["manzana", "banana", "mango", "melón", "mora", "naranja"]

# Extraigo la primera letra de cada palabra y creo un conjunto
primeras_letras = {palabra[0] for palabra in palabras}

# Muestro las primeras letras únicas (sin repetir)
print(primeras_letras)  # {'m', 'b', 'n'}