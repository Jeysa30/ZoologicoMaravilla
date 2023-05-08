import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel
import models.Habitat as habitatModel

class Zoo:
    def menuZoo(zoologico):
        idAnimal = 1

        while True:
            print("\n------EL ZOOLOGICO MARAVILLA------\n")
            print("1. Agrega un habitat.")
            print("2. Agregar animal.")
            print("3. Modificar alimentacion de un animal.")
            print("4. Acciones animales.")
            print("5. Ver informacion del zoologico.")
            print("0. Salir del zoologico.\n")
            op = int(input("Ingrese la opcion: "))
            try:
                if op not in [0, 1, 2, 3, 4, 5]:
                    raise ValueError("Se ingreso una opción invalida, ingrese un numero entero del 0 al 5.")
            except ValueError as error:
                print(f"\nSE PRESENTO UN ERROR: {error}")
                continue

            if op == 0:
                print("---GRACIAS POR VISITAR AL ZOOLOGICO MARAVILLA---")
            elif op == 1:
                print("opcion 1")
            elif op == 2:
                print("opcion 2")
            elif op == 3:
                print("opcion 3")
            elif op == 4:
                print("opcion 4")
            elif op == 5:
                print("opcion 5")

