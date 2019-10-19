from helpers import helper
from app.models.role import Role as RoleModel


class Role():
    def __init__(self, name = None, status = None):
        self.name = name
        self.status = status

    def add_role(self, role, app):
        try:
            RoleModel.insert({
                'name': role.name,
                'status': role.status
            })
            message = f'''Se agregó el role: {role.name}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def list_roles(self, app):
        roles_dict = {}
        try:
            roles = RoleModel.get()
            roles_dict = roles.serialize()
            message = f'''Lista de roles'''
            print(message)
            return helper.handler_response(app, 201, message, roles_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def update_role(self, role_id, role, app):
        try:
            RoleModel \
                .where('id', role_id) \
                .update({
                'name': role.name,
                'status': role.status
            })
            message = f'''Se actualizó el role: {role.name}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def delete_role(self, role_id, app):
        try:
            RoleModel \
                .where('id', role_id) \
                .delete()
            message = f'''Se eliminó el role: {role_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def find_role(self, role_id, role_name, app):
        roles_dict = {}
        try:
            roles = RoleModel \
                .where('id', role_id) \
                .or_where('name', role_name) \
                .first()
            roles_dict = roles.serialize()
            message = f'''Lista de roles'''
            print(message)
            return helper.handler_response(app, 201, message, roles_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')
