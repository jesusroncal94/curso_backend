from helpers import helper
from app.models.user_role import User_role as User_roleModel
from app.models.business import Business as BusinessModel
from app.models.user import User as UserModel
from app.models.role import Role as RoleModel


class User_role():
    def __init__(self, business_id = None, user_id = None, role_id = None):
        self.business_id = business_id
        self.user_id = user_id
        self.role_id = role_id

    def add_user_role(self, user_role, app):
        try:
            business = BusinessModel.find(user_role.business_id)
            user = UserModel.find(user_role.user_id)
            role = RoleModel.find(user_role.role_id)
            if business and user and role:
                User_roleModel.insert({
                    'business_id': user_role.business_id,
                    'user_id': user_role.user_id,
                    'role_id': user_role.role_id
                })
                message = f'''Se agregó el user_role: {user_role.business_id}-{user_role.user_id}-{user_role.role_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            message = f'''No existe empresa, usuario o rol'''
            print(message)
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def list_user_roles(self, app):
        user_roles_dict = {}
        try:
            user_roles = User_roleModel.get()
            user_roles.load('business', 'user', 'role')
            user_roles_dict = user_roles.serialize()
            message = f'''Lista de user_roles'''
            print(message)
            return helper.handler_response(app, 201, message, user_roles_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_user_role(self, user_role_id, user_role, app):
        try:
            user = UserModel.find(user_role.user_id)
            role = RoleModel.find(user_role.role_id)
            if user != None and role != None:
                User_roleModel \
                    .where('user_role_id', user_role_id) \
                    .update({
                    'user_id': user_role.user_id,
                    'role_id': user_role.role_id
                })
                message = f'''Se actualizó el user_role: {user_role.user_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            else:
                message = f'''No existe usuario o rol'''
                return helper.handler_response(app, 500, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_user_role(self, user_role_id, app):
        try:
            User_roleModel \
                .where('user_role_id', user_role_id) \
                .delete()
            message = f'''Se eliminó el user_role: {user_role_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_user_role(self, user_role_id, user_role_business_id, user_role_user_id, user_role_role_id, app):
        user_roles_dict = {}
        try:
            user_roles = User_roleModel \
                .where('user_role_id', user_role_id) \
                .or_where('business_id', user_role_business_id) \
                .or_where('user_id', user_role_user_id) \
                .or_where('role_id', user_role_role_id) \
                .first()
            user_roles_dict = user_roles.serialize()
            message = f'''Lista de user_roles'''
            print(message)
            return helper.handler_response(app, 201, message, user_roles_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
