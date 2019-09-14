from personas import Alumno, Docente
from archivos import Archivo
import validacion as v

def sistemaNotas():
    print("""
***BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS***""")
    #Validación de numero de docentes
    validacion4 = True
    while validacion4 == True:
        numDoc = input("Ingrese el numero de docentes: ")
        info4 = v.validar_numero(numDoc)
        numeroDocentes = info4[0]
        validacion4 = info4[1]

    #Validación de numero de alumnos y numero de notas por alumno
    validacion1 = True
    while validacion1 == True:
        numAlu = input("Ingrese el numero de alumnos: ")
        info = v.validar_numero(numAlu)
        numeroAlumnos = info[0]
        validacion1 = info[1]

    validacion2 = True
    while validacion2 == True:
        numNot = input("Ingrese el número de notas a ingresar: ")
        info2 = v.validar_numero(numNot)
        numeroNotas = info2[0]
        validacion2 = info2[1]
    
    #Se adiciona 1 a cada parámetro para usar el range iniciado en 1
    numeroAlumnos = numeroAlumnos + 1
    numeroNotas = numeroNotas + 1 
    numeroDocentes = numeroDocentes + 1
    #Se almacenan y validan los datos de los docentes
    for i in range(1, numeroDocentes):
        print("Docente: ", str(i))
        nombreDocente = input("Nombre: ")
        DNIDocente = input("DNI: ")
        validacion5 = True
        while validacion5 == True:
            edadDocente = input("Edad: ")
            info5 = v.validar_numero(edadDocente)
            edadDocente = info5[0]
            validacion5 = info5[1]
    
    #Se almacenan y validan los datos de los alumnos, especialmente las notas
    for j in range(1, numeroAlumnos):
        print("Alumno: ", str(j))
        nombre = input("Nombre: ")
        DNI = input("DNI: ")
        validacion3 = True
        while validacion3 == True:
            edad = input("Edad: ")
            info3 = v.validar_numero(edad)
            edad = info3[0]
            validacion3 = info3[1]
        notas = []
        #Validación y almacenado de notas
        for k in range(1, numeroNotas):
            again = True
            while again == True: 
                nota = input(f"Ingrese nota {k}: ")
                datos = v.validar_notas(k, nota)
                again = datos[1]
                if again == False:
                    notas.append(datos[0])
        #Se agregan los elementos obtenidos a una lista principal llamada alumnos
        alumno = Alumno(nombre, DNI, edad, notas)
        docente = Docente(nombreDocente, DNIDocente, edadDocente)
        archivo = Archivo("Alumnos.txt", "Docentes.txt")
        archivo.agregarAlumno(alumno)
        archivo.agregarDocente(docente)

    print("""
***REGISTRO FINALIZADO***""")

sistemaNotas()