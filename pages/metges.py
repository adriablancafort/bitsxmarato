import streamlit as st
from db import Database
import pandas as pd
from datetime import datetime, date
import altair as alt

st.set_page_config(
    page_title="Metges",
    page_icon="👨‍⚕️",
    layout="wide"
)
st.page_link("app.py", label="Tornar", icon="↩️")

st.title("🤒 Simptomes registrats")
st.divider()

# Connect to the database
db = Database()
responses = db.db["responses"]

# Define available symptoms
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

# Load data from MongoDB
data = list(responses.find())

if data:
    df = pd.DataFrame(data)

    # Convert the timestamp field to date
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date

    # Pivot the data for visualization
    pivot_df = df.pivot_table(
        index="timestamp", columns="simptom", values="count", aggfunc="sum"
    ).fillna(0)

    # Melt the DataFrame for Altair compatibility
    melted_df = pivot_df.reset_index().melt("timestamp", var_name="Symptom", value_name="Count")

    # Define the multi-selection for interactive filtering
    selection = alt.selection_multi(fields=['Symptom'], bind='legend')

    # Plot the data with a clickable legend (multiple selections)
    chart = (
        alt.Chart(melted_df)
        .mark_line(point=True)
        .encode(
            x="timestamp:T",
            y="Count:Q",
            color=alt.Color("Symptom:N", legend=alt.Legend(title="Symptom")),
            tooltip=["timestamp:T", "Symptom:N", "Count:Q"],
        )
        .add_selection(
            selection
        )
        .transform_filter(
            selection
        )
        .properties(width=700, height=400, title="Evolució dels símptomes seleccionats")
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)

    # Display raw data
    st.write("Dades filtrades:")
    st.write(df)
else:
    st.write("No data found in the database.")
