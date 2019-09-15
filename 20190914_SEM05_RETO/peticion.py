import validacion as v
from clases.docente import Docente
from clases.alumno import Alumno
from clases.archivo import Archivo

archivoAlumno = "Alumnos.txt"
archivoDocente = "Docentes.txt"
archivoReporteGeneral = "ReporteGeneral.txt"

def sistemaNotas():
    print("*** SISTEMA DE REGISTRO DE DOCENTES, ALUMNOS Y NOTAS ***")
    registrarDocentes()
    registrarAlumnos()
    print("***REGISTRO FINALIZADO***")
    mostrarDocentes()
    mostrarAlumnos()
    mostrarReporteGeneral()

def registrarDocentes():
    print("***REGISTRO DE DOCENTES***")
    #Número de docentes a registrar
    peticion = "Ingrese número de docentes a registrar: "
    tipoValidacion = 0
    numeroDocentes = v.validarNumero(tipoValidacion, peticion)
    
    #Obtener el último código de docente ingresado
    ultimoCodigoDocente = 0
    try:
        fichero = open(archivoDocente, 'r')
        ultimoCodigoDocente = len(fichero.readlines())
    except Exception as e:
        print(f"Error: {str(e)}")
    else:
        fichero.close()
    
    #Registro de n docentes
    for i in range(1, numeroDocentes+1):
        #Codigo generado de docente
        codigo = f"D{ultimoCodigoDocente+1}"
        print(f"Ingreso nro. {i}: Docente {codigo}")
        datosPersona = solicitarDatosPersona()
        nombre = datosPersona[0]
        DNI = datosPersona[1]
        edad = datosPersona[2]
        docente = Docente(codigo, nombre, DNI, edad)
        archivo = Archivo(archivoDocente=archivoDocente)
        archivo.agregarDocente(docente)
        ultimoCodigoDocente += 1

def registrarAlumnos():
    print("***REGISTRO DE ALUMNOS Y NOTAS***")
    #Número de alumnos a registrar
    peticion = "Ingrese número de alumnos a registrar: "
    tipoValidacion = 0
    numeroAlumnos = v.validarNumero(tipoValidacion, peticion)
    #Número de notas a registrar por alumno
    peticion = "Ingrese número de notas a registrar por alumno: "
    tipoValidacion = 0
    numeroNotas = v.validarNumero(tipoValidacion, peticion)
    
    #Obtener el último código de alumno ingresado
    ultimoCodigoAlumno = 0
    try:
        fichero = open(archivoAlumno, 'r')
        ultimoCodigoAlumno = len(fichero.readlines())
    except Exception as e:
        print(f"Error: {str(e)}")
    else:
        fichero.close()
    
    #Registro de n alumnos
    for i in range(1, numeroAlumnos+1):
        codigo = f"A{ultimoCodigoAlumno+1}"
        print(f"Ingreso nro. {i}: Alumno {codigo}")
        datosPersona = solicitarDatosPersona()
        nombre = datosPersona[0]
        DNI = datosPersona[1]
        edad = datosPersona[2]
        #Notas
        notas = []
        for i in range(1, numeroNotas+1):
            peticion = f"Ingrese nota {i}: "
            tipoValidacion = 1
            notas.append(v.validarNumero(tipoValidacion, peticion))
        alumno = Alumno(codigo, nombre, DNI, edad, notas)
        archivo = Archivo(archivoAlumno=archivoAlumno)
        archivo.agregarAlumno(alumno)
        ultimoCodigoAlumno += 1
    
def solicitarDatosPersona():
    nombre = input("Ingrese nombre completo: ")
    DNI = input("Ingrese DNI: ")
    peticion = "Ingrese edad: "
    tipoValidacion = 0
    edad = v.validarNumero(tipoValidacion, peticion)
    datos = [nombre, DNI, edad]
    return datos

def mostrarAlumnos():
    alumnos = Archivo(archivoAlumno=archivoAlumno)
    return alumnos.reporteAlumnos()

def mostrarDocentes():
    docentes = Archivo(archivoDocente=archivoDocente)
    return docentes.reporteDocentes()

def mostrarReporteGeneral():
    reporteGeneral = Archivo(archivoAlumno=archivoAlumno, archivoDocente=archivoDocente)
    reporteGeneral.reporteGeneral(archivoReporteGeneral)