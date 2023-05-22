# -*- coding: utf-8 -*-
import models.Habitat as habitatModel
import models.Animal as animalModel
import models.Dieta as dietaModel
import streamlit as st

#Creamos la clase ZoologicoController como controller, ya que este sera el encargado de anexar y utilizar los metodos
# que hay en view y models.

class ZoologicoController():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    #Este es el metodo que recibira la selección del usuario y ejecutara la lógica correspondiente para cada opción:
    def ejecutarMenu(self, op):
        if op == 1:
            try:
                self.crearHabitat()
            except ValueError:
                self.vista.mensajeError("Se presentó un error creando el habitat")

        elif op == 2:
            try:
                self.crearAnimal()

            except ValueError:
                self.vista.mensajeError("Se presentó un error creando al animal")

        elif op == 3:
            self.agregarAnimalHabitat()
        elif op == 4:
            self.modificarAlimentacion()
        elif op == 5:
            self.accionesAnimales()
        elif op == 6:
            self.vista.mostrarTodoZoo()

    #Este es el metodo de la opción de crear el habitat, lo hicimos de tal forma que aparezca un formulario seleccionando
    # primero que tipo de habitat es y cual seria la dieta que manejara:
    def crearHabitat(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            #Por ejemplo, en esta linea se llama al metodo para seleccionar el tipo de habitat.
            tipoHabitat = self.vista.menuHabitat()
            #Aqui se el usuario eligira y guardara el tipo de dieta que tendra el habitat.
            dieta = self.vista.elegirDieta()
            cantMax = int(self.vista.solicitar_dato("Ingrese la cantidad maxima de animales en el habitat: "))
            #Y aqui es algo interno que hace el programa, el cual se le aumentara el número del ID del habitat,
            # por ejemplo, si es el primer habitat a crear su ID sera 1.
            id = self.modelo.idHabitat

            #Aqui ya se maneja es la opción seleccionada por el usuario del tipo de habitat, de tal manera que se ira
            # guardando la información perteneciente a cada tipo.
            if tipoHabitat == 1:
                nuevaHabitat = habitatModel.Desertico("Desierto", 60, 40, dieta, cantMax, id,
                int(self.vista.solicitar_dato("Ingrese la cantidad de captus en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de agua en el habitat:")))

            elif tipoHabitat == 2:
                nuevaHabitat = habitatModel.Selvatico("Selva", 39, 20, dieta, cantMax, id,
                int(self.vista.solicitar_dato("Ingrese la cantidad de arboles en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de rios en el habitat: ")))

            elif tipoHabitat == 3:
                nuevaHabitat = habitatModel.Acuatico("Acuatico", 19, 0, dieta, cantMax, id,
                int(self.vista.solicitar_dato("Ingrese la cantidad de algas en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de corales en el habitat: ")))

            elif tipoHabitat == 4:
                nuevaHabitat = habitatModel.Artico("Polar", -1, -20, dieta, cantMax, id,
                int(self.vista.solicitar_dato("Ingrese la cantidad de glaciares en el habitat: ")),
                int(self.vista.solicitar_dato("Ingrese la cantidad de iglus en el habitat: ")))

            botonAccion = st.button("Crear nuevo habitat")

        #Decidimos colocar un boton para mostrarle al usuario que el habitat se creo correctamente, de lo contrario, si
        # el usuario le falto espacios por llenar información necesarios para el programa, entonces tambien le muestre
        # que le hace falta datos por llenar para completar la creación del habitat.
        if botonAccion:
            if tipoHabitat and dieta and cantMax != 0:
                self.modelo.agregarHabitat(nuevaHabitat)
                self.vista.mensajeExitoso("El habitat fue creado correctamente")
                self.modelo.idHabitat += 1
                st.session_state["idHabitat"] = self.modelo.idHabitat
            else:
                self.vista.mensajeError("Faltan datos por llenar, llene los datos para poder crear el animal")

    #Este es el metodo de la opción crear animal, cada animal creado irá directamente al registro del zoológico:
    def crearAnimal(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo animal")
            #Aqui solo se hace el llamado del metodo solicitar_dato del view, dependiendo de lo que queremos guardar.
            nombre = self.vista.solicitar_dato_string("\nIngrese el nombre del animal: ")
            especieAnimal = self.vista.solicitar_dato_string("\nIngrese la especie del animal: ")
            temperatura = int(self.vista.solicitar_dato_rango("\nIngrese la temperatura promedio del animal: ", -20, 60))
            edad = int(self.vista.solicitar_dato_rango("\nIngrese la edad del animal: ", 1, 150))
            estadoSalud = int(self.vista.solicitar_dato_rango("\nIngrese el estado de salud actual del animal (del 1 al 10): ", 1, 10))
            cantDormir = int(self.vista.solicitar_dato_rango("\nIngrese la cantidad de horas que puede dormir máximo: ", 1, 24))
            cantComer = int(self.vista.solicitar_dato_rango("\nIngrese la cantidad (Kg) que puede comer el animal: ", 1 , 50))
            dieta = self.vista.elegirDieta()

            boton_accion = st.button("Crear nuevo animal")

        # Decidimos colocar un boton para mostrarle al usuario que el animal se creo correctamente, de lo contrario, si
        # el usuario le falto espacios por llenar información necesarios para el programa, entonces tambien le muestre
        # que le hace falta datos por llenar para completar la creación del animal.
        if boton_accion:
            if nombre != "" and especieAnimal != "" and dieta:
                dieta = dietaModel.Dieta(dieta)
                dieta.listaDieta()
                nuevoAnimal = animalModel.Animal(nombre, especieAnimal, dieta, temperatura, st.session_state["idAnimal"], edad, estadoSalud, cantDormir, cantComer)
                self.modelo.agregarAnimalRegistro(nuevoAnimal)
                self.vista.mensajeExitoso("El animal fue creado correctamente")
                # Y al igual que el habitat, el programa internamente le asigna el ID del animal creado.
                self.modelo.idAnimal += 1
                st.session_state["idAnimal"] = self.modelo.idAnimal
            else:
                self.vista.mensajeError("Faltan datos por llenar, llene los datos para poder crear el animal")

    #Este es el metodo de la opción agregar animal seleccionado a un habitat ya creado:
    def agregarAnimalHabitat(self):
        st.divider()
        st.subheader("Agregue un animal al habitat")
        #Aqui decidimos que el usuario pueda ver los animales que hay en el registro del zoológico, de tal manera escoge uno
        #para añadirlo a un habitat.
        animalAgregar = self.modelo.listarAnimalesRegistro()
        if animalAgregar:
            #Y cuando el usuario alla colocado el animal, se vuelva visibile los habitats que se han creado y que cumpla
            #con los requisitos del animal; de lo contrario, si no coloca un animal no se le mostrara ningú habitat.
            habitatAgregar = self.modelo.listarHabitats(animalAgregar)

            #Al final se le muestra el boton de agregar el animal al habitat mostrandole al usuario que se agrego correctamete;
            # si el usuario no selecciono ningún habitat y presiona el boton de agregar, el programa le avisara que no selecciono
            # ningún habitat
            boton_agregar = st.button("Agregar el animal al habitat")
            if boton_agregar:
                if habitatAgregar:
                    habitatAgregar.agregarAnimal(animalAgregar)
                    self.modelo.eliminarAnimalRegistro(animalAgregar)
                    habitatAgregar.cantAnimales += 1
                    self.vista.mensajeExitoso("El animal fue agregado al habitat correctamente")
                else:
                    self.vista.mensajeError("No has seleccionado a ningun habitat para agregar al animal")

    # Este es el metodo de la opcion que permite modificar la alimentación del animal, siempre y cuando este en un habitat:
    def modificarAlimentacion(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para modificar la alimentación del animal")
            #Aqui se le mostrara al usuario los animales que hay en cada habitat
            escogerAnimal = self.modelo.listarAnimalesHabitats("Escoja el animal al que le quiere editar la alimentación")
            if escogerAnimal:
                st.write("Seleccionaste->   ID:", escogerAnimal.id, "Nombre:", escogerAnimal.nombre, "Dieta:",escogerAnimal.dieta.tipoDieta)
                #Aqui se hace visible al usuario lo que decea modificar en la alimentación del animal seleccionado.
                seleccion = self.vista.menuAlimento()
                #Y aqui internamente revisa el tipo de dieta del animal, si es carnivoro, herbivoro u omnivoro.
                dietaAnimal = escogerAnimal.dieta
                if seleccion == 1:
                    #si la opción es agregar se le muestra al usuario la lista de posibles alimentos según su dieta
                    agregar = dietaAnimal.listaPosiblesAlimentos()
                    if st.button("Realizar acción"):
                        st.session_state["accion_select"] = st.empty()
                        if agregar in dietaAnimal.posiblesAlimentos:
                            # Una vez seleccionado el alimento a agregar, se elimina de la lista de posibles alimentos(de tal manera,
                            # que no vuelva a aperecer cuando quiera volver a agregar otro alimento) y se agrega en la lista de
                            # alimentos del animal.
                            dietaAnimal.agregarAlimento(agregar, dietaAnimal.alimento)
                            dietaAnimal.eliminarAlimento(agregar, dietaAnimal.posiblesAlimentos)
                            self.vista.mensajeExitoso("El alimento se agrego correctamente")
                        else:
                            self.vista.mensajeError("Ese elmento no se puede agregar a los alimentos del animal")
                elif seleccion == 2:
                    #De lo contrario, si la opción es eliminar un alimeto, se le muestra la lista de alimentos que tiene el
                    # animal.
                    eliminar = dietaAnimal.listarAlimentos()
                    if st.button("Realizar acción"):
                        st.session_state["accion_select"] = st.empty()
                        if eliminar in dietaAnimal.alimento:
                            # Y una vez seleccionado el alimento a eliminar, se elimina de la lista de alimentos y se
                            # agrega en la lista de posibles alimentos del animal(de tal manera, pueda aperecer cuando
                            # quiera agregar un alimento).
                            dietaAnimal.eliminarAlimento(eliminar, dietaAnimal.alimento)
                            dietaAnimal.agregarAlimento(eliminar, dietaAnimal.posiblesAlimentos)
                            self.vista.mensajeExitoso("El alimento se elimino correctamente")
                        else:
                            self.vista.mensajeError("Ese elmento no se puede eliminar de los alimentos del animal")

    #Y este es el metodo de la opción de realizar una acción a un animal:
    def accionesAnimales(self):
        st.divider()
        with st.container():
            st.subheader("Acciones para que el animal realice")
            # Aqui se le mostrara al usuario los animales que hay en cada habitat.
            escogerAnimal = self.modelo.listarAnimalesHabitats("Escoge el animal que quieres que realice la acción")

            if escogerAnimal:
                #Aqui llamamos al metodo de view, el cual se le muestra al usuario las 3 acciones que puede realizar el animal.
                accion = self.vista.menuAccion()
                if accion == 1:
                    #Si la opción es comer, se mira internamente el tipo de dieta del animal, de tal manera que el usuario
                    # pueda ver la lista de alimentos del animal para poder seleccionar.
                    comerAnimal = escogerAnimal.dieta
                    comer = int(self.vista.solicitar_dato("Ingrese la cantidad de Kg que el animal va a comer: "))
                    opcion = comerAnimal.listarAlimentos()
                    if st.button("Realizar acción"):
                        st.divider()
                        #Se hace las condiciones al momento de presionar el boton de realizar acción:

                        # Se tiene en cuenta cuantos Kg se le dio al animal, para saber si es posible la cantidad que el usuario
                        # ingreso para darle al animal.
                        if (escogerAnimal.cantComerTemporal - comer) >= 0 and comer != 0:
                            # Si la cantidad es adecuada entonces se le restara al atributo temporal de comer del animal
                            if opcion:
                                escogerAnimal.cantComerTemporal -= comer
                                self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} comio {comer} Kg de los {escogerAnimal.cantComer} disponibles, le quedan {escogerAnimal.cantComerTemporal} Kg para comer.")

                            else:
                                self.vista.mensajeError("la opción ingresada no exite")

                        #De lo contrario, si el usuario ingreso una cantidad mayor, se le mostrara al usuario que el animal
                        # no puede comer tal cantidad.
                        else:
                            st.write(f"El animal {escogerAnimal.nombre} no puede comer {comer} Kg, solo le quedan {escogerAnimal.cantComerTemporal} disponibles para comer")

                elif accion == 2:
                    #Si la opción es dormir, solo el usuario ingresa la cantidad de horas que quiere que duerma.
                    dormir = int(self.vista.solicitar_dato("Ingrese la cantidad de horas que el animal va a dormir: "))
                    if st.button("Realizar acción"):
                        st.session_state["accion_seleccionada"] = st.empty()
                        st.divider()
                        # Y se hace las condiciones al momento de presionar el boton de realizar acción:

                        # Se tiene en cuenta la cantidad de horas del animal, para saber si es posible la cantidad que
                        # el usuario ingreso para poner a dormir al animal.
                        if (escogerAnimal.cantDormirTemporal - dormir) >= 0 and dormir != 0:
                            # Si la cantidad es adecuada entonces se le restara al atributo temporal de dormir del animal.
                            escogerAnimal.cantDormirTemporal -= dormir
                            self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} durmio {dormir} horas de los {escogerAnimal.cantDormir} disponibles, le quedan {escogerAnimal.cantDormirTemporal} horas para dormir.")

                        #De lo contrario si la cantidad de horas a dormir es mayor, se le muestra al usuario que el animal
                        # no puede dormir esa cantidad.
                        else:
                            self.vista.mensajeError(f"El animal {escogerAnimal.nombre} no puede dormir {dormir} horas, solo le quedan {escogerAnimal.cantDormirTemporal} disponibles para dormir")

                elif accion == 3:
                    #Si la opción es jugar, entonces solo se le mostrara al usuario una información dependiendo si el animal
                    # ya jugo o no, ya que el artributo es un booleano:
                    st.session_state["accion_seleccionada"] = st.empty()
                    st.divider()
                    #Asi que verifica que el atributo del animal este en False(lo que significa que el animal no a jugado).
                    if escogerAnimal.jugar == False:
                        escogerAnimal.jugar = True
                        self.vista.mensajeExitoso(f"El animal {escogerAnimal.nombre} acaba de jugar.")

                    #De lo contrario, si es True se le muestra al usuario que el animal ya jugo en el día.
                    else:
                        st.write(f"El animal {escogerAnimal.nombre} ya jugo en el dia.")