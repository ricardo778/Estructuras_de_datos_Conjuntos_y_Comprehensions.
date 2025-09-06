# Ingredientes que tengo en total
ingredientes_disponibles = {"harina", "huevos", "azúcar", "leche", "mantequilla"}
# Ingredientes que ya usé
ingredientes_usados = {"harina", "huevos", "azúcar"}

# Veo qué ingredientes me quedan sin usar
ingredientes_restantes = ingredientes_disponibles - ingredientes_usados

# Muestro los ingredientes que todavía tengo disponibles
print(ingredientes_restantes)  # {'leche', 'mantequilla'}