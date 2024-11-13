import random

class Estudiante:
    def __init__(self, horario_preferido, horas_libres, caseta_preferida, factor_influencia, tiempo_espera_dispuesto, presupuesto):
        self.horario_preferido = horario_preferido
        self.horas_libres = horas_libres
        self.caseta_preferida = caseta_preferida
        self.factor_influencia = factor_influencia
        self.tiempo_espera_dispuesto = tiempo_espera_dispuesto
        self.presupuesto = presupuesto
        self.ruta = []

    def mover_a_caseta(self, caseta, densidad_mapa):
        # Simula la ruta hacia la caseta preferida
        x_inicial, y_inicial = random.uniform(0, 1), random.uniform(0, 1)  # Coordenadas de inicio
        x_final, y_final = caseta.ubicacion

        # Simulación de movimiento hacia la caseta, añadiendo puntos a la ruta
        pasos = 10  # Dividir el movimiento en 10 pasos
        for i in range(pasos + 1):
            x = x_inicial + (x_final - x_inicial) * i / pasos
            y = y_inicial + (y_final - y_inicial) * i / pasos
            self.ruta.append((x, y))

            # Incrementar la densidad en el mapa de calor en cada punto
            if (x, y) in densidad_mapa:
                densidad_mapa[(x, y)] += 1
            else:
                densidad_mapa[(x, y)] = 1
