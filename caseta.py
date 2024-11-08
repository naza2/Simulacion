class caseta:
    def __init__(self, id_caseta, nombre_caseta, ubicacion):
        self.id_caseta = id_caseta
        self.nombre_caseta = nombre_caseta
        self.ubicacion = ubicacion
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
