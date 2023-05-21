# -*- coding: utf-8 -*-
import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel
import streamlit as st

#Creamos la clase Zoo como view, ya que aqui se van a ir colocando los metodos visibles para el usuario y la mayoria de los input.
class Zoo:

    #Este init es para hacer las conexión de la creación del objeto y conexión con el controlador.
    def __init__(self):
        self.ZoologicoMaravilla = zooModel.Zoologico("Zoologico Maravilla")
        self.controlador = zooController.ZoologicoController(self.ZoologicoMaravilla, self)

    #Este es el metodo que le mostrara al usuario el menu inicial del zoológico con las opciones a realizar.
    def menuZoo(self):
        #Haciendo uso de la libreria de streamlit:

        # De esta manera le mostramos el nombre de nuestro zoológico al usuario.
        st.markdown(
            f"<h1 style='text-align: center; color: green;'>BIENVENIDO AL ZOOLÓGICO MARAVILLA</h1>",
            unsafe_allow_html=True,
        )

        #Decidimos mostrar cada opción del zoológico por medio de un expander.
        with st.expander("ZOO"):
            boton_crear_habitat = st.button("Crea un habitat")
            boton_crear_animal = st.button("Crea un animal")
            boton_agregar_animal = st.button("Agrega un animal a un habitat")
            boton_modificar_alimentacion = st.button("Modifica la alimentación de un animal")
            boton_accion_animal = st.button("Realiza una acción a un animal")
            boton_ver_zoo = st.button("Ver información del zoológico")

        if boton_crear_habitat:
            st.session_state["opcion"] = 1
        elif boton_crear_animal:
            st.session_state["opcion"] = 2
        elif boton_agregar_animal:
            st.session_state["opcion"] = 3
        elif boton_modificar_alimentacion:
            st.session_state["opcion"] = 4
        elif boton_accion_animal:
            st.session_state["opcion"] = 5
        elif boton_ver_zoo:
            st.session_state["opcion"] = 6

        if "opcion" in st.session_state:
            self.mostrarFormulario = self.controlador.ejecutar_menu(st.session_state["opcion"])

    #Hicimos este metodo con el fin de mostrarle al usuario los habitats junto con su temperatura para el momento en que desea crear
    #un habitat.
    def menuHabitat(self):
        opciones = {
            "": 0,
            "Desierto(40 a 60 grados)": 1,
            "Selva(20 a 39 grados)": 2,
            "Acuatico(0 a 19 grados)": 3,
            "Polar(-20 a -1 grados)": 4
        }
        opcion = st.selectbox(
            "Escoge el tipo de habitat",
            tuple(opciones.keys()),
        )
        st.write('Seleccionaste:', opcion)

        if opcion != "" and opcion in tuple(opciones.keys()):
            st.session_state["opcion_elegida"] = opciones[opcion]
            return opciones[opcion]
        else:
            return None

    # Como habiamos mencionado antes, aunque tengamos 4 tipos de habitats ya definidos, se pueden crear según la dieta que
    # el usuario desea que tenga el habitat; con esto en mente, decidimos mostrarle al usuario las dietas que puede tener el habitat.
    def elegirDieta(self):
        listaDieta = ["", "Omnivoro", "Carnivoro", "Herbivoro"]
        opcion = st.selectbox(
            "Dietas para el habitat disponibles",
            listaDieta
        )

        st.write('Seleccionaste:', opcion)

        if opcion != "" and opcion in listaDieta:
            return opcion

        else:
            return None

    #Estos metodos nos permiten guardar la información que ponga el usuario de 3 maneras(estos lo utilizamos en el controller):

    #Aqui el usuario podra poner un numero sin limite para algunos atributos, como la cantidad de animales a un habitat, cantidad
    # de rios, arboles, etc.
    def solicitar_dato(self, mensaje):
        return st.number_input(mensaje, 0)

    #Aqui el usuario puede poner un string, lo utilizamos para cuando el usurio coloque el nombre del animal y su especie.
    def solicitar_dato_string(self, mensaje):
        return st.text_input(mensaje)

    #Este es el que permite colocar un numero limitado, como la cantidad de horas que quiera dormir(limite de 24 horas),
    # la edad(limite 150), etc.
    def solicitar_dato_rango(self, mensaje, min, max):
        return st.slider(mensaje, min, max)

    #Este metodo permite al usuario mostrarle un mini menú dentro de la opción de acción animal, con el fin de que el usuario
    # pueda agregar o eliminar un alimento de un animal seleccionado siempre y cuando este dentro de un habitat.
    def menuAlimento(self):
        st.markdown("Que modificacion desea realizar")

        if st.button("Agregar una nueva comida"):
            st.session_state["accion_select"] = 1

        if st.button("Eliminar alguna comida"):
            st.session_state["accion_select"] = 2

        if "accion_select" in st.session_state:
            accion_select = st.session_state["accion_select"]
            return accion_select

    #Este es el menú que le permite al usuario escoger que acción puede realizar el animal seleccionado mostrandolo por
    # medio de botones(se decidio de esta manera ya que sera mas facil guardar la opción elegida por el usuario).
    def menuAccion(self):
        st.markdown("Acciones que puede realizar el animal")

        if st.button("Comer"):
            st.session_state["accion_seleccionada"] = 1

        if st.button("Dormir"):
            st.session_state["accion_seleccionada"] = 2

        if st.button("Jugar"):
            st.session_state["accion_seleccionada"] = 3

        if "accion_seleccionada" in st.session_state:
            accion_seleccionada = st.session_state["accion_seleccionada"]
            return accion_seleccionada

    def mensajeExitoso(self, mensaje):
        st.success(mensaje)

    def mensajeError(self, mensaje):
        st.error(mensaje)

    #Este metodo lo hicimos con el fin de ser solo informativo, de tal manera muestre al usuario por medio de expander
    # los habitats que hay creados junto con su informacion, y si tienen animales en el habitat se le muestrara la
    # información de dicho animal, de lo contrario se le mostrara al usuario que el habitat no tiene animal, y lo mismo
    # para los habitats.
    def mostrarTodoZoo(self):
        st.divider()
        if self.ZoologicoMaravilla.habitats:
            st.subheader("Lista de habitats creados y su información")
            for habitat in self.ZoologicoMaravilla.habitats:
                with st.expander(habitat.nombre):
                    st.subheader("Informacion habitat")
                    st.write("Tipo de habitat: ", habitat.nombre)
                    st.write("Cantidad animales: ", habitat.cantAnimales)
                    st.write("Cantidad Maxima Animales: ", habitat.cantMaxAnimales)
                    st.write("Dieta: ", habitat.dieta)
                    st.divider()
                    if habitat.animales:
                        st.subheader("Animales:")
                        for animal in habitat.animales:
                            st.subheader(animal.nombre)
                            st.write("ID: ", animal.id)
                            st.write("Especie: ", animal.especieAnimal)
                            st.write("Edad: ", animal.edad)
                            st.write("Estado de salud: ", animal.estadoSalud)
                            st.write("Dieta: ", animal.dieta.tipoDieta)
                            st.divider()
                    else:
                        st.error("Este habitat no tiene animales, puede agregar uno en la opcion del menu.")
        else:
            st.error("El zoologico no tiene habitats, puede agregar uno en la opcion del menu.")