import streamlit as st
#Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
st.sidebar.image("logo.jpeg")

st.markdown("<h1 style='text-align: center; color: White;'>INTEGRANTES </h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h1 style='text-align: center; color: White;'>Álvaro José Assis Arciria </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: White;'>Carlos Andrés tajan Ruiz </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: White;'>Fabricio Javier Durango Falo </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: White;'>Jonathan Esteban castro padilla  </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: White;'>Marcos David García negrete  </h1>", unsafe_allow_html=True)
st.balloons()