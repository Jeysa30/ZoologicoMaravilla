import models.Habitat as habitatModel
import models.Animal as animalModel
import models.Dieta as dietaModel

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
            return "Se agrego el animal correctamente al habitat"
        elif op == 4:
            self.modificarAlimentacion()
            return "El alimento se modifico correctamente"
        elif op == 5:
            print("opcion 5")
        elif op == 6:
            print("opcion 6")

    def crearHabitat(self, tipoHabitat):
        dieta = self.vista.elegirDieta("habitat")
        cantMax = int(self.vista.solicitar_dato("Ingrese la cantidad maxima de animales en el habitat: "))

        if tipoHabitat == 1:
            nuevaHabitat = habitatModel.Desertico("Desierto", 60, 40, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de captus en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de agua en el habitat:")))
        elif tipoHabitat == 2:
            nuevaHabitat = habitatModel.Selvatico("Selva", 39, 20, dieta, cantMax,
            self.vista.solicitar_dato("Ingrese la cantidad de arboles en el habitat: "),
            self.vista.solicitar_dato("Ingrese la cantidad de rios en el habitat: "))
        elif tipoHabitat == 3:
            nuevaHabitat = habitatModel.Acuatico("Acuatico", 19, 0, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de algas en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de corales en el habitat: ")))
        elif tipoHabitat == 4:
            nuevaHabitat = habitatModel.Artico("Polar", -1, -20, dieta, cantMax,
            int(self.vista.solicitar_dato("Ingrese la cantidad de glaciares en el habitat: ")),
            int(self.vista.solicitar_dato("Ingrese la cantidad de iglus en el habitat: ")))

        self.modelo.agregarHabitat(nuevaHabitat)


    def crearAnimal(self, id):
        nombre = self.vista.solicitar_dato("\nIngrese el nombre del animal: ")
        especieAnimal = self.vista.solicitar_dato("\nIngrese la especie del animal: ")
        temperatura = int(self.vista.solicitar_dato("\nIngrese la temperatura promedio del animal: "))
        edad = int(self.vista.solicitar_dato("\nIngrese la edad del animal: "))
        estadoSalud = int(self.vista.solicitar_dato("\nIngrese el estado de salud actual del animal (del 1 al 10): "))
        cantDormir = int(self.vista.solicitar_dato("\nIngrese la cantidad de horas que puede dormir máximo: "))
        cantComer = int(self.vista.solicitar_dato("\nIngrese la cantidad (Kg) que puede comer el animal: "))
        dieta = dietaModel.Dieta(self.vista.elegirDieta("animal "))
        dieta.listaDieta()


        nuevoAnimal = animalModel.Animal(nombre, especieAnimal, dieta, temperatura, id, edad, estadoSalud, cantDormir, cantComer)
        self.modelo.agregarAnimalRegistro(nuevoAnimal)

    def agregarAnimalHabitat(self):
        self.modelo.listarAnimales()
        animalAgregar = int(self.vista.solicitar_dato("Ingrese el numero del animal que quiere agregar a un habitat: "))
        self.modelo.listarHabitats()
        habitatAgregar = int(self.vista.solicitar_dato("Ingrese el numero del habitat que quiere agregar al animal: "))
        animalAgregar = self.modelo.registro[animalAgregar-1]
        habitatAgregar = self.modelo.habitats[habitatAgregar-1]
        habitatAgregar.animales[animalAgregar.id] = animalAgregar
        self.modelo.eliminarAnimalRegistro(animalAgregar)

    def modificarAlimentacion(self):
        self.modelo.listarAnimales()
        escogerAnimal = int(self.vista.solicitar_dato("Ingrese el numero del animal al cual desee modificar su alimentacion: "))
        self.modelo.listarAlimentos()
        self.vista.menuAlimento("\n--Modificaciones de los alimentos del animal: ")
        seleccion = int(self.vista.solicitar_dato("Que modificaciones quieres realizar: "))

        if seleccion == 1:
            self.modelo.listaTipoAlimento()
            opcion = int(self.vista.solicitar_dato("Ingrese el numero del alimento que quiere agregar: "))
            agregar = self.modelo.alimento[opcion-1]
            self.modelo.agregarAlimento(agregar)
            eliminar = self.modelo.posiblesAlimentos[opcion-1]
            self.modelo.eliminarAlimento(eliminar)

        elif seleccion == 2:
            self.modelo.listarAlimentos()
            opcion = int(self.vista.solicitar_dato("Ingrese el numero del alimento que quiere eliminar: "))
            eliminar = self.modelo.alimento[opcion-1]
            self.modelo.eliminarAlimento(eliminar)
            agregar = self.modelo.posiblesAlimentos[opcion-1]
            self.modelo.agregarAlimento(agregar)