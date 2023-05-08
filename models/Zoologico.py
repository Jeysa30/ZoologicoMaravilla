class Zoologico:
    def __init__(self, nombre = "", habitats = []):
        self.nombre = nombre
        self.habitats = habitats


    def setNombre(self, nombre):
        self.nombre = nombre
    def setHabitats(self, habitats):
        self.habitats = habitats
    def getNombre(self):
        return self.nombre
    def getHabitats(self):
        return self.habitats

    def agregar(self, Habitat):
        self.habitats.append(Habitat)
