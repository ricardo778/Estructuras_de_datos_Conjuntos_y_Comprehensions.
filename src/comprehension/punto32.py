# Tengo un texto en español
texto = "el perro corre tras el gato y el gato corre tras el ratón"

# Divido el texto en palabras individuales
palabras = texto.split()

# Creo un diccionario con palabras únicas y sus longitudes
diccionario_longitudes = {palabra: len(palabra) for palabra in {p for p in palabras}}

# Muestro el diccionario resultante
print(diccionario_longitudes)
# {'perro': 5, 'el': 2, 'corre': 5, 'tras': 4, 'gato': 4, 'y': 1, 'ratón': 5}