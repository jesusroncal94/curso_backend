import validacion as v
from clases.docente import Docente
from clases.alumno import Alumno
from clases.colegio import Colegio

#AGREGAR
print("*** SISTEMA DE REGISTRO DE DOCENTES, ALUMNOS Y NOTAS ***")
registrarDocentes()
registrarAlumnos()
print("***REGISTRO FINALIZADO***")

#LISTAR
print("***LISTA DE ALUMNOS***")
listarAlumnos()
print("***LISTA DE DOCENTES***")
listarDocentes()

#ACTUALIZAR ALUMNO
alumnoActualizado = Alumno("", "Jesus E.", "48082945", "89", [18, 19, 20])
actualizarPersona("A12345678", alumnoActualizado, "alumno")
#ACTUALIZAR DOCENTE
docenteActualizado = Docente("", "Jose A", "99999999", "100")
actualizarPersona("D12345678", docenteActualizado, "docente")

#ELIMINAR
eliminarPersona("A12345678")
eliminarPersona("D12345678")


def registrarDocentes():
    print("***REGISTRO DE DOCENTES***")
    #Número de docentes a registrar
    peticion = "Ingrese número de docentes a registrar: "
    tipoValidacion = 0
    numeroDocentes = v.validarNumero(tipoValidacion, peticion)
    #Registro de n docentes
    for i in range(1, numeroDocentes+1):       
        print(f"Docente nro. {i}")
        datosPersona = solicitarDatosPersona()
        nombre = datosPersona[0]
        DNI = datosPersona[1]
        codigo = f"D{DNI}"
        edad = datosPersona[2]
        docente = Docente(codigo, nombre, DNI, edad)
        nuevoDocente = Colegio()
        nuevoDocente.agregarPersona(docente, "docente")

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
    #Registro de n alumnos
    for i in range(1, numeroAlumnos+1):
        print(f"Alumno nro. {i}: ")
        datosPersona = solicitarDatosPersona()
        nombre = datosPersona[0]
        DNI = datosPersona[1]
        codigo = f"A{DNI}"
        edad = datosPersona[2]
        #Notas
        notas = []
        for j in range(1, numeroNotas+1):
            peticion = f"Ingrese nota {j}: "
            tipoValidacion = 1
            notas.append(v.validarNumero(tipoValidacion, peticion))
        alumno = Alumno(codigo, nombre, DNI, edad, notas)
        nuevoAlumno = Colegio()
        nuevoAlumno.agregarPersona(alumno, "alumno")

def solicitarDatosPersona():
    nombre = input("Ingrese nombre completo: ")
    DNI = input("Ingrese DNI: ")
    peticion = "Ingrese edad: "
    tipoValidacion = 0
    edad = v.validarNumero(tipoValidacion, peticion)
    datos = [nombre, DNI, edad]
    return datos

def listarAlumnos():
    alumnos = Colegio()
    alumnos.listarPersonas("alumno")

def listarDocentes():
    alumnos = Colegio()
    alumnos.listarPersonas("docente")

def actualizarPersona(codigo, objeto, tipo):
    persona = Colegio()
    persona.actualizarPersona(codigo, objeto, tipo)

def eliminarPersona(codigo):
    persona = Colegio()
    persona.eliminarPersona(codigo)