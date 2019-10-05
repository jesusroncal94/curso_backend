import pymysql

class Conexion():
    def __init__(self, host = "localhost", user = "root", password = "", baseDatos = "colegio"):
        self.bd = pymysql.connect(host, user, password, baseDatos)
        self.cursor = self.bd.cursor()
        print("Conexion a base de datos exitosa")    

    def ejecutarSentencia(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def cerrarConexion(self):
        self.bd.close()
    
    def commit(self):
        self.bd.commit()
        return
    
    def rollback(self):
        self.bd.rollback()
        return