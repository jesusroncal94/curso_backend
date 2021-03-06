from helpers import helper
from app.models.user import User as UserModel


class User():
    def __init__(self, name = None, last_name = None, age = None, gender = None, status = None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.status = status

    def add_user(self, user, app):
        try:
            UserModel.insert({
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
            UserModel \
                .where('id', user_id) \
                .update({
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
                .where('id', user_id) \
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
                .where('id', user_id) \
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
