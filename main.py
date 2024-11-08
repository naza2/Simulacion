from caseta import Caseta

from IntervaloFila import IntervaloFila
from observacion import Observacion
from simulacion import Simulacion
# Crear casetas
Caseta1 = Caseta(1, "Caseta Blanca", "Lado A")
Caseta2 = Caseta(2, "CafeITO", "Lado B")

# Crear observación para la caseta blanca
observacion_blanca = Observacion(1, "2023-10-25", "11:20", "12:20", 40, 2.31, Caseta2)

# Agregar intervalos de fila
observacion_blanca.agregar_intervalo(IntervaloFila("11:25", 3))
observacion_blanca.agregar_intervalo(IntervaloFila("11:30", 1))
# (Continúa agregando intervalos según sea necesario)

# Crear simulación
simulacion = Simulacion([Caseta1, Caseta2], [observacion_blanca])

# Iniciar simulación
simulacion.iniciar()
