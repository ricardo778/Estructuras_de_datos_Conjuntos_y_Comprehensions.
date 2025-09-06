# Conjunto de inventario y conjunto de artículos vendidos.
inventario = {"laptop", "teléfono", "tablet", "auriculares"}
vendidos = {"laptop", "auriculares"}

# Usamos la diferencia para encontrar los artículos disponibles.
disponibles = inventario.difference(vendidos)

# Imprimimos el conjunto de artículos disponibles.
print(disponibles)
