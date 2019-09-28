from clases.docente import Docente
from clases.alumno import Alumno
from clases.conexion import Conexion

class Colegio():
    __conexion = Conexion()
    __con = __conexion.conn

    def agregarPersona(self, objeto, tipo):
        try:
            nomColeccion = "personas"
            if tipo == "alumno":
                alumno = objeto
                diccionario = {"codigo": alumno.codigo, "tipo": tipo, "nombre": alumno.nombre, "dni": alumno.dni, "edad": alumno.edad, "notas": alumno.notas, "promedio": alumno.getPromedio(), "notamax": alumno.getNotaMaxima(), "notamin": alumno.getNotaMinima()}
            elif tipo == "docente":
                docente = objeto
                diccionario = {"codigo": docente.codigo, "tipo": tipo, "nombre": docente.nombre, "dni": docente.dni, "edad": docente.edad}
            coleccion = self.__conexion.connect()[nomColeccion]
            coleccion.insert_one(diccionario)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            self.__conexion.close()
    
    def listarPersonas(self, tipo):
        try:
            nomColeccion = "personas"
            coleccion = self.__conexion.connect()[nomColeccion]
            query = {"tipo": tipo}
            personas = coleccion.find(query)
            for persona in personas:
                print(persona)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            self.__conexion.close()

    def obtenerCodigoPersona(self, codigoBuscar):
        try:
            nomColeccion = "personas"
            coleccion = self.__conexion.connect()[nomColeccion]
            query = {"codigo": codigoBuscar}
            personas = coleccion.find(query)
            for persona in personas:
                return persona.codigo
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            self.__conexion.close()
    
    def actualizarPersona(self, codigoActualizar, objeto, tipo):
        try:
            nomColeccion = "personas"
            coleccion = self.__conexion.connect()[nomColeccion]
            query = {"codigo": codigoActualizar}
            if tipo == "alumno":
                queryUpdate = {"$set": {"nombre": objeto.nombre, "dni": objeto.dni, "edad": objeto.edad, "notas": objeto.notas, "promedio": objeto.getPromedio(), "notamax": objeto.getNotaMaxima(), "notamin": objeto.getNotaMinima()}}
            elif  tipo == "docente":
                queryUpdate = {"$set": {"nombre": objeto.nombre, "dni": objeto.dni, "edad": objeto.edad}}
            coleccion.update(query, queryUpdate, upsert=False)
            print("Registro Actualizado")
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            self.__conexion.close()

    def eliminarPersona(self, codigoEliminar):
        try:
            nomColeccion = "personas"
            coleccion = self.__conexion.connect()[nomColeccion]
            query = {"codigo": codigoEliminar}
            coleccion.remove(query)
            print("Registro eliminado")
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            self.__conexion.close()