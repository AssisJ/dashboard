import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import numpy as np
# Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
#@st.cache(allow_output_mutation=True)
def load_data(filename: str):
    return pd.read_csv(filename, sep=";")
st.sidebar.image("logo.jpeg")


datos = load_data("cintia.csv")


st.markdown("<h1 style='text-align: center; color: White;'>BIENVENIDOS </h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("Bienvenidos al Dashboard, en este tablero se mostraran datos los cuales creemos que son relevantes para la toma de desiciones. Los datos utilizados para este análisis tiene por nombre user_loggedin, dicho dataset se encuentra información de las entradas de usuarios al sitio web CINTIA, estos datos tambien cuentan con la información del usuario y programa respectectivo de la Universidad.")

st.markdown("---")
st.markdown("A continación se muestra un gráfico que detalla la cantidad de usuarios por fechas del 2022")

st.markdown("# Cantidad de ID's ordenados por fecha")
def grafico_line(datos_bar):
    datos_bar = datos_bar.set_index("DATECREATED")
    fig = px.line(
        datos_bar.groupby([datos_bar.index])["IDENTIFICACION"]
        .count(),
        color_discrete_sequence=["green"],
        y="IDENTIFICACION",
        #text='IDENTIFICACION',
    )
    return fig
varfig = grafico_line(datos)
st.plotly_chart(
    varfig,
    use_container_width=True
)
