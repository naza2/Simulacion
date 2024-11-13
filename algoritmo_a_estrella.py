import heapq

def a_star(cuadricula, inicio, objetivo):
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
            return ruta[::-1]  # Devuelve la ruta en orden desde inicio hasta objetivo

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos posibles
            vecino = (actual[0] + dx, actual[1] + dy)
            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas and cuadricula[vecino[0]][vecino[1]] == 1:
                nuevo_costo = costo_actual[actual] + 1
                if vecino not in costo_actual or nuevo_costo < costo_actual[vecino]:
                    costo_actual[vecino] = nuevo_costo
                    prioridad = nuevo_costo + abs(objetivo[0] - vecino[0]) + abs(objetivo[1] - vecino[1])
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    padres[vecino] = actual

    return None  # Retorna None si no hay ruta al objetivo
