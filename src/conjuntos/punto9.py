# Creamos un conjunto llamado 'numeros'.
# Los conjuntos eliminan automáticamente los elementos duplicados.
# Por lo tanto, el '1' aparecerá solo una vez.
numeros = {3, 1, 4, 1, 5, 9}
print(numeros)

# Declarar llaves vacías {} crea un diccionario, NO un conjunto.
no_es_conjunto = {}
print(f"Tipo de 'no_es_conjunto': {type(no_es_conjunto)}")

# Para crear un conjunto vacío, siempre debes usar la función set().
conjunto_vacio = set()
print(f"Tipo de 'conjunto_vacio': {type(conjunto_vacio)}")