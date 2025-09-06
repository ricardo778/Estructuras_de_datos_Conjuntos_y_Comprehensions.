# Esto funciona (todos los elementos son inmutables)
conjunto_valido = {1, "hola", (1, 2)}
print("Este conjunto es válido:", conjunto_valido)

# Esto produce un error (las listas son mutables)
# conjunto_invalido = {1, [2, 3]}  # TypeError: unhashable type: 'list'
# Si descomentas la línea de arriba y la ejecutas, verás el error en la consola.
print("Las listas no se pueden agregar a conjuntos porque son mutables.")