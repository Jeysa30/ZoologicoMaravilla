class Zoologico:
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.idAnimal = 1
        self.habitats = []
        self.registro = []

    def agregarHabitat(self, Habitat):
        self.habitats.append(Habitat)

    def agregarAnimalRegistro(self, animal):
        self.registro.append(animal)

    def eliminarAnimalRegistro(self, animal):
        self.registro.remove(animal)

    def listarHabitats(self):
        posicion = 1
        print("---Habitats: ")
        for habitat in self.habitats:
            print(posicion, "-",habitat.nombre)
            posicion += 1

    def listarAnimales(self):
        posicion = 1
        print("---Animales: ")
        for animal in self.registro:
            print(posicion, "-",animal.nombre)
            posicion += 1