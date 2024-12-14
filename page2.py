import pymongo
import streamlit as st
import pandas as pd
import time
import random
from db import Database
import pickle

st.set_page_config(layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv('qualitat-aire-punts-mesurament-automatic-socrata.csv')
    df['DATA'] = pd.to_datetime(df['DATA'])

    dfplot = df
    # dfplot = dfplot[dfplot['CONTAMINANT'] == 'NO2']
    dfplot['TOTAL'] = sum(dfplot[h] for h in [f'0{i}h' for i in range(1,10)]+[f'{i:2d}h' for i in range(10,25)])
    dfplot = dfplot[['DATA','TOTAL', 'CONTAMINANT']]
    dfplot = dfplot.groupby(['DATA', 'CONTAMINANT']).mean().reset_index()
    dfplot = dfplot[dfplot['DATA'] > '2024-01-01']
    return dfplot



dfplot = load_data()

contaminants = dfplot['CONTAMINANT'].unique()
# contaminant_checkboxes = {contaminant: st.checkbox(contaminant, value=True) for contaminant in contaminants}
# selected_contaminants = [contaminant for contaminant, selected in contaminant_checkboxes.items() if selected]
# filtered_df = dfplot[dfplot['CONTAMINANT'].isin(selected_contaminants)]
# pivot_df = filtered_df.pivot(index='DATA', columns='CONTAMINANT', values='TOTAL')

# st.line_chart(pivot_df)



# Crear els checkboxes en columnes petites
# Injectar CSS per personalitzar els checkboxes
col1, col2 = st.columns([1, 5])  

# Simular dades (exemple per a contaminants)
contaminants = ['C6H6', 'CO', 'H2S', 'Hg', 'NO', 'NO2', 'NOX', 'O3', 'PM1', 'PM10', 'PM2.5', 'SO2']

# Injectar CSS personalitzat per reduir l'espaiat vertical
st.markdown("""
    <style>
        /* Reduir l'espai vertical dels checkboxes */
        .stCheckbox {
            margin-bottom: -10px;
        }
    </style>
""", unsafe_allow_html=True)

# Crear checkboxes amb menys espai
with col1:
    contaminant_checkboxes = {
        contaminant: st.checkbox(contaminant, value=True, key=contaminant) for contaminant in contaminants
    }

    # Mostrar els contaminants seleccionats
    selected_contaminants = [k for k, v in contaminant_checkboxes.items() if v]

    filtered_df = dfplot[dfplot['CONTAMINANT'].isin(selected_contaminants)]
    pivot_df = filtered_df.pivot(index='DATA', columns='CONTAMINANT', values='TOTAL')

# Mostrar el gràfic
with col2:
    st.line_chart(pivot_df)