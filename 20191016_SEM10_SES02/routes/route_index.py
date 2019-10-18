from flask import request


def routes(app):
    @app.route('/')
    def hello_world():
        return '<h1>Hola Pachaqtec</h1>'