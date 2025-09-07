# Creo un conjunto vacío para guardar los cuadrados
cuadrados = set()

# Recorro números del 0 al 4
for numero in range(5):
    # Calculo el cuadrado de cada número y lo agrego al conjunto
    cuadrados.add(numero ** 2)

# Muestro el conjunto con todos los cuadrados
print(cuadrados)  # {0, 1, 4, 9, 16}