import streamlit as st
import pandas as pd
import plotly.express as px
#from globals import mes_seleccionado
import globals

from backend import  pt1_trans, lista_meses, filtrar_mes, graf_pt1



st.set_page_config(layout='centered')

if 'mes_seleccionado' not in st.session_state: st.session_state.mes_seleccionado= None


#elementos de la barra lateral

st.sidebar.text('Opciones')
#seleccion del año completo o por meses
rango=st.sidebar.radio("Seleccionar rango temporarl", ['Año completo', 'Por meses'], key="rango_temporal")
if rango =='Por meses' : 
    st.sidebar.selectbox('Seleccionar mes', lista_meses, key='mes_seleccionado')
elif rango=='Año completo':
    st.session_state.mes_seleccionado=None  


globals.mes_seleccionado=st.session_state.mes_seleccionado
df_filtrado = filtrar_mes(globals.mes_seleccionado)

st.sidebar.write("st.session_state object:", st.session_state)




## Datos de la página principal
st.title("Telemindex 2024 webapp")
st.text("Tu aplicación para saber los precios minoristas de indexado")
st.text("Copyright by Jose Vidal")

pt1_trans2=pt1_trans()
graf_pt2=graf_pt1()

st.plotly_chart(graf_pt2)
if st.checkbox ('Mostrar tabla de datos'): 
    st.write(pt1_trans2)

