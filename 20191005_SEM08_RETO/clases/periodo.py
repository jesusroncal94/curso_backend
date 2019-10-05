from clases.conexion import Conexion


class Periodo():
    __conn = Conexion()

    def __init__(self, periodo):
        self.periodo = periodo

    def agregarPeriodo(self, periodo):
        try:
            sql = """INSERT INTO periodos(periodo)
            VALUES('{}')""".format(periodo.periodo)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def listarPeriodos(self):
        try:
            sql = "SELECT * FROM periodos"
            cursor = self.__conn.ejecutarSentencia(sql)
            filas = cursor.fetchall()
            for fila in filas:
                print("""Periodo: {} \n""".format(fila[1]))
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def obtenerPeriodo(self, idPeriodo):
        try:
            sql = """SELECT * FROM periodos
            WHERE idPeriodo = {}""".format(idPeriodo)
            cursor = self.__conn.ejecutarSentencia(sql)
            lista = cursor.fetchone()
            periodo = Periodo(lista[1])
            return periodo
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def actualizarPeriodo(self, periodo, idPeriodo):
        try:
            sql = """UPDATE periodos SET periodo = {}
            WHERE idPeriodo = {}""".format(periodo.periodo, idPeriodo)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def eliminarPeriodo(self, idPeriodo):
        try:
            sql = """DELETE FROM periodos
            WHERE idPeriodo = {}""".format(idPeriodo)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()
