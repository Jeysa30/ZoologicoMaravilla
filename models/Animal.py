class Animal:
    def __init__(self, nombre = "", especieAnimal = "", dieta = "", temperatura = 0, id = 0, edad = 0, estadoSalud = 0, cantDormir = 0, cantComer = 0):
        self.nombre = nombre
        self.especieAnimal = especieAnimal
        self.dieta = dieta
        self.temperatura = temperatura
        self.id = id
        self.edad = edad
        self.estadoSalud = estadoSalud
        self.cantDormir = cantDormir
        self.cantComer = cantComer
        self.cantDormirTemporal = cantDormir
        self.cantComerTemporal = cantComer
        self.jugar = False