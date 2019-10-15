from flask import request
from app.classes.empleado import Empleado


empleado = Empleado()

def routes(app):    
    @app.route('/empleados/add', methods = ['POST'])
    def empleados_add():
        values = request.values
        empleado.nombres = values.get('nombres')
        empleado.apellidos = values.get('apellidos')
        empleado.dni = values.get('dni')
        empleado.edad = values.get('edad')
        return empleado.add_empleado(empleado, app)

    @app.route('/empleados/list', methods = ['GET'])
    def empleados_list():
        return empleado.list_empleados(app)

    @app.route('/empleados/update', methods = ['PUT'])
    def empleados_update():
        values = request.values
        idempleado = values.get('idempleado')
        empleado.nombres = values.get('nombres')
        empleado.apellidos = values.get('apellidos')
        empleado.dni = values.get('dni')
        empleado.edad = values.get('edad')
        return empleado.update_empleado(idempleado, empleado, app)

    @app.route('/empleados/delete', methods = ['DELETE'])
    def empleados_delete():
        values = request.values
        idempleado = values.get('idempleado')
        return empleado.delete_empleado(idempleado, app)

    @app.route('/empleados/get/', methods = ['POST'])
    def empleados_get():
        values = request.values
        idempleado = values.get('idempleado')
        return empleado.get_empleado(idempleado, app)
