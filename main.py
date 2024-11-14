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

    def limitar_valor(self, valor):
        """
        Limita el valor entre 1 y 5.
        """
        return max(1, min(5, valor))

    def obtener_casetas_bdd(self):
        """
        Obtiene las casetas y sus características de la base de datos y asegura que los valores están entre 1 y 5.
        """
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            SELECT nombre_caseta, ubicacion, tiempo_promedio_atencion, flujo_clientes,
                   variedad_productos, calidad_comida, precios
            FROM casetas
        """)
        resultados = cursor.fetchall()
        
        casetas = []
        for row in resultados:
            caseta = Caseta(
                nombre=row[0],
                ubicacion=row[1],
                tiempo_promedio_atencion=self.limitar_valor(row[2]),
                flujo_clientes=self.limitar_valor(row[3]),
                variedad_productos=self.limitar_valor(row[4]),
                calidad_comida=self.limitar_valor(row[5]),
                precios=self.limitar_valor(row[6])
            )
            casetas.append(caseta)
        
        cursor.close()
        return casetas

    def obtener_opciones_estudiantes(self):
        """
        Obtiene las opciones posibles para cada característica de los estudiantes desde la base de datos.
        """
        cursor = self.conexion_db.cursor()

        # Obtener opciones para cada característica
        cursor.execute("SELECT DISTINCT horario_preferido FROM encuestas_estudiantes")
        horarios = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT horas_libres FROM encuestas_estudiantes")
        horas_libres = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT caseta_preferida FROM encuestas_estudiantes")
        casetas_preferidas = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT factor_influencia FROM encuestas_estudiantes")
        factores_influencia = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT tiempo_espera_dispuesto FROM encuestas_estudiantes")
        tiempos_espera_dispuesto = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT presupuesto FROM encuestas_estudiantes")
        presupuestos = [row[0] for row in cursor.fetchall()]

        cursor.close()

        return horarios, horas_libres, casetas_preferidas, factores_influencia, tiempos_espera_dispuesto, presupuestos

    def generar_estudiantes(self, cantidad):
        """
        Genera estudiantes en base a las opciones de la base de datos y añade aleatorios si es necesario.
        """
        # Obtener todas las opciones de la base de datos
        horarios, horas_libres, casetas_preferidas, factores_influencia, tiempos_espera_dispuesto, presupuestos = self.obtener_opciones_estudiantes()

        estudiantes = []
        for _ in range(cantidad):
            estudiante = Estudiante(
                horario_preferido=random.choice(horarios),
                horas_libres=random.choice(horas_libres),
                caseta_preferida=random.choice(casetas_preferidas),
                factor_influencia=random.choice(factores_influencia),
                tiempo_espera_dispuesto=random.choice(tiempos_espera_dispuesto),
                presupuesto=random.choice(presupuestos)
            )
            estudiantes.append(estudiante)
        
        return estudiantes

    def elegir_caseta_por_preferencia(self, estudiante):
        """
        Elige una caseta para el estudiante según sus preferencias extendidas.
        """
        preferencia = estudiante.factor_influencia
        if preferencia == "Calidad de los alimentos":
            seleccion = max(self.casetas, key=lambda c: c.calidad_comida)
        elif preferencia == "Rapidez en la entrega de tu pedido":
            seleccion = min(self.casetas, key=lambda c: c.tiempo_promedio_atencion)
        elif preferencia == "Variedad de opciones":
            seleccion = max(self.casetas, key=lambda c: c.variedad_productos)
        elif preferencia == "Precios":
            seleccion = min(self.casetas, key=lambda c: c.precios)
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

    def iniciar_generacion_estudiantes(self, cantidad):
        # Generar estudiantes en base a la información de la base de datos y de forma aleatoria si es necesario
        estudiantes = self.generar_estudiantes(cantidad)
        print(f"Generando {len(estudiantes)} estudiantes en base a la información de la BDD...")

        # Guardar resultados en CSV
        self.guardar_estudiantes_en_csv(estudiantes)

# Ejecución principal
if __name__ == "__main__":
    # Solicitar la cantidad de estudiantes al usuario
    cantidad = int(input("Ingrese la cantidad de estudiantes que desea generar: "))
    main = Main(dbname="Simulacion", user="diego", password="facilita", host="localhost")
    main.iniciar_generacion_estudiantes(cantidad)
