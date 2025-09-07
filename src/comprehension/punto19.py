# Tengo datos de ventas organizados por región y producto
ventas_por_region = [
    {"region": "Norte", "producto": "A", "ventas": 100},
    {"region": "Norte", "producto": "B", "ventas": 200},
    {"region": "Sur", "producto": "A", "ventas": 300},
    {"region": "Sur", "producto": "B", "ventas": 150},
    {"region": "Este", "producto": "A", "ventas": 250},
    {"region": "Oeste", "producto": "B", "ventas": 50}
]

# Método 1: Bucle tradicional para sumar ventas por región
total_por_region = {}
for venta in ventas_por_region:
    region = venta["region"]
    if region in total_por_region:
        total_por_region[region] += venta["ventas"]
    else:
        total_por_region[region] = venta["ventas"]

print(total_por_region)
# {'Norte': 300, 'Sur': 450, 'Este': 250, 'Oeste': 50}

# Método 2: Usando defaultdict para agrupar más eficientemente
from collections import defaultdict

ventas_agrupadas = defaultdict(int)
for venta in ventas_por_region:
    ventas_agrupadas[venta["region"]] += venta["ventas"]

total_por_region = dict(ventas_agrupadas)
print(total_por_region)
# {'Norte': 300, 'Sur': 450, 'Este': 250, 'Oeste': 50}

# Método 3: Dict comprehension para filtrar solo producto A
productos_a = {venta["region"]: venta["ventas"] for venta in ventas_por_region if venta["producto"] == "A"}
print(productos_a)
# {'Norte': 100, 'Sur': 300, 'Este': 250}