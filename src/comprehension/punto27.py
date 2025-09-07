# Genero residuos de dividir números del 0 al 19 entre 5
residuos = {numero % 5 for numero in range(20)}

# Muestro los residuos únicos posibles (siempre del 0 al 4)
print(residuos)  # {0, 1, 2, 3, 4}