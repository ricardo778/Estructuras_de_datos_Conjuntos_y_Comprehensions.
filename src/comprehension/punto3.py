# Primero con bucle tradicional: filtro números pares
pares = []
for numero in range(10):
    if numero % 2 == 0:  # Solo agrego si el número es par
        pares.append(numero)

print(pares)  # [0, 2, 4, 6, 8]

# Ahora con list comprehension: mismo resultado en una línea
pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]