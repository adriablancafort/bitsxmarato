import streamlit as st
from db import Database
import pandas as pd
from datetime import datetime, date
import altair as alt


st.set_page_config(
    page_title="Metges",
    page_icon="👨‍⚕️",
)
st.page_link("app.py", label="Tornar", icon="↩️")

st.title("🤒Simptomes registrats")
st.divider()

db = Database()
responses = db.db["responses"]

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


    st.write("Raw data:")
    st.write(df)
else:
    st.write("No data found in database")