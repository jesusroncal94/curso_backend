#Clase Persona que contiene atributos
#comunes de Alumno y Docente
class Persona():
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
    
    def getNombre(self):
        return self.nombre
    
    def getDni(self):
        return self.dni
    
    def getEdad(self):
        return self.edad

#Clase Alumno que hereda los atributos de la 
#clase Persona, además de definir el atributo notas
#y los métodos para obtener nota máxima, mínima
# y el promedio
class Alumno(Persona):
    def __init__(self, nombre, dni, edad, notas=[]):
        super().__init__(nombre, dni, edad)
        self.notas = notas

    def getNotaMax(self):
        notaMax = max(self.notas)
        return notaMax
    
    def getNotaMin(self):
        notaMax = max(self.notas)
        return notaMax
    
    def getPromedio(self):
        promedio = 0
        suma = 0
        nroNotas = 1    
        for nota in self.notas:
            suma += nota
            nroNotas += 1
        promedio = suma/nroNotas
        return promedio

#Clase Docentes que hereda los atributos de la clase Personas
class Docente(Persona):
    pass

#Prueba
#abc = Alumno('gerald', '48082321', 13, [12, 15])
#print(abc.nombre)