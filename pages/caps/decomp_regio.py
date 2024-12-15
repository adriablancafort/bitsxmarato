

import pandas as pd
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import streamlit as st
from db import Database


def decomposition_plot():
    db = Database()
    sivic = db.db['sivic']
    cursor = sivic.find()

    df = pd.DataFrame(list(cursor))

    regions = df['nom_regio'].unique()

    region_seleccionada = st.selectbox(
        "Selecciona una regió sanitària:",
        regions
    )

    df_region = df[df['nom_regio'] == region_seleccionada]


    decomposition = seasonal_decompose(df_region['casos'], model='additive', period=365)


    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
    axes[0].plot(df['casos'], label='Original')
    axes[0].set_title('Sèrie original')
    axes[1].plot(decomposition.trend, label='Tendència', color='orange')
    axes[1].set_title('Tendència')
    axes[2].plot(decomposition.seasonal, label='Estacionalitat', color='green')
    axes[2].set_title('Estacionalitat')
    axes[3].plot(decomposition.resid, label='Residus', color='red')
    axes[3].set_title('Residus')
    for ax in axes:
        ax.legend()
        ax.grid()

    plt.tight_layout()
    st.pyplot(fig)
