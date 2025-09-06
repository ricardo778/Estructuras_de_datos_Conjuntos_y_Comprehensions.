# Tengo un grupo de vegetales y otro de frutas
vegetales = {"zanahoria", "pepino", "lechuga"}
frutas = {"manzana", "plátano", "naranja"}

# Pregunto si estos dos grupos no tienen nada en común
print(vegetales.isdisjoint(frutas))  # True - No comparten ningún elemento

# Tengo números pares y números primos
numeros_pares = {2, 4, 6, 8}
numeros_primos = {2, 3, 5, 7}

# Pregunto si no tienen elementos iguales
print(numeros_pares.isdisjoint(numeros_primos))  # False - Comparten el número 2