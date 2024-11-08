class Cliente:
    def __init__(self, id_cliente, hora_visita, tiempo_atencion, caseta):
        self.id_cliente = id_cliente
        self.hora_visita = hora_visita
        self.tiempo_atencion = tiempo_atencion
        self.caseta = caseta  # Asociación con la clase Caseta
    