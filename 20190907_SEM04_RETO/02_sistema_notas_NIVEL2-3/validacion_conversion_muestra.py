"""
FORMATO DE LISTA ALUMNOS
alumnos = [
            [codigo1, nombre, apellido, notas[nota1, nota2, nota3, ..., nota n]],
            [codigo2, nombre, apellido, notas[nota1, nota2, nota3, ..., nota n]],
            [codigo3, nombre, apellido, notas[nota1, nota2, nota3, ..., nota n]], 
            .
            .
            .
            [codigon, nombre, apellido, notas[nota1, nota2, nota3, ..., nota n]],
          ]
"""
#Valida un numero y retorna una lista, que incluye el numero validado junto con un estado 
# para usarlo en un while
def validar_numero(n):
    try:
        numero = int(n)
        again = False
        datos = [numero, again]
        return datos
    except ValueError:
        print("Ingrese solo datos numéricos enteros.")
        numero = []
        again = True
        datos = [numero, again]
        return datos

#Valida la lista de notas y retorna una lista, que incluye las notas validadas (numeros entre el 0 y 20) 
#junto con un estado para usarlo en un while
def validar_notas(i, nota):
    try:
        nota = float(nota)
        if nota >= 0 and nota <= 20:
            again = False
            datos = [nota, again]
            return datos
        else:
            print(f"¡Ingrese nota{i} nuevamente!")
            print("Se aceptan solo valores numéricos del 0 al 20.")
            nota = ""
            again = True
            datos = [nota, again]
            return datos
    except ValueError:
        print(f"¡Ingrese nota{i} nuevamente!")
        print("Se aceptan solo valores numéricos del 0 al 20.")
        nota = ""
        again = True
        datos = [nota, again]
        return datos

#Devuelve impresión de una lista de los alumnos
def mostrar_lista(alumnos):
    a = len(alumnos)
    print("***REPORTE DE NOTAS: CURSO BACKEND DEVELOPER***")
    for x in range(0, a):
        print("Código: ", alumnos[x][0], end=', ')
        print("Nombre completo: ", alumnos[x][1], alumnos[x][2], end=', ')
        print("Notas: ", alumnos[x][3], end=', ')
        print("Promedio: ", alumnos[x][4], end=', ')
        print("Max: ", alumnos[x][5], end=', ')
        print("Min: ", alumnos[x][6])

#Convierte de una lista a un diccionario
def lista_to_diccionario(alumnos):
    dict_alumnos = {}
    a = len(alumnos)
    for x in range(0, a):
        codigo = alumnos[x][0]
        nombreCompleto = alumnos[x][1] + " " + alumnos[x][2]
        notas = alumnos[x][3]
        promedio = alumnos[x][4]
        mayor = alumnos[x][5]
        menor = alumnos[x][6]
        dict_alumnos[codigo] = {}
        dict_alumnos[codigo]["nombreCompleto"] = nombreCompleto
        dict_alumnos[codigo]["notas"] = notas
        dict_alumnos[codigo]["promedio"] = promedio
        dict_alumnos[codigo]["mayor"] = mayor
        dict_alumnos[codigo]["menor"] = menor
    return dict_alumnos

#Devuelve impresión de un diccionario de los alumnos
def mostrar_diccionario(alumnos):
    print("***REPORTE DE NOTAS: CURSO BACKEND DEVELOPER***")
    for clave, valor in alumnos.items():
        print("Código: ", clave, end=', ')
        print("Nombre completo: ", alumnos[clave]["nombreCompleto"], end=', ')
        print("Notas: ", alumnos[clave]["notas"], end=', ')
        print("Promedio: ", alumnos[clave]["promedio"], end=', ')
        print("Max: ", alumnos[clave]["mayor"], end=', ')
        print("Min: ", alumnos[clave]["menor"])