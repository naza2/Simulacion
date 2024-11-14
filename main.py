import csv
import random
from caseta import Caseta
from estudiante import Estudiante
from conectar_bdd import ConectarBDD

class Main:
    def __init__(self, dbname, user, password, host):
        # Conexión a la base de datos
        self.conexion_db = ConectarBDD(dbname, user, password, host).conectar()
        self.casetas = self.obtener_casetas_bdd()  # Cargar casetas desde la base de datos

    def obtener_casetas_bdd(self):
        """
        Obtiene las casetas y sus características de la base de datos.
        """
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            SELECT nombre_caseta, ubicacion, tiempo_promedio_atencion, flujo_clientes
            FROM casetas
        """)
        resultados = cursor.fetchall()
        
        casetas = []
        for row in resultados:
            caseta = Caseta(
                nombre=row[0],
                ubicacion=row[1],
                tiempo_promedio_atencion=row[2],
                flujo_clientes=row[3]
            )
            casetas.append(caseta)
        
        cursor.close()
        return casetas

    def obtener_estudiantes_bdd(self):
        """
        Obtiene los estudiantes y sus preferencias de la base de datos.
        """
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            SELECT horario_preferido, horas_libres, caseta_preferida, factor_influencia,
                   tiempo_espera_dispuesto, presupuesto
            FROM encuestas_estudiantes
        """)
        resultados = cursor.fetchall()
        
        estudiantes = []
        for row in resultados:
            estudiante = Estudiante(
                horario_preferido=row[0],
                horas_libres=row[1],
                caseta_preferida=row[2],
                factor_influencia=row[3],
                tiempo_espera_dispuesto=row[4],
                presupuesto=row[5]
            )
            estudiantes.append(estudiante)
        
        cursor.close()
        return estudiantes

    def elegir_caseta_por_preferencia(self, estudiante):
        """
        Elige una caseta para el estudiante según sus preferencias.
        """
        preferencia = estudiante.factor_influencia
        if preferencia == "Calidad de los alimentos":
            seleccion = min(self.casetas, key=lambda c: c.tiempo_promedio_atencion)
        elif preferencia == "Rapidez en la entrega de tu pedido":
            seleccion = min(self.casetas, key=lambda c: c.tiempo_promedio_atencion)
        elif preferencia == "Variedad de opciones":
            seleccion = max(self.casetas, key=lambda c: c.flujo_clientes)
        else:
            seleccion = random.choice(self.casetas)

        return seleccion.nombre

    def guardar_estudiantes_en_csv(self, estudiantes):
        """
        Guarda los datos de los estudiantes y sus casetas elegidas en un archivo CSV.
        """
        with open("estudiantes.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Horario Preferido", "Horas Libres", "Caseta Preferida", "Factor Influencia",
                             "Tiempo Espera Dispuesto", "Presupuesto", "Caseta Elegida"])

            for estudiante in estudiantes:
                caseta_elegida = self.elegir_caseta_por_preferencia(estudiante)
                writer.writerow([
                    estudiante.horario_preferido,
                    estudiante.horas_libres,
                    estudiante.caseta_preferida,
                    estudiante.factor_influencia,
                    estudiante.tiempo_espera_dispuesto,
                    estudiante.presupuesto,
                    caseta_elegida
                ])
        print("Datos de estudiantes guardados en estudiantes.csv")

    def iniciar_generacion_estudiantes(self):
        # Obtener estudiantes desde la base de datos
        estudiantes = self.obtener_estudiantes_bdd()
        print(f"Generando {len(estudiantes)} estudiantes y sus preferencias desde la base de datos...")

        # Guardar resultados en CSV
        self.guardar_estudiantes_en_csv(estudiantes)

# Ejecución principal
if __name__ == "__main__":
    main = Main(dbname="Simulacion", user="diego", password="facilita", host="localhost")
    main.iniciar_generacion_estudiantes()
