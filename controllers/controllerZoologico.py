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
                self.crearAnimal()


            except ValueError:
                self.vista.mensajeError("Se presentó un error creando el producto")

        elif op == 3:
            self.agregarAnimalHabitat()
        elif op == 4:
            self.modificarAlimentacion()
        elif op == 5:
            self.accionesAnimales()
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
            if tipoHabitat and dieta and cantMax != 0:
                self.modelo.agregarHabitat(nuevaHabitat)
                self.vista.mensajeExitoso("El habitat fue creado correctamente")
            else:
                self.vista.mensajeError("Faltan datos por llenar, llene los datos para poder crear el animal")

    def crearAnimal(self):
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
            dieta = self.vista.elegirDieta()

            boton_accion = st.button("Crear nuevo animal")

        if boton_accion:
            if nombre != "" and especieAnimal != "" and dieta:
                dieta = dietaModel.Dieta(dieta)
                dieta.listaDieta()
                nuevoAnimal = animalModel.Animal(nombre, especieAnimal, dieta, temperatura, st.session_state["idAnimal"], edad, estadoSalud, cantDormir, cantComer)
                self.modelo.agregarAnimalRegistro(nuevoAnimal)
                self.vista.mensajeExitoso("El animal fue creado correctamente")
                self.modelo.idAnimal += 1
                st.session_state["idAnimal"] = self.modelo.idAnimal
            else:
                self.vista.mensajeError("Faltan datos por llenar, llene los datos para poder crear el animal")

    def agregarAnimalHabitat(self):
        animalAgregar = self.modelo.listarAnimalesRegistro()
        if animalAgregar:
            habitatAgregar = self.modelo.listarHabitats(animalAgregar)

            boton_agregar = st.button("Agregar el animal al habitat")
            if boton_agregar:
                if habitatAgregar != "":
                    habitatAgregar.agregarAnimal(animalAgregar)
                    self.modelo.eliminarAnimalRegistro(animalAgregar)
                    habitatAgregar.cantAnimales += 1
                    self.vista.mensajeExitoso("El animal fue agregado al habitat correctamente")
                else:
                    self.vista.mensajeError("no has seleccionado a ningun habitat para agregar al animal")

    def modificarAlimentacion(self):
        st.divider()
        with st.container():
            escogerAnimal = self.modelo.listarAnimalesHabitats("Escoja el animal al que le quiere editar la alimentacion")
            if escogerAnimal:
                st.write("Seleccionaste->   ID:", escogerAnimal.id, "Nombre:", escogerAnimal.nombre, "Dieta:", escogerAnimal.dieta.tipoDieta)
                seleccion = self.vista.menuAlimento()
                dietaAnimal = escogerAnimal.dieta
                if seleccion == 1:
                    agregar = dietaAnimal.listaTipoAlimento()
                    if st.button("Realizar accion"):
                        st.session_state["accion_select"] = st.empty()
                        if agregar in dietaAnimal.posiblesAlimentos:
                            dietaAnimal.agregarAlimento(agregar, dietaAnimal.alimento)
                            dietaAnimal.eliminarAlimento(agregar, dietaAnimal.posiblesAlimentos)
                            self.vista.mensajeExitoso("El alimento se agrego correctamente")
                        else:
                            self.vista.mensajeError("Ese elmento no se puede agregar a los alimentos del animal")
                elif seleccion == 2:
                    eliminar = dietaAnimal.listarAlimentos()
                    if st.button("Realizar accion"):
                        st.session_state["accion_select"] = st.empty()
                        if eliminar in dietaAnimal.alimento:
                            dietaAnimal.eliminarAlimento(eliminar, dietaAnimal.alimento)
                            dietaAnimal.agregarAlimento(eliminar, dietaAnimal.posiblesAlimentos)
                            self.vista.mensajeExitoso("El alimento se elimino correctamente")
                        else:
                            self.vista.mensajeError("Ese elmento no se puede eliminar de los alimentos del animal")

    def accionesAnimales(self):
        st.divider()
        with st.container():
            st.subheader("Acciones para que el animal realice")
            escogerAnimal = self.modelo.listarAnimalesHabitats("Escoge el animal que quieres que realice la accion")

            if escogerAnimal:
                accion = self.vista.menuAccion()
                if accion == 1:
                    comerAnimal = escogerAnimal.dieta
                    comer = int(self.vista.solicitar_dato("Ingrese la cantidad de Kg que el animal va a comer: "))
                    opcion = comerAnimal.listarAlimentos()
                    if st.button("Realizar accion"):
                        st.divider()
                        if (escogerAnimal.cantComerTemporal - comer) >= 0 and comer != 0:
                            if opcion:
                                escogerAnimal.cantComerTemporal -= comer
                                self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} comio {comer} Kg de los {escogerAnimal.cantComer} disponibles, le quedan {escogerAnimal.cantComerTemporal} Kg para comer.")

                            else:
                                self.vista.mensajeError("la opcion ingresada no exite")

                        else:
                            st.write(f"El animal {escogerAnimal.nombre} no puede comer {comer} Kg, solo le quedan {escogerAnimal.cantComerTemporal} disponibles para comer")

                elif accion == 2:
                    dormir = int(self.vista.solicitar_dato("Ingrese la cantidad de horas que el animal va a dormir: "))
                    if st.button("Realizar accion"):
                        st.session_state["accion_seleccionada"] = st.empty()
                        st.divider()
                        if (escogerAnimal.cantDormirTemporal - dormir) >= 0 and dormir != 0:
                            escogerAnimal.cantDormirTemporal -= dormir
                            self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} durmio {dormir} horas de los {escogerAnimal.cantDormir} disponibles, le quedan {escogerAnimal.cantDormirTemporal} horas para dormir.")

                        else:
                            self.vista.mensajeError(f"El animal {escogerAnimal.nombre} no puede dormir {dormir} horas, solo le quedan {escogerAnimal.cantDormirTemporal} disponibles para dormir")

                elif accion == 3:
                    st.session_state["accion_seleccionada"] = st.empty()
                    st.divider()
                    if escogerAnimal.jugar == False:
                        escogerAnimal.jugar = True
                        self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} acaba de jugar.")

                    else:
                        st.write(f"El animal {escogerAnimal.nombre} ya jugo en el dia.")