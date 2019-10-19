from database.config import Conexion
from orator.orm import belongs_to
from app.models.business import Business as BusinessModel
from app.models.user import User as UserModel
from app.models.role import Role as RoleModel


conn = Conexion()
Model = conn.model()



class User_role(Model):
    __table__ = 'user_roles'
    __primary_key__ = 'user_role_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['business_id', 'user_id', 'role_id']
    __casts__ = {
        'business_id': 'int',
        'user_id': 'int',
        'role_id': 'int'
    }

    @belongs_to
    def business(self):
        return BusinessModel

    @belongs_to
    def user(self):
        return UserModel

    @belongs_to
    def role(self):
        return RoleModel
