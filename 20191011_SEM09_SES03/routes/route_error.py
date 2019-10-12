def error_handler(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return '<h1>Página no encontrada...</h1>', 404
