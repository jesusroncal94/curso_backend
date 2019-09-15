from clases.persona import Persona

class Docente(Persona):
    def mostrarDatos(self):
        return f"Codigo: {self.codigo}, nombre completo: {self.nombre}, DNI: {self.dni}, edad: {self.edad}"