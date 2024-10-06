class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def __repr__(self):
        return f"({self.nombre}, {self.edad}, {self.promedio})"
