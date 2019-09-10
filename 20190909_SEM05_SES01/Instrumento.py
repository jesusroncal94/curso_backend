class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    
    def tocar(self):
        print("Estamos tocando música")
    
    def romper(self):
        print("Eso lo pagas tú")
        print("Son ", self.precio, "$$$")

class Bateria(Instrumento):
    pass

class Flauta(Instrumento):
    def __init__

    def tocar(self):
        print("Suena la flauta")

flauta = Flauta(35)
print(flauta.tocar())