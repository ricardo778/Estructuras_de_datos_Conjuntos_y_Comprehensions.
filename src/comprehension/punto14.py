# Tengo dos listas: una con claves y otra con valores
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]

# Método 1: Creo diccionario usando índices
persona = {claves[i]: valores[i] for i in range(len(claves))}
print(persona)  # {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}

# Método 2: Uso zip para combinar las listas (más eficiente)
persona = {clave: valor for clave, valor in zip(claves, valores)}
print(persona)  # {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}