import streamlit as st
import pandas as pd

st.markdown(
    "<style>img{max-width: 100%; height: auto;}</style>", 
    unsafe_allow_html=True
)

st.title("Mental Health Monitor")

# Function to upload CSV file
def upload_csv():
    uploaded_file = st.file_uploader("Upload a dataset in CSV format", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Column Names:", df.columns.tolist())

# Function to upload Excel file
def upload_excel():
    uploaded_file = st.file_uploader("Upload a dataset in Excel format", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Column Names:", df.columns.tolist())

# Main code
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://cdn.pixabay.com/photo/2017/01/30/02/20/mental-health-2019924_1280.jpg")
with col2:
    upload_csv()
    upload_excel()
