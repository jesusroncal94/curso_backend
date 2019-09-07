def validarNotas(notas):
    notasNum = []
    try:
        for n in notas:
            if float(n) >= 0 and float(n) <= 20:
                notasNum.append(float(n))
            else:
                return "errorNum"
        return notasNum
    except ValueError:
        return "errorNum"