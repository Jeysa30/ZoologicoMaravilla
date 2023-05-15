# -*- coding: utf-8 -*-
import views.viewZoologico as viewZoo
import streamlit as st


if __name__ == '__main__':
    st.set_page_config(
        page_title= "Zoológico Maravilla",
        page_icon= "🐨",
        layout= "wide",
    )

    zoo = viewZoo.Zoo()
    zoo.menuZoo()