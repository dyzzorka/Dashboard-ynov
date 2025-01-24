import streamlit as st 
import pandas as pd
import seaborn as sns
import json
import requests

st.set_page_config(
    page_title="TP du 23/01 aprem",
    page_icon="😎",
    layout="wide",
)
api_url = st.sidebar.text_input("Entrez une URL pour l'api :", "")

api_url+= "/predict"

with st.form('predictform', False):
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=0, max_value=100, value=22)
    graduated = st.selectbox("Graduated", ["Yes", "No"])
    profession = st.selectbox("Profession", ["Artist", "Lawyer", "Marketing", "Doctor", "Executive", "Engineer", "Healthcare", "Entertainment", "Homemaker", "Other"])
    work_experience = st.number_input("Work Experience (years)", min_value=0, max_value=50, value=1)
    spending_score = st.selectbox("Spending Score", ["Low", "Average", "High"])
    family_size = st.number_input("Family Size", min_value=1, max_value=20, value=4)
    segmentation = st.selectbox("Segmentation", ["A", "B", "C", "D"])
    
    if st.form_submit_button("Soumettre"):
        data = {
            "Gender": gender,
            "Age": age,
            "Graduated": graduated,
            "Profession": profession,
            "Work_Experience": work_experience,
            "Spending_Score": spending_score,
            "Family_Size": family_size,
            "Segmentation": segmentation
        }
        
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(api_url, headers=headers,json=data)
        if response.status_code == 200:
            st.success("Données envoyées avec succès !")
            
            if response.content == "b'1'":
                st.write("Married") 
            else :
                st.write("Not married") 
        else:
            st.error(f"Erreur lors de l'envoi: {response.status_code} {response.content}")
