from algoritmo_a_estrella import a_star

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
        inicio = (4, 1)  # Define una posición de inicio accesible
        objetivo = caseta.posicion_cuadricula

        # Calcular la ruta usando A*
        ruta = a_star(croquis_cuadricula, inicio, objetivo)
        
        if ruta is None:
            print(f"No se encontró una ruta desde {inicio} hasta {objetivo}.")
            return
        
        print(f"Ruta encontrada desde {inicio} hasta {objetivo}: {ruta}")

        # Registrar cada punto de la ruta en densidad_mapa
        for punto in ruta:
            x, y = punto[1] / len(croquis_cuadricula[0]), punto[0] / len(croquis_cuadricula)
            self.ruta.append((x, y))
            
            if (x, y) in densidad_mapa:
                densidad_mapa[(x, y)] += 1
            else:
                densidad_mapa[(x, y)] = 1
            print(f"Registrando punto en densidad_mapa: ({x}, {y})")
