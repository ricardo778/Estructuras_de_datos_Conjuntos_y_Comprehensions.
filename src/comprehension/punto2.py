# Creo la lista de cuadrados usando list comprehension
# En una sola línea genero todos los cuadrados del 0 al 9
cuadrados = [numero ** 2 for numero in range(10)]

# Muestro el resultado que es idéntico al método tradicional
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]