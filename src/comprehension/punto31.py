# Creo un rango grande de números
numeros_grandes = range(10000)

# Convierto el rango a un conjunto usando set comprehension
conjunto_numeros = {n for n in numeros_grandes}

# Verificar si un elemento está en el conjunto es muy rápido
print(9999 in conjunto_numeros)  # True