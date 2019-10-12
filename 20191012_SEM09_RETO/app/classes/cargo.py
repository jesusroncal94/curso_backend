from database.config import Conexion
from helpers import helper


class Cargo():
    def __init__(self, descripcion = None, idcargo = None):
        self.descripcion = descripcion
        self.idecargo = idcargo

    def add_cargo(self, cargo, app):
        try:
            conn = Conexion()
            query = f'''
                    INSERT INTO cargos (descripcion, idcargo)
                    VALUES
                    ('{cargo.descripcion}', {cargo.idarea})
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agregó el cargo: {cargo.descripcion}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
            conn.rollback()
        finally:
            conn.cerrar_conexion()

    def list_cargos(self, app):
        diccionario_cargo = {}
        diccionario_cargos = {}
        lista = []
        try:
            conn = Conexion()
            query = f'''SELECT * FROM cargos'''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                diccionario_cargo = {
                    'idcargo': fila[0],
                    'descripcion': fila[1],
                    'idarea': fila[2]}
                lista.append(diccionario_cargo)
            diccionario_cargos['cargos'] = lista
            message = '''Lista de cargos'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_cargos)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def update_cargo(self, idcargo, cargo, app):
        try:
            conn = Conexion()
            query = f'''
                    UPDATE cargos
                    SET descripcion = '{cargo.descripcion}',
                        idarea = {cargo.idarea}
                    WHERE idcargo = {idcargo}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el cargo de ID: {idcargo}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def delete_cargo(self, idcargo, app):
        try:
            conn = Conexion()
            query = f'''
                    DELETE FROM cargos
                    WHERE idcargo = {idcargo}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el cargo de ID: {idcargo}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def get_cargo(self, idcargo, app):
        diccionario_cargo = {}
        try:
            conn = Conexion()
            query = f'''SELECT * FROM cargos
                    WHERE idcargo = {idcargo}
                    '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            diccionario_cargo = {
                'idcargo': fila[0],
                'descripcion': fila[1],
                'idarea': fila[2]}
            message = f'''cargo ID: {idcargo}'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_cargo)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
