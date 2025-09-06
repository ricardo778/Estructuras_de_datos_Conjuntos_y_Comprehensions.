# Creamos dos conjuntos, uno para el "grupo_a" y otro para el "grupo_b".
grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Elena", "Fernando", "Gabriela", "Carlos"}

# Usamos el signo de menos (-) para encontrar a las personas que están en el grupo A pero no en el grupo B.
# El resultado se guarda en una variable llamada 'solo_en_a'.
solo_en_a = grupo_a - grupo_b

# Imprimimos el resultado.
print(solo_en_a)  # Esto mostrará: {'Ana', 'David'}
