import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from db import Database

st.set_page_config(layout='wide')
st.markdown("""
    <style>
        /* Reduir l'espai vertical dels checkboxes */
        .stCheckbox {
            margin-bottom: -15px;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    db = Database()
    data = db.db['sivic']
    cursor = data.find()
    df = pd.DataFrame(list(cursor))
    df['data'] = pd.to_datetime(df['data'])
    df['diagnostic'] = df['diagnostic'].replace('Faringoamigdalitis estreptocòccica', 'Faringoamigdalitis estr.')

    return df


def downsample_data(df, freq='D'):
    # Set the index to the datetime column
    df = df.set_index('data')
    
    # Select only numeric columns for aggregation
    numeric_columns = df.select_dtypes(include='number')
    
    # Resample and compute the mean
    downsampled = numeric_columns.resample(freq).mean()
    
    # Reset index to keep 'data' as a column
    return downsampled.reset_index()

df = load_data()
filtered_df = df[df['data'] > '2024-01-01']
downsampled_df = downsample_data(filtered_df, freq='W')  # Weekly aggregation


col1, col2 = st.columns([1, 5])  

malalties = [
    "Altres IRA",
    "Bronquiolitis",
    "COVID-19",
    "Escarlatina",
    "Faringoamigdalitis estr.",
    "Faringoamigdalitis",
    "Grip",
    "Pneumònia"
]

regions = [
    "Alt Pirineu i Aran",
    "Barcelona Ciutat",
    "Barcelona Metropolitana Nord",
    "Barcelona Metropolitana Sud",
    "Camp de Tarragona",
    "Catalunya Central",
    "Girona",
    "Lleida",
    "Penedès",
    "Terres de l'Ebre"
]


with col1:
    region = st.selectbox("Regió Sanitària", regions)
    disease_checkboxes = {
        disease: st.checkbox(disease, value=(disease in ['COVID-19']),
                                key=f"{disease}_{i}") for i, disease in enumerate(malalties)
    }

    selected_diseases = [disease for disease, selected in disease_checkboxes.items() if selected]

    filtered_df = df[(df['data'] > '2024-01-01') & (df['nom_regio'] == region)]
    filtered_df = filtered_df[filtered_df['diagnostic'].isin(selected_diseases)]
    filtered_df = filtered_df.drop_duplicates(subset=['data', 'diagnostic'])
    pivot_df = filtered_df.pivot(index='data', columns='diagnostic', values='casos')
with col2:
    color_map = {
        "Altres IRA": "blue",
        "Bronquiolitis": "green",
        "COVID-19": "red",
        "Escarlatina": "purple",
        "Faringoamigdalitis estr.": "orange",
        "Faringoamigdalitis": "yellow",
        "Grip": "pink",
        "Pneumònia": "gray"
    }

    fig = go.Figure()

    for disease in selected_diseases:
        if disease in pivot_df:
            fig.add_trace(go.Scatter(x=pivot_df.index, y=pivot_df[disease], mode='lines', name=disease, line=dict(color=color_map[disease])))

    st.plotly_chart(fig)
