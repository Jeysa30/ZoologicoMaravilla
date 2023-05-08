class Animal:
    def __init__(self, nombre = "", especieAnimal = "", dieta = "", id = 0, edad = 0, estadoSalud = 0, cantDormir = 0, cantComer = 0, alimento = []):
        self.nombre = nombre
        self.especieAnimal = especieAnimal
        self.dieta = dieta
        self.id = id
        self.edad = edad
        self.estadoSalud = estadoSalud
        self.cantDormir = cantDormir
        self.cantComer = cantComer
        self.cantDormirTemporal = cantDormir
        self.cantComerTemporal = cantComer
        self.jugar = False
        self.alimento = alimento
