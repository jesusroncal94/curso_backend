from database.config import Conexion
from helpers import helper


class Empleado():
    def __init__(self, nombres = None, apellidos = None, dni = None, edad = None):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    def add_empleado(self, empleado, app):
        try:
            conn = Conexion()
            query = f'''
                    INSERT INTO empleados (nombres, apellidos, dni, edad)
                    VALUES
                    ('{empleado.nombres}', '{empleado.apellidos}', '{empleado.dni}', {empleado.edad})
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agregó el empleado: {empleado.nombres} {empleado.apellidos}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
            conn.rollback()
        finally:
            conn.cerrar_conexion()

    def list_empleados(self, app):
        diccionario_empleado = {}
        diccionario_empleados = {}
        lista = []
        try:
            conn = Conexion()
            query = f'''SELECT * FROM empleados'''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                diccionario_empleado = {
                    'idempleado': fila[0],
                    'nombres': fila[1],
                    'apellidos': fila[2],
                    'dni': fila[3],
                    'edad': fila[4]}
                lista.append(diccionario_empleado)
            diccionario_empleados['empleados'] = lista
            message = '''Lista de empleados'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_empleados)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def update_empleado(self, idempleado, empleado, app):
        try:
            conn = Conexion()
            query = f'''
                    UPDATE empleados
                    SET nombres = '{empleado.nombres}',
                        apellidos = '{empleado.apellidos}',
                        dni = '{empleado.dni}',
                        edad = {empleado.edad}
                    WHERE idempleado = {idempleado}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el empleado de ID: {idempleado}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def delete_empleado(self, idempleado, app):
        try:
            conn = Conexion()
            query = f'''
                    DELETE FROM empleados
                    WHERE idempleado = {idempleado}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el empleado de ID: {idempleado}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def get_empleado(self, idempleado, app):
        diccionario_empleado = {}
        try:
            conn = Conexion()
            query = f'''SELECT * FROM empleados
                    WHERE idempleado = {idempleado}
                    '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            diccionario_empleado = {
                'idempleado': fila[0],
                'nombres': fila[1],
                'apellidos': fila[2],
                'dni': fila[3],
                'edad': fila[4]}
            message = f'''empleado ID: {idempleado}'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_empleado)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
