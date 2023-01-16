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

#Title
st.markdown("<h1 style='text-align: center; color: White;'>Gráfico de Barras de calor </h1>", unsafe_allow_html=True)

#@st.cache(allow_output_mutation=True)
def load_data(filename: str):
    return pd.read_csv(filename, sep=";")

datos = load_data("cintia.csv")

st.sidebar.image("logo.jpeg")

st.markdown("# Cantidad de ID's de usuarios por hora")
#@st.cache
def grafico_bar_plot(data_grafico):
    #cantidad_matriculas_zonas = data_grafico.groupby(["MUNICIPIO"])[["TOTAL_MATRICULA"]].count()
    #cantidad = np.sort(cantidad_matriculas_zonas["TOTAL_MATRICULA"].unique())
    #municipios = data_grafico["MUNICIPIO"].unique()
    fig = px.bar(
        data_grafico.groupby(["HOUR"])[["IDENTIFICACION"]].count()
        .sort_values(by="IDENTIFICACION"),
        #color_continuous_scale=px.colors.sequential.bluered,
        color_discrete_sequence=["green"],
        y = "IDENTIFICACION"
    )
    return fig
    
            

varfig2 = grafico_bar_plot(datos)
st.plotly_chart(
        varfig2,
        use_container_width=True
    )


st.markdown("# Cantidad de ID's de usuarios por programa")

prog = st.selectbox(label="Busqueda por Programa", options=datos["PROGRAMA"].unique())

@st.cache(allow_output_mutation=True)
def grap(df,ps):
    df = df.dropna()
    df = df[df["PROGRAMA"]==ps]
    fig =  px.bar(
        df.groupby(["PROGRAMA"])[["IDENTIFICACION"]].count(),
        color_discrete_sequence=["green"],
        y ="IDENTIFICACION",
        log_y=True)
    return fig

st.plotly_chart(
    grap(datos,prog),
    use_container_width=True,
)
       