def sistemaNotas():
    continuar = "si"
    while continuar != "no":
        notas = []
        print("""
***BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS***""")
        notas = []
        x = input("Ingrese el número de notas a ingresar: ")
        numeroNotas = int(x) + 1        
        for i in range(1, numeroNotas):
            again = True
            while again == True: 
                nota = input(f"Ingrese nota {i}: ")
                try:
                    nota = float(nota)
                    if nota >= 0 and nota <= 20:
                        notas.append(nota)
                        again = False
                    else:
                        print(f"¡Ingrese nota{i} nuevamente!")
                        print("Se aceptan solo valores numéricos del 0 al 20.")
                        again = True
                except ValueError:
                    print(f"¡Ingrese nota{i} nuevamente!")
                    print("Se aceptan solo valores numéricos del 0 al 20.")
                    again = True
        print("Notas ingresadas: ", str(notas))
        promedioNotas(notas)
        notaMayor(notas)
        notaMenor(notas)
        continuar = "no"
        print("""
***REGISTRO FINALIZADO***""")    

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