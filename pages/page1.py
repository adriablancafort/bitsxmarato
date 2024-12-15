import streamlit as st
from db import Database
import pandas as pd
from datetime import datetime, date
from pages.overview.corr_matrix import corr_matrix
from pages.overview.plot_simptomes import plot_simptomes, plot_be_regular_malament
import altair as alt

@st.cache_data
def simptomes():
    db = Database()
    responses = db.db["responses"]
    data = list(responses.find())
    simptoms = [
    {"name": "Diarrea", "slug": "diarrea"},
    {"name": "Esgotament", "slug": "esgotament"},
    {"name": "Mal de cap", "slug": "mal_de_cap"},
    {"name": "Mal de coll", "slug": "mal_de_coll"},
    {"name": "Mal de panxa", "slug": "mal_de_panxa"},
    {"name": "Mocs", "slug": "mocs"},
    {"name": "Tos", "slug": "tos"},
    {"name": "Vòmits", "slug": "vomits"},
    {"name": "Altres", "slug": "altres"},
    ]

    data = list(responses.find())
    if data:
        df = pd.DataFrame(data)

        df['timestamp'] = pd.to_datetime(df['timestamp'])

        st.line_chart(df, x='timestamp', y=['simptom'])

        st.write("Raw data:")
        st.write(df)
    else:
        st.write("No data found in database")
    return df

def page1():
    with st.container():
        df = simptomes()
        st.text('Evolució dels símptomes a Catalunya')
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date
        pivot_df = df.pivot_table(
        index="timestamp", columns="simptom", values="count", aggfunc="sum"
    ).fillna(0)

        chart = (
        alt.Chart(pivot_df.reset_index().melt("timestamp", var_name="Symptom", value_name="Count"))
        .mark_line(point=True)
        .encode(
            x="timestamp:T",
            y="Count:Q",
            color="Symptom:N",
            tooltip=["timestamp:T", "Symptom:N", "Count:Q"],
        )
        .properties(width=700, height=400, title="")
        )

        st.altair_chart(chart, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.title("Mapa de calor de la correlació de símptomes i diagnòstics")
        st.pyplot(corr_matrix())
    with col2:
        st.pyplot(plot_be_regular_malament())





