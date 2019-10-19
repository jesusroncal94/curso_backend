from flask import request
from app.controllers.user import User
from routes.auth import route as route_auth
from helpers import helper


user = User()



def routes(app):
    route_auth.auth(app, user)
    
    @app.route('/users/add', methods = ['POST'])
    def users_add():
        values = request.values
        user.name = values.get('name')
        user.last_name = values.get('last_name')
        user.age = values.get('age')
        user.gender = values.get('gender')
        user.status = values.get('status')
        return user.add_user(user, app)

    @app.route('/users/list', methods = ['GET'])
    @helper.token_required
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
        user.status = values.get('status')
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
