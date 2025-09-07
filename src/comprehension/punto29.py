# Tengo una lista de compras de diferentes clientes
compras = [
    {"cliente": "Ana", "producto": "laptop"},
    {"cliente": "Juan", "producto": "teléfono"},
    {"cliente": "Ana", "producto": "auriculares"},
    {"cliente": "Pedro", "producto": "laptop"},
    {"cliente": "Juan", "producto": "auriculares"},
    {"cliente": "Ana", "producto": "teléfono"}
]

# Extraigo todos los productos únicos que se compraron
productos_unicos = {compra["producto"] for compra in compras}
print(productos_unicos)  # {'laptop', 'teléfono', 'auriculares'}

# Filtro solo los clientes que compraron laptops
compradores_laptop = {compra["cliente"] for compra in compras if compra["producto"] == "laptop"}
print(compradores_laptop)  # {'Ana', 'Pedro'}

# Obtengo las iniciales únicas de todos los clientes
iniciales_clientes = {cliente["cliente"][0] for cliente in compras}
print(iniciales_clientes)  # {'A', 'J', 'P'}