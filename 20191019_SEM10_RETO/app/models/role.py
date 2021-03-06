from database.config import Conexion


conn = Conexion()
Model = conn.model()



class Role(Model):
    __table__ = 'roles'
    __primary_key__ = 'role_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['name', 'status']
    __casts__ = {
        'name': 'str',
        'status': 'int',
    }
