from clases.docente import Docente
from clases.alumno import Alumno

class Archivo():
    def __init__(self, archivoAlumno = None, archivoDocente = None):
        self.archivoAlumno = archivoAlumno
        self.archivoDocente = archivoDocente
    
    def reporteAlumnos(self):
        try:
            file = open(self.archivoAlumno, 'r')
            for line in file.readlines():
                print(line)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            file.close()
    
    def reporteDocentes(self):
        try:
            file = open(self.archivoDocente, 'r')
            for line in file.readlines():
                print(line)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            file.close()
    
    def reporteGeneral(self, reporte):
        #Reporte Alumnos.txt y Docentes.txt agregados a ReporteGeneral.txt
        try:
            reporteGeneral = open(reporte, 'w')
            archivoDocente = open(self.archivoDocente, 'r')
            archivoAlumno = open(self.archivoAlumno, 'r')
            reporteGeneral.write("***DOCENTES***\n")
            for lineDocente in archivoDocente.readlines():
                reporteGeneral.write(f"{lineDocente}")
            reporteGeneral.write("\n\n***ALUMNOS***\n")
            for lineAlumno in archivoAlumno.readlines():
                reporteGeneral.write(f"{lineAlumno}")
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            reporteGeneral.close()
        #Mostrando reporte ReporteGeneral.txt
        try:
            file = open(reporte, 'r')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            file.close()

    def agregarAlumno(self, alumno):
        try:
            file = open(self.archivoAlumno, 'a')
            nuevoAlumno = f"{alumno.mostrarDatos()}\n"
            file.write(nuevoAlumno)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            file.close()
    
    def agregarDocente(self, docente):
        try:
            file = open(self.archivoDocente, 'a')
            nuevoDocente = f"{docente.mostrarDatos()}\n"
            file.write(nuevoDocente)
        except Exception as e:
            print(f"Error: {str(e)}")
        else:
            file.close()