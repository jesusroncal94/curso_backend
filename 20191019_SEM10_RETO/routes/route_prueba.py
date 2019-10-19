from flask import request
from helpers import helper


def routes(app):
    @app.route('/prueba', methods = ['POST'])
    @helper.token_required
    def prueba():
        return helper.token_get_object()
