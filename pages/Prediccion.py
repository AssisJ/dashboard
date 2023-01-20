import streamlit as st
import requests
import pandas as pd
#Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
st.sidebar.image("logo.jpeg")

st.markdown("<h1 style='text-align: center; color: White;'>Predicción </h1>", unsafe_allow_html=True)

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")

datos = cargar_datos("cintia.csv")
@st.cache
def convert(dat):        
    if dat.isnumeric():
        dat = int(dat)
    else:
        st.markdown('El dato ingresado no es un número')
    return dat



st.markdown('La selección de datos escogidos, tales como: IDENTIFICACION, el cual es el numero generado para identificar la sesión del usuario, el TIMECREATED, que viene siendo el tiempo en el que se creo la sesión, HOUR, que es la hora en la que entro el usuario, ORIGIN, es el medio por el cual el usaurio inicio sesión y el PROGRAMA el cual es el programa academico al que pertenece el usuario. Estos datos nos permitirá predecir de forma casi exacta el mejor día que el usuario puede iniciar sesión.')


dv = st.text_input('Identificación','1000000000',max_chars=12)
tm = st.text_input('Tiempo de creación','10000000000',max_chars=12)


IDENTIFICACION = convert(dv)
TIME = convert(tm)
HOUR = st.slider(label= "Hora de Entrada", min_value=0, max_value=23, value=23)
ORIGIN = st.selectbox(label="Origen", options=["web","cli"])
PROGRAMA = st.selectbox(label="Programas Universitarios", options=['INGENIERIA AMBIENTAL', 'LICENCIATURA EN EDUCACION INFANTIL',
        'INGENIERIA MECANICA', 'QUIMICA', 'ADMINISTRACION EN SALUD','ACUICULTURA', 'DPTO DE INGENIERIA AMBIENTAL',
        'LIC EN LITERATURA Y LENGUA CASTELLANA', 'INGENIERIA DE ALIMENTOS','MEDICINA VETERINARIA Y ZOOTECNIA', 'INGENIERIA DE SISTEMAS',
        'DEPARTAMENTO DE INGENIERIA DE ALIMENTOS', 'MATEMATICAS','DEPARTAMENTO DE QUIMICA',
        'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNAC','FISICA', 'GEOGRAFIA',
        'INGENIERIA INDUSTRIAL', 'DPTO CIENCIAS ADMINISTRATIVAS',
        'INGENIERIA AGRONOMICA', 'DEPARTAMENTO DE CIENCIAS PECUARIAS',
        'DEPARTAMENTO DE GEOGRAFIA Y MEDIO AMBIEN',
        'LIC EN LENGUAS EXTRAN CON ENFA EN INGLES',
        'DEPARTAMENTO DE IDIOMAS EXTRANJEROS',
        'DEPARTAMENTO DE INFORMATICA EDUCATIVA',
        'LICENCIATURA EN EDUCACION INFANTIL', 'ENFERMERIA',
        'DPTO DE ING DE SISTEMAS Y TELECOMUNICACI', 'DERECHO',
        'LICENCIATURA EN INFORMATICA','TECNOLOGIA EN REGENCIA DE FARMACIA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADISTIC',
        'LIC. EDUCACION FISICA RECREACION Y DEPOR', 'ESTADISTICA',
        'LIC EN CIENCIAS NATURALES Y EDU AMBIENTA', 'BACTERIOLOGIA',
        'CINTIA', 'DEPARTAMENTO DE SALUD PUBLICA', 'BIOLOGIA',
        'DEPARTAMENTO DE BIOLOGIA', 'DIPLOMADO ETHICAL HACKING',
        'DEPARTAMENTO DE REGENCIA Y FARMACIA',
        'DEPARTAMENTO DE INGENIERIA MECANICA', 'LIC EN CIENCIAS SOCIALES',
        'LIC EN INFORMATICA', 'DEPARTAMENTO DE PSICOPEDAGOGIA',
        'BACTERIOLOGIA', 'LIC EN EDUC BASICA CON ENF HUM LENG CAST',
        'LIC EN EDUCACION ARTISTICA',
        'LICENCIATURA EN INFORMATICA Y MEDIOS AUD',
        'DPTO DE ING AGRONOMICA Y DESARROLL RURAL',
        'DPTO INGENIERIA INDUSTRIAL', 'ING SISTEMAS',
        'DEPARTAMENTO DE FISICA Y ELECTRONICA',
        'DEPARTAMENTO DE CIENCIAS JURIDICAS',
        'DEPARTAMENTO DE INGENIERIA INDUSTRIAL',
        'DEPARTAMENTO DE ENFERMERIA', 'DEPARTAMENTO DE BACTERIOLOGIA',
        'DPTO DE ING. AMBIENTAL', 'DPTO DE CIENCIAS NATURALES',
        'LIC EN EDUC BASICA CON ENF EN HUMAN INGL',
        'ADMINISTRACION EN FINANZAS Y NEGOCIOS INTERNACIONALES',
        'DPTO DE CULTURA FISICA, RECREAC Y DEPORT', 'ENFERMERIA',
        'DEPARTAMENTO DE ARTES', 'FUNCIONARIOS TEMPORALES',
        'DEPARTAMENTO DE CIENCIAS ACUICOLAS',
        'DEPARTAMENTO DE ESPAÑOL Y LITERATURA', 'DPTO PSICOPEDAGOGIA',
        'REGENCIA DE FARMACIA', 'REGENCIA Y FARMACIA', 'QUIMICA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADISTICAS',
        'DEPARTAMENTO DE INFORMATICA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADIS',
        'DEPARTAMENTO DE CIENCIAS SOCIALES', 'CIENCIAS',
        'LICENCIATURA EN EDUCACIÓN INFANTIL ', 'DPTO DE BIOLOGIA',
        'INGENIERIA AGRONOMICA', 'LIC. EN INFORMATICA ',
        'MEDICINA VETERINARIA', 'LIC. EN INFORMATICA',
        'LICENCIATURA EN INGLES',
        'DPTO DE ING DE SISTEMAS Y TELECOMUNICACIONES', 'ESTADI\xadSTICA',
        'LIC. EN INFORMATICA Y MEDIOS AUDIOVISUALES',
        'INGENIERIA AGRONOMICA', 'DPTO BACTEROLOGÍA',
        'INGENIERIA AMBIENTAL',
        'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNACIONALES',
        'ADMON FINANZAS Y NEGOCIOS INTERNACIONALES',
        'TEC PROF EN MANEJO Y CONSERV DE PROD AGR', 'ACUICULURA',
        'BIOLOGIA', 'DPTO DE CULTURA FISICA, RECREAC Y DEPORTES', 'FISICA',
        'LIC EN EDUC BASICA CON ENF EN CIEN SOCIA',
        'LIC EN CIENCIAS NATURALES Y EDU AMBIENTAL',
        'ADMINISTRACION EN SALUD',
        'OFICINA DE BIBLIOTECAS Y RECURSOS EDUCATIVOS',
        'IDIOMAS EXTRANJEROS CON ENFASIS EN INGLES', 'LIC. EN INFORMATICA',
        'PRUEBAS', 'INGENIERIA DE ALIMENTO', 'QUI\xadMICA',
        'INGENIERIA AGRONOMICA ', 'CIENCIAS ADMINISTRATIVAS',
        'DIVISION DE BIBLIOTECAS Y RECURSOS EDUCATIVOS BIBLIOTECA CENTRAL "MISAEL DIAZ URZOLA"',
        'QUIMICA ', 'DECANATURA/GESTOR DE CALIDAD',
        'DPTO MEDICINA VETERINARIA Y ZOOTECNIA',
        'DPTO INGENIERIA AMBIENTAL', 'GEOGRAFIA', 'INGENIERIA AGRONOMIA',
        'LIC. EDUCACION BASICA ENFASIS ARTISTICA', 'VETERINARIA',
        'ADMINISTRACION EN FINANZAS Y NEGOCIOS INTERNACIONALES ',
        'DIVISION DE POSTGRADOS Y EDUCACION CONTINUADA',
        'FUNCIONARIOS ADM. PLANTA', 'INGENIERIA AMBIENTAL ',
        'DEPARTAMENTO DE INGENIERIA AMBIENTAL',
        'DPTO DE GEOGRAFIA Y MEDIO AMBIENTE', 'ING AMBIENTAL'])

request_data = [
    {
        "IDENTIFICACION": IDENTIFICACION,
        "TIMECREATED": TIME,
        "HOUR": HOUR,
        "ORIGIN": ORIGIN,
        "PROGRAMA": PROGRAMA
    }
]

url_api = "https://apidiplo-bhgjakfgjq-uc.a.run.app/predict"
data = str(request_data).replace("'", '"')
pred= requests.post(url=url_api, data=data).text
#st.write(pred)
st.metric(
    value=f'{pd.read_json(pred)["DAY"][0]}',
    label="La predicción del día es: ")
