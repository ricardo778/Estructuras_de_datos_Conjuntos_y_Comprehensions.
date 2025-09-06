# Usuarios que están activos en este momento
usuarios_activos = {"user1", "user2", "user3", "user4"}

# Usuarios que pagan suscripción premium  
usuarios_premium = {"user2", "user4", "user5"}

# Filtro para quedarme solo con los usuarios activos que son premium
usuarios_activos.intersection_update(usuarios_premium)

# Muestro el resultado final
print(usuarios_activos)  # {'user2', 'user4'}