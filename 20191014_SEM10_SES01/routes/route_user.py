from flask import request
from app.user import User


user = User()



def routes(app):
    @app.route('/')
    def hello_world():
        return '<h1>Hola Pachaqtec</h1>'

    @app.route('/users/add', methods = ['POST'])
    def users_add():
        values = request.values
        user.name = values.get('name')
        user.last_name = values.get('last_name')
        user.age = values.get('age')
        user.gender = values.get('gender')
        user.state = values.get('state')
        return user.add_user(user, app)

    @app.route('/users/list', methods = ['GET'])
    def users_list():
        return user.list_users(app)

    @app.route('/users/update', methods = ['PUT'])
    def users_update():
        values = request.values
        user_id = values.get('id')
        user.name = values.get('name')
        user.last_name = values.get('last_name')
        user.age = values.get('age')
        user.gender = values.get('gender')
        user.state = values.get('state')
        return user.update_user(user_id, user, app)

    @app.route('/users/delete', methods = ['DELETE'])
    def users_delete():
        values = request.values
        user_id = values.get('id')
        return user.delete_user(user_id, app)

    @app.route('/users/find', methods = ['GET'])
    def users_find():
        values = request.values
        user_id = values.get('id')
        user_name = values.get('name')
        return user.find_user(user_id, user_name, app)

    @app.route('/users/gender_age_range_user', methods = ['GET'])
    def users_find_gender_age_range_user():
        values = request.values
        user_gender = values.get('gender')
        user_initial_age = values.get('initial_age')
        user_final_age = values.get('final_age')
        return user.find_gender_age_range_user(user_gender, user_initial_age, user_final_age, app)
