# Conjunto de asignaturas de ciencias y artes.
ciencias = {"física", "química", "biología", "matemáticas"}
artes = {"literatura", "música", "pintura", "matemáticas"}

# Usamos la diferencia simétrica para encontrar los elementos que no están en ambos conjuntos.
exclusivos = ciencias.symmetric_difference(artes)

# Imprimimos el conjunto de asignaturas exclusivas.
print(exclusivos)
