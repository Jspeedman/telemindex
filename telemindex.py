import streamlit as st
import pandas as pd
import plotly.express as px
import globals

from backend import  max_reg, lista_meses, filtrar_mes, aplicar_margen, pt1_trans,graf_pt1, pt5_trans



st.set_page_config(layout='centered')

if 'mes_seleccionado' not in st.session_state: st.session_state.mes_seleccionado= None
if 'margen' not in st.session_state: st.session_state.margen=0

#elementos de la barra lateral

st.sidebar.subheader('Opciones')
#seleccion del año completo o por meses
rango=st.sidebar.radio("Seleccionar rango temporal", ['Año completo', 'Por meses'], key="rango_temporal")
if rango =='Por meses' : 
    st.sidebar.selectbox('Seleccionar mes', lista_meses, key='mes_seleccionado')
    texto_precios = f'Mes seleccionado: {st.session_state.mes_seleccionado}'
elif rango=='Año completo':
    st.session_state.mes_seleccionado=None  
    texto_precios = f'Año 2024, hasta el día {max_reg}'

globals.mes_seleccionado=st.session_state.mes_seleccionado
#ejecutamos la función para obtener el mes seleccionado
#y que sea usado en backend.py


if st.sidebar.checkbox('Marca si quieres añadir margen'):
    globals.margen_aplicado=st.sidebar.slider("Añadir margen al gusto (en €/MWh)", min_value=0, max_value=50,value=0) #key="margen"
    texto_margen=f'Se ha añadido {globals.margen_aplicado} €/MWh'
    st.sidebar.caption(texto_margen)
    #st.session_state.margen
else:
    #st.session_state.margen=0
    globals.margen_aplicado=0  

#globals.margen_aplicado=st.session_state.margen
#aplicar_margen(globals.margen_aplicado)
aplicar_margen(globals.mes_seleccionado,globals.margen_aplicado)
#filtrar_mes(globals.mes_seleccionado)


#esta linea sobrará
#st.sidebar.write("st.session_state object:", st.session_state)

#ejecutamos la función para obtener la tabla resumen
pt6_trans=pt5_trans()
#ejecutamos la función para graficar
graf_pt2=graf_pt1()
#ejecutamos la función para obtener la tabla de valores de la gráfica
pt1_trans2=pt1_trans()



## Datos de la página principal
st.title("Telemindex 2024 webapp")
st.text("Tu aplicación para saber los precios minoristas de indexado")
st.caption("Copyright by Jose Vidal :ok_hand:")

st.subheader("Tabla resumen de precios minoristas por peaje de acceso", divider='rainbow')
texto_precios=f'{texto_precios}. Precios en c€/kWh'
st.caption(texto_precios)
st.write(pt6_trans,)

st.plotly_chart(graf_pt2)
if st.checkbox ('Mostrar tabla de datos'): 
    st.write(pt1_trans2)



