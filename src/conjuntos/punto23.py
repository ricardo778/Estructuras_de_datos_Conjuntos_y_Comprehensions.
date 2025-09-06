# Conjunto de frutas.
frutas = {"manzana", "naranja", "plátano", "fresa", "kiwi"}

# Conjunto de frutas tropicales.
frutas_tropicales = {"plátano", "kiwi"}

# Verifica si 'frutas' es un superconjunto de 'frutas_tropicales'.
print(frutas.issuperset(frutas_tropicales))

# También se puede usar el operador '>='.
print(frutas >= frutas_tropicales)
