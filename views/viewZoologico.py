import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel

class Zoo:
    def menuZoo(self):
        print("\n------BIENVENIDOS AL ZOOLOGICO MARAVILLA------\n")
        ZoologicoMaravilla = zooModel.Zoologico("Zoologico Maravilla")
        controlador = zooController.ZoologicoController(ZoologicoMaravilla, self)


        while True:
            print(" ----- MENU -----\n")
            print("1. Agrega un habitat.")
            print("2. Agregar animal.")
            print("3. Modificar alimentacion de un animal.")
            print("4. Acciones animales.")
            print("5. Ver informacion del zoologico.")
            print("0. Salir del zoologico.\n")
            op = int(input("Ingrese la opcion: "))
            try:
                if op not in [0, 1, 2, 3, 4, 5]:
                    raise ValueError("Se ingreso una opción invalida, ingrese un numero entero del 0 al 5.\n")
            except ValueError as error:
                print(f"\nSE PRESENTO UN ERROR: {error}")
                continue

            if op == 0:
                print("\n---GRACIAS POR VISITAR AL ZOOLOGICO MARAVILLA---")
                break

            else:
                controlador.ejecutar_menu(op)

    def menuAgregarAnimal(self, id):
        nombre = input("\nIngrese el nombre del animal: ")
        especieAnimal = input("\nIngrese la especie del animal: ")
        edad = int(input("\nIngrese la edad del animal: "))
        estadoSalud = int(input("\nIngrese el estado de salud actual del animal (del 1 al 10): "))
        cantDormir = int(input("\nIngrese la cantidad de horas que puede dormir máximo: "))
        cantComer = int(input("\nIngrese la cantidad (Kg) que puede comer el animal: "))

        nuevoAnimal = animalModel.Animal(nombre, especieAnimal, id, edad, estadoSalud, cantDormir, cantComer)
        return nuevoAnimal

    def menuHabitat(self):
        print("\nHabitats disponibles:")
        print("1. Desierto (grados)")
        print("2. Selva(Grados)")
        print("3. Acuatico()")
        print("4. Polar()")
        return int(input("Ingrese el habitat que quiere crear: "))

    def dietaHabitat(self):
        print("\n Dietas para habitats disponibles:")
        print("1. Omnivoro")
        print("2. Carnivoro")
        print("3. Herbivoro")
        dieta = int(input("Ingrese la dieta del habitat que quiere crear: "))
        if dieta == 1: return "Omnivoro"
        elif dieta == 2: return "Carnivoro"
        elif dieta == 3: return "Herbivoro"

    def solicitar_dato(self, mensaje):
        return input(mensaje)

