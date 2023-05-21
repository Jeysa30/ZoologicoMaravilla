
#Se hace la creación de la clase animal como model con sus respectivos atributos que tendra cada objeto de dicha clase para el zoológico
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

        #En este caso hacemos 2 atributos temporales que son comer y dormir que guardaran lo mismo que el cantComer y el cantDormir,
        #pero, estos temporales nos serviran para irle restando el numero y mostrarle al usuario cuanto le queda al animal,
        #y los otros dos son fijos para que no se pierda la información del objeto animal.