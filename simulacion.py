class Simulacion:
    def __init__(self, casetas, observaciones):
        self.casetas = casetas
        self.observaciones = observaciones

    def iniciar(self):
        for observacion in self.observaciones:
            print(f"Simulando para la caseta {observacion.caseta.nombre_caseta} en {observacion.fecha}")
            for intervalo in observacion.intervalos_fila:
                print(f"A las {intervalo.hora_observacion} hay {intervalo.personas_en_fila} personas en fila.")
