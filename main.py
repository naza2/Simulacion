from conectar_bdd import conectar_bdd
from datos import cargar_casetas, cargar_encuestas
from modelo import entrenar_modelo
from visualizar import visualizar_distribucion

from caseta import Caseta
from estudiante import Estudiante

def main():
    conexion = conectar_bdd()
    if conexion:
        # Cargar datos desde la base de datos
        casetas_data = cargar_casetas(conexion)
        encuestas_data = cargar_encuestas(conexion)

        # Crear instancias de Caseta y Estudiante
        casetas = [Caseta(nombre=caseta[1], ubicacion=(0, 0)) for caseta in casetas_data]  # Ubicación es temporal
        estudiantes = [Estudiante(
    horario_preferido=encuesta[2],
    horas_libres=encuesta[3],
    caseta_preferida=encuesta[4],
    factor_influencia=encuesta[5],
    tiempo_espera_dispuesto=encuesta[6],
    presupuesto=encuesta[7]
) for encuesta in encuestas_data]


        # Entrenar el modelo
        entrenar_modelo(estudiantes, casetas)

        # Visualizar la distribución
        visualizar_distribucion(casetas)

        conexion.close()

if __name__ == "__main__":
    main()
