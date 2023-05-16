import streamlit as st
class Zoologico:
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.idAnimal = 1
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

    def listarHabitats(self):
        opciones = [""]
        for habitat in self.habitats:
            opciones.append(habitat.nombre)
        opcion = st.selectbox(
            "Escoge el animal que quieres aregar al habitat",
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
            opciones.append(animal.nombre)
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

    def listarAnimalesHabitats(self):
        for habitat in self.habitats:
            habitat.listarAnimales()

    def buscarAnimalHabitatsID(self, id):
        for habitat in self.habitats:
            if habitat.animales[id]:
                return habitat.animales[id]