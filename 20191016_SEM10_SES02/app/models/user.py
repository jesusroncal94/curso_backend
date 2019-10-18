from database.config import Conexion
from orator.orm import belongs_to_many
from app.models.role import Role


conn = Conexion()
Model = conn.model()



class User(Model):
    __table__ = 'users'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __guarded__ = ['id']
    __fillable__ = ['name', 'last_name', 'age', 'gender', 'status']
    __casts__ = {
        'name': 'str',
        'last_name': 'str',
        'age': 'int',
        'gender': 'str',
        'status': 'int'
    }

    @belongs_to_many('user_roles', 'user_id')
    def roles(self):
        return Role
