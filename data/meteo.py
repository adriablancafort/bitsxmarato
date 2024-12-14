import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('datasets/DadesMeteoCat_temp.csv', sep=';', encoding='latin1')

# Convertir 'timestamp' a formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d')

# Crear el gráfico interactivo con Plotly
fig = px.line(df, 
              x='timestamp', 
              y='mean_temperature', 
              color='station_name',  # Cada estación será una línea diferente
              title='Evolución de la temperatura media por estación',
              labels={'timestamp': 'Fecha', 'mean_temperature': 'Temperatura media (°C)', 'station_name': 'Estación'})

# Personalización del gráfico (opcional)
fig.update_layout(
    xaxis_title='Fecha',
    yaxis_title='Temperatura media (°C)',
    template='plotly_dark',  # Puedes cambiar esto por 'plotly' o 'seaborn' si prefieres otro estilo
    hovermode='x unified'  # Mostrar todos los valores de la estación cuando pasas el ratón por encima
)

# Mostrar el gráfico interactivo en Streamlit
st.plotly_chart(fig)
