# Tengo una lista de palabras en minúsculas
palabras = ["python", "es", "genial"]

# Convierto todas las palabras a mayúsculas
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['PYTHON', 'ES', 'GENIAL']

# Extraigo solo la primera letra de cada palabra
primeras_letras = [palabra[0] for palabra in palabras]
print(primeras_letras)  # ['p', 'e', 'g']