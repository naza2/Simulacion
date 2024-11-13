import matplotlib.pyplot as plt
import numpy as np

def generar_mapa_calor_solo_densidad(densidad_mapa):
    if not densidad_mapa:
        print("No se encontraron datos en densidad_mapa.")
        return
    x = [punto[0] for punto in densidad_mapa.keys()]
    y = [punto[1] for punto in densidad_mapa.keys()]
    z = [densidad_mapa[punto] for punto in densidad_mapa.keys()]
    print("Puntos registrados en densidad_mapa:", len(z))
    print("Valores de densidad:", z[:10])  # Muestra los primeros 10 valores para verificar

    # Crear el mapa de calor con una cuadrícula de densidad y mayor resolución
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=150, weights=z, range=[[0, 1], [0, 1]])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    # Mostrar el mapa de calor sin fondo y asignarlo a una variable
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot', interpolation='nearest')

    # Agregar barra de color
    plt.colorbar(label="Frecuencia de Visita")

    # Etiquetas y título
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title("Mapa de Calor de la Distribución de Estudiantes (Sin Croquis)")
    plt.show()