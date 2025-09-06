# Estudiantes que toman matemáticas
estudiantes_matematicas = {"Ana", "Carlos", "Elena", "David"}
# Estudiantes que toman física
estudiantes_fisica = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Busco los estudiantes que están en ambas clases
estudiantes_ambas = estudiantes_matematicas & estudiantes_fisica

# Muestro los estudiantes que toman las dos materias
print(estudiantes_ambas)  # {'Carlos', 'Elena'}