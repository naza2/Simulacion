from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
import random
import heapq
import re
from matplotlib.colors import LinearSegmentedColormap

colors = [
    (0.9, 0.9, 0.9),
    (1, 1, 0.8),
    (1, 1, 0.6),
    (1, 0.9, 0.4),
    (1, 0.8, 0.2),
    (1, 0.7, 0),
    (1, 0.5, 0),
    (1, 0.3, 0),
    (1, 0.1, 0),
    (1, 0, 0),
    (0.8, 0, 0),
    (0.6, 0, 0),
]
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)


def col_letter_to_index(col_letter):
    index = 0
    for i, char in enumerate(reversed(col_letter.upper())):
        index += (ord(char) - ord('A') + 1) * (26 ** i)
    return index - 1  # Índice basado en cero

def cell_address_to_indices(cell_address):
    match = re.match(r"([A-Z]+)(\d+)", cell_address)
    if match:
        col_letters = match.group(1)
        row_number = int(match.group(2))
        col_index = col_letter_to_index(col_letters)
        row_index = row_number - 1  # Índice basado en cero
        return row_index, col_index
    else:
        raise ValueError(f"Dirección de celda inválida: {cell_address}")

def parse_cell_range(cell_range):
    start_cell, end_cell = cell_range.split(':')
    start_row, start_col = cell_address_to_indices(start_cell)
    end_row, end_col = cell_address_to_indices(end_cell)
    
    rows = range(min(start_row, end_row), max(start_row, end_row) + 1)
    cols = range(min(start_col, end_col), max(start_col, end_col) + 1)
    
    coordinates = [(row, col) for row in rows for col in cols]
    return coordinates

class HeatmapGenerator:
    def __init__(self, data, cmap='Oranges'):
        self.data = np.array(data, dtype=float)
        if self.data.ndim != 2:
            raise ValueError("Los datos deben ser una matriz bidimensional")
        self.cmap = cmap

    def plot(self, caminos_coords=None, annotate=False, images_coords=None):
        plt.figure(facecolor='white')
        masked_data = np.ma.masked_invalid(self.data)

        # Encontrar el valor mínimo y máximo para normalizar el colormap
        vmin = np.nanmin(self.data)
        vmax = np.nanmax(self.data)

        # Mostrar la imagen con el colormap personalizado y límites de valores
        extent = [0, self.data.shape[1], self.data.shape[0], 0]
        plt.imshow(masked_data, cmap=self.cmap, interpolation='nearest', vmin=vmin, vmax=vmax, extent=extent)
        plt.colorbar()

        # Dibujar líneas manualmente en los bordes de cada celda de camino
        if caminos_coords is not None:
            for (row, col) in caminos_coords:
                # Límites superior, inferior, izquierdo, derecho
                if (row - 1, col) not in caminos_coords:  # Línea superior
                    plt.plot([col, col + 1], [row, row], color='black', linewidth=2)
                if (row + 1, col) not in caminos_coords:  # Línea inferior
                    plt.plot([col, col + 1], [row + 1, row + 1], color='black', linewidth=2)
                if (row, col - 1) not in caminos_coords:  # Línea izquierda
                    plt.plot([col, col], [row, row + 1], color='black', linewidth=2)
                if (row, col + 1) not in caminos_coords:  # Línea derecha
                    plt.plot([col + 1, col + 1], [row, row + 1], color='black', linewidth=2)

        # Si se necesita anotar las celdas
        if annotate:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    if not np.isnan(self.data[i, j]):
                        plt.text(j + 0.5, i + 0.5, f'{int(self.data[i, j])}', ha='center', va='center')

        # Añadir imágenes en coordenadas específicas con ajustes
        if images_coords is not None:
            ax = plt.gca()
            for (row, col, image_path, ajuste_x, ajuste_y) in images_coords:
                if os.path.isfile(image_path):
                    img = plt.imread(image_path)
                    imagebox = OffsetImage(img, zoom=0.5)  # Ajusta el zoom según sea necesario
                    ab = AnnotationBbox(imagebox, (col + ajuste_x, row + ajuste_y), frameon=False)
                    ax.add_artist(ab)
                else:
                    print(f"Archivo de imagen no encontrado: {image_path}")

        # Establecer límites de los ejes para ajustarse a la cuadrícula
        plt.xlim(0, self.data.shape[1])
        plt.ylim(self.data.shape[0], 0)
        plt.gca().set_aspect('equal')  # Mantener proporción 1:1
        plt.axis('on')  # Mostrar los ejes
        plt.show()





