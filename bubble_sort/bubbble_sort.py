class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def __repr__(self):
        return f"({self.nombre}, {self.edad}, {self.promedio})"

estudiantes = [
    Estudiante("Juan", 20, 85),
    Estudiante("Ana", 19, 90),
    Estudiante("Carlos", 22, 85),
    Estudiante("Lucía", 21, 95),
    Estudiante("Pedro", 20, 90)
]   

def bubble_sort_estudiantes(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n-i-1):
            # Comparamos primero por promedio
            if estudiantes[j].promedio > estudiantes[j+1].promedio:
                estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]
            # Si tienen el mismo promedio, ordenamos por edad
            elif estudiantes[j].promedio == estudiantes[j+1].promedio:
                if estudiantes[j].edad > estudiantes[j+1].edad:
                    estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]

bubble_sort_estudiantes(estudiantes)
print(estudiantes)
