from database.config import Conexion
from orator.orm import belongs_to_many
from app.models.role import Role
import bcrypt

conn = Conexion()
Model = conn.model()



class User(Model):
    __table__ = 'users'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['password']
    __fillable__ = ['username', 'password', 'name', 'last_name', 'age', 'gender', 'status']
    __casts__ = {
        'username': 'str',
        'password': 'str',
        'name': 'str',
        'last_name': 'str',
        'age': 'int',
        'gender': 'str',
        'status': 'int'
    }

    @belongs_to_many('user_roles', 'user_id')
    def roles(self):
        return Role

    def password_valid(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
