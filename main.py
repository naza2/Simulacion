import csv
import random

from caseta import Caseta
from estudiante import Estudiante
from conectar_bdd import ConectarBDD
from mapadeCalor import simular_distribucion
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class Main:
    def __init__(self, dbname, user, password, host):
        self.conexion_db = ConectarBDD(dbname, user, password, host).conectar()
        self.casetas = self.obtener_casetas_bdd()

    def limitar_valor(self, valor):
        return max(1, min(5, valor))

    def obtener_casetas_bdd(self):
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            SELECT nombre_caseta, ubicacion, tiempo_promedio_atencion, flujo_clientes,
                   variedad_productos, calidad_comida, precios
            FROM casetas
        """)
        resultados = cursor.fetchall()
        
        casetas = []
        caseta_nombres = set()
        for row in resultados:
            nombre = row[0].strip()
            caseta_nombres.add(nombre)
            caseta = Caseta(
                nombre=nombre,
                ubicacion=row[1].strip(),
                tiempo_promedio_atencion=self.limitar_valor(int(row[2])),
                flujo_clientes=self.limitar_valor(int(row[3])),
                variedad_productos=self.limitar_valor(int(row[4])),
                calidad_comida=self.limitar_valor(int(row[5])),
                precios=self.limitar_valor(int(row[6]))
            )
            casetas.append(caseta)
        
        cursor.close()
        self.caseta_nombres = caseta_nombres
        print("Casetas disponibles:", self.caseta_nombres)
        return casetas

    def obtener_opciones_estudiantes(self):
        cursor = self.conexion_db.cursor()

        cursor.execute("SELECT horario_preferido, COUNT(*) FROM encuestas_estudiantes GROUP BY horario_preferido")
        horarios = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de horario_preferido:", horarios)  # Verificar

        cursor.execute("SELECT horas_libres, COUNT(*) FROM encuestas_estudiantes GROUP BY horas_libres")
        horas_libres = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de horas_libres:", horas_libres)  # Verificar

        cursor.execute("SELECT caseta_preferida, COUNT(*) FROM encuestas_estudiantes GROUP BY caseta_preferida")
        casetas_preferidas = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de caseta_preferida:", casetas_preferidas)  # Para verificar las frecuencias

        cursor.execute("SELECT factor_influencia, COUNT(*) FROM encuestas_estudiantes GROUP BY factor_influencia")
        factores_influencia = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de factor_influencia:", factores_influencia)  # Verificar

        cursor.execute("SELECT tiempo_espera_dispuesto, COUNT(*) FROM encuestas_estudiantes GROUP BY tiempo_espera_dispuesto")
        tiempos_espera_dispuesto = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de tiempo_espera_dispuesto:", tiempos_espera_dispuesto)  # Verificar

        cursor.execute("SELECT presupuesto, COUNT(*) FROM encuestas_estudiantes GROUP BY presupuesto")
        presupuestos = [(row[0].strip(), row[1]) for row in cursor.fetchall()]
        print("Frecuencias de presupuesto:", presupuestos)  # Verificar

        cursor.close()

        return horarios, horas_libres, casetas_preferidas, factores_influencia, tiempos_espera_dispuesto, presupuestos

    def seleccionar_opcion_con_probabilidades(self, opciones):
        total = sum(freq for opcion, freq in opciones)
        rand_val = random.uniform(0, total)
        acumulado = 0
        for opcion, freq in opciones:
            acumulado += freq
            if rand_val <= acumulado:
                return opcion
        return opciones[-1][0]  # En caso de algún error numérico

    def generar_estudiantes(self, cantidad):
        horarios, horas_libres, casetas_preferidas, factores_influencia, tiempos_espera_dispuesto, presupuestos = self.obtener_opciones_estudiantes()
        contador_casetas_preferidas = {opcion: 0 for opcion, _ in casetas_preferidas}

        estudiantes = []
        for _ in range(cantidad):
            caseta_pref = self.seleccionar_opcion_con_probabilidades(casetas_preferidas)
            contador_casetas_preferidas[caseta_pref] += 1  # Incrementar contador

            if caseta_pref not in self.caseta_nombres:
                print(f"Advertencia: Caseta preferida '{caseta_pref}' no encontrada en la lista de casetas disponibles.")
                # Asignar una caseta al azar si la preferida no está disponible
                caseta_pref = random.choice(list(self.caseta_nombres))
            
            estudiante = Estudiante(
                horario_preferido=self.seleccionar_opcion_con_probabilidades(horarios),
                horas_libres=self.seleccionar_opcion_con_probabilidades(horas_libres),
                caseta_preferida=caseta_pref,
                factor_influencia=self.seleccionar_opcion_con_probabilidades(factores_influencia),
                tiempo_espera_dispuesto=self.seleccionar_opcion_con_probabilidades(tiempos_espera_dispuesto),
                presupuesto=self.seleccionar_opcion_con_probabilidades(presupuestos)
            )
            estudiantes.append(estudiante)
        
        print("Contador de casetas preferidas:", contador_casetas_preferidas)  # Para verificar la distribución
        return estudiantes

    def asignar_caseta_elegida(self, estudiantes):
        caseta_elegida = []
        for idx, estudiante in enumerate(estudiantes, start=1):
            puntajes = {}
            for caseta in self.casetas:
                puntaje = 0

                if estudiante.presupuesto == "Menos de $30":
                    puntaje += (6 - caseta.precios)  # Preferir precios bajos
                elif estudiante.presupuesto == "$30 - $50":
                    puntaje += caseta.precios
                elif estudiante.presupuesto == "$50 - $70":
                    puntaje += caseta.precios
                elif estudiante.presupuesto == "Más de $70":
                    puntaje += caseta.precios

                # Factor de Influencia: Dependiendo del factor, agregar puntuaciones
                if estudiante.factor_influencia == "Calidad de los alimentos":
                    puntaje += caseta.calidad_comida
                elif estudiante.factor_influencia == "Precios":
                    puntaje += (6 - caseta.precios)
                elif estudiante.factor_influencia == "Atención al cliente":
                    puntaje += caseta.flujo_clientes
                elif estudiante.factor_influencia == "Variedad de opciones":
                    puntaje += caseta.variedad_productos
                elif estudiante.factor_influencia == "Espacio para comer ahi mismo":
                    puntaje += caseta.flujo_clientes
                elif estudiante.factor_influencia == "Rapidez en la entrega de tu pedido":
                    puntaje += (6 - caseta.tiempo_promedio_atencion)
                else:
                    puntaje += 1  # Puntuación mínima si no hay factor reconocido

                # Tiempo Espera Dispuesto: Preferir casetas con tiempos de atención menores
                if estudiante.tiempo_espera_dispuesto == "Menos de 5 minutos":
                    puntaje += (6 - caseta.tiempo_promedio_atencion)
                elif estudiante.tiempo_espera_dispuesto == "5-10 minutos":
                    puntaje += (6 - caseta.tiempo_promedio_atencion)
                elif estudiante.tiempo_espera_dispuesto == "10-15 minutos":
                    puntaje += caseta.tiempo_promedio_atencion
                elif estudiante.tiempo_espera_dispuesto == "15-20 minutos":
                    puntaje += caseta.tiempo_promedio_atencion
                elif estudiante.tiempo_espera_dispuesto == "Más de 20 minutos":
                    puntaje += caseta.tiempo_promedio_atencion

                if caseta.nombre == "Lado Chedraui":
                    puntaje -= 1.1
                puntaje = max(0, puntaje)

                puntajes[caseta.nombre] = puntaje
            casetas_con_puntaje = {caseta: puntaje for caseta, puntaje in puntajes.items() if puntaje > 0}
            if not casetas_con_puntaje:
                caseta_asignada = random.choice([caseta.nombre for caseta in self.casetas if caseta.nombre != "Lado Chedraui"])
            else:

                caseta_asignada = random.choices(
                    population=list(casetas_con_puntaje.keys()),
                    weights=list(casetas_con_puntaje.values()),
                    k=1
                )[0]
            caseta_elegida.append(caseta_asignada)

        return caseta_elegida

    def guardar_estudiantes_en_csv(self, estudiantes):
        with open("estudiantes.csv", mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Horario Preferido", "Horas Libres", "Caseta Preferida",
                "Factor Influencia", "Tiempo Espera Dispuesto", "Presupuesto"
            ])

            for estudiante in estudiantes:
                writer.writerow([
                    estudiante.horario_preferido,
                    estudiante.horas_libres,
                    estudiante.caseta_preferida,
                    estudiante.factor_influencia,
                    estudiante.tiempo_espera_dispuesto,
                    estudiante.presupuesto
                ])
        print("Datos de estudiantes guardados en estudiantes.csv")

    def guardar_caseta_elegida_en_csv(self, caseta_elegida):
        with open("caseta_elegida.csv", mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Caseta Elegida"])

            for caseta in caseta_elegida:
                writer.writerow([caseta])
        print("Datos de Caseta Elegida guardados en caseta_elegida.csv")

    def iniciar_generacion_estudiantes(self, cantidad):
        # Generar estudiantes en base a la información de la base de datos y las distribuciones reales
        estudiantes = self.generar_estudiantes(cantidad)
        print(f"Generando {len(estudiantes)} estudiantes en base a la información de la BDD...")

        # Guardar datos de estudiantes en CSV
        self.guardar_estudiantes_en_csv(estudiantes)

        # Asignar Caseta Elegida
        caseta_elegida = self.asignar_caseta_elegida(estudiantes)
        self.guardar_caseta_elegida_en_csv(caseta_elegida)
        simular_distribucion()

if __name__ == "__main__":
    try:
        cantidad = int(input("Ingrese la cantidad de estudiantes que desea generar: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
    except ValueError as ve:
        print("Entrada inválida:", ve)
        exit(1)
    
    main = Main(dbname="Simulacion", user="diego", password="facilita", host="localhost")
    main.iniciar_generacion_estudiantes(cantidad)

