class Habitat:
    def __init__(self, nombre = "", animales = {}, maxTemperatura = 0, minTemperatura = 0, cantMaxAnimales = 0, dieta = ""):
        self.nombre = nombre
        self.animales = animales
        self.maxTemperatura = maxTemperatura
        self.minTemperatura = minTemperatura
        self.cantMaxAnimales = cantMaxAnimales
        self.dieta = dieta
        self.cantAnimales = 0

    def agregar(self, Animal):
        self.animales[Animal.id] = Animal


class Desierto(Habitat):
    def __init__(self, nombre = "", animales = {}, maxTemperatura = 0, minTemperatura = 0, cantMaxAnimales = 0, dieta = "", captus = 0, agua = 0):
        super().__init__((nombre, animales, maxTemperatura, minTemperatura, cantMaxAnimales, dieta))
        self.captus = captus
        self.agua = agua

    def agregar(self, Animal):
        super.agregar(Animal)


class Selvatico(Habitat):
    def __init__(self, nombre = "", animales = {}, maxTemperatura = 0, minTemperatura = 0, cantMaxAnimales = 0, dieta = "", arboles = 0, rios = 0):
        super().__init__((nombre, animales, maxTemperatura, minTemperatura, cantMaxAnimales, dieta))
        self.arboles = arboles
        self.rios = rios

    def agregar(self, Animal):
        super.agregar(Animal)


class Acuatico(Habitat):
    def __init__(self, nombre = "", animales = {}, maxTemperatura = 0, minTemperatura = 0, cantMaxAnimales = 0, dieta = "", algas = 0, Corales = 0):
        super().__init__((nombre, animales, maxTemperatura, minTemperatura, cantMaxAnimales, dieta))
        self.algas = algas
        self.corales = corales

    def agregar(self, Animal):
        super.agregar(Animal)


class Polar(Habitat):
    def __init__(self, nombre = "", animales = {}, maxTemperatura = 0, minTemperatura = 0, cantMaxAnimales = 0, dieta = "", glaciares = 0, iglus = 0):
        super().__init__((nombre, animales, maxTemperatura, minTemperatura, cantMaxAnimales, dieta))
        self.glaciares = glaciares
        self.iglus = iglus

    def agregar(self, Animal):
        super.agregar(Animal)