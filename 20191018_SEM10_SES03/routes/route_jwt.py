from flask import request
import jwt
import bcrypt

user = {
    'od': 1,
    'name': 'Jesus',
    'last_name': 'Roncal'
}



def routes(app):
    @app.route('/autorizado')
    def autorizado():
        password = 'yisus'
        token = request.values.get('token')
        #result = jwt.decode(token, password)
        result = bcrypt.checkpw(password.encode('utf-8'), token.encode('utf-8'))
        return {'check': result}

    @app.route('/noautorizado')
    def no_autorizado():
        password = 'yisus'
        #token = jwt.encode(user, password, algorithm='HS256')
        token = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return token
