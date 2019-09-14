from personas import Alumno, Docente

class Archivo():
    def __init__(self, archivoAlumno, archivoDocente=None):
        self.archivoAlumno = archivoAlumno
        self.archivoDocente = archivoDocente
    
    def reporteAlumnos(self):
        try:
            archivo = open(self.archivoAlumno, 'r')
            for line in archivo:
                print(line)
        except Exception as error:
            print(f"Error al abrir archivo: {str(error)}")
        else:
            archivo.close()
    
    def reporteProfesores(self):
        try:
            archivo = open(self.archivoDocente, 'r')
            for line in archivo:
                print(line)
        except Exception as error:
            print(f"Error al abrir archivo: {str(error)}")
        else:
            archivo.close()
    
    def agregarAlumno(self, Alumno):
        try:
            archivo = open(self.archivoAlumno, 'a')
            alumno = "Alumno: {}, Nota máxima: {}, Nota mínima: {}, Promedio: {}".format(Alumno.getNombre, Alumno.getNotaMax, Alumno.getNotaMin, Alumno.getPromedio)
            archivo.write(alumno)
        except Exception as error:
            print(f"Error al agregar alumno: {str(error)}")
        else:
            archivo.close()
            print(archivo)
    
    def agregarDocente(self, Docente):
        try:
            archivo = open(self.archivoDocente, 'a')
            alumno = "Docente: {}, DNI: {}, Edad: {}".format(Docente.getNombre, Docente.getDni, Docente.getEdad)
            archivo.write(alumno)
        except Exception as error:
            print(f"Error al agregar docente: {str(error)}")
        else:
            archivo.close()
            print(archivo)