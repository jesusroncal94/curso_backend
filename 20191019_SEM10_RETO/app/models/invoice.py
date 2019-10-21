from database.config import Conexion
from orator.orm import has_one, belongs_to, belongs_to_many, has_many
from app.models.user_role import User_role as User_roleModel
from app.models.invoice_detail import Invoice_detail as Invoice_detailModel
from app.models.product import Product as ProductModel

conn = Conexion()
Model = conn.model()



class Invoice(Model):
    __table__ = 'invoices'
    __primary_key__ = 'invoice_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['user_role_id', 'subtotal', 'igv', 'total']
    __casts__ = {
        'user_role_id': 'int',
        'subtotal': 'float',
        'igv': 'float',
        'total': 'float'
    }

    @belongs_to('user_role_id', 'user_role_id')
    def user_role(self):
        return User_roleModel

    @has_many('invoice_id', 'invoice_id')
    def invoice_details(self):
        return Invoice_detailModel
