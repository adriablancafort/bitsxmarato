import streamlit as st
from db import Database
import pandas as pd
from datetime import datetime, date


st.set_page_config(
    page_title="Metges",
    page_icon="👨‍⚕️",
)
st.page_link("app.py", label="Tornar", icon="↩️")

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

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    st.line_chart(df, x='timestamp', y=['simptom'])

    st.write("Raw data:")
    st.write(df)
else:
    st.write("No data found in database")