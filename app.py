import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Ecommerce Sales Analysis Dashboard\n")

data =pd.read_csv("supermarket_sales.csv.csv")

#st.dataframe(data)

def load_data(file_path):

    data = pd.read_csv(filepath)
    data["Date"] = pd.to_datetime(df["Data"], errors = "coerce")
    data = data.dropna(subset=["Date"])
    return data

data_path = "./supermarket_sales.csv.csv"

data = load_data(data_path)
