import streamlit as st

class Habitat:
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0):
        self.nombre = nombre
        self.animales = []
        self.maxTemperatura = maxTemperatura
        self.minTemperatura = minTemperatura
        self.cantMaxAnimales = cantMaxAnimales
        self.dieta = dieta
        self.cantAnimales = 0

    def agregarAnimal(self, Animal):
        self.animales.append(Animal)
        st.session_state["animalesHabitat"] = self.animales

    def listarAnimales(self):
        st.write(f"Lista de animales:")
        for animal in self.animales.values():
            st.write(f"Nombre: {animal.nombre} --- ID: {animal.id}")


class Desertico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, captus = 0, agua = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.captus = captus
        self.agua = agua


class Selvatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, arboles = 0, rios = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.arboles = arboles
        self.rios = rios


class Acuatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, algas = 0, corales = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.algas = algas
        self.corales = corales


class Artico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, glaciares = 0, iglus = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales)
        self.glaciares = glaciares
        self.iglus = iglus