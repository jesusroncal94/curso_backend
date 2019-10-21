from database.config import Conexion


conn = Conexion()
Model = conn.model()



class Invoice_detail(Model):
    __table__ = 'invoice_details'
    __primary_key__ = 'invoice_detail_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['invoice_id', 'product_id', 'price', 'quantity']
    __casts__ = {
        'invoice_id': 'int',
        'product_id': 'int',
        'price': 'float',
        'quantity': 'int'
    }
