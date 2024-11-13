from conectar_bdd import conectar_bdd
from datos import cargar_casetas, cargar_encuestas
from simulacion import Estudiante
from visualizar import generar_mapa_calor
from caseta import Caseta
import random

def main():
    conexion = conectar_bdd()
    if conexion:
        casetas_data = cargar_casetas(conexion)
        encuestas_data = cargar_encuestas(conexion)

        # Asignar ubicaciones a cada caseta
        ubicaciones_casetas = {
            "Caseta Blanca": (0.2, 0.8),
            "CafeITO": (0.5, 0.5),
            "Casetas Chedraui": (0.8, 0.8),
            "Caseta de Vigilancia": (0.9, 0.9)
        }
        casetas = [Caseta(nombre=caseta[1], ubicacion=ubicaciones_casetas.get(caseta[1], (0, 0))) for caseta in casetas_data]

        # Crear estudiantes y simular el movimiento
        estudiantes = [Estudiante(
            horario_preferido=encuesta[2],
            horas_libres=encuesta[3],
            caseta_preferida=encuesta[4],
            factor_influencia=encuesta[5],
            tiempo_espera_dispuesto=encuesta[6],
            presupuesto=encuesta[7]
        ) for encuesta in encuestas_data]

        densidad_mapa = {}
        for estudiante in estudiantes:
            # Elegir la caseta preferida o una al azar
            caseta_elegida = next((c for c in casetas if c.nombre == estudiante.caseta_preferida), random.choice(casetas))
            estudiante.mover_a_caseta(caseta_elegida, densidad_mapa)

        # Generar el mapa de calor
        generar_mapa_calor(densidad_mapa)

        conexion.close()

if __name__ == "__main__":
    main()
