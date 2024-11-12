import random

class Estudiante:
    def __init__(self, horario_preferido, horas_libres, caseta_preferida, factor_influencia, tiempo_espera_dispuesto, presupuesto):
        self.horario_preferido = horario_preferido
        self.horas_libres = horas_libres
        self.caseta_preferida = caseta_preferida
        self.factor_influencia = factor_influencia
        self.tiempo_espera_dispuesto = tiempo_espera_dispuesto
        self.presupuesto = presupuesto

    def elegir_caseta(self, casetas):
        # Selección de caseta basada en preferencias
        preferidas = [caseta for caseta in casetas if caseta.nombre == self.caseta_preferida]
        if preferidas:
            return random.choice(preferidas)
        return random.choice(casetas)
