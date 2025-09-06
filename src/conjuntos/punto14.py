# Creamos un conjunto llamado 'colores' con tres elementos.
colores = {"rojo", "verde", "azul"}

# Usamos el método '.pop()' para eliminar y obtener un elemento aleatorio del conjunto.
# Los conjuntos no tienen un orden fijo, por lo que el elemento que se elimina es impredecible.
color_eliminado = colores.pop()

# Imprimimos el color que fue eliminado.
print(f"Se eliminó: {color_eliminado}")

# Imprimimos el conjunto para ver qué elementos quedaron.
print(f"Conjunto resultante: {colores}")