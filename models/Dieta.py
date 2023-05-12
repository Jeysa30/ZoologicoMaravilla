class Dieta:
    def __init__(self, tipoDieta = "", alimento = [], posiblesAlimentos = []):
        self.alimento = alimento
        self.tipoDieta = tipoDieta
        self.posiblesAlimentos = posiblesAlimentos

    def listaDieta(self):
        if (self.tipoDieta == "Omnivoro"):
            self.alimento = ["carne", "pescado", "futas", "verduras"]
            self.posiblesAlimentos = ["aves", "insectos", "huevos", "gusanos", "hojas", "raices", "flores", "nectar", "polen",
                                      "corteza", "miel"]

        elif (self.tipoDieta == "Carnivoro"):
            self.alimento = ["carne", "pescado", "presas"]
            self.posiblesAlimentos = ["aves", "insectos", "huevos", "gusanos"]

        elif (self.tipoDieta == "Herbivoro"):
            self.alimento = ["hierva", "frutas", "vegetales"]
            self.posiblesAlimentos = ["hojas", "raices", "flores", "nectar", "polen", "corteza"]

    def agregarAlimento(self, alimento):
        self.alimento.append(alimento)

    def eliminarAlimento(self, alimento):
        self.alimento.remove(alimento)

    def listarAlimentos(self):
        posicion = 1
        print("---Alimento: ")
        for alimentos in self.alimento:
            print(posicion, "-", alimentos)
            posicion += 1

    def listaTipoAlimento(self):
        posicion = 1
        print("\n---Estos son los alimentos que puedes agregar: ")
        for alimentos in self.posiblesAlimentos:
            print(posicion, "-", alimentos)
            posicion += 1
