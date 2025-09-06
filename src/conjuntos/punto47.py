# Tareas que tengo que hacer
tareas_pendientes = {"informe", "reunión", "correos", "presentación"}
# Tareas que ya terminé
tareas_completadas = {"informe", "correos"}

# Quito las tareas completadas de mi lista
tareas_pendientes -= tareas_completadas

# Muestro las tareas que me faltan por hacer
print(tareas_pendientes)  # {'reunión', 'presentación'}