# Creo un conjunto original con números y una tupla
original = {1, 2, (3, 4)}

# Hago una copia independiente del conjunto original
copia = original.copy()

# Agrego un nuevo elemento solo al conjunto original
original.add(5)

# Muestro ambos conjuntos para ver que son independientes
print(original)  # {1, 2, (3, 4), 5} - Tiene el nuevo elemento
print(copia)     # {1, 2, (3, 4)} - La copia no cambió