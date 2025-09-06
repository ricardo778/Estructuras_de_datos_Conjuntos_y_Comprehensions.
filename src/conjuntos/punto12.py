# Creamos un conjunto llamado 'numeros' con tres elementos únicos.
numeros = {1, 2, 3}

# Usamos el método '.add()' para intentar añadir un elemento que ya está en el conjunto.
# Los conjuntos no permiten elementos duplicados.
numeros.add(2)

# Imprimimos el conjunto actualizado.
# El resultado muestra que el conjunto no ha cambiado.
print(numeros)