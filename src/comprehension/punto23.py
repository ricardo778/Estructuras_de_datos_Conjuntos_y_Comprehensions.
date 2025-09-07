# Método 1: Bucle tradicional para cuadrados de números pares
pares_cuadrados = set()
for numero in range(10):
    if numero % 2 == 0:  # Solo agrego si el número es par
        pares_cuadrados.add(numero ** 2)

print(pares_cuadrados)  # {0, 4, 16, 36, 64}

# Método 2: Set comprehension para el mismo resultado
pares_cuadrados = {numero ** 2 for numero in range(10) if numero % 2 == 0}
print(pares_cuadrados)  # {0, 4, 16, 36, 64}