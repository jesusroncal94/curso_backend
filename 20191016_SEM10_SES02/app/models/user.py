from database.config import Conexion


conn = Conexion()
Model = conn.model()



class Users(Model):
    __table__ = 'users'
    __primary_key__ = 'id'
    __timestamps__
