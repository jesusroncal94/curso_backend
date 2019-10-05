from clases.persona import Persona
from clases.conexion import Conexion


class Alumno(Persona):
    __conn = Conexion()

    def __init__(self, dni, nombres, apellidos, edad, notas = []):
        super().__init__(dni, nombres, apellidos, edad)
        self.notas = notas
    
    def agregaralumno(self, alumno):
        try:
            sql = """INSERT INTO alumnos(dni, nombres, apellidos, edad)
            VALUES('{}', '{}', '{}', {})""".format(alumno.dni, alumno.nombres, alumno.apellidos, alumno.edad)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def listaralumnos(self):
        try:
            sql = "SELECT * FROM alumnos"
            cursor = self.__conn.ejecutarSentencia(sql)
            filas = cursor.fetchall()
            for fila in filas:
                print("""DNI: {}, Nombres: {}, Apellidos: {}, Edad: {} \n""".format(fila[1], fila[2], fila[3], fila[4]))
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def obteneralumno(self, idalumno):
        try:
            sql = """SELECT * FROM alumnos
            WHERE idalumno = {}""".format(idalumno)
            cursor = self.__conn.ejecutarSentencia(sql)
            fila = cursor.fetchone()
            alumno = Alumno(fila[1], fila[2], fila[3], fila[4])
            return alumno
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def actualizaralumno(self, alumno, idalumno):
        try:
            sql = """UPDATE alumnos SET dni = {}, nombres = {}, apellidos = {}, edad = {}
            WHERE idalumno = {}""".format(alumno.dni, alumno.nombres, alumno.apellidos, alumno.edad, idalumno)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()

    def eliminaralumno(self, idalumno):
        try:
            sql = """DELETE FROM alumnos
            WHERE idalumno = {}""".format(idalumno)
            self.__conn.ejecutarSentencia(sql)
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.__conn.rollback()
        else:
            self.__conn.cerrarConexion()
    
    def obtenerNotaMax(self):
        return max(self.notas)
    
    def obtenerNotaMin(self):
        return min(self.notas)
    
    def obtenerPromedio(self):
        for nota in self.notas:
            suma += nota
        promedio = suma / len(self.notas)
        return promedio

alumnoagregar = Alumno("48082945", "Jesus Enrique", "Roncal Huatta", 25)
alumnoagregar.agregaralumno(alumnoagregar)
alumnoagregar.listaralumnos()