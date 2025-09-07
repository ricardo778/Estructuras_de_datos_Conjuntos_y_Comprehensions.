# Primero con bucle tradicional: filtro números pares y sus cuadrados
pares_cuadrados = {}
for numero in range(10):
    if numero % 2 == 0:  # Solo agrego si el número es par
        pares_cuadrados[numero] = numero ** 2

print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Ahora con dict comprehension: mismo resultado en una línea
pares_cuadrados = {numero: numero ** 2 for numero in range(10) if numero % 2 == 0}
print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}