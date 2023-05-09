import models.Habitat as habitatModel
import models.Animal as animalModel

class ZoologicoController():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_menu(self, op):
        if op == 1:
            self.crearHabitat(self.vista.menuHabitat())
            print("Se creo exitosamente el habitat")
        if op == 2:
            animal = self.vista.menuAgregarAnimal(self.modelo.idAnimal)
            self.modelo.idAnimal += 1
            self.modelo.agregar(animal)
        if op == 3:
            print("opcion 3")
        if op == 4:
            print("opcion 4")
        if op == 5:
            print("opcion 5")

    def crearHabitat(self, tipoHabitat):
        dieta = self.vista.dietaHabitat()
        if tipoHabitat == 1:
            nuevaHabitat = habitatModel.Desertico("Desierto", 100, 40, dieta,
            self.vista.solicitar_dato("Ingrese la cantidad de captus en el habitat: "),
            self.vista.solicitar_dato("Ingrese la cantidad de agua en el habitat:"))
        elif tipoHabitat == 2:
            nuevaHabitat = habitatModel.Selvatico("Selva", 39, 10, dieta,
            self.vista.solicitar_dato("Ingrese la cantidad de arboles en el habitat"),
            self.vista.solicitar_dato("Ingrese la cantidad de rios en el habitat"))
        elif tipoHabitat == 3:
            nuevaHabitat = habitatModel.Acuatico("Acuatico", 9, -20, dieta,
            self.vista.solicitar_dato("Ingrese la cantidad de algas en el habitat"),
            self.vista.solicitar_dato("Ingrese la cantidad de corales en el habitat"))
        elif tipoHabitat == 4:
            nuevaHabitat = habitatModel.Artico("Polar", -21, -70, dieta,
            self.vista.solicitar_dato("Ingrese la cantidad de glaciares en el habitat"),
            self.vista.solicitar_dato("Ingrese la cantidad de iglus en el habitat"))

        self.modelo.agregar(nuevaHabitat)