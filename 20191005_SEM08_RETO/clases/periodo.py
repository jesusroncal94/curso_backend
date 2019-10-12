from clases.conexion import Conexion
import pymysql

class Periodo():
    def __init__(self, periodo):
        self.periodo = periodo

    def agregarPeriodo(self, periodo):
        try:
            sql = f"""INSERT INTO periodos(periodo)
            VALUES('{periodo.periodo}')"""
            conexion = Conexion()
            cliente = conexion.cliente
            cursor = cliente.cursor()
            cursor.execute(sql)
            cliente.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            cliente.rollback()
        else:
            cliente.close()

    def listarPeriodos(self):
        try:
            sql = "SELECT * FROM periodos"
            self.__cursor.execute(sql)
            filas = self.__cursor.fetchall()
            for fila in filas:
                print(f"ID: {str(fila[0])}, Periodo: {fila[1]} \n")
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__cliente.rollback()
        else:
            self.__cliente.close()

    def obtenerPeriodo(self, idPeriodo):
        try:
            sql = f"""SELECT * FROM periodos
            WHERE idPeriodo = {idPeriodo}"""
            cursor = self.__cursor.execute(sql)
            lista = cursor.fetchone()
            periodo = Periodo(lista[1])
            return periodo
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__cliente.rollback()
        else:
            self.__cliente.close()

    def actualizarPeriodo(self, periodo, idPeriodo):
        try:
            sql = f"UPDATE periodos SET periodo = '{periodo.periodo}' WHERE idPeriodo = '{idPeriodo}'"
            self.__cursor.execute(sql)
            self.__cliente.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__cliente.rollback()
        else:
            self.__cliente.close()

    def eliminarPeriodo(self, idPeriodo):
        try:
            sql = f"""DELETE FROM periodos
            WHERE idPeriodo = {idPeriodo}"""
            self.__cursor.execute(sql)
            self.__cliente.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__cliente.rollback()
        else:
            self.__cliente.close()

periodo = Periodo("20190709")
periodo.agregarPeriodo(periodo)
periodo.listarPeriodos()
periodo.actualizarPeriodo(periodo, 1)
periodo.eliminarPeriodo(1)
