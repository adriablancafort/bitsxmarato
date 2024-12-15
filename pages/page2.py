import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from db import Database
import random


@st.cache_data
def load_data():
    db = Database()
    data = db.db['airquality']
    cursor = data.find()
    df = pd.DataFrame(list(cursor))
    df['DATA'] = pd.to_datetime(df['DATA'])

    return df


@st.cache_data
def generate_temp_data():
    dataBCN = {
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



    dataSQG = {
        "Date": [
            "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05",
            "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10",
            "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14"
        ],
        "mean_temperature": [
            24.75, 30.51, 28.32, 26.99, 22.56, 22.56, 21.58, 
            29.66, 27.01, 28.08, 21.21, 30.70, 29.32, 23.12
        ],
        "mean_relative_humidity": [
            69.09, 69.17, 75.21, 86.24, 81.60, 74.56, 90.59, 
            66.97, 74.61, 78.32, 82.80, 99.26, 69.98, 85.71
        ]
    }


    dataBDN = {
        "Date": [
            "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05",
            "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10",
            "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14"
        ],
        "mean_temperature": [
            25.75, 31.51, 29.32, 27.99, 23.56, 23.56, 22.58, 
            30.66, 28.01, 29.08, 22.21, 31.70, 30.32, 24.12
        ],
        "mean_relative_humidity": [
            79.09, 79.17, 85.21, 96.24, 91.60, 84.56, 100.59, 
            76.97, 84.61, 88.32, 92.80, 109.26, 79.98, 95.71
        ]
    }


    # Randomize data for Barcelona
    dataBCN["mean_temperature"] = [round(random.uniform(20, 30), 2) for _ in dataBCN["Date"]]
    dataBCN["mean_relative_humidity"] = [round(random.uniform(50, 90), 2) for _ in dataBCN["Date"]]

    # Randomize data for Sant Cugat del Vallès
    dataSQG["mean_temperature"] = [round(random.uniform(20, 30), 2) for _ in dataSQG["Date"]]
    dataSQG["mean_relative_humidity"] = [round(random.uniform(50, 90), 2) for _ in dataSQG["Date"]]

    return [dataBCN, dataSQG, dataBDN]

def page2():
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
                margin-bottom: -15px;
            }
        </style>
    """, unsafe_allow_html=True)

    municipis = ['Barcelona', 'Sant Cugat del Vallès', 'Badalona']

    # Crear checkboxes amb menys espai
    with col1:
        municipi = st.selectbox("Municipi", municipis)
        st.write("Select Contaminants")

        contaminant_checkboxes = {
            contaminant: st.checkbox(contaminant, value=(contaminant in ['NO2', 'PM10', 'PM1', 'PM2.5']), key=contaminant) for contaminant in contaminants
        }

        # Mostrar els contaminants seleccionats
        selected_contaminants = [k for k, v in contaminant_checkboxes.items() if v]

        filtered_df = dfplot[dfplot['CONTAMINANT'].isin(selected_contaminants)]
        filtered_df = filtered_df[filtered_df['MUNICIPI'] == municipi]
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



    temp_data = generate_temp_data()


    if municipi == 'Barcelona':
        df = pd.DataFrame(temp_data[0])
    elif municipi == 'Sant Cugat del Vallès':
        df = pd.DataFrame(temp_data[1])
    else:
        df = pd.DataFrame(temp_data[2])

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