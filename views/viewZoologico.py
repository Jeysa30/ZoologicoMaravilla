import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel
import models.Habitat as habitatModel

class Zoo:
    def menuZoo(self):
        print("\n------BIENVENIDOS AL ZOOLOGICO MARAVILLA------\n")
        idAnimal = 1
        habitat = habitatModel.Habitat()
        controlador = zooController.ZoologicoController(habitat, self)

        while True:
            print("-> SELECCIONA LA OPCION A REALIZAR.\n")
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
