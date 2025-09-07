# Tengo un diccionario original con letras como claves y números como valores
original = {"a": 1, "b": 2, "c": 3}

# Invierto el diccionario: ahora los números son claves y las letras son valores
invertido = {valor: clave for clave, valor in original.items()}

# Muestro el diccionario invertido
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}