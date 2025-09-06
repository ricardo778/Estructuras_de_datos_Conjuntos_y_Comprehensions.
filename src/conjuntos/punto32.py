# Todos los cursos que tengo disponibles
todos_cursos = {"Python", "Java", "SQL", "JavaScript", "C++"}

# Cursos que ya terminé de estudiar
cursos_completados = {"Python", "SQL"}

# Quito los cursos que ya completé de mi lista total
todos_cursos.difference_update(cursos_completados)

# Muestro los cursos que me faltan por hacer
print(todos_cursos)  # {'Java', 'JavaScript', 'C++'}