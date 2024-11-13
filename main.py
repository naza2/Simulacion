from conectar_bdd import conectar_bdd
from datos import cargar_casetas, cargar_encuestas
from simulacion import Estudiante
from visualizar import generar_mapa_calor_solo_densidad
from caseta import Caseta
import random
def main():
    conexion = conectar_bdd()
    if conexion:
        casetas_data = cargar_casetas(conexion)
        encuestas_data = cargar_encuestas(conexion)

        # Define la cuadrícula de caminos y ubicaciones de las casetas en la cuadrícula
        croquis_cuadricula = [
           [1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 0],
           [0, 1, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 0, 0, 0, 1, 0],
           [0, 1, 1, 1, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 0, 0, 0]
        ]
        ubicaciones_casetas = {
            "Caseta Blanca": (4, 0),
            "CafeITO": (4, 7),
            "Casetas Chedraui": (0, 5),
            "Caseta de Vigilancia": (7, 5)
        }

        # Crear casetas y estudiantes
        casetas = [Caseta(nombre=caseta[1], posicion_cuadricula=ubicaciones_casetas.get(caseta[1])) for caseta in casetas_data]
        estudiantes = [Estudiante(*encuesta[2:8]) for encuesta in encuestas_data]

        densidad_mapa = {}
        for estudiante in estudiantes:
            caseta_elegida = next((c for c in casetas if c.nombre == estudiante.caseta_preferida), random.choice(casetas))
            estudiante.mover_a_caseta(caseta_elegida, densidad_mapa, croquis_cuadricula)

        # Generar el mapa de calor sin fondo
        generar_mapa_calor_solo_densidad(densidad_mapa)

        conexion.close()

if __name__ == "__main__":
    main()
