# Tengo tres grupos diferentes de números
grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7}
grupo_c = {1, 5, 7, 9}

# Busco los números que están en A y B, pero NO en C
resultado = grupo_a.intersection(grupo_b).difference(grupo_c)

# Muestro el resultado de esta búsqueda combinada
print(resultado)  # {4} - El único número que cumple todas las condiciones