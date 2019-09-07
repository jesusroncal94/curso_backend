#Devuelve el promedio de las notas
def promedioNotas(notasNum):
    cantNotas = len(notasNum)
    suma = 0
    for n in notasNum:
        suma += n
    promedio = suma / cantNotas
    return promedio

#Devuelve el valor máximo de las notas
def notaMayor(notasNum):
    notasNum.sort()
    mayor = notasNum[-1]
    return mayor

#Devuelve el valor mínimo de las notas
def notaMenor(notasNum):
    notasNum.sort()
    menor = notasNum[0]
    return menor