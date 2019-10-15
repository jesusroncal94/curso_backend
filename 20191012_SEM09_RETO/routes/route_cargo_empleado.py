from flask import request
from app.classes.cargo_empleado import Cargo_empleado

cargo_empleado = Cargo_empleado()

def routes(app):    
    @app.route('/cargos_empleados/add', methods = ['POST'])
    def cargos_empleado_add():
        values = request.values
        cargo_empleado.idempleado = values.get('idempleado')
        cargo_empleado.idcargo = values.get('idcargo')
        return cargo_empleado.add_cargo_empleado(cargo_empleado, app)

    @app.route('/cargos_empleados/list', methods = ['GET'])
    def cargos_empleado_list():
        return cargo_empleado.list_cargos_empleados(app)

    @app.route('/cargos_empleados/update', methods = ['PUT'])
    def cargos_empleado_update():
        values = request.values
        idcargo_empleado = values.get('idcargo_empleado')
        cargo_empleado.idempleado = values.get('idempleado')
        cargo_empleado.idcargo = values.get('idcargo')
        return cargo_empleado.update_cargo_empleado(idcargo_empleado, cargo_empleado, app)

    @app.route('/cargos_empleados/delete', methods = ['DELETE'])
    def cargos_empleado_delete():
        values = request.values
        idcargo_empleado = values.get('idcargo_empleado')
        return cargo_empleado.delete_cargo_empleado(idcargo_empleado, app)

    @app.route('/cargos_empleados/get/', methods = ['POST'])
    def cargos_empleado_get():
        values = request.values
        idcargo_empleado = values.get('idcargo_empleado')
        return cargo_empleado.get_cargo_empleado(idcargo_empleado, app)

    @app.route('/cargos_empleados/list_organigrama', methods = ['GET'])
    def cargos_empleado_list_organigrama():
        return cargo_empleado.list_organigrama(app)
