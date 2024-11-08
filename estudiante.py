from datetime import time
import random

class Estudiante:
    def __init__(self, hora_llegada, sensibilidad_calidad, tiempo_disponible, dinero_disponible):
        self.hora_llegada = hora_llegada
        self.sensibilidad_calidad = sensibilidad_calidad
        self.tiempo_disponible = tiempo_disponible
        self.dinero_disponible = dinero_disponible

    def __str__(self):
        return (f"Hora de llegada: {self.hora_llegada.strftime('%H:%M')}, "
                f"Calidad: {self.sensibilidad_calidad}, "
                f"Tiempo disponible: {self.tiempo_disponible}, "
                f"Dinero disponible: {self.dinero_disponible}")

# Función para generar una hora de llegada aleatoria entre 08:00 y 16:00
def generar_hora_llegada():
    hora = random.randint(8, 15)  # Horas entre 08 y 15
    minuto = random.randint(0, 59)  # Minutos entre 00 y 59
    return time(hora, minuto)

# Opciones para cada atributo
sensibilidad_calidad = ["Alta", "Media", "Baja"]
tiempo_disponible = ["No tengo libre", "1 hora", "2 horas", "3 horas", "Más de 3 horas"]
dinero_disponible = ["Menos de 30", "30 - 50", "50 - 70", "Más de 70"]

# Crear algunos estudiantes con horas de llegada con minutos aleatorios
estudiantes = []

for _ in range(20):  # Crear 5 estudiantes como ejemplo
    hora_llegada = generar_hora_llegada()
    sensibilidad = random.choice(sensibilidad_calidad)
    tiempo = random.choice(tiempo_disponible)
    dinero = random.choice(dinero_disponible)
    
    estudiante = Estudiante(hora_llegada, sensibilidad, tiempo, dinero)
    estudiantes.append(estudiante)

# Imprimir los estudiantes
for estudiante in estudiantes:
    print(estudiante)
