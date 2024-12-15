import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from db import Database

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    db = Database()
    data = db.db['airquality']
    cursor = data.find()
    df = pd.DataFrame(list(cursor))
    df['DATA'] = pd.to_datetime(df['DATA'])

    return df

dfplot = load_data()

contaminants = dfplot['CONTAMINANT'].unique()

# Injectar CSS per personalitzar els checkboxes
col1, col2 = st.columns([1, 5])  

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
fig = go.Figure()

for contaminant in pivot_df.columns:
    fig.add_trace(
        go.Scatter(
            x=pivot_df.index,
            y=pivot_df[contaminant],
            mode='lines',
            name=contaminant
        )
    )

fig.update_layout(
    title=dict(
        text="Contaminant Levels Over Time",
        y=0.85 # Adjust the y position of the title
    ),
    xaxis=dict(title="Date"),
    yaxis=dict(title="Total"),
    legend=dict(orientation="h", x=0, y=1),
)


# Mostrar gràfic a Streamlit
fig.update_layout(height=400)  # Adjust the height as needed

with col2:
    st.plotly_chart(fig)



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