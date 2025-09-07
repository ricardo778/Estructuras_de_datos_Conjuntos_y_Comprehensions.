# Tengo datos de ventas de diferentes productos
ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

# Calculo el valor total de ventas para cada producto
valor_por_producto = [item["unidades"] * item["precio"] for item in ventas]
print(valor_por_producto)  # [16000, 1250, 450, 2000]

# Filtro los productos que vendieron más de $1000
productos_alto_valor = [item["producto"] for item in ventas if item["unidades"] * item["precio"] > 1000]
print(productos_alto_valor)  # ['laptop', 'teclado', 'monitor']