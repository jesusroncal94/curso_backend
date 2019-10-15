from flask import request
from app.classes.cargo import Cargo


cargo = Cargo()

def routes(app):
    @app.route('/cargos/add', methods = ['POST'])
    def cargos_add():
        values = request.values
        cargo.descripcion = values.get('descripcion')
        cargo.idarea = values.get('idarea')
        cargo.peso = values.get('peso')
        return cargo.add_cargo(cargo, app)

    @app.route('/cargos/list', methods = ['GET'])
    def cargos_list():
        return cargo.list_cargos(app)

    @app.route('/cargos/update', methods = ['PUT'])
    def cargos_update():
        values = request.values
        idcargo = values.get('idcargo')
        cargo.descripcion = values.get('descripcion')
        cargo.idarea = values.get('idarea')
        cargo.peso = values.get('peso')
        return cargo.update_cargo(idcargo, cargo, app)

    @app.route('/cargos/delete', methods = ['DELETE'])
    def cargos_delete():
        values = request.values
        idcargo = values.get('idcargo')
        return cargo.delete_cargo(idcargo, app)

    @app.route('/cargos/get/', methods = ['POST'])
    def cargos_get():
        values = request.values
        idcargo = values.get('idcargo')
        return cargo.get_cargo(idcargo, app)
