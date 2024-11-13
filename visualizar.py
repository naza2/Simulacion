import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def generar_mapa_calor(densidad_mapa):
    # Cargar el croquis como fondo
    img = mpimg.imread('/home/diego/Escritorio/Simulacion/Simulacion/img/Croquis.png')  # Ruta a la imagen del croquis

    # Crear figura y ejes
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 1, 0, 1])  # Ajustar la imagen al fondo

    # Crear una matriz de densidad para el mapa de calor
    x = [punto[0] for punto in densidad_mapa.keys()]
    y = [punto[1] for punto in densidad_mapa.keys()]
    z = [densidad_mapa[punto] for punto in densidad_mapa.keys()]

    # Crear el mapa de calor con una cuadrícula de densidad
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=50, weights=z, range=[[0, 1], [0, 1]])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    # Mostrar el mapa de calor sobre el croquis y asignarlo a una variable
    heatmap_img = ax.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot', alpha=0.6)

    # Agregar la barra de color usando el mapa de calor como referencia
    plt.colorbar(heatmap_img, label="Frecuencia de Visita")

    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title("Mapa de Calor de la Distribución de Estudiantes")
    plt.show()
