class Caseta:
    def __init__(self, nombre, ubicacion=None, posicion_cuadricula=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.posicion_cuadricula = posicion_cuadricula
        self.estudiantes_atendidos = []

    def atender_estudiante(self, estudiante):
        self.estudiantes_atendidos.append(estudiante)

    def __str__(self):
        return f"Caseta {self.nombre} - Estudiantes atendidos: {len(self.estudiantes_atendidos)}"
