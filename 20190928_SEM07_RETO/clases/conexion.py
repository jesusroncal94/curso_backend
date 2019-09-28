import pymongo

class Conexion():
    def __init__(self, host = "localhost", puerto = "27017", usuario = "", password = "", bd = "colegio"):
        self.host = host
        self.puerto = puerto
        self.usuario = usuario
        self.password = password
        self.bd = bd
        self.conn = pymongo.MongoClient("mongodb://{}:{}/".format(self.host, self.puerto))
        self.cliente = self.conn[self.bd]

    def connect(self): 
        return self.cliente
    
    def close(self):
        self.conn.close()