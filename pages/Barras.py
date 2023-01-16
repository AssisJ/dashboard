import streamlit as st
import pandas as pd
import plotly.express as px

#Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
st.sidebar.image("logo.jpeg")

#Title
st.markdown("<h1 style='text-align: center; color: White;'>Gráficos de Barras </h1>", unsafe_allow_html=True)
#Loading data
@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")


datos = cargar_datos("cintia.csv")

st.markdown("# Cantidad de ID's de usuarios por los días de la semana.")

@st.cache(allow_output_mutation=True)
def graph_bar(df):
    fig =  px.bar(
        df.groupby(["DAY"])[["IDENTIFICACION"]].count()
        .reset_index(),
        color_discrete_sequence=["green"],
        x="DAY",
        y ="IDENTIFICACION",
        log_y=True)
    return fig

st.plotly_chart(
    graph_bar(datos),
    use_container_width=False, 
)

st.markdown("# Cantidad de ID's de usuarios por Origen.")

@st.cache(allow_output_mutation=True)
def graph_bar1(df):
    fig =  px.bar(
        df.groupby(["ORIGIN"])[["IDENTIFICACION"]].count(),
        color_discrete_sequence=["green"],
        y ="IDENTIFICACION",
        log_y=True)
    return fig

st.plotly_chart(
    graph_bar1(datos),
    use_container_width=False, 
)

