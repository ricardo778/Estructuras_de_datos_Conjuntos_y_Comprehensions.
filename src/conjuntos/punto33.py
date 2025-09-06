# Tengo dos grupos de personas diferentes
grupo1 = {"Ana", "Carlos", "David"}
grupo2 = {"Carlos", "Elena", "Fernando"}

# Quiero saber quiénes están solo en un grupo, no en los dos
# Esto me deja en grupo1 solo las personas que son únicas de cada grupo
grupo1.symmetric_difference_update(grupo2)

# Ahora grupo1 tiene a las personas que no se repiten entre los grupos
print(grupo1)  # {'Ana', 'David', 'Elena', 'Fernando'}