# Defino dos conjuntos de números
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Creo un conjunto con el doble de los elementos de la unión de A y B
union_doble = {elemento * 2 for elemento in A.union(B)}
print(union_doble)  # {2, 4, 6, 8, 10, 12, 14, 16}

# Creo un conjunto con el cuadrado de los elementos comunes entre A y B
interseccion_cuadrado = {elemento ** 2 for elemento in A.intersection(B)}
print(interseccion_cuadrado)  # {16, 25}