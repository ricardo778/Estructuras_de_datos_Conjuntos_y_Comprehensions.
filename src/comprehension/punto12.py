# Tengo un diccionario de frutas con claves y valores en minúsculas
frutas = {"a": "apple", "b": "banana", "c": "cherry"}

# Convierto todos los valores a mayúsculas manteniendo las mismas claves
frutas_mayusculas = {clave: valor.upper() for clave, valor in frutas.items()}

# Muestro el diccionario con los valores en mayúsculas
print(frutas_mayusculas)  # {'a': 'APPLE', 'b': 'BANANA', 'c': 'CHERRY'}