import operaciones as op
import validacion_conversion_muestra as f

def sistemaNotas():
    print("""
***BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS***""")
    #Validación de numero de alumnos y numero de notas por alumno
    validacion1 = True
    while validacion1 == True:
        numAlu = input("Ingrese el numero de alumnos: ")
        info = f.validar_numero(numAlu)
        numeroAlumnos = info[0]
        validacion1 = info[1]
    validacion2 = True
    while validacion2 == True:
        numNot = input("Ingrese el número de notas a ingresar: ")
        info2 = f.validar_numero(numNot)
        numeroNotas = info2[0]
        validacion2 = info2[1]
    
    #Se adiciona 1 a cada parámetro para usar el range iniciado en 1
    numeroAlumnos = numeroAlumnos + 1
    numeroNotas = numeroNotas + 1 
    alumnos = []
    #Se almacenan y validan los datos de los alumnos, especialmente las notas
    for j in range(1, numeroAlumnos):
        print("Alumno: ", str(j))
        alumno = []
        codigo = "000000" + str(j)
        alumno.append(codigo)
        nombre = input("Nombre: ")
        alumno.append(nombre)
        apellido = input("Apellido: ")
        alumno.append(apellido)
        notas = []
        #Validación y almacenado de notas
        for i in range(1, numeroNotas):
            again = True
            while again == True: 
                nota = input(f"Ingrese nota {i}: ")
                datos = f.validar_notas(i, nota)
                again = datos[1]
                if again == False:
                    notas.append(datos[0])
        #Se agregan los elementos obtenidos a una lista principal llamada alumnos
        alumno.append(notas)
        alumno.append(op.promedioNotas(notas))
        alumno.append(op.notaMayor(notas))
        alumno.append(op.notaMenor(notas))        
        alumnos.append(alumno)
    print("""
***REGISTRO FINALIZADO***""")

    #LISTA: Impresión de alumnos registrados con sus respectivos atributos (datos y notas)
    f.mostrar_lista(alumnos)
    #Conversión de lista alumnos a un diccionario
    #dict_alumnos = f.lista_to_diccionario(alumnos)
    #DICCIONARIO: Impresión de alumnos registrados con sus respectivos atributos (datos y notas)
    #f.mostrar_diccionario(dict_alumnos)