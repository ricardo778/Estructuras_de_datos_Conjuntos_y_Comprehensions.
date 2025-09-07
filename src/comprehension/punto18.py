# Tengo una lista con letras, algunas repetidas
letras = ["a", "b", "a", "c"]

# Primero muestro cómo funciona la sobrescritura de claves
conteo = {letra: letras.count(letra) for letra in letras}
print(conteo)  # {'a': 2, 'b': 1, 'c': 1}

# Luego muestro la solución usando set para evitar claves duplicadas
conteo = {letra: letras.count(letra) for letra in set(letras)}
print(conteo)  # {'a': 2, 'b': 1, 'c': 1}