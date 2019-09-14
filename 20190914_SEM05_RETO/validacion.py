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