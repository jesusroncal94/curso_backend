from clases.persona import Persona

class Alumno(Persona):
    def __init__(self, codigo, nombre, dni, edad, notas):
        super().__init__(codigo, nombre, dni, edad)
        self.notas = notas
    
    def getNotaMaxima(self):
        notaMaxima = max(self.notas)
        return notaMaxima

    def getNotaMinima(self):
        notaMinima = min(self.notas)
        return notaMinima
    
    def getPromedio(self):
        suma = 0
        numeroNotas = len(self.notas)
        for nota in self.notas:
            suma += nota
        promedio = suma / numeroNotas
        return promedio

    def mostrarDatos(self):
        return f"Codigo: {self.codigo}, nombre completo: {self.nombre}, DNI: {self.dni}, edad: {self.edad}, nota mayor: {self.getNotaMaxima()}, nota menor: {self.getNotaMinima()}, promedio: {self.getPromedio()}, notas: {self.notas}"