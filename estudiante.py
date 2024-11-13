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

    def mover_a_caseta(self, caseta, densidad_mapa, croquis_cuadricula):
        # Genera una posición de inicio completamente aleatoria en celdas con valor 1
        posibles_inicios = [(i, j) for i in range(len(croquis_cuadricula)) 
                            for j in range(len(croquis_cuadricula[0])) if croquis_cuadricula[i][j] == 1]
        inicio = random.choice(posibles_inicios)
        
        objetivo = caseta.posicion_cuadricula

        # Calcular la ruta usando A* con posibilidad de desviación
        ruta = a_star_con_desviacion(croquis_cuadricula, inicio, objetivo)
        
        if ruta is None:
            print(f"No se encontró una ruta desde {inicio} hasta {objetivo}.")
            return
        
        print(f"Ruta encontrada desde {inicio} hasta {objetivo}: {ruta}")

        # Registrar cada punto de la ruta en densidad_mapa
        for punto in ruta:
            x, y = punto[1] / len(croquis_cuadricula[0]), punto[0] / len(croquis_cuadricula)
            self.ruta.append((x, y))
            
            # Actualizar densidad de cada punto en el mapa de calor
            if (x, y) in densidad_mapa:
                densidad_mapa[(x, y)] += 1
            else:
                densidad_mapa[(x, y)] = 1
            print(f"Registrando punto en densidad_mapa: ({x}, {y})")

def a_star_con_desviacion(cuadricula, inicio, objetivo, desviacion_prob=0.3):
    """
    Algoritmo A* modificado para permitir desviaciones aleatorias.
    """
    import heapq
    filas, columnas = len(cuadricula), len(cuadricula[0])
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    costo_actual = {inicio: 0}
    padres = {inicio: None}

    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)

        if actual == objetivo:
            ruta = []
            while actual is not None:
                ruta.append(actual)
                actual = padres[actual]
            return ruta[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos posibles
            vecino = (actual[0] + dx, actual[1] + dy)
            if (0 <= vecino[0] < filas and 0 <= vecino[1] < columnas and cuadricula[vecino[0]][vecino[1]] == 1):
                # Probabilidad de desviación aleatoria
                if random.random() < desviacion_prob:
                    nuevo_costo = costo_actual[actual] + random.randint(1, 3)  # Coste aleatorio para la desviación
                else:
                    nuevo_costo = costo_actual[actual] + 1

                if vecino not in costo_actual or nuevo_costo < costo_actual[vecino]:
                    costo_actual[vecino] = nuevo_costo
                    prioridad = nuevo_costo + abs(objetivo[0] - vecino[0]) + abs(objetivo[1] - vecino[1])
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    padres[vecino] = actual

    return None  # Retorna None si no hay ruta al objetivo
