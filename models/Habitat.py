class Habitat:
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0):
        self.nombre = nombre
        self.animales = {}
        self.maxTemperatura = maxTemperatura
        self.minTemperatura = minTemperatura
        self.cantMaxAnimales = cantMaxAnimales
        self.dieta = dieta
        self.cantAnimales = 0

    def agregar(self, Animal):
        self.animales[Animal.id] = Animal


class Desertico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, captus = 0, agua = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.captus = captus
        self.agua = agua

    def agregar(self, Animal):
        super.agregar(Animal)


class Selvatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, arboles = 0, rios = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, cantMaxAnimales, dieta)
        self.arboles = arboles
        self.rios = rios

    def agregar(self, Animal):
        super.agregar(Animal)


class Acuatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, algas = 0, Corales = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.algas = algas
        self.corales = corales

    def agregar(self, Animal):
        super.agregar(Animal)


class Artico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, glaciares = 0, iglus = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.glaciares = glaciares
        self.iglus = iglus

    def agregar(self, Animal):
        super.agregar(Animal)