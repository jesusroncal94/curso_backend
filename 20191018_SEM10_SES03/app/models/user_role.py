from database.config import Conexion
from orator.orm import belongs_to
from app.models.user import User
from app.models.role import Role


conn = Conexion()
Model = conn.model()



class User_role(Model):
    __table__ = 'user_roles'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __guarded__ = ['id']
    __fillable__ = ['user_id', 'role_id']
    __casts__ = {
        'user_id': 'int',
        'role_id': 'int'
    }

    @belongs_to('user_id', 'id')
    def user(self):
        return User

    @belongs_to('role_id', 'id')
    def role(self):
        return Role
