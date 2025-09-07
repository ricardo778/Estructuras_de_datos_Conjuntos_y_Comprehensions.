# Creo un diccionario vacío para guardar números y sus cuadrados
cuadrados = {}

# Recorro números del 0 al 4
for numero in range(5):
    # Asigno a cada número su cuadrado como valor
    cuadrados[numero] = numero ** 2

# Muestro el diccionario resultante
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}