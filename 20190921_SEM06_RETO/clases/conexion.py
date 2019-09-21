import pymysql as m

class Conexion():
    __servidor = 'localhost'
    __usuario = 'root'
    __contrasena = ''
    __bd = 'facturacion'

    def __init__(self):
        pass

    def conectar(self):
        conexion = m.connect(host = self.__servidor, 
                        user = self.__usuario,
                        passwd = self.__contrasena,
                        db = self.__bd)
        return conexion