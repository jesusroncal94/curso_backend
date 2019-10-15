from database.config import Conexion
from helpers import helper


class Area():
    def __init__(self, descripcion = None, relacion = None):
        self.descripcion = descripcion
        self.relacion = relacion

    def add_area(self, area, app):
        try:
            conn = Conexion()
            query = f'''
                    INSERT INTO areas (descripcion, relacion)
                    VALUES
                    ('{area.descripcion}', {area.relacion})
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agregó el área: {area.descripcion}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
            conn.rollback()
        finally:
            conn.cerrar_conexion()

    def list_areas(self, app):
        diccionario_area = {}
        diccionario_areas = {}
        lista = []
        try:
            conn = Conexion()
            query = f'''SELECT * FROM areas'''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                diccionario_area = {
                    'idarea': fila[0],
                    'descripcion': fila[1],
                    'relacion': fila[2]}
                lista.append(diccionario_area)
            diccionario_areas['areas'] = lista
            message = '''Lista de áreas'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_areas)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def update_area(self, idarea, area, app):
        try:
            conn = Conexion()
            query = f'''
                    UPDATE areas
                    SET descripcion = '{area.descripcion}',
                        relacion = {area.relacion}
                    WHERE idarea = {idarea}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el área de ID: {idarea}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def delete_area(self, idarea, app):
        try:
            conn = Conexion()
            query = f'''
                    DELETE FROM areas
                    WHERE idarea = {idarea}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el área de ID: {idarea}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def get_area(self, idarea, app):
        diccionario_area = {}
        try:
            conn = Conexion()
            query = f'''SELECT * FROM areas
                    WHERE idarea = {idarea}
                    '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            diccionario_area = {
                'idarea': fila[0],
                'descripcion': fila[1],
                'relacion': fila[2]}
            message = f'''Area ID: {idarea}'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_area)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()