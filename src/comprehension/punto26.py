# Tengo una lista de palabras de diferentes longitudes
palabras = ["casa", "perro", "sol", "luna", "mar", "montaña"]

# Calculo la longitud de cada palabra y creo un conjunto
longitudes_unicas = {len(palabra) for palabra in palabras}

# Muestro las longitudes únicas (sin valores repetidos)
print(longitudes_unicas)  # {3, 4, 5, 7}