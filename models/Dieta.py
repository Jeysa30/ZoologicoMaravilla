class Dieta:
    def __init__(self, tipoDieta = "", alimento = []):
        self.alimento = alimento
        self.tipoDieta = tipoDieta

    def listaDieta(self):
        if (self.tipoDieta == "Omnivoro"):
            self.alimento = ["carne", "pescado", "futas", "verduras"]
        elif (self.tipoDieta == "Carnivoro"):
            self.alimento = ["carne", "pescado", "presas"]
        elif (self.tipoDieta == "Herbivoro"):
            self.alimento = ["hierva", "frutas", "vegetales"]

    def agregarAlimento(self, alimento):
        self.alimento.append(alimento)

    def eliminarAlimento(self, alimento):
        self.alimento.remove(alimento)

    def listarAlimentos(self):
        posicion = 1
        print("Alimentos: ")
        for alimento in self.alimento:
            print(posicion, "-",alimento)
            posicion += 1