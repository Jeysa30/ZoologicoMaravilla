import streamlit as st

#La creación de la clase habitat(que es la clase padre) como model, es el que guardara el animal según su temperatura y dieta a un habitat especifico(ya que el habitat
# tambien cuenta con atributo de temperatura fijo para 4 tipos de habitat, pero que pueden crearce más habitat según el tipo de dieta
# que el usuario quiere que se maneje en dicho habitat).
class Habitat:
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, id = 0):
        self.nombre = nombre
        self.animales = []
        self.maxTemperatura = maxTemperatura
        self.minTemperatura = minTemperatura
        self.cantMaxAnimales = cantMaxAnimales
        self.dieta = dieta
        self.cantAnimales = 0
        self.id = id

    def agregarAnimal(self, Animal):
        self.animales.append(Animal)
        st.session_state["animalesHabitat"] = self.animales

#Hacemos uso de herencia en la clase de habitat para los 4 tipos de habitats que pueden haber en el zoológico, con su temperatura
# ya fija, y con otros 2 atributos haciendo referencia a su habitat
class Desertico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, id = 0, captus = 0, agua = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales, id)
        self.captus = captus
        self.agua = agua


class Selvatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, id = 0, arboles = 0, rios = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales, id)
        self.arboles = arboles
        self.rios = rios


class Acuatico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, id = 0, algas = 0, corales = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales, id)
        self.algas = algas
        self.corales = corales


class Artico(Habitat):
    def __init__(self, nombre = "", maxTemperatura = 0, minTemperatura = 0, dieta = "", cantMaxAnimales = 0, id = 0, glaciares = 0, iglus = 0):
        super().__init__(nombre, maxTemperatura, minTemperatura, dieta, cantMaxAnimales, id)
        self.glaciares = glaciares
        self.iglus = iglus