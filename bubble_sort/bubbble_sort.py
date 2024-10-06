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