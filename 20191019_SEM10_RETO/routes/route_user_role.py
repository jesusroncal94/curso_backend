from flask import request
from app.controllers.user_role import User_role
from helpers import helper


user_role = User_role()



def routes(app):
    @app.route('/user_roles/add', methods = ['POST'])
    @helper.token_required
    @helper.role_gerente
    def user_roles_add():
        values = request.values
        user_role.business_id = values.get('business_id')
        user_role.user_id = values.get('user_id')
        user_role.role_id = values.get('role_id')
        return user_role.add_user_role(user_role, app)

    @app.route('/user_roles/list', methods = ['GET'])
    @helper.token_required
    @helper.role_supervisor
    def user_roles_list():
        return user_role.list_user_roles(app)

    @app.route('/user_roles/update', methods = ['PUT'])
    @helper.token_required
    @helper.role_gerente
    def user_roles_update():
        values = request.values
        user_role_id = values.get('user_role_id')
        user_role.business_id = values.get('business_id')
        user_role.user_id = values.get('user_id')
        user_role.role_id = values.get('role_id')
        return user_role.update_user_role(user_role_id, user_role, app)

    @app.route('/user_roles/delete', methods = ['DELETE'])
    @helper.token_required
    @helper.role_gerente
    def user_roles_delete():
        values = request.values
        user_role_id = values.get('user_role_id')
        return user_role.delete_user_role(user_role_id, app)

    @app.route('/user_roles/find', methods = ['GET'])
    @helper.token_required
    @helper.role_supervisor
    def user_roles_find():
        values = request.values
        user_role_id = values.get('user_role_id')
        user_role_business_id = values.get('business_id')
        user_role_user_id = values.get('user_id')
        user_role_role_id = values.get('role_id')
        return user_role.find_user_role(user_role_id, user_role_business_id, user_role_user_id, user_role_role_id, app)
