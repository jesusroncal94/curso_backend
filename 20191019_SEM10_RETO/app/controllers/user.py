from helpers import helper
from app.models.user import User as UserModel
from app.models.user_role import User_role as User_roleModel
import jwt
import bcrypt


class User():
    def __init__(self, username = None, password = None, name = None, last_name = None, age = None, gender = None, status = None):
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.status = status

    def add_user(self, user, app):
        try:
            hash_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            UserModel.insert({
                'username': user.username,
                'password': hash_pw,
                'name': user.name,
                'last_name': user.last_name,
                'age': user.age,
                'gender': user.gender,
                'status': user.status
            })
            message = f'''Se agregó el usuario: {user.name} {user.last_name}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def list_users(self, app):
        users_dict = {}
        try:
            users = UserModel.get()
            users_dict = users.serialize()
            message = f'''Lista de usuarios'''
            print(message)
            return helper.handler_response(app, 201, message, users_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def update_user(self, user_id, user, app):
        try:
            hash_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            UserModel \
                .where('user_id', user_id) \
                .update({
                'username': user.username,
                'password': hash_pw,
                'name': user.name,
                'last_name': user.last_name,
                'age': user.age,
                'gender': user.gender,
                'status': user.status
            })
            message = f'''Se actualizó el usuario: {user.name} {user.last_name}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def delete_user(self, user_id, app):
        try:
            UserModel \
                .where('user_id', user_id) \
                .delete()
            message = f'''Se eliminó el usuario: {user_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def find_user(self, user_id, user_name, app):
        users_dict = {}
        try:
            users = UserModel \
                .where('user_id', user_id) \
                .or_where('name', user_name) \
                .first()
            users_dict = users.serialize()
            message = f'''Lista de usuarios'''
            print(message)
            return helper.handler_response(app, 201, message, users_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def find_gender_age_range_user(self, user_gender, user_initial_age, user_final_age, app):
        users_dict = {}
        try:
            users = UserModel \
                .where('gender', user_gender) \
                .where_between('age', [user_initial_age, user_final_age]) \
                .get()
            users_dict = users.serialize()
            message = f'''Lista de usuarios por género y rango de edad'''
            print(message)
            return helper.handler_response(app, 201, message, users_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def login(self, app, username, password):
        user_dict = {}
        try:
            user_found = UserModel.where_username(username).first()
            
            user_dict = user_found.serialize()
            user_role_found = User_roleModel.where('user_id', user_dict['user_id']).first()
            user_dict['user_role'] = user_role_found.serialize()
            
            if user_found and user_found.password_valid(password):
                token = jwt.encode(user_dict, helper.jwt_secret(), algorithm='HS256')
                response = {
                    'token': token,
                    'data': user_dict
                }
                return helper.handler_response(app, 201, 'Logeado con éxito', response)
            message = f'El usuario y/o contraseña son incorrectos: {username}'
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
