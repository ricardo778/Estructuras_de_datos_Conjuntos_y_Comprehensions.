# Tres grupos de números diferentes
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

# Busco números que están en A y B, pero NO en C
resultado = (A & B) - C
print(resultado)  # {3, 4}

# Busco números que están en A o C, pero NO en B  
resultado2 = (A | C) - B
print(resultado2)  # {1, 2, 7, 8}