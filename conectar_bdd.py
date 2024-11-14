import psycopg2

class ConectarBDD:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def conectar(self):
        try:
            conexion = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host
            )
            print("Conexión exitosa a la base de datos")
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None
