from flask import request
from app.controllers.role import Role
from helpers import helper


role = Role()



def routes(app):
    @app.route('/roles/add', methods = ['POST'])
    @helper.token_required
    def roles_add():
        values = request.values
        role.name = values.get('name')
        role.status = values.get('status')
        return role.add_role(role, app)

    @app.route('/roles/list', methods = ['GET'])
    @helper.token_required
    def roles_list():
        return role.list_roles(app)

    @app.route('/roles/update', methods = ['PUT'])
    @helper.token_required
    def roles_update():
        values = request.values
        role_id = values.get('role_id')
        role.name = values.get('name')
        role.status = values.get('status')
        return role.update_role(role_id, role, app)

    @app.route('/roles/delete', methods = ['DELETE'])
    @helper.token_required
    def roles_delete():
        values = request.values
        role_id = values.get('role_id')
        return role.delete_role(role_id, app)

    @app.route('/roles/find', methods = ['POST'])
    @helper.token_required
    def roles_find():
        values = request.values
        role_id = values.get('role_id')
        role_name = values.get('name')
        return role.find_role(role_id, role_name, app)
