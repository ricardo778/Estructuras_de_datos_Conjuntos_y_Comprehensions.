# Define una función para eliminar duplicados de una lista manteniendo el orden original.
def eliminar_duplicados(secuencia):
    # La función utiliza 'dict.fromkeys' para crear un diccionario.
    # Los diccionarios solo pueden tener claves únicas, así que elimina los duplicados.
    # Luego, 'list()' convierte el resultado de nuevo a una lista.
    return list(dict.fromkeys(secuencia))

# Esta es una lista con números repetidos.
lista_con_duplicados = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Llama a la función y muestra la lista sin duplicados.
print(eliminar_duplicados(lista_con_duplicados))  # Imprime: [3, 1, 4, 5, 9, 2, 6]