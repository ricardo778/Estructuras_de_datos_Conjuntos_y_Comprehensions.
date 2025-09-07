# Tengo una lista con números duplicados y desordenados
numeros = [5, 2, 3, 1, 4, 3]

# Uso dict.fromkeys para eliminar duplicados manteniendo el orden
numeros_unicos_ordenados = list(dict.fromkeys(numeros))

# Muestro la lista sin duplicados pero conservando el orden original
print(numeros_unicos_ordenados)  # [5, 2, 3, 1, 4]