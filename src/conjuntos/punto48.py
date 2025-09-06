# Muebles que tengo en mi inventario actual
inventario_actual = {"mesa", "silla", "lámpara", "estantería"}
# Muebles que me acaban de entregar
nueva_entrega = {"mesa", "sofá", "alfombra", "estantería"}

# Actualizo mi inventario quitando duplicados y agregando lo nuevo
inventario_actual ^= nueva_entrega

# Muestro mi inventario actualizado sin repetidos
print(inventario_actual)  # {'silla', 'lámpara', 'sofá', 'alfombra'}