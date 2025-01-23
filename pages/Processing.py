import streamlit as st 
import pandas as pd

upload = st.file_uploader("Choose file", type="csv")
if upload != None:
    
    df = pd.read_csv(upload, delimiter=";")
    
    columns = df.columns
    
    selected = st.multiselect("Select columns", columns)
    
    edited_df = st.data_editor(df[selected])
    
    st.download_button(
        label="Download",
        data=edited_df.to_csv(),
        file_name="large_df.csv",
        mime="text/csv"
    )