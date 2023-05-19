# -*- coding: utf-8 -*-
import streamlit as st
class Zoologico:
    def __init__(self, nombre = ""):
        self.nombre = nombre
        if "idAnimal":
            if "idAnimal" in st.session_state:
                self.idAnimal = st.session_state["idAnimal"]
            else:
                self.idAnimal = 1
                st.session_state["idAnimal"] = 1

        if "idHabitat":
            if "idHabitat" in st.session_state:
                self.idHabitat = st.session_state["idHabitat"]
            else:
                self.idHabitat = 1
                st.session_state["idHabitat"] = 1

        if "habitats":
            if "habitats" in st.session_state:
                self.habitats = st.session_state["habitats"]

            else:
                self.habitats = []
                st.session_state["habitats"] = []

        if "registro":
            if "registro" in st.session_state:
                self.registro = st.session_state["registro"]

            else:
                self.registro = []
                st.session_state["registro"] = []


    def agregarHabitat(self, Habitat):
        self.habitats.append(Habitat)
        st.session_state["habitats"] = self.habitats

    def agregarAnimalRegistro(self, animal):
        self.registro.append(animal)
        st.session_state["registro"] = self.registro

    def eliminarAnimalRegistro(self, animal):
        self.registro.remove(animal)
        st.session_state["registro"] = self.registro

    def listarHabitats(self, animal):
        opciones = [""]
        posicionesHabitat = []
        for habitat in self.habitats:
            if habitat.dieta == animal.dieta.tipoDieta and (habitat.cantAnimales)+1 <= habitat.cantMaxAnimales and habitat.minTemperatura <= animal.temperatura and habitat.maxTemperatura >= animal.temperatura:
                texto = habitat.nombre + " - " + habitat.dieta
                posicionesHabitat.append(habitat.id)
                opciones.append(texto)
        opcion = st.selectbox(
            "Escoge el habitat al que vas a agregar el animal",
            opciones,
            key="listaHabitats"
        )
        st.write('Seleccionaste:', opcion)

        if opcion:
            numeroHabitat = posicionesHabitat[opciones.index((opcion))-1]
            st.session_state["opcion_elegida_habitat"] = self.habitats[numeroHabitat-1]
            return self.habitats[numeroHabitat-1]
        else:
            return None

    def listarAnimalesRegistro(self):
        opciones = [""]
        for animal in self.registro:
                texto = "ID: " + str(animal.id) + " - " + "Nombre: " + animal.nombre + " - "  + "Dieta: " + animal.dieta.tipoDieta
                opciones.append(texto)
        opcion = st.selectbox(
            "Escoge el animal que quieres aregar al habitat",
            opciones,
            key ="listaAnimales"
        )
        st.write('Seleccionaste:', opcion)

        if opcion:
            st.session_state["opcion_elegida_animal"] = self.registro[opciones.index(opcion)-1]
            return self.registro[opciones.index(opcion)-1]
        else:
            return None

    def listarAnimalesHabitats(self, mensaje):
        opciones = [""]
        for habitat in self.habitats:
            for animal in habitat.animales:
                texto = "ID: " + str(animal.id) + " - " + "Nombre: " +  animal.nombre + " - " + "Dieta: " +  animal.dieta.tipoDieta
                opciones.append(texto)
        opcion = st.selectbox(
            mensaje,
            opciones,
            key="listaAnimalesHabitats"
        )

        if opcion:
            for habitat in self.habitats:
                for animal in habitat.animales:
                    if "ID: " + str(animal.id) + " - " + "Nombre: " +  animal.nombre + " - " + "Dieta: " +  animal.dieta.tipoDieta == opcion:
                        st.session_state["opcion_animal_zoo"] = animal
                        return animal
        else:
            return None


    def mostrarTodoZoo(self):
        st.divider()
        if self.habitats:
            st.subheader("Lista de habitats creados y su información")
            for habitat in self.habitats:
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