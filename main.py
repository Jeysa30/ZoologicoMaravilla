# -*- coding: utf-8 -*-
import views.viewZoologico as viewZoo
import streamlit as st


if __name__ == '__main__':
    #Configuración inicial de la pagina a visualizar mediante la libreria de streamlit
    st.set_page_config(
        page_title= "Zoológico Maravilla",
        page_icon= "🐨",
        layout= "wide",
    )

    #Se hace el llamado del menu para lograr su ejecución y visualización al usuario
    zoo = viewZoo.Zoo()
    zoo.menuZoo()