def a_star(start, goal, grid):
    filas, columnas = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            # Reconstruir el camino
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Invertir el camino

        x, y = current
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if not np.isnan(grid[nx, ny]):  # Evitar celdas no transitables
                    neighbors.append((nx, ny))

        for neighbor in neighbors:
            tentative_g_score = g_score[current] + grid[neighbor[0], neighbor[1]]  # Utilizar el costo de la celda
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return []

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def leer_estudiantes():
    estudiantes = []
    with open('caseta_elegida.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            estudiantes.append(row['Caseta Elegida'])
    return estudiantes

def generar_punto_inicio_desde_entradas(entradas):
    # Elegir una entrada al azar
    entrada_elegida = random.choice(list(entradas.keys()))
    # Elegir un punto al azar dentro de la entrada elegida
    punto_inicio = random.choice(entradas[entrada_elegida])
    return punto_inicio

def actualizar_mapa_de_calor(mapa, caminos):
    for camino in caminos:
        for (x, y) in camino:
            mapa[x, y] += 1  # Incrementar el valor en la celda
    return mapa

def simular_distribucion():
    # Definir los rangos de las entradas
    entradas_ranges = [
        'A6:A8',
        'A17:A19',
        'A34:A35',
        'A35:G35',
        'N35:P35',
        'Y35:AA35'
    ]

    # Convertir las entradas a coordenadas
    entradas = {}
    for idx, entrada_range in enumerate(entradas_ranges):
        coords = parse_cell_range(entrada_range)
        entradas[f'Entrada {idx+1}'] = coords

    # Definir los rangos de los caminos
    caminos_ranges = [
        'A6:M8',
        'K4:AD6',
        'Y7:AA35',
        'E23:P25',
        'K6:M19',
        'N12:T14',
        'A17:P19',
        'N17:P35',
        'E17:G35',
        'E29:P31',
        'A34:G35'
    ]
    caminos_coords = []
    for camino_range in caminos_ranges:
        coords = parse_cell_range(camino_range)
        caminos_coords.extend(coords)
        
    casetas = {
        'Caseta Blanca': 'C24:D27',
        'CafeITO': 'I24:L25',
        'Lado Chedraui': 'AE4:AF6'
    }
    casetas_coords = {}
    casetas_centers = {}
    for caseta_name, caseta_range in casetas.items():
        coords = parse_cell_range(caseta_range)
        casetas_coords[caseta_name] = coords
        # Calcular el centro de la caseta
        rows = [row for row, col in coords]
        cols = [col for row, col in coords]
        center_row = int(np.mean(rows))
        center_col = int(np.mean(cols))
        casetas_centers[caseta_name] = (center_row, center_col)

    max_row = max([row for row, col in caminos_coords + [coord for coords in casetas_coords.values() for coord in coords]])
    max_col = max([col for row, col in caminos_coords + [coord for coords in casetas_coords.values() for coord in coords]])
    grid_size = max(max_row, max_col) + 1 # Añadir margen

    cuadricula = np.full((grid_size, grid_size), np.nan)

    for row, col in caminos_coords:
        if 0 <= row < grid_size and 0 <= col < grid_size:
            cuadricula[row, col] = 1  # Camino transitable

    for entrada_coords in entradas.values():
        for row, col in entrada_coords:
            if 0 <= row < grid_size and 0 <= col < grid_size:
                cuadricula[row, col] = 1  # Entrada transitable

    for coords in casetas_coords.values():
        for row, col in coords:
            if 0 <= row < grid_size and 0 <= col < grid_size:
                cuadricula[row, col] = 1  # Caseta transitable

    # Leer estudiantes y mapa
    estudiantes_casetas = leer_estudiantes()
    filas, columnas = cuadricula.shape
    caminos = []

    for caseta in estudiantes_casetas:
        # Generar punto de inicio desde las entradas
        inicio = generar_punto_inicio_desde_entradas(entradas)

        # Obtener el destino basado en la caseta elegida
        if caseta in casetas_centers:
            destino = casetas_centers[caseta]
        else:
            continue  # Si la caseta no es reconocida, saltamos

        camino = a_star(inicio, destino, cuadricula)
        if camino:
            caminos.append(camino)

    # Actualizar el mapa de calor con los caminos
    mapa_actualizado = np.zeros((filas, columnas), dtype=float)
    mapa_actualizado = actualizar_mapa_de_calor(mapa_actualizado, caminos)

    # Visualizar el mapa de calor actualizado con el colormap personalizado
    images_coords = []
    for caseta_name, coords in casetas_coords.items():
        # Construir el nombre del archivo de imagen correspondiente
        image_filename = caseta_name.replace(' ', '').lower() + '.jpg'
        image_path = os.path.join('img', image_filename)

        if not os.path.isfile(image_path):
            print(f"Archivo de imagen no encontrado: {image_path}")
            continue

        # Calcular la coordenada central de la caseta
        rows = [row for row, col in coords]
        cols = [col for row, col in coords]
        center_row = int(np.mean(rows))
        center_col = int(np.mean(cols))

        # Ajustes específicos para la posición de la imagen
        if caseta_name == 'Caseta Blanca':
            ajuste_x = -1.0  # Ajusta este valor
            ajuste_y = 0.5   # Ajusta este valor
        elif caseta_name == 'Lado Chedraui':
            ajuste_x = +1.5  # Ajusta este valor
            ajuste_y = + 0.4   # Ajusta este valor
        elif caseta_name == 'CafeITO':
            ajuste_x = 0.0
            ajuste_y = +1.9
        else:
            ajuste_x = 0.0
            ajuste_y = 0.0

        images_coords.append((center_row, center_col, image_path, ajuste_x, ajuste_y))

    # Agregar la imagen del Edificio L
    image_path_edificioL = os.path.join('img', 'edificioL.png')
    if os.path.isfile(image_path_edificioL):
        row_edificioL = 15  # Ajusta este valor
        col_edificioL = 20  # Ajusta este valor
        ajuste_x = 0.0      # Ajusta este valor
        ajuste_y = 0.0      # Ajusta este valor
        images_coords.append((row_edificioL, col_edificioL, image_path_edificioL, ajuste_x, ajuste_y))
    else:
        print(f"Archivo de imagen no encontrado: {image_path_edificioL}")

    # Visualizar el mapa de calor actualizado con el colormap personalizado
    heatmap = HeatmapGenerator(mapa_actualizado, cmap=custom_cmap)
    heatmap.plot(caminos_coords=caminos_coords, annotate=False, images_coords=images_coords)

#if __name__ == "__main__":
#    simular_distribucion()
