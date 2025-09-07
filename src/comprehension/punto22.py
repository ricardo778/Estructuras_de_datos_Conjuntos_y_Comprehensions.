# Tengo una lista con números duplicados
numeros = [1, 2, 2, 3, 4, 3, 5, 5, 1]

# Convierto la lista en un conjunto para eliminar duplicados
numeros_unicos = {numero for numero in numeros}

# Muestro el conjunto con números únicos
print(numeros_unicos)  # {1, 2, 3, 4, 5}