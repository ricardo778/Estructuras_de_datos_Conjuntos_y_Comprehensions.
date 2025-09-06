# Ciudades que están en Europa
ciudades_europa = {"Madrid", "París", "Roma", "Berlín"}
# Ciudades que están en Asia
ciudades_asia = {"Tokio", "Pekín", "Seúl", "Bangkok"}

# Uno todas las ciudades de ambos continentes
todas_ciudades = ciudades_europa | ciudades_asia

# Muestro la lista completa de ciudades
print(todas_ciudades)  # {'Madrid', 'París', 'Roma', 'Berlín', 'Tokio', 'Pekín', 'Seúl', 'Bangkok'}