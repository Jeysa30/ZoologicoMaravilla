import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel

class Zoo:
    def menuZoo(self):
        print("\n------BIENVENIDOS AL ZOOLOGICO MARAVILLA------\n")
        ZoologicoMaravilla = zooModel.Zoologico("Zoologico Maravilla")
        controlador = zooController.ZoologicoController(ZoologicoMaravilla, self)


        while True:
            print(" ----- MENU -----\n")
            print("1. Agregar un habitat.")
            print("2. Agregar animal.")
            print("3. Agregar un animal a un habitat.")
            print("4. Modificar alimentacion de un animal.")
            print("5. Acciones animales.")
            print("6. Ver informacion del zoologico.")
            print("0. Salir del zoologico.\n")
            op = int(input("Ingrese la opcion: "))
            try:
                if op not in [0, 1, 2, 3, 4, 5, 6]:
                    raise ValueError("Se ingreso una opción invalida, ingrese un numero entero del 0 al 5.\n")
            except ValueError as error:
                print(f"\nSE PRESENTO UN ERROR: {error}")
                continue

            if op == 0:
                print("\n---GRACIAS POR VISITAR AL ZOOLOGICO MARAVILLA---")
                break

            else:
                print(controlador.ejecutar_menu(op))

    def menuHabitat(self):
        print("\nHabitats disponibles:")
        print("1. Desierto(40 a 60)")
        print("2. Selva(20 a 39)")
        print("3. Acuatico(0 a 19)")
        print("4. Polar(-20 a -1)")
        opcion = int(input("Ingrese el habitat que quiere crear: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Ese numero no es valido, vuelva a ingresar uno valido: "))
        return opcion

    def elegirDieta(self, mensaje):
        print("\n Dietas para el ", mensaje, "disponibles:")
        print("1. Omnivoro")
        print("2. Carnivoro")
        print("3. Herbivoro")
        dieta = int(input("Ingrese el numero de la dieta: "))
        while dieta < 1 or dieta > 3:
            dieta = int(input("Ese numero no es valido, vuelva a ingresar el numero de la dieta: "))
        if dieta == 1: return "Omnivoro"
        elif dieta == 2: return "Carnivoro"
        elif dieta == 3: return "Herbivoro"

    def solicitar_dato(self, mensaje):
        return input(mensaje)

    def menuAlimento(self):
        print("\n--Modificaciones de los alimentos del animal: ")
        print("1. Agregar una nueva comida." )
        print("2. Eliminar alguna comida.")

    def menuAccion(self):
        print("\n--Acciones que puede realizar el animal ")
        print("1. Comer.")
        print("2. Dormir.")
        print("3. Jugar.")