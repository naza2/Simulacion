import matplotlib.pyplot as plt

def visualizar_distribucion(casetas):
    x = [caseta.ubicacion[0] for caseta in casetas]
    y = [caseta.ubicacion[1] for caseta in casetas]
    tamanos = [len(caseta.estudiantes_atendidos) * 10 for caseta in casetas]

    plt.scatter(x, y, s=tamanos, alpha=0.5)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title("Distribución de Estudiantes en las Casetas")
    plt.show()
