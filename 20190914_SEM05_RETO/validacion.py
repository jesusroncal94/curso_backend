#Validación de dato numérico
def validarNumero(tipoValidacion, peticion):
    while True:
        if tipoValidacion == 0: #Edad, numero entero
            try:
                numero = int(input(peticion))
                if numero >= 0:
                    break 
                else: print("Dato fuera de rango")
            except Exception:
                print("Dato inválido")
        elif tipoValidacion == 1: #Nota
            try:
                numero = float(input(peticion))
                if numero >= 0 and numero <= 20:
                    break 
                else: print("Dato fuera de rango")
            except Exception:
                print("Dato inválido")
    return numero