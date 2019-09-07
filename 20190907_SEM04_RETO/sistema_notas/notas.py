import validacion as v

def sistemaNotas():
    continuar = "si"
    while continuar != "no":
        notas = []
        print("""
***BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS***""")
        for i in range(1, 6):
            notas.append(input(f"Ingrese nota {i}: "))
        notasNum = v.validarNotas(notas)
        if notasNum != "errorNum":
            print("Notas ingresadas: ", str(notasNum))
            promedioNotas(notasNum)
            notaMayor(notasNum)
            notaMenor(notasNum)
            continuar = "no"
            print("""
***REGISTRO FINALIZADO***""")
        else:
            print("¡Ingrese solo valores numéricos y en el rango de 0 a 20!")
            print("Intente nuevamente")
            continuar = "si"

def promedioNotas(notasNum):
    cantNotas = len(notasNum)
    suma = 0
    for n in notasNum:
        suma += n
    promedio = suma / cantNotas
    print("El promedio es: ", str(promedio))

def notaMayor(notasNum):
    notasNum.sort()
    mayor = notasNum[-1]
    print("La mayor nota es: ", str(mayor))

def notaMenor(notasNum):
    notasNum.sort()
    menor = notasNum[0]
    print("La menor nota es: ", str(menor))