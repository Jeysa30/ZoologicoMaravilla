class Zoologico:
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.idAnimal = 1
        self.registro = []
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []

    def agregarHabitat(self, Habitat):
        self.habitats.append(Habitat)
        st.session_state["habitats"] = self.habitats

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

    def listarAnimalesRegistro(self):
        posicion = 1
        print("---Animales: ")
        for animal in self.registro:
            print(posicion, "-",animal.nombre)
            posicion += 1

    def listarAnimalesHabitats(self):
        for habitat in self.habitats:
            habitat.listarAnimales()

    def buscarAnimalHabitatsID(self, id):
        for habitat in self.habitats:
            if habitat.animales[id]:
                return habitat.animales[id]