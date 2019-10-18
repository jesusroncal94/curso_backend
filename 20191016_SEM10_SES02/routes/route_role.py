from flask import request
from app.controllers.role import Role


role = Role()



def routes(app):
    @app.route('/roles/add', methods = ['POST'])
    def roles_add():
        values = request.values
        role.name = values.get('name')
        role.status = values.get('status')
        return role.add_role(role, app)

    @app.route('/roles/list', methods = ['GET'])
    def roles_list():
        return role.list_roles(app)

    @app.route('/roles/update', methods = ['PUT'])
    def roles_update():
        values = request.values
        role_id = values.get('id')
        role.name = values.get('name')
        role.status = values.get('status')
        return role.update_role(role_id, role, app)

    @app.route('/roles/delete', methods = ['DELETE'])
    def roles_delete():
        values = request.values
        role_id = values.get('id')
        return role.delete_role(role_id, app)

    @app.route('/roles/find', methods = ['GET'])
    def roles_find():
        values = request.values
        role_id = values.get('id')
        role_name = values.get('name')
        return role.find_role(role_id, role_name, app)
