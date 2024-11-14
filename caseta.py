class Caseta:
    def __init__(self, nombre, ubicacion, tiempo_promedio_atencion, flujo_clientes, variedad_productos, calidad_comida, precios):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tiempo_promedio_atencion = tiempo_promedio_atencion  # en minutos
        self.flujo_clientes = flujo_clientes  # Número de clientes por hora
        self.variedad_productos = variedad_productos  # Variedad de productos (1-5)
        self.calidad_comida = calidad_comida  # Calidad de la comida (1-5)
        self.precios = precios  # Precios (1-5)
