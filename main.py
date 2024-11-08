# Crear casetas
caseta_blanca = Caseta(1, "Caseta Blanca", "Lado A")
caseta_caffeito = Caseta(2, "CafeITO", "Lado B")

# Crear observación para la caseta blanca
observacion_blanca = Observacion(1, "2023-10-25", "11:20", "12:20", 40, 2.31, caseta_blanca)

# Agregar intervalos de fila
observacion_blanca.agregar_intervalo(IntervaloFila("11:25", 3))
observacion_blanca.agregar_intervalo(IntervaloFila("11:30", 1))
# (Continúa agregando intervalos según sea necesario)

# Crear simulación
simulacion = Simulacion([caseta_blanca, caseta_caffeito], [observacion_blanca])

# Iniciar simulación
simulacion.iniciar()
