import streamlit as st
import pandas as pd
import plotly.express as px

from backend import graf_pt1

st.set_page_config(layout='wide')
st.title("Telemindex webapp")
st.plotly_chart(graf_pt1)

