# Creo el mismo diccionario usando dict comprehension
# En una línea genero números como claves y sus cuadrados como valores
cuadrados = {numero: numero ** 2 for numero in range(5)}

# Muestro el diccionario resultante
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}