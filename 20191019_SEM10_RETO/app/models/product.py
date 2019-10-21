from database.config import Conexion


conn = Conexion()
Model = conn.model()



class Product(Model):
    __table__ = 'products'
    __primary_key__ = 'product_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['name', 'price', 'quantity']
    __casts__ = {
        'name': 'str',
        'price': 'float',
        'quantity': 'int'
    }
