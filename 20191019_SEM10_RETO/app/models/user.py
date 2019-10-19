from database.config import Conexion
import bcrypt


conn = Conexion()
Model = conn.model()



class User(Model):
    __table__ = 'users'
    __primary_key__ = 'user_id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['password', 'created_at', 'updated_at']
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

    def password_valid(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))