class Caseta:
    def __init__(self, nombre, ubicacion, tiempo_promedio_atencion, flujo_clientes):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tiempo_promedio_atencion = tiempo_promedio_atencion  # en minutos
        self.flujo_clientes = flujo_clientes  # Número de clientes por hora
