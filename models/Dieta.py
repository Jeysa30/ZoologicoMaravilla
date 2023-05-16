import streamlit as st

class Dieta:
    def __init__(self, tipoDieta = ""):
        if "TipoDieta":
            if "TipoDieta" in st.session_state:
                self.tipoDieta = tipoDieta
            else:
                self.tipoDieta = tipoDieta
        if "AlimentoAnimal":
            if "AlimentoAnimal" in st.session_state:
                self.alimento = st.session_state["AlimentoAnimal"]
            else:
                self.alimento = []
        if "AlimentoAnimalPosibles":
            if "AlimentoAnimalPosibles" in st.session_state:
                self.posiblesAlimentos = st.session_state["AlimentoAnimalPosibles"]
            else:
                self.posiblesAlimentos = []

    def listaDieta(self):
        if (self.tipoDieta == "Omnivoro"):
            self.alimento = ["carne", "pescado", "futas", "verduras"]
            self.posiblesAlimentos = ["aves", "insectos", "huevos", "gusanos", "hojas", "raices", "flores", "nectar", "polen",
                                      "corteza", "miel"]

        elif (self.tipoDieta == "Carnivoro"):
            self.alimento = ["carne", "pescado", "presas"]
            self.posiblesAlimentos = ["aves", "insectos", "huevos", "gusanos"]

        elif (self.tipoDieta == "Herbivoro"):
            self.alimento = ["hierva", "frutas", "vegetales"]
            self.posiblesAlimentos = ["hojas", "raices", "flores", "nectar", "polen", "corteza"]

    def agregarAlimento(self, alimento, lista):
        lista.append(alimento)

    def eliminarAlimento(self, alimento, lista):
        lista.remove(alimento)

    def listarAlimentos(self):
        listaAlimentos = [""]
        for alimento in self.alimento:
            listaAlimentos.append(alimento)
        seleccionar_alimento = st.selectbox(
            "Escoge el alimento que le vas a dar al animal",
            listaAlimentos,
            key="listaAlimentos"
        )
        st.write('Seleccionaste:', seleccionar_alimento)

        if seleccionar_alimento:
            st.session_state["seleccionar_alimento"] = seleccionar_alimento
            return seleccionar_alimento
        else:
            return None

    def listaTipoAlimento(self):
        listaAlimentosPosibles = [""]
        for alimentoPosibles in self.posiblesAlimentos:
            listaAlimentosPosibles.append(alimentoPosibles)
        seleccionar_alimento_posible = st.selectbox(
            "Escoge el alimento que le vas a agregar al animal",
            listaAlimentosPosibles,
            key="listaAlimentosPosibles"
        )
        st.write('Seleccionaste:', seleccionar_alimento_posible)

        if seleccionar_alimento_posible:
            st.session_state["seleccionar_alimento_posible"] = seleccionar_alimento_posible
            return seleccionar_alimento_posible
        else:
            return None