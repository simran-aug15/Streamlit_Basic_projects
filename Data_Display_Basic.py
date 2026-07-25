import streamlit as st
import pandas as pd
st.title("Data Display")
df=pd.DataFrame({
    "Name":["Simran","Samar"],
    "Marks":[90,89]
})
st.dataframe(df)
