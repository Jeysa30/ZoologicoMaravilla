class Zoologico:
    def __init__(self, nombre = "", habitats = [], registro = []):
        self.nombre = nombre
        self.habitats = habitats
        self.registro = registro

    def agregar(self, Habitat):
        self.habitats.append(Habitat)
