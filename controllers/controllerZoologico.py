import models.Habitat as habitatModel
import models.Animal as animalModel

class ZoologicoController():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_menu(self, op):
        if op == 1:
            self.crearHabitat(self.vista.menuHabitat())
            return "Se creo exitosamente el habitat en el zoologico"
        elif op == 2:
            self.crearAnimal(self.modelo.idAnimal)
            self.modelo.idAnimal += 1
            return "Se creo exitosamente el animal en el registro del zoologico"
        elif op == 3:
            self.agregarAnimalHabitat()
        elif op == 4:
            print("opcion 4")
        elif op == 5:
            print("opcion 5")
        elif op == 6:
            print("opcion 6")

    def crearHabitat(self, tipoHabitat):
        dieta = self.vista.elegirDieta("habitat")
        cantMax = int(self.vista.solicitar_dato("Ingrese la cantidad maxima de animales en el habitat: "))

        if tipoHabitat == 1:
            nuevaHabitat = habitatModel.Desertico("Desierto", 100, 40, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de captus en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de agua en el habitat:")))
        elif tipoHabitat == 2:
            nuevaHabitat = habitatModel.Selvatico("Selva", 39, 10, dieta, cantMax,
            self.vista.solicitar_dato("Ingrese la cantidad de arboles en el habitat: "),
            self.vista.solicitar_dato("Ingrese la cantidad de rios en el habitat: "))
        elif tipoHabitat == 3:
            nuevaHabitat = habitatModel.Acuatico("Acuatico", 9, -20, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de algas en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de corales en el habitat: ")))
        elif tipoHabitat == 4:
            nuevaHabitat = habitatModel.Artico("Polar", -21, -70, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de glaciares en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de iglus en el habitat: ")))

        self.modelo.agregarHabitat(nuevaHabitat)


    def crearAnimal(self, id):
        nombre = self.vista.solicitar_dato("\nIngrese el nombre del animal: ")
        especieAnimal = self.vista.solicitar_dato("\nIngrese la especie del animal: ")
        dieta = self.vista.elegirDieta("animal")
        edad = int(self.vista.solicitar_dato("\nIngrese la edad del animal: "))
        estadoSalud = int(self.vista.solicitar_dato("\nIngrese el estado de salud actual del animal (del 1 al 10): "))
        cantDormir = int(self.vista.solicitar_dato("\nIngrese la cantidad de horas que puede dormir máximo: "))
        cantComer = int(self.vista.solicitar_dato("\nIngrese la cantidad (Kg) que puede comer el animal: "))

        if(dieta == "Omnivoro"):
            alimento = ["carne", "pescado", "futas", "verduras"]
        elif(dieta == "Carnivoro"):
            alimento = ["carne", "pescado", "presas"]
        elif(dieta == "Herbivoro"):
            alimento = ["hierva", "frutas", "vegetales"]

        nuevoAnimal = animalModel.Animal(nombre, especieAnimal, dieta, id, edad, estadoSalud, cantDormir, cantComer, alimento)
        self.modelo.agregarAnimalRegistro(nuevoAnimal)

    def agregarAnimalHabitat(self):
        self.modelo.listarAnimales()
        animalAgregar = int(self.vista.solicitar_dato("Ingrese el numero del animal que quiere agregar a un habitat: "))
        self.modelo.listarHabitats()
        habitatAgregar = int(self.vista.solicitar_dato("Ingrese el numero del animal que quiere agregar a un habitat: "))
        self.modelo.habitats[habitatAgregar-1].animales[animalModel.id] = self.modelo.registro[animalAgregar-1]
