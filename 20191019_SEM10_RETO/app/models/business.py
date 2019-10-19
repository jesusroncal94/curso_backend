from database.config import Conexion


conn = Conexion()
Model = conn.model()



class Business(Model):
    __table__ = 'business'
    __primary_key__ = 'business_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['ruc', 'name', 'direccion']
    __casts__ = {
        'ruc': 'str',
        'name': 'str',
        'address': 'str'
    }
