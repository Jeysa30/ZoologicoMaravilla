# -*- coding: utf-8 -*-
import streamlit as st

#Creamos la clase del zoológico como model, ya que esta se hara cargo de guardar 3 cosas: los habitat creados, los animales que no estan
# agregados a ningún habitat y los ID correspondientes a cada habitat y a cada animal.
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

    #Este metodo estara a cargo de eliminar un animal del registro del zoológico ya que pasara a estar guardado en un habitat
    #seleccionado por el usuario.
    def eliminarAnimalRegistro(self, animal):
        self.registro.remove(animal)
        st.session_state["registro"] = self.registro

    #Este metodo permitira listar los habitats que el usuario puede escoger dependiendo de la temperatura y dieta
    # del animal seleccionado anteriormente para guardarlo.
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

    #Este metodo le muestra al usuario los animales que no estan en ningún habitat permitiendo seleccionarlo para poder agregarlo a uno.
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

    #En este metodo listara los animales que hay en cada habitat.
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
