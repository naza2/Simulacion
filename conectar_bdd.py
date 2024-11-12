import psycopg2

def conectar_bdd():
    try:
        conexion = psycopg2.connect(
            dbname="Simulacion",
            user="diego",
            password="facilita",
            host="localhost"
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
