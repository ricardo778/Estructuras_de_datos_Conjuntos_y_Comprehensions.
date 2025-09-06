# Creamos un conjunto llamado 'original' con algunos números.
original = {1, 2, 3}

# Usamos el método .copy() para crear una copia.
# Esto es importante porque crea un nuevo objeto en memoria,
# en lugar de simplemente apuntar a 'original'.
copia = original.copy()

# Añadimos un nuevo elemento al conjunto 'copia'.
copia.add(4)

# Imprimimos el conjunto 'original'.
# Como 'copia' es una versión separada, 'original' no cambia.
print(original)

# Imprimimos el conjunto 'copia', que ahora tiene un nuevo elemento.
print(copia)
