# Tengo un texto en español
texto = "python es un lenguaje de programación versátil"

# Extraigo solo las vocales del texto y creo un conjunto
vocales = {letra for letra in texto.lower() if letra in "aeiou"}

# Muestro las vocales únicas que aparecen en el texto
print(vocales)  # {'a', 'e', 'i', 'o', 'u'}