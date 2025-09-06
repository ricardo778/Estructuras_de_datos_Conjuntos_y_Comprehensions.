# Productos que vende la tienda A
productos_tienda_a = {"laptop", "teléfono", "tablet", "auriculares"}
# Productos que están en oferta
productos_oferta = {"laptop", "auriculares", "cámara"}

# Me quedo solo con los productos que están en oferta
productos_tienda_a &= productos_oferta

# Muestro los productos que tienen descuento
print(productos_tienda_a)  # {'laptop', 'auriculares'}