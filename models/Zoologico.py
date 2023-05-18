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
        for habitat in self.habitats:
            if habitat.dieta == animal.dieta.tipoDieta and (habitat.cantAnimales)+1 <= habitat.cantMaxAnimales and habitat.minTemperatura <= animal.temperatura and habitat.maxTemperatura >= animal.temperatura:
                texto = habitat.nombre + " - " + habitat.dieta
                opciones.append(texto)
        opcion = st.selectbox(
            "Escoge el habitat al que vas a agregar el animal",
            opciones,
            key="listaHabitats"
        )
        st.write('Seleccionaste:', opcion)

        if opcion:
            st.session_state["opcion_elegida_habitat"] = self.habitats[opciones.index(opcion)-1]
            return self.habitats[opciones.index(opcion)-1]
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
                    if str(animal.id) + " - " + animal.nombre + " - " + animal.dieta.tipoDieta == opcion:
                        st.session_state["opcion_animal_zoo"] = animal
                        return animal
        else:
            return None


    def buscarAnimalHabitatsID(self, id):
        for habitat in self.habitats:
            if habitat.animales[id]:
                return habitat.animales[id]