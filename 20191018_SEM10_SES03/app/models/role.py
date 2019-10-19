from database.config import Conexion
from orator.orm import belongs_to_many


conn = Conexion()
Model = conn.model()



class Role(Model):
    __table__ = 'roles'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __guarded__ = ['id']
    __fillable__ = ['name', 'status']
    __casts__ = {
        'name': 'str',
        'status': 'int'
    }

    @belongs_to_many('user_roles', 'role_id')
    def users(self):
        return User
