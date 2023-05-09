class Zoologico:
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.habitats = []
        self.registro = []
        self.idAnimal = 1

    def agregar(self, Habitat):
        self.habitats.append(Habitat)
