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
    
    choose = st.sidebar.radio("Choose what you went to do with your data", ["Data Modification", "Data Visualisation"], horizontal=True)

    if choose == "Data Modification":
        st.title("Data Modification")
        
        selected = df.columns
        start, end = (0, len(df))
        filtered_df = df.copy()
        if st.checkbox('Active columns selector', True):
            selected = st.multiselect("Unselect columns", df.columns, default=df.columns)
            
        if "deleted_rows" not in st.session_state:
            st.session_state.deleted_rows = []
        if 'filters' not in st.session_state:
            st.session_state.filters = []
        if 'row_range' not in st.session_state:
            st.session_state.row_range = (0, len(df))

        if st.checkbox('Active value filter', True):

            col = st.selectbox("Select column", ["None"] + df.columns.tolist())

            if col != "None":
                value = st.selectbox("Select value", df[col].unique().tolist())

                if st.button("Add Filter"):
                    if (col, value) not in st.session_state.filters:
                        st.session_state.filters.append((col, value))

            if st.session_state.filters:
                filters_display = [f"{col}: {val}" for col, val in st.session_state.filters]
                selected_filters = st.multiselect("Filters apply :", filters_display, default=filters_display)

                st.session_state.filters = [(col, val) for col, val in st.session_state.filters if f"{col}: {val}" in selected_filters]

                filtered_df = df.copy()
                for col, val in st.session_state.filters:
                    filtered_df = filtered_df[filtered_df[col] == val]

            else:
                st.write("Any filters apply.")
                
        if st.checkbox('Active row filter', True):
            max_rows = len(filtered_df)

            if st.session_state.row_range[1] > max_rows:
                st.session_state.row_range = (0, max_rows)

            st.session_state.row_range = st.slider(
                "Select quantity rows",
                0, max_rows,
                st.session_state.row_range
            )

            start, end = st.session_state.row_range
            filtered_df = filtered_df.iloc[start:end]
        
        if st.checkbox('Active delete rows', True):
            row_indices = st.multiselect("Select rows to delete", filtered_df.index.tolist())

            for idx in row_indices:
                st.session_state.deleted_rows.append(filtered_df.loc[idx].to_dict())
            filtered_df.drop(index=row_indices, inplace=True)

        if st.checkbox('Active rename column', True):
            col1, col2 = st.columns([1, 2])
            with col1:
                column_to_rename = st.selectbox("Select column to rename", filtered_df.columns.tolist())
            with col2:
                new_column_name = st.text_input("Enter new column name", value=column_to_rename)
            
            if st.button("Rename Column"):
                if new_column_name and column_to_rename in filtered_df.columns:
                    filtered_df.rename(columns={column_to_rename: new_column_name}, inplace=True)
                    selected = [new_column_name if col == column_to_rename else col for col in selected]
                    st.success(f"Column '{column_to_rename}' renamed to '{new_column_name}'")
                    
        edited_df = st.data_editor(filtered_df[selected])
    
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