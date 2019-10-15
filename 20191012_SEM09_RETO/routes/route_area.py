from flask import request
from app.classes.area import Area


area = Area()

def routes(app):    
    @app.route('/areas/add', methods = ['POST'])
    def areas_add():
        values = request.values
        area.descripcion = values.get('descripcion')
        area.relacion = values.get('relacion')
        return area.add_area(area, app)

    @app.route('/areas/list', methods = ['GET'])
    def areas_list():
        return area.list_areas(app)

    @app.route('/areas/update', methods = ['PUT'])
    def areas_update():
        values = request.values
        idarea = values.get('idarea')
        area.descripcion = values.get('descripcion')
        area.relacion = values.get('relacion')
        return area.update_area(idarea, area, app)

    @app.route('/areas/delete', methods = ['DELETE'])
    def areas_delete():
        values = request.values
        idarea = values.get('idarea')
        return area.delete_area(idarea, app)

    @app.route('/areas/get/', methods = ['POST'])
    def areas_get():
        values = request.values
        idarea = values.get('idarea')
        return area.get_area(idarea, app)
