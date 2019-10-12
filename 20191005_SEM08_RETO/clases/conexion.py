import pymysql


class Conexion():
    def __init__(self, host="localhost", user="root", password="root",
                 baseDatos="colegio"):
        self.cliente = pymysql.connect(host, user, password, baseDatos)
        self.cursor = self.cliente.cursor()
        print("Conexion a base de datos exitosa")

    def ejecutarSentencia(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def cerrarConexion(self):
        self.cliente.close
