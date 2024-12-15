import pymongo
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from db import Database

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
        contaminant: st.checkbox(contaminant, value=(contaminant in ['NO2', 'PM10', 'PM1', 'PM2.5']), key=contaminant) for contaminant in contaminants
    }

    # Mostrar els contaminants seleccionats
    selected_contaminants = [k for k, v in contaminant_checkboxes.items() if v]

    filtered_df = dfplot[dfplot['CONTAMINANT'].isin(selected_contaminants)]
    pivot_df = filtered_df.pivot(index='DATA', columns='CONTAMINANT', values='TOTAL')

# Mostrar el gràfic
with col2:
    st.line_chart(pivot_df)



data = {
    "Date": [
        "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05",
        "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10",
        "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14"
    ],
    "mean_temperature": [
        23.75, 29.51, 27.32, 25.99, 21.56, 21.56, 20.58, 
        28.66, 26.01, 27.08, 20.21, 29.70, 28.32, 22.12
    ],
    "mean_relative_humidity": [
        59.09, 59.17, 65.21, 76.24, 71.60, 64.56, 80.59, 
        56.97, 64.61, 68.32, 72.80, 89.26, 59.98, 75.71
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Configurar gràfic Plotly
fig = go.Figure()

# Afegir la primera línia (mean_temperature)
fig.add_trace(
    go.Scatter(
        x=df["Date"], 
        y=df["mean_temperature"], 
        mode='lines+markers',
        name='Mean Temperature (°C)',
        yaxis='y1'
    )
)

# Afegir la segona línia (mean_relative_humidity)
fig.add_trace(
    go.Scatter(
        x=df["Date"], 
        y=df["mean_relative_humidity"], 
        mode='lines+markers',
        name='Mean Relative Humidity (%)',
        yaxis='y2'
    )
)

# Configurar eixos Y dobles
fig.update_layout(
    title="Mean Temperature and Relative Humidity",
    xaxis=dict(title="Date"),
    yaxis=dict(
        title="Mean Temperature (°C)",
        side="left",
        showgrid=False
    ),
    yaxis2=dict(
        title="Mean Relative Humidity (%)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(x=0, y=1.39),
)


# Mostrar gràfic a Streamlit
fig.update_layout(height=300)  # Adjust the height as needed
with col2:
    st.plotly_chart(fig)