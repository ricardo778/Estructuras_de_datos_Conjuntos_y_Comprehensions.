# Frutas que se cultivan en nuestra región
frutas_locales = {"manzana", "pera", "naranja"}

# Frutas que vienen de otros países
frutas_importadas = {"piña", "mango", "kiwi"}

# Agrego todas las frutas importadas a la lista de locales
frutas_locales.update(frutas_importadas)

# Muestro la colección completa de frutas disponibles
print(frutas_locales)  # {'manzana', 'pera', 'naranja', 'piña', 'mango', 'kiwi'}