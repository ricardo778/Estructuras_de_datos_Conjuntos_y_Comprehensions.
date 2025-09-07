# Voy a crear una lista con los cuadrados de los números del 0 al 9
# Primero creo una lista vacía donde guardaré los resultados
cuadrados = []

# Recorro cada número del 0 al 9 usando un bucle for
for numero in range(10):
    # Calculo el cuadrado de cada número y lo agrego a la lista
    cuadrados.append(numero ** 2)

# Muestro la lista final con todos los cuadrados
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]