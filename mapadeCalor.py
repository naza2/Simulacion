# Definir mapeo de casetas preferidas para alinear con nombres en casetas_bdd
caseta_mapping = {
    "cafeITO": "CafeITO",
    "Blanca": "Caseta Blanca",
    "Chedraui": "Lado Chedraui"
}

for _ in range(cantidad):
    caseta_pref = self.seleccionar_opcion_con_probabilidades(casetas_preferidas)
    contador_casetas_preferidas[caseta_pref] += 1  # Incrementar contador

    # Mapear 'caseta_pref' a nombres exactos en 'casetas'
    caseta_pref_mapped = caseta_mapping.get(caseta_pref, None)
    if caseta_pref_mapped is None:
        print(f"Advertencia: Caseta preferida '{caseta_pref}' no reconocida en el mapeo.")
        # Asignar una caseta al azar si la preferida no está reconocida
        caseta_pref_final = random.choice(list(self.caseta_nombres))
    elif caseta_pref_mapped not in self.caseta_nombres:
        print(f"Advertencia: Caseta preferida mapeada '{caseta_pref_mapped}' no encontrada en la lista de casetas disponibles.")
        # Asignar una caseta al azar si la preferida mapeada no está disponible
        caseta_pref_final = random.choice(list(self.caseta_nombres))
    else:
        caseta_pref_final = caseta_pref_mapped

    estudiante = Estudiante(
        horario_preferido=self.seleccionar_opcion_con_probabilidades(horarios),
        horas_libres=self.seleccionar_opcion_con_probabilidades(horas_libres),
        caseta_preferida=caseta_pref_final,
        factor_influencia=self.seleccionar_opcion_con_probabilidades(factores_influencia),
        tiempo_espera_dispuesto=self.seleccionar_opcion_con_probabilidades(tiempos_espera_dispuesto),
        presupuesto=self.seleccionar_opcion_con_probabilidades(presupuestos)
    )
    estudiantes.append(estudiante)
