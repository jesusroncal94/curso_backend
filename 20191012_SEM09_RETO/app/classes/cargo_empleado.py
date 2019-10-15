from database.config import Conexion
from helpers import helper


class Cargo_empleado():
    def __init__(self, idempleado = None, idcargo = None):
        self.idempleado = idempleado
        self.idcargo = idcargo

    def add_cargo_empleado(self, cargo_empleado, app):
        try:
            conn = Conexion()
            query = f'''
                    INSERT INTO cargos_empleado (idempleado, idcargo)
                    VALUES
                    ({cargo_empleado.idempleado}, {cargo_empleado.idcargo})
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agregó el cargo_empleado: {cargo_empleado.idempleado}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
            conn.rollback()
        finally:
            conn.cerrar_conexion()

    def list_cargos_empleados(self, app):
        diccionario_cargo_empleado = {}
        diccionario_cargo_empleados = {}
        lista = []
        try:
            conn = Conexion()
            query = f'''SELECT a.idcargo_empleado, b.idempleado, b.nombres,
                    b.apellidos, c.idcargo, c.descripcion, d.idarea, d.descripcion
                    FROM cargos_empleado as a
                    INNER JOIN empleados as b ON a.idempleado = b.idempleado
                    INNER JOIN cargos as c ON a.idcargo = c.idcargo
                    INNER JOIN areas as d ON c.idarea = d.idarea'''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                diccionario_cargo_empleado = {
                    'idcargo_empleado': fila[0],
                    'idempleado': fila[1],
                    'nombres': fila[2],
                    'apellidos': fila[3],
                    'idcargo': fila [4],
                    'cargo': fila[5],
                    'idarea': fila[6],
                    'area': fila[7]}
                lista.append(diccionario_cargo_empleado)
            diccionario_cargo_empleados['cargos_empleado'] = lista
            message = '''Lista de cargos_empleados'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_cargo_empleados)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def update_cargo_empleado(self, idcargo_empleado, cargo_empleado, app):
        try:
            conn = Conexion()
            query = f'''
                    UPDATE cargos_empleado
                    SET idempleado = '{cargo_empleado.idempleado}',
                        idcargo = {cargo_empleado.idcargo}
                    WHERE idcargo_empleado = {idcargo_empleado}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el cargo_empleado de ID: {idcargo_empleado}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def delete_cargo_empleado(self, idcargo_empleado, app):
        try:
            conn = Conexion()
            query = f'''
                    DELETE FROM cargos_empleado
                    WHERE idcargo_empleado = {idcargo_empleado}
                    '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el cargo_empleado de ID: {idcargo_empleado}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def get_cargo_empleado(self, idcargo_empleado, app):
        diccionario_cargo_empleado = {}
        try:
            conn = Conexion()
            query = f'''SELECT * FROM cargos_empleado
                    WHERE idcargo_empleado = {idcargo_empleado}
                    '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            diccionario_cargo_empleado = {
                'idcargo_empleado': fila[0],
                'idempleado': fila[1],
                'idcargo': fila[2]}
            message = f'''cargo_empleado ID: {idcargo_empleado}'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_cargo_empleado)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def list_organigrama(self, app):
        organigrama = []
        diccionario_organigrama = {}
        empleados_lista = []
        try:
            conn = Conexion()
            query = f'''SELECT a.idarea, a.descripcion, a.relacion
                    FROM areas as a'''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                #Query de jefes de cada area
                conn2 = Conexion()
                query2 = f'''SELECT b.idempleado, CONCAT(b.nombres, ' ', b.apellidos), c.descripcion, c.relacion
                    FROM cargos_empleado as a
                    INNER JOIN empleados as b ON a.idempleado = b.idempleado
                    INNER JOIN cargos as c ON a.idcargo = c.idcargo
                    INNER JOIN areas as d ON c.idarea = d.idarea
                    WHERE d.idarea = {fila[0]}'''
                cursor2 = conn2.ejecutar_sentencia(query2)
                empleados = cursor2.fetchall()
                for empleado in empleados:
                    empleado_dict = {
                        'idempleado': empleado[0],
                        'nombres_completos': empleado[1], 
                        'cargo': empleado[2], 
                        'relacion': empleado[3]
                    }
                    empleados_lista.append(empleado_dict)
                diccionario_empleados = self.create_tree(empleados_lista, 'idempleado', 'relacion', 'empleados')
                #Diccionario que almacena los datos de un area con sus respectivos jefe y empleados
                registro = {
                    'idarea': fila[0], 
                    'area': fila[1], 
                    'relacion': fila[2],
                    'jefe': diccionario_empleados
                }
                empleados_lista = []
                organigrama.append(registro)
            diccionario_organigrama = self.create_tree(organigrama, 'idarea', 'relacion', 'subareas')
            message = '''ORGANIGRAMA'''
            print(message)
            return helper.handler_response(app, 201, message, diccionario_organigrama)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
            conn2.cerrar_conexion()

    def create_tree(self, tree, idchild, idparent, tagchild):
        #Convertir estructura lista-diccionario a diccionario completamente
        tree_dict = dict((area[idchild], area) for area in tree)
        #Recorrido y agregado de areas y subareas a organigrama
        for area in tree:
            if area[idparent] != False:
                parent = tree_dict[area[idparent]]
                parent.setdefault(tagchild, []).append(area)
        #Ordenado de areas y subareas anidados
        tree = [area for area in tree if area[idparent] == False]
        return tree[0]
