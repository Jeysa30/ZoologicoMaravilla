class ZoologicoController():
    idAnimal = 0
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_menu(self, op):
        if op == 1:
            print("opcion 1")
        if op == 2:
            animal = self.vista.menuAgregarAnimal(idAnimal)
            idAnimal += 1
            self.modelo.agregar(animal)
        if op == 3:
            print("opcion 3")
        if op == 4:
            print("opcion 4")
        if op == 5:
            print("opcion 5")