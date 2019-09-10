class Gato():

    tipo_animal = "Mamífero"
    __vidas = 7

    def __init__(self, nombre, edad, raza, alimentos):
        self.g_nombre = nombre
        self.g_edad = edad
        self.g_raza = raza
        self.g_alimentos = alimentos

    def adulto_bebe(self):
        if self.g_edad >= 3:
            return print("El gato es adulto")
        elif self.g_edad < 3 and self.g_edad >=0:
            return print("El gato es bebé")
        else:
            return print("Dato inválido")

    def existe_alimento(self, alimento):
        if alimento in self.g_alimentos:
            return print("El alimento se encuentra en lista")
        else:
            return print("El alimento no se encuentra en lista")

    def getVida(self):
        return print(self.__vidas)

    def setVida(self, vidas):
        self.__vidas = vidas

    def multiparametros(self, **multi):
        print(multi["valor1"])
        print(multi["valor2"])

nombre1 = "Michifus"
edad1 = 4
raza1 = "Persa"
alimentos1 = ["pera", "carne", "leche"]
gato1 = Gato(nombre1, edad1, raza1, alimentos1)

gato1.adulto_bebe()
gato1.existe_alimento("pera")

gato1.getVida()
gato1.setVida(10)
gato1.getVida()


hash_datos = {"valor1": 1, "valor2": 2}
gato2 = Gato(nombre1, edad1, raza1, alimentos1)
print(gato2.multiparametros(**hash_datos))