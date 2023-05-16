# -*- coding: utf-8 -*-
import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel
import streamlit as st

class Zoo:
    def __init__(self):
        self.ZoologicoMaravilla = zooModel.Zoologico("Zoologico Maravilla")
        self.controlador = zooController.ZoologicoController(self.ZoologicoMaravilla, self)

    def menuZoo(self):

        st.markdown(
            f"<h1 style='text-align: center; color: green;'>BIENVENIDO AL ZOOLÓGICO MARAVILLA</h1>",
            unsafe_allow_html=True,
        )

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

        if opcion:
            st.session_state["opcion_elegida"] = opciones[opcion]
            return opciones[opcion]
        else:
            return None

    def elegirDieta(self):
        opcion = st.selectbox(
            "Dietas para el habitat disponibles",
            ("", "Omnivoro", "Carnivoro", "Herbivoro")
        )

        st.write('Seleccionaste:', opcion)

        if opcion:
            return opcion

        else:
            return None

    def solicitar_dato(self, mensaje):
        return st.number_input(mensaje, 0)

    def solicitar_dato_string(self, mensaje):
        return st.text_input(mensaje)

    def solicitar_dato_rango(self, mensaje, min, max):
        return st.slider(mensaje, min, max)

    def menuAlimento(self):
        print("\n--Modificaciones de los alimentos del animal: ")
        print("1. Agregar una nueva comida." )
        print("2. Eliminar alguna comida.")

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

    def mensajeExitoso(self, mensaje):
        st.success(mensaje)

    def mensajeError(self, mensaje):
        st.error(mensaje)