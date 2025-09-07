# Tengo una lista de estudiantes, cada uno con id, nombre y nota
estudiantes = [
    {"id": 1, "nombre": "Ana", "nota": 8.5},
    {"id": 2, "nombre": "Carlos", "nota": 7.2},
    {"id": 3, "nombre": "Elena", "nota": 9.3}
]

# Creo un diccionario que usa el id como clave y el nombre como valor
id_nombre = {estudiante["id"]: estudiante["nombre"] for estudiante in estudiantes}
print(id_nombre)  # {1: 'Ana', 2: 'Carlos', 3: 'Elena'}

# Creo otro diccionario que usa el nombre como clave y la nota como valor
nombre_nota = {estudiante["nombre"]: estudiante["nota"] for estudiante in estudiantes}
print(nombre_nota)  # {'Ana': 8.5, 'Carlos': 7.2, 'Elena': 9.3}