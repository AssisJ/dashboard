import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd
import numpy as np
# Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
#@st.cache(allow_output_mutation=True)
def load_data(filename: str):
    return pd.read_csv(filename, sep=";")

datos = load_data("cintia.csv")

st.sidebar.image("logo.jpeg")
st.markdown("# Cantidad de ID's por hora")
#@st.cache
def grafico_bar_plot(data_grafico):
    #cantidad_matriculas_zonas = data_grafico.groupby(["MUNICIPIO"])[["TOTAL_MATRICULA"]].count()
    #cantidad = np.sort(cantidad_matriculas_zonas["TOTAL_MATRICULA"].unique())
    #municipios = data_grafico["MUNICIPIO"].unique()
    fig = px.bar(
        data_grafico.groupby(["HOUR"])[["IDENTIFICACION"]].count()
        .sort_values(by="IDENTIFICACION"),
        color = "IDENTIFICACION",
        #color_continuous_scale=px.colors.sequential.bluered,
        color_continuous_scale = "bluyl",
        y = "IDENTIFICACION"
    )
    return fig
    
            

varfig2 = grafico_bar_plot(datos)
st.plotly_chart(
        varfig2,
        use_container_width=True
    )
col1, col = st.columns(2)
with col1:
    st.markdown("estoy con cule hambre")
        