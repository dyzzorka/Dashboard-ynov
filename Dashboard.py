import streamlit as st 
import pandas as pd
import seaborn as sns


st.set_page_config(
    page_title="My Dashboard",
    page_icon="😎",
    layout="wide",
)

df = pd.read_csv("https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv")

st.title('My Dashboard')

st.subheader('Presentation de data')

st.write('Presentation des data avec streamlit')

if st.checkbox('Afficher le df'):

    st.write(df)

if st.checkbox('Afficher le formulaire'):

    name = st.text_input('Entrez votre nom')
    if name != "":
        st.write(f"Salut, {name}")
        
st.sidebar.image("https://cdn.cookielaw.org/logos/09f2ba89-076e-413b-b34f-a8d20370f3f5/35c98a5f-cba8-4b1a-959f-c5a7c260dfda/e0191cfb-2e2a-43c1-a11f-929eb86731a0/logo.png", width=300)

st.sidebar.video("https://www.youtube.com/watch?v=LUcyjBQy3vc")


with st.form(key='my_form'):
    
    col1, col2 = st.columns(2)
    
    with col1:
        profession = st.selectbox("Selectioné une profession", df.Profession.unique())
        
        age = st.slider("Selectionnez un age", df.Age.min(), df.Age.max(), (df.Age.min(), df.Age.max()))
        valid = st.form_submit_button("Valider")
        
    with col2:
        data_age = df[(df['Profession'] == profession) & (df['Age'] >= age[0]) & (df['Age'] <= age[1])].Age

        if valid:
            plot = sns.histplot(data_age, bins=age[1]-age[0])
            st.pyplot(plot.figure)