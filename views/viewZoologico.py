# -*- coding: utf-8 -*-
import controllers.controllerZoologico as zooController
import models.Zoologico as zooModel
import streamlit as st

class Zoo:
    def __init__(self):
        ZoologicoMaravilla = zooModel.Zoologico("Zoologico Maravilla")
        controlador = zooController.ZoologicoController(ZoologicoMaravilla, self)

    def menuZoo(self):
        st.markdown(
            f"<h1 style='text-align: center; color: green;'>BIENVENIDO AL ZOOLÓGICO MARAVILLA</h1>",
            unsafe_allow_html=True,
        )

        expander = st.expander("ZOO")
        with expander:
            boton_crear_habitat = st.button("Crea un habitat", 1)
            boton_crear_animal = st.button("Crea un animal", 2)
            boton_agregar_animal = st.button("Agrega un animal a un habitat", 3)
            boton_crear_habitat = st.button("Modifica la alimentación de un animal", 4)
            boton_accion_animal = st.button("Realiza una acción a un animal", 5)
            boton_ver_zoo = st.button("Ver información del zoológico", 6)

        if boton_crear_habitat:
            st.session_state["opcion"] = 1
        elif boton_crear_animal:
            st.session_state["opcion"] = 2
        elif boton_agregar_animal:
            st.session_state["opcion"] = 3
        elif boton_crear_habitat:
            st.session_state["opcion"] = 4
        elif boton_accion_animal:
            st.session_state["opcion"] = 5
        elif boton_ver_zoo:
            st.session_state["opcion"] = 6

        if "opcion" in st.session_state:
            self.controlador.ejecutar_menu(st.session_state["opcion"])

        """
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
        """

    def menuHabitat(self):
        opciones = {
            "Desierto(40 a 60)": 1,
            "Selva(20 a 39)": 2,
            "Acuatico(0 a 19)": 3,
            "Polar(-20 a -1)": 4
        }
        opcion = st.selectbox(
            "Escoge el tipo de habitat",
            tuple(opciones.keys())
        )
        st.write('Seleccionaste:', opcion)

        if opcion:
            st.session_state["opcion_elegida"] = opciones[opcion]
            return opciones[opcion]
        else:
            return None

    #    print("\nHabitats disponibles:")
    #    print("1. Desierto(40 a 60)")
    #    print("2. Selva(20 a 39)")
    #    print("3. Acuatico(0 a 19)")
    #    print("4. Polar(-20 a -1)")
    #    opcion = int(input("Ingrese el habitat que quiere crear: "))
    #    while opcion < 1 or opcion > 4:
    #        opcion = int(input("Ese numero no es valido, vuelva a ingresar uno valido: "))
    #    return opcion

    def elegirDieta(self):
        opcion = st.selectbox(
            "Dietas para el habitat disponibles",
            ("Omnivora", "Carnivora", "Herbivora")
        )

        st.write('Seleccionaste:', opcion)

        if opcion:
            st.session_state["opcion_elegida"] = opcion
            return opcion

        else:
            return None

    #    print("\n Dietas para el ", mensaje, "disponibles:")
    #    print("1. Omnivoro")
    #    print("2. Carnivoro")
    #    print("3. Herbivoro")
    #    dieta = int(input("Ingrese el numero de la dieta: "))
    #    while dieta < 1 or dieta > 3:
    #        dieta = int(input("Ese numero no es valido, vuelva a ingresar el numero de la dieta: "))
    #    if dieta == 1: return "Omnivoro"
    #    elif dieta == 2: return "Carnivoro"
    #   elif dieta == 3: return "Herbivoro"

    def solicitar_dato(mensaje):
        return st.number_input(mensaje, value = 0)

    def menuAlimento(self):
        print("\n--Modificaciones de los alimentos del animal: ")
        print("1. Agregar una nueva comida." )
        print("2. Eliminar alguna comida.")

    def menuAccion(self):
        print("\n--Acciones que puede realizar el animal ")
        print("1. Comer.")
        print("2. Dormir.")
        print("3. Jugar.")

    def mensajeExitoso(self, mensaje):
        st.success(mensaje)

    def mensajeError(self, mensaje):
        st.error(mensaje)