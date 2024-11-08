class Observacion:
    def __init__(self, id_observacion, fecha, hora_inicio, hora_fin, total_clientes, promedio_tiempo, caseta):
        self.id_observacion = id_observacion
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.total_clientes = total_clientes
        self.promedio_tiempo = promedio_tiempo
        self.caseta = caseta  # Asociación con la clase Caseta
        self.intervalos_fila = []

    def agregar_intervalo(self, intervalo):
        self.intervalos_fila.append(intervalo)
