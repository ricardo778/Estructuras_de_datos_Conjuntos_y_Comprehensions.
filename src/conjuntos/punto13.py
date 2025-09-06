# Creamos un conjunto llamado 'animales' con tres elementos.
animales = {"perro", "gato", "conejo"}

# Usamos el método '.discard()' para intentar eliminar un elemento.
# El elemento "pájaro" no existe en el conjunto, pero este método no produce un error.
animales.discard("pájaro")

# Imprimimos el conjunto. Como el elemento no estaba, el conjunto sigue igual.
print(animales)