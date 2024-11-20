import tkinter as tk
from tkinter import ttk
from conectar_bdd import ConectarBDD

class AjusteCasetasGUI:
    def __init__(self, dbname, user, password, host):
        # Conexión a la base de datos
        self.conexion_db = ConectarBDD(dbname, user, password, host).conectar()
        self.casetas = self.obtener_casetas_bdd()

        # Configuración de la interfaz de Tkinter
        self.root = tk.Tk()
        self.root.title("Ajuste de Parámetros de Casetas")
        self.root.geometry("1100x300")  # Establece el tamaño de la ventana
        self.root.configure(bg="#e6e6e6")
        self.crear_interfaz()

    def obtener_casetas_bdd(self):
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            SELECT id_caseta, nombre_caseta, tiempo_promedio_atencion, flujo_clientes, 
                   variedad_productos, calidad_comida, precios
            FROM casetas
        """)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def crear_interfaz(self):
        headers = ["Nombre", "Tiempo Atención", "Flujo Clientes", "Variedad Productos", "Calidad Comida", "Precios", "Acción"]
        for i, header in enumerate(headers):
            tk.Label(self.root, text=header, font=("Arial", 10, "bold"), bg="#e6e6e6").grid(row=0, column=i, padx=10, pady=5)

        # Crear controles para cada caseta
        for i, (id_caseta, nombre_caseta, tiempo, flujo, variedad, calidad, precio) in enumerate(self.casetas, start=1):
            # Etiqueta de nombre de caseta
            tk.Label(self.root, text=nombre_caseta, bg="#e6e6e6").grid(row=i, column=0, padx=10, pady=5)

            # Deslizador para tiempo promedio de atención
            tiempo_slider = tk.Scale(self.root, from_=1, to=5, orient="horizontal", bg="#e6e6e6")
            tiempo_slider.set(tiempo)
            tiempo_slider.grid(row=i, column=1, padx=5, pady=5)

            # Deslizador para flujo de clientes
            flujo_slider = tk.Scale(self.root, from_=1, to=5, orient="horizontal", bg="#e6e6e6")
            flujo_slider.set(flujo)
            flujo_slider.grid(row=i, column=2, padx=5, pady=5)

            # Deslizador para variedad de productos
            variedad_slider = tk.Scale(self.root, from_=1, to=5, orient="horizontal", bg="#e6e6e6")
            variedad_slider.set(variedad)
            variedad_slider.grid(row=i, column=3, padx=5, pady=5)

            # Deslizador para calidad de la comida
            calidad_slider = tk.Scale(self.root, from_=1, to=5, orient="horizontal", bg="#e6e6e6")
            calidad_slider.set(calidad)
            calidad_slider.grid(row=i, column=4, padx=5, pady=5)

            # Deslizador para precios
            precio_slider = tk.Scale(self.root, from_=1, to=5, orient="horizontal", bg="#e6e6e6")
            precio_slider.set(precio)
            precio_slider.grid(row=i, column=5, padx=5, pady=5)

            # Botón para actualizar cada caseta
            update_button = tk.Button(self.root, text="Actualizar", command=lambda id=id_caseta, t=tiempo_slider, f=flujo_slider, v=variedad_slider, c=calidad_slider, p=precio_slider: self.actualizar_caseta(id, t.get(), f.get(), v.get(), c.get(), p.get()))
            update_button.grid(row=i, column=6, padx=10, pady=5)

    def actualizar_caseta(self, id_caseta, tiempo, flujo, variedad, calidad, precio):
        cursor = self.conexion_db.cursor()
        cursor.execute("""
            UPDATE casetas
            SET tiempo_promedio_atencion = %s, flujo_clientes = %s, variedad_productos = %s, calidad_comida = %s, precios = %s
            WHERE id_caseta = %s
        """, (tiempo, flujo, variedad, calidad, precio, id_caseta))
        self.conexion_db.commit()
        cursor.close()
        print(f"Caseta {id_caseta} actualizada: Tiempo Atención={tiempo}, Flujo Clientes={flujo}, Variedad={variedad}, Calidad={calidad}, Precios={precio}")

    def ejecutar(self):
        self.root.mainloop()
if __name__ == "__main__":
    gui = AjusteCasetasGUI(dbname="Simulacion", user="diego", password="facilita", host="localhost")
    gui.ejecutar()
