import models.Habitat as habitatModel
import models.Animal as animalModel
import models.Dieta as dietaModel
import streamlit as st

class ZoologicoController():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_menu(self, op):
        if op == 1:
            try:
                self.crearHabitat()

            except ValueError:
                self.vista.mensajeError("Se presentó un error creando el producto")

        elif op == 2:
            try:
                self.crearAnimal(self.modelo.idAnimal)
                self.modelo.idAnimal += 1

            except ValueError:
                self.vista.mensajeError("Se presentó un error creando el producto")

        elif op == 3:
            self.agregarAnimalHabitat()
            return "Se agrego el animal correctamente al habitat"
        elif op == 4:
            self.modificarAlimentacion()
            return "El alimento se modifico correctamente"
        elif op == 5:
            return self.accionesAnimales()
        elif op == 6:
            print("opcion 6")

    def crearHabitat(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            tipoHabitat = self.vista.menuHabitat()
            dieta = self.vista.elegirDieta()
            cantMax = int(self.vista.solicitar_dato("Ingrese la cantidad maxima de animales en el habitat: "))

            if tipoHabitat == 1:
                nuevaHabitat = habitatModel.Desertico("Desierto", 60, 40, dieta, cantMax,
                int(self.vista.solicitar_dato("Ingrese la cantidad de captus en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de agua en el habitat:")))

            elif tipoHabitat == 2:
                nuevaHabitat = habitatModel.Selvatico("Selva", 39, 20, dieta, cantMax,
                int(self.vista.solicitar_dato("Ingrese la cantidad de arboles en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de rios en el habitat: ")))

            elif tipoHabitat == 3:
                nuevaHabitat = habitatModel.Acuatico("Acuatico", 19, 0, dieta, cantMax,
                int(self.vista.solicitar_dato("Ingrese la cantidad de algas en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de corales en el habitat: ")))

            elif tipoHabitat == 4:
                nuevaHabitat = habitatModel.Artico("Polar", -1, -20, dieta, cantMax,
                int(self.vista.solicitar_dato("Ingrese la cantidad de glaciares en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de iglus en el habitat: ")))

            botonAccion = st.button("Crear nuevo habitat")

        if botonAccion:
            self.modelo.agregarHabitat(nuevaHabitat)
            st.success("El habitat fue creado correctamente")

    def crearAnimal(self, id):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo animal")
            nombre = self.vista.solicitar_dato_string("\nIngrese el nombre del animal: ")
            especieAnimal = self.vista.solicitar_dato_string("\nIngrese la especie del animal: ")
            temperatura = int(self.vista.solicitar_dato_rango("\nIngrese la temperatura promedio del animal: ", -20, 60))
            edad = int(self.vista.solicitar_dato_rango("\nIngrese la edad del animal: ", 1, 150))
            estadoSalud = int(self.vista.solicitar_dato_rango("\nIngrese el estado de salud actual del animal (del 1 al 10): ", 1, 10))
            cantDormir = int(self.vista.solicitar_dato_rango("\nIngrese la cantidad de horas que puede dormir máximo: ", 1, 24))
            cantComer = int(self.vista.solicitar_dato_rango("\nIngrese la cantidad (Kg) que puede comer el animal: ", 1 , 50))
            dieta = dietaModel.Dieta(self.vista.elegirDieta())
            dieta.listaDieta()

            boton_accion = st.button("Crear nuevo animal")

        if boton_accion:
            nuevoAnimal = animalModel.Animal(nombre, especieAnimal, dieta, temperatura, id, edad, estadoSalud, cantDormir, cantComer)
            self.modelo.agregarAnimalRegistro(nuevoAnimal)
            st.success("El animal fue creado correctamente")

    def agregarAnimalHabitat(self):
        animalAgregar = self.modelo.listarAnimalesRegistro()
        habitatAgregar = self.modelo.listarHabitats()

        boton_agregar = st.button("Agregar el animal al habitat")
        if boton_agregar:
            habitatAgregar.agregarAnimal(animalAgregar)
            self.modelo.eliminarAnimalRegistro(animalAgregar)
            st.success("El animal fue agregado al habitat correctamente")

    def modificarAlimentacion(self):
        self.modelo.listarAnimalesHabitats()
        escogerAnimal = int(self.vista.solicitar_dato("Ingrese la id del animal al cual desea modificar su alimentacion: "))
        escogerAnimal = self.modelo.buscarAnimalHabitatsID(escogerAnimal)
        self.vista.menuAlimento()
        seleccion = int(self.vista.solicitar_dato("Que modificaciones quieres realizar: "))
        dietaAnimal = escogerAnimal.dieta

        if seleccion == 1:
            dietaAnimal.listaTipoAlimento()
            opcion = int(self.vista.solicitar_dato("Ingrese el numero del alimento que quiere agregar: "))
            agregar = dietaAnimal.posiblesAlimentos[opcion-1]
            dietaAnimal.agregarAlimento(agregar, dietaAnimal.alimento)
            dietaAnimal.eliminarAlimento(agregar, dietaAnimal.posiblesAlimentos)

        elif seleccion == 2:
            dietaAnimal.listarAlimentos()
            opcion = int(self.vista.solicitar_dato("Ingrese el numero del alimento que quiere eliminar: "))
            eliminar = dietaAnimal.alimento[opcion-1]
            dietaAnimal.eliminarAlimento(eliminar, dietaAnimal.alimento)
            dietaAnimal.agregarAlimento(eliminar, dietaAnimal.posiblesAlimentos)

    def accionesAnimales(self):
        st.divider()
        with st.container():
            st.subheader("Acciones para realizarle al animal")
            self.modelo.listarAnimalesHabitats()
            escogerAnimal_Id = int(self.vista.solicitar_dato("Ingrese la id del animal el cual va a realizar la accion: "))
            escogerAnimal = self.modelo.buscarAnimalHabitatsID(escogerAnimal_Id)

            if escogerAnimal:
                st.write(f"Animal seleccionado: Nombre: {escogerAnimal.nombre} - ID: {escogerAnimal.id}")
            else:
                st.write("No se encontró ningún animal con el ID proporcionado.")

            accion = self.vista.menuAccion()

            if accion == 1:
                comerAnimal = escogerAnimal.dieta
                comer = int(self.vista.solicitar_dato("Ingrese la cantidad de Kg que el animal va a comer: "))
                if (escogerAnimal.cantComerTemporal - comer) >= 0:
                    opcion = comerAnimal.listarAlimentos()
                    if comerAnimal.alimento[opcion]:
                        escogerAnimal.cantComerTemporal -= comer
                        st.write(f"El animal {escogerAnimal.nombre} comio {comer} Kg de los {escogerAnimal.cantComer} disponibles, le quedan {escogerAnimal.cantComerTemporal} Kg para comer.")

                    else:
                        st.write("la opcion ingresada no exite")

                else:
                    st.write(f"El animal {escogerAnimal.nombre} no puede comer {comer} Kg, solo le quedan {escogerAnimal.cantComerTemporal} disponibles para comer")

            elif accion == 2:
                dormir = int(self.vista.solicitar_dato("Ingrese la cantidad de horas que el animal va adormir: "))
                if (escogerAnimal.cantDormirTemporal - dormir) >= 0:
                    escogerAnimal.cantDormirTemporal -= dormir
                    return "El animal", escogerAnimal.nombre, "durmio", dormir, "horas de las", escogerAnimal.cantDormir,"disponibles, le quedan", escogerAnimal.cantDormirTemporal, "horas para dormir."

                else:
                    return "El animal", escogerAnimal.nombre, "no puede dormir", dormir, "horas, solo le quedan", escogerAnimal.cantDormirTemporal, "disponibles para dormir"

            elif accion == 3:
                if escogerAnimal.jugar == False:
                    escogerAnimal.jugar = True
                    return "El animal", escogerAnimal.nombre, "acaba de jugar."

                else:
                    return "El animal ", escogerAnimal.nombre, " ya jugo en el dia."