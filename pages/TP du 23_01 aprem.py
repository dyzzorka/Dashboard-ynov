import streamlit as st 
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="TP du 23/01 aprem",
    page_icon="😎",
    layout="wide",
)

upload = st.sidebar.file_uploader("Choose .csv file", type="csv")

if upload != None:
    df = pd.read_csv(upload)
    
    choose = st.sidebar.radio("Choose wath u went to do with ur data", ["Data Modification", "Data Visualisation"], horizontal=True)

    if choose == "Data Modification":
        st.title("Data Modification")
        
        selected = df.columns
        lenrows = (0, len(df))
        filtered_df = df
        
        if st.checkbox('Display columns selector', True):
            selected = st.multiselect("Unselect columns", df.columns, default=df.columns)
        
        if st.checkbox('Display row filter', True):
            lenrows = st.slider("Select quantity rows", 0, len(df), (0, len(df)))
            
        if st.checkbox('Diplay value filter', True):
            
            col = st.selectbox("Selectioné une colone", selected.insert(0, "None"))
            if col != "None":
                value = st.selectbox("Selectioné une valeur", df[col].unique().tolist())
                filtered_df = df[df[col] == value]
            
        edited_df = st.data_editor(filtered_df[selected].iloc[lenrows[0]:lenrows[1] + 1])
    
        st.download_button(
            label="Download",
            data=edited_df.to_csv(),
            file_name="large_df.csv",
            mime="text/csv"
        )
    else:
        st.title("Data Visualisation")
        
        col1, col2 = st.columns(2)
    
        with col1:
            profession = st.selectbox("Selectioné une profession", df.Profession.unique())
            
            age = st.slider("Selectionnez un age", df.Age.min(), df.Age.max(), (df.Age.min(), df.Age.max()))
            
            
        with col2:
            data_age = df[(df['Profession'] == profession) & (df['Age'] >= age[0]) & (df['Age'] <= age[1])].Age

            
            plot = sns.histplot(data_age, bins=age[1]-age[0])
            st.pyplot(plot.figure)


else:
    st.sidebar.title("Select your csv for continue")