# Personas que están en el equipo A
equipo_a = {"Juan", "María", "Carlos", "Ana"}
# Personas que están en el equipo B  
equipo_b = {"Carlos", "Ana", "Pedro", "Lucía"}

# Busco las personas que están solo en un equipo, no en los dos
miembros_exclusivos = equipo_a ^ equipo_b

# Muestro los miembros que son únicos de cada equipo
print(miembros_exclusivos)  # {'Juan', 'María', 'Pedro', 'Lucía'}