import streamlit as st 
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="TP du 23/01 aprem",
    page_icon="😎",
    layout="wide",
)

st.sidebar.title("Affichage d'une page web dans Streamlit")

# Ajouter un champ pour permettre à l'utilisateur d'entrer une URL personnalisée
custom_url = st.sidebar.text_input("Entrez une URL pour l'afficher :", "")

if custom_url:
        st.markdown(
        f'<iframe src="{custom_url}" width="100%" height="1000px" style="border:none; overflow:auto;"></iframe>',
        unsafe_allow_html=True
    )