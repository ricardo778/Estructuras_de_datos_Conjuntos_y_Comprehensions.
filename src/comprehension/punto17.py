# Usando la misma lista de estudiantes del punto anterior
estudiantes = [
    {"id": 1, "nombre": "Ana", "nota": 8.5},
    {"id": 2, "nombre": "Carlos", "nota": 7.2},
    {"id": 3, "nombre": "Elena", "nota": 9.3}
]

# Creo un diccionario con nombres en mayúsculas y notas redondeadas
nombre_nota_formateado = {
    estudiante["nombre"].upper(): round(estudiante["nota"])
    for estudiante in estudiantes
}

# Muestro el diccionario formateado
print(nombre_nota_formateado)  # {'ANA': 8, 'CARLOS': 7, 'ELENA': 9}