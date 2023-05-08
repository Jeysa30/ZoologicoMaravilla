class Habitat:
    def __init__(self, nombre = "", animales = {}):
        self.nombre = nombre
        self.animales = animales

    def setNombre(self, nombre):
        self.nombre = nombre
    def setAnimales(self, animales):
        self.animales = animales
    def getNombre(self):
        return self.nombre
    def getAnimales(self):
        return self.animales

    def agregar(self, Animal):
        self.animales[Animal.getId] = Animal