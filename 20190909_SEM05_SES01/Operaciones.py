class Operaciones():

    #Constructor
    def __init__(self, parametro_1, parametro_2):
        self.variable_1 = parametro_1
        self.variable_2 = parametro_2
    
    def sumar(self):
        return self.variable_1 + self.variable_2

operacion_1 = Operaciones(2, 3)
print(operacion_1.sumar())