# Creo el conjunto de cuadrados usando set comprehension
# En una sola línea genero todos los cuadrados del 0 al 4
cuadrados = {numero ** 2 for numero in range(5)}

# Muestro el conjunto resultante
print(cuadrados)  # {0, 1, 4, 9, 16